import os
import inspect
import importlib
import logging
from typing import Any, Dict


current_dir = os.path.dirname(__file__)


def _build_kwargs(sig: inspect.Signature, body: Dict[str, Any]) -> Dict[str, Any]:
    """Construct kwargs dict for a function signature given the incoming body."""
    kwargs: Dict[str, Any] = {}
    for param, param_obj in sig.parameters.items():
        if param in body:
            kwargs[param] = body[param]
        else:
            if param_obj.default != inspect.Parameter.empty:
                kwargs[param] = param_obj.default
    return kwargs


def create_dynamic_strategy(module_path: str, function_name: str):
    """Dynamically create a strategy function that wraps a library function."""

    def dynamic_strategy(self, body: Dict[str, Any]):
        try:
            module = importlib.import_module(module_path)
            func = getattr(module, function_name)

            sig = inspect.signature(func)
            kwargs = _build_kwargs(sig, body)

            result = func(**kwargs)
            try:
                self.publish(result)
            except Exception:
                logging.exception("Failed to publish dynamic strategy result")
        except Exception as e:
            _publish_error(self, e, function_name, module_path)

    dynamic_strategy.__name__ = f"{function_name}_strategy"
    return dynamic_strategy


def _publish_error(publisher, exc: Exception, fn: str, mod: str):
    """Publish a consistent error payload for failed dynamic strategies."""
    try:
        publisher.publish({"error": str(exc), "function": fn, "module": mod})
    except Exception:
        logging.exception("Failed to publish error: %s", exc)


def _define_grouped_modules() -> Dict[str, list]:
    VECTORS_MODULE = 'dsl.c04_linear_algebra.e0401_vectors'
    MATRICES_MODULE = 'dsl.c04_linear_algebra.e0402_matrices'
    CENTRAL_TENDENCY_MODULE = 'dsl.c05_statistics.e0501_central_tendancy'
    DISPERSION_MODULE = 'dsl.c05_statistics.e0502_dispersion'
    CORRELATION_MODULE = 'dsl.c05_statistics.e0503_correlation'
    UNIFORM_MODULE = 'dsl.c06_probability.e0602_uniform'
    NORMAL_MODULE = 'dsl.c06_probability.e0603_normal'
    BINOM_MODULE = 'dsl.c06_probability.e0604_binom'
    CONDITIONAL_MODULE = 'dsl.c06_probability.e0601_conditional'
    ESTIMATING_GRADIENT_MODULE = 'dsl.c08_gradient_descent.e0801_estimating_gradient'
    USING_GRADIENT_MODULE = 'dsl.c08_gradient_descent.e0802_using_gradient'
    FITTING_MODELS_MODULE = 'dsl.c08_gradient_descent.e0803_fitting_models'
    MINIBATCH_GD_MODULE = 'dsl.c08_gradient_descent.e0804_minibatch_gd'
    STOCHASTIC_GD_MODULE = 'dsl.c08_gradient_descent.e0805_stochastic_gd'

    return {
        VECTORS_MODULE: ['vector_add', 'vector_subtract', 'vector_sum', 'scalar_multiply', 'vector_mean', 'dot', 'sum_of_squares', 'magnitude', 'squared_distance', 'distance', 'distance2'],
        MATRICES_MODULE: ['shape', 'get_row', 'get_column', 'make_matrix', 'is_diagonal', 'make_identity_matrix', 'matrix_add', 'matrix_multiply', 'make_random_matrix'],
        CENTRAL_TENDENCY_MODULE: ['mean', 'median', 'quantile', 'mode'],
        DISPERSION_MODULE: ['data_range', 'de_mean', 'variance', 'standard_deviation', 'interquartile_range'],
        CORRELATION_MODULE: ['covariance', 'correlation'],
        UNIFORM_MODULE: ['uniform_pd', 'uniform_cd'],
        NORMAL_MODULE: ['normal_pd', 'normal_cd', 'inverse_normal_cd'],
        BINOM_MODULE: ['bernoulli_trial', 'binomial', 'binom_pd', 'binom_cd', 'binom_pp'],
        CONDITIONAL_MODULE: ['random_kid'],
        ESTIMATING_GRADIENT_MODULE: ['difference_quotient', 'partial_difference_quotient', 'estimate_gradient'],
        USING_GRADIENT_MODULE: ['gradient_step', 'sum_of_squares_gradient'],
        FITTING_MODELS_MODULE: ['linear_gradient'],
        MINIBATCH_GD_MODULE: ['minibatches', 'minimize_batch', 'maximize_batch'],
        STOCHASTIC_GD_MODULE: ['in_random_order', 'minimize_stochastic', 'maximize_stochastic'],
    }


