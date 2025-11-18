import os
import inspect
import importlib
from typing import Any, Dict

def create_dynamic_strategy(module_path: str, function_name: str):
    """Dynamically create a strategy function that wraps a library function"""
    def dynamic_strategy(self):
        try:
            # Import the module and get the function
            module = importlib.import_module(module_path)
            func = getattr(module, function_name)

            # Build kwargs (helper below) from the incoming payload
            sig = inspect.signature(func)
            kwargs = _build_kwargs(sig, getattr(self, 'input_payload', {}))

            # Call the function
            result = func(**kwargs)
            self.publish(result)

        except Exception as e:
            _publish_error(self, e, function_name, module_path)
    
    # Set a proper name for the function
    dynamic_strategy.__name__ = f"{function_name}_strategy"
    return dynamic_strategy


def get_all_library_functions():
    """Discover all functions in the data-scratch-library"""
    functions = {}
    
    # Define constants for commonly used modules
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
    
    # Build module_mappings by grouping function names to module constants to
    # avoid large numbers of duplicated string literals (reduces S1192 findings)
    module_mappings = {}

    grouped = {
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

    # Simple helper modules for other grouped functions
    ML_MODULE = 'dsl.c11_machine_learning.machine_learning'
    try:
        # Prefer shared constants module to reduce duplicated literals across files
        from common.constants import (
            WORKING_DATA_MODULE,
            WORKING_E1004,
            WORKING_E1006,
            WORKING_E1007,
            WORKING_E1008,
            WORKING_E1009,
        )
    except Exception:
        # Fallback to local definitions if the shared module isn't available in the
        # runtime environment (keeps this file robust for standalone use).
        WORKING_DATA_MODULE = 'dsl.c10_working_with_data'
        WORKING_E1004 = WORKING_DATA_MODULE + '.e1004_named_tuples'
        WORKING_E1006 = WORKING_DATA_MODULE + '.e1006_cleaning'
        WORKING_E1007 = WORKING_DATA_MODULE + '.e1007_manipulation'
        WORKING_E1008 = WORKING_DATA_MODULE + '.e1008_rescaling'
        WORKING_E1009 = WORKING_DATA_MODULE + '.e1009_dimensionality_reduction'

    for module_const, fnames in grouped.items():
        for fn in fnames:
            module_mappings[fn] = module_const

    # Machine learning group
    for fn in ['split_data', 'train_test_split', 'accuracy', 'precision', 'recall', 'f1_score']:
        module_mappings[fn] = ML_MODULE

    # Working-with-data mappings (use fully qualified names where functions live)
    working_map = {
    'bucketize': WORKING_DATA_MODULE + '.e1001_univariate',
    'make_histogram': WORKING_DATA_MODULE + '.e1001_univariate',
    'correlation_matrix': WORKING_DATA_MODULE + '.e1003_multivariate',
    'random_normal': WORKING_DATA_MODULE + '.e1002_bivariate',
    'demo_deque': WORKING_DATA_MODULE + '.e1000_circular_buffer',
    'create_stock_price_namedtuple': WORKING_E1004,
    'create_stock_price': WORKING_E1004,
    'create_price_dict': WORKING_E1004,
    'parse_row': WORKING_E1006,
    'try_parse_row': WORKING_E1006,
    'process_csv': WORKING_E1006,
    'max_stock_price': WORKING_E1007,
    'max_prices_by_symbol': WORKING_E1007,
    'pct_change': WORKING_E1007,
    'day_over_day_changes': WORKING_E1007,
    'group_prices_by_symbol': WORKING_E1007,
    'find_largest_and_smallest_changes': WORKING_E1007,
    'average_daily_change_by_month': WORKING_E1007,
    'create_stock_price_dataclass': WORKING_DATA_MODULE + '.e1005_dataclass',
    'vector_mean': WORKING_E1008,
    'standard_deviation': WORKING_E1008,
    'scale': WORKING_E1008,
    'rescale': WORKING_E1008,
    'simple_trange': WORKING_E1009,
    'de_mean': WORKING_E1009,
    'direction': WORKING_E1009,
    'directional_variance': WORKING_E1009,
    'directional_variance_gradient': WORKING_E1009,
    'first_principal_component': WORKING_E1009,
    'project': WORKING_E1009,
    'remove_projection_from_vector': WORKING_E1009,
    'remove_projection': WORKING_E1009,
    }

    module_mappings.update(working_map)

    # Dynamic discovery: scan the 'dsl' package for additional functions and add
    # them to module_mappings when not already present. Keeps parity between AMQP and MQTT modules.
    try:
        import pkgutil
        import dsl

        for finder, mod_name, ispkg in pkgutil.walk_packages(dsl.__path__, dsl.__name__ + '.'):
            try:
                mod = importlib.import_module(mod_name)
            except Exception:
                continue

            for obj_name, obj in inspect.getmembers(mod, inspect.isfunction):
                if obj_name not in module_mappings:
                    module_mappings[obj_name] = mod_name
    except ImportError:
        # If pkgutil import fails, attempt filesystem fallback like the AMQP module
        try:
            import ast
            candidate = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir, 'data-scratch-library', 'dsl')
            candidate = os.path.normpath(candidate)
            if os.path.isdir(candidate):
                for root, _, files in os.walk(candidate):
                    for fname in files:
                        if not fname.endswith('.py'):
                            continue
                        fpath = os.path.join(root, fname)
                        try:
                            with open(fpath, 'r', encoding='utf-8') as fh:
                                src = fh.read()
                            parsed = ast.parse(src)
                        except Exception:
                            continue

                        rel = os.path.relpath(fpath, candidate)
                        mod_name = 'dsl.' + rel.replace(os.sep, '.')[:-3]
                        for node in parsed.body:
                            if isinstance(node, ast.FunctionDef):
                                if node.name not in module_mappings:
                                    module_mappings[node.name] = mod_name
        except Exception:
            pass

    # Utility functions from crash course
    module_mappings['mysqrt'] = 'dsl.c02_crash_course.e0203_functions'
    module_mappings['strength'] = 'dsl.c06_probability.e0604_binom'
    
    # Helper: consistent warning and error publishing to reduce duplicated
    # string literals across the module (reduces S1192 findings)
    WARNING_IMPORT_FMT = 'Warning: Could not import {} from {}: {}'

    def _publish_error(publisher, exc: Exception, fn: str, mod: str):
        publisher.publish({"error": str(exc), "function": fn, "module": mod})

    # Create dynamic strategies for all functions
    for func_name, module_path in module_mappings.items():
        try:
            functions[func_name] = create_dynamic_strategy(module_path, func_name)
        except ImportError as e:
            print(WARNING_IMPORT_FMT.format(func_name, module_path, e))
    
    return functions


# Create all dynamic strategies
dynamic_strategies = get_all_library_functions()


def _build_kwargs(sig: inspect.Signature, source: Dict[str, Any]) -> Dict[str, Any]:
    """Build kwargs from a function signature and a source mapping.

    This centralizes default handling and reduces nesting in the wrapper.
    """
    kwargs: Dict[str, Any] = {}
    for param, param_obj in sig.parameters.items():
        if param in source:
            kwargs[param] = source[param]
        else:
            if param_obj.default != inspect.Parameter.empty:
                kwargs[param] = param_obj.default
    return kwargs
