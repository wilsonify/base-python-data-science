import ast
import importlib
import inspect
import logging
import os
import pkgutil
from typing import Any, Dict


def _build_kwargs(sig: inspect.Signature, source: Dict[str, Any]) -> Dict[str, Any]:
    """Build kwargs from a function signature and a source mapping."""
    kwargs: Dict[str, Any] = {}
    for param, param_obj in sig.parameters.items():
        if param in source:
            kwargs[param] = source[param]
        elif param_obj.default != inspect.Parameter.empty:
            kwargs[param] = param_obj.default
    return kwargs


def _publish_error(publisher, exc: Exception, fn: str, mod: str) -> None:
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
        VECTORS_MODULE: [
            'vector_add', 'vector_subtract', 'vector_sum', 'scalar_multiply', 'vector_mean',
            'dot', 'sum_of_squares', 'magnitude', 'squared_distance', 'distance', 'distance2',
        ],
        MATRICES_MODULE: [
            'shape', 'get_row', 'get_column', 'make_matrix', 'is_diagonal', 'make_identity_matrix',
            'matrix_add', 'matrix_multiply', 'make_random_matrix',
        ],
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
        working_data_module = 'dsl.c10_working_with_data'
        return {
            'WORKING_DATA_MODULE': working_data_module,
            'WORKING_E1004': working_data_module + '.e1004_named_tuples',
            'WORKING_E1006': working_data_module + '.e1006_cleaning',
            'WORKING_E1007': working_data_module + '.e1007_manipulation',
            'WORKING_E1008': working_data_module + '.e1008_rescaling',
            'WORKING_E1009': working_data_module + '.e1009_dimensionality_reduction',
        }


def _working_map(
    working_data_module: str,
    working_e1004: str,
    working_e1006: str,
    working_e1007: str,
    working_e1008: str,
    working_e1009: str,
) -> Dict[str, str]:
    return {
        'bucketize': working_data_module + '.e1001_univariate',
        'make_histogram': working_data_module + '.e1001_univariate',
        'correlation_matrix': working_data_module + '.e1003_multivariate',
        'random_normal': working_data_module + '.e1002_bivariate',
        'demo_deque': working_data_module + '.e1000_circular_buffer',
        'create_stock_price_namedtuple': working_e1004,
        'create_stock_price': working_e1004,
        'create_price_dict': working_e1004,
        'parse_row': working_e1006,
        'try_parse_row': working_e1006,
        'process_csv': working_e1006,
        'max_stock_price': working_e1007,
        'max_prices_by_symbol': working_e1007,
        'pct_change': working_e1007,
        'day_over_day_changes': working_e1007,
        'group_prices_by_symbol': working_e1007,
        'find_largest_and_smallest_changes': working_e1007,
        'average_daily_change_by_month': working_e1007,
        'create_stock_price_dataclass': working_data_module + '.e1005_dataclass',
        'vector_mean': working_e1008,
        'standard_deviation': working_e1008,
        'scale': working_e1008,
        'rescale': working_e1008,
        'simple_trange': working_e1009,
        'de_mean': working_e1009,
        'direction': working_e1009,
        'directional_variance': working_e1009,
        'directional_variance_gradient': working_e1009,
        'first_principal_component': working_e1009,
        'project': working_e1009,
        'remove_projection_from_vector': working_e1009,
        'remove_projection': working_e1009,
    }


def _discover_dsl_functions_with_pkgutil(existing: Dict[str, str]) -> Dict[str, str]:
    module_mappings: Dict[str, str] = {}
    try:
        import dsl
        for finder, mod_name, _ in pkgutil.walk_packages(dsl.__path__, dsl.__name__ + '.'):
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


def _discover_ast_function_definitions(
    fpath: str,
    base_candidate: str,
    existing: Dict[str, str],
    module_mappings: Dict[str, str],
) -> None:
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
        candidate = os.path.join(os.path.dirname(__file__), os.pardir, 'data-scratch-library', 'dsl')
        candidate = os.path.normpath(candidate)
        if os.path.isdir(candidate):
            for root, _, files in os.walk(candidate):
                for fname in files:
                    if not fname.endswith('.py'):
                        continue
                    fpath = os.path.join(root, fname)
                    _discover_ast_function_definitions(fpath, candidate, existing, module_mappings)
    except Exception:
        pass
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

    ml_module = 'dsl.c11_machine_learning.machine_learning'
    for fn in ['split_data', 'train_test_split', 'accuracy', 'precision', 'recall', 'f1_score']:
        target[fn] = ml_module

    wc = _get_working_constants()
    working_map = _working_map(
        wc['WORKING_DATA_MODULE'],
        wc['WORKING_E1004'],
        wc['WORKING_E1006'],
        wc['WORKING_E1007'],
        wc['WORKING_E1008'],
        wc['WORKING_E1009'],
    )
    target.update(working_map)

    discovered = _discover_dsl_functions(target)
    target.update(discovered)

    target['mysqrt'] = 'dsl.c02_crash_course.e0203_functions'
    target['strength'] = 'dsl.c06_probability.e0604_binom'


def _create_strategies(source: Dict[str, str], strategy_factory) -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    warning_fmt = 'Warning: Could not import {} from {}: {}'
    for func_name, module_path in source.items():
        try:
            out[func_name] = strategy_factory(module_path, func_name)
        except Exception as e:
            try:
                print(warning_fmt.format(func_name, module_path, e))
            except Exception:
                pass
    return out