def _get_working_constants() -> Dict[str, str]:
    try:
        from common.constants import (
            WORKING_DATA_MODULE,
            WORKING_E1004,
            WORKING_E1006,
            WORKING_E1007,
            WORKING_E1008,
            WORKING_E1009,
        )
        return {
            'WORKING_DATA_MODULE': WORKING_DATA_MODULE,
            'WORKING_E1004': WORKING_E1004,
            'WORKING_E1006': WORKING_E1006,
            'WORKING_E1007': WORKING_E1007,
            'WORKING_E1008': WORKING_E1008,
            'WORKING_E1009': WORKING_E1009,
        }
    except Exception:
        WORKING_DATA_MODULE = 'dsl.c10_working_with_data'
        return {
            'WORKING_DATA_MODULE': WORKING_DATA_MODULE,
            'WORKING_E1004': WORKING_DATA_MODULE + '.e1004_named_tuples',
            'WORKING_E1006': WORKING_DATA_MODULE + '.e1006_cleaning',
            'WORKING_E1007': WORKING_DATA_MODULE + '.e1007_manipulation',
            'WORKING_E1008': WORKING_DATA_MODULE + '.e1008_rescaling',
            'WORKING_E1009': WORKING_DATA_MODULE + '.e1009_dimensionality_reduction',
        }


def _working_map(working_data_module: str, e1004: str, e1006: str, e1008: str) -> Dict[str, str]:
    return {
        'parse_rows': working_data_module + '.e1001_univariate',
        'bucketize': working_data_module + '.e1001_univariate',
        'scale': e1008,
        'rescale': e1008,
        'clean_rows': e1006,
        'named_tuples': e1004,
    }


def _discover_dsl_functions_with_pkgutil(existing: Dict[str, str]) -> Dict[str, str]:
    module_mappings: Dict[str, str] = {}
    try:
        import pkgutil
        import dsl

        for finder, mod_name, ispkg in pkgutil.walk_packages(dsl.__path__, dsl.__name__ + '.'):
            try:
                mod = importlib.import_module(mod_name)
            except Exception:
                continue

            for obj_name, obj in inspect.getmembers(mod, inspect.isfunction):
                if obj_name not in existing and obj_name not in module_mappings:
                    module_mappings[obj_name] = mod_name
    except Exception:
        pass
    return module_mappings


def _discover_ast_function_definitions(fpath: str, base_candidate: str, existing: Dict[str, str], module_mappings: Dict[str, str]) -> None:
    try:
        with open(fpath, 'r', encoding='utf-8') as fh:
            src = fh.read()
        parsed = ast.parse(src)
    except Exception:
        return

    rel = os.path.relpath(fpath, base_candidate)
    mod_name = 'dsl.' + rel.replace(os.sep, '.')[:-3]

    for node in parsed.body:
        if isinstance(node, ast.FunctionDef):
            if node.name not in existing and node.name not in module_mappings:
                module_mappings[node.name] = mod_name


def _discover_dsl_functions_with_ast(existing: Dict[str, str]) -> Dict[str, str]:
    module_mappings: Dict[str, str] = {}
    try:
        import ast
        base_candidate = os.path.normpath(
            os.path.join(current_dir, os.pardir, os.pardir, os.pardir, 'data-scratch-library', 'dsl')
        )
        if os.path.isdir(base_candidate):
            for root, _, files in os.walk(base_candidate):
                for fname in files:
                    if not fname.endswith('.py'):
                        continue
                    fpath = os.path.join(root, fname)
                    _discover_ast_function_definitions(fpath, base_candidate, existing, module_mappings)
    except Exception:
        pass
    return module_mappings


def _discover_dsl_functions(existing: Dict[str, str]) -> Dict[str, str]:
    module_mappings = _discover_dsl_functions_with_pkgutil(existing)
    module_mappings.update(_discover_dsl_functions_with_ast(existing))
    return module_mappings


def _discover_dsl_functions(existing: Dict[str, str]) -> Dict[str, str]:
    module_mappings = _discover_dsl_functions_with_pkgutil(existing)
    module_mappings.update(_discover_dsl_functions_with_ast(existing))
    return module_mappings


def _populate_module_mappings(target: Dict[str, str]) -> None:
    grouped = _define_grouped_modules()
    for module_const, fnames in grouped.items():
        for fn in fnames:
            target[fn] = module_const

    ML_MODULE = 'dsl.c11_machine_learning.machine_learning'
    for fn in ['split_data', 'train_test_split', 'accuracy', 'precision', 'recall', 'f1_score']:
        target[fn] = ML_MODULE

    wc = _get_working_constants()
    working_map = _working_map(
        wc['WORKING_DATA_MODULE'],
        wc['WORKING_E1004'],
        wc['WORKING_E1006'],
        wc['WORKING_E1008'],
    )
    target.update(working_map)

    discovered = _discover_dsl_functions(target)
    target.update(discovered)

    target['mysqrt'] = 'dsl.c02_crash_course.e0203_functions'
    target['strength'] = 'dsl.c06_probability.e0604_binom'


def _create_strategies(source: Dict[str, str]) -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    WARNING_IMPORT_FMT = 'Warning: Could not import {} from {}: {}'
    for func_name, module_path in source.items():
        try:
            out[func_name] = create_dynamic_strategy(module_path, func_name)
        except Exception:
            try:
                print(WARNING_IMPORT_FMT.format(func_name, module_path, 'ImportError'))
            except Exception:
                pass
    return out


def get_all_library_functions() -> Dict[str, Any]:
    module_mappings: Dict[str, str] = {}
    _populate_module_mappings(module_mappings)
    return _create_strategies(module_mappings)


# Build strategies at import time (best-effort)
dynamic_strategies = get_all_library_functions()
