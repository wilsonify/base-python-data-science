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
            
            # Get function signature to extract parameters
            sig = inspect.signature(func)
            parameters = list(sig.parameters.keys())
            
            # Extract arguments from input_payload, handling defaults
            kwargs = {}
            for param in parameters:
                if param in self.input_payload:
                    kwargs[param] = self.input_payload[param]
                else:
                    # Check if parameter has a default value
                    param_obj = sig.parameters[param]
                    if param_obj.default != inspect.Parameter.empty:
                        kwargs[param] = param_obj.default
            
            # Call the function
            result = func(**kwargs)
            self.publish(result)
            
        except Exception as e:
            self.publish({"error": str(e), "function": function_name, "module": module_path})
    
    # Set a proper name for the function
    dynamic_strategy.__name__ = f"{function_name}_strategy"
    return dynamic_strategy


def get_all_library_functions():
    """Discover all functions in the data-scratch-library"""
    functions = {}
    
    # Define the module mappings (same as AMQP version)
    module_mappings = {
        # Linear Algebra
        'vector_add': 'dsl.c04_linear_algebra.e0401_vectors',
        'vector_subtract': 'dsl.c04_linear_algebra.e0401_vectors',
        'vector_sum': 'dsl.c04_linear_algebra.e0401_vectors',
        'scalar_multiply': 'dsl.c04_linear_algebra.e0401_vectors',
        'vector_mean': 'dsl.c04_linear_algebra.e0401_vectors',
        'dot': 'dsl.c04_linear_algebra.e0401_vectors',
        'sum_of_squares': 'dsl.c04_linear_algebra.e0401_vectors',
        'magnitude': 'dsl.c04_linear_algebra.e0401_vectors',
        'squared_distance': 'dsl.c04_linear_algebra.e0401_vectors',
        'distance': 'dsl.c04_linear_algebra.e0401_vectors',
        'distance2': 'dsl.c04_linear_algebra.e0401_vectors',
        'shape': 'dsl.c04_linear_algebra.e0402_matrices',
        'get_row': 'dsl.c04_linear_algebra.e0402_matrices',
        'get_column': 'dsl.c04_linear_algebra.e0402_matrices',
        'make_matrix': 'dsl.c04_linear_algebra.e0402_matrices',
        'is_diagonal': 'dsl.c04_linear_algebra.e0402_matrices',
        'make_identity_matrix': 'dsl.c04_linear_algebra.e0402_matrices',
        'matrix_add': 'dsl.c04_linear_algebra.e0402_matrices',
        'matrix_multiply': 'dsl.c04_linear_algebra.e0402_matrices',
        'make_random_matrix': 'dsl.c04_linear_algebra.e0402_matrices',
        
        # Statistics
        'mean': 'dsl.c05_statistics.e0501_central_tendancy',
        'median': 'dsl.c05_statistics.e0501_central_tendancy',
        'quantile': 'dsl.c05_statistics.e0501_central_tendancy',
        'mode': 'dsl.c05_statistics.e0501_central_tendancy',
        'data_range': 'dsl.c05_statistics.e0502_dispersion',
        'de_mean': 'dsl.c05_statistics.e0502_dispersion',
        'variance': 'dsl.c05_statistics.e0502_dispersion',
        'standard_deviation': 'dsl.c05_statistics.e0502_dispersion',
        'interquartile_range': 'dsl.c05_statistics.e0502_dispersion',
        'covariance': 'dsl.c05_statistics.e0503_correlation',
        'correlation': 'dsl.c05_statistics.e0503_correlation',
        'correlation_matrix': 'dsl.c05_statistics.e0503_correlation',
        
        # Probability
        'uniform_pdf': 'dsl.c06_probability.e0602_uniform',
        'uniform_cdf': 'dsl.c06_probability.e0602_uniform',
        'normal_pdf': 'dsl.c06_probability.e0603_normal',
        'normal_cdf': 'dsl.c06_probability.e0603_normal',
        'inverse_normal_cdf': 'dsl.c06_probability.e0603_normal',
        'bernoulli_trial': 'dsl.c06_probability.e0604_binom',
        'binomial': 'dsl.c06_probability.e0604_binom',
        'binom_pdf': 'dsl.c06_probability.e0604_binom',
        'binom_cdf': 'dsl.c06_probability.e0604_binom',
        'binom_ppf': 'dsl.c06_probability.e0604_binom',
        'random_kid': 'dsl.c06_probability.e0601_conditional',
        
        # Gradient Descent
        'difference_quotient': 'dsl.c08_gradient_descent.e0801_estimating_gradient',
        'partial_difference_quotient': 'dsl.c08_gradient_descent.e0801_estimating_gradient',
        'estimate_gradient': 'dsl.c08_gradient_descent.e0801_estimating_gradient',
        'gradient_step': 'dsl.c08_gradient_descent.e0802_using_gradient',
        'sum_of_squares_gradient': 'dsl.c08_gradient_descent.e0802_using_gradient',
        'linear_gradient': 'dsl.c08_gradient_descent.e0803_fitting_models',
        'minibatches': 'dsl.c08_gradient_descent.e0804_minibatch_gd',
        'minimize_batch': 'dsl.c08_gradient_descent.e0804_minibatch_gd',
        'maximize_batch': 'dsl.c08_gradient_descent.e0804_minibatch_gd',
        'in_random_order': 'dsl.c08_gradient_descent.e0805_stochastic_gd',
        'minimize_stochastic': 'dsl.c08_gradient_descent.e0805_stochastic_gd',
        'maximize_stochastic': 'dsl.c08_gradient_descent.e0805_stochastic_gd',
        
        # Machine Learning
        'split_data': 'dsl.c11_machine_learning.machine_learning',
        'train_test_split': 'dsl.c11_machine_learning.machine_learning',
        'accuracy': 'dsl.c11_machine_learning.machine_learning',
        'precision': 'dsl.c11_machine_learning.machine_learning',
        'recall': 'dsl.c11_machine_learning.machine_learning',
        'f1_score': 'dsl.c11_machine_learning.machine_learning',
        
        # Working with Data
        'bucketize': 'dsl.c10_working_with_data.e1001_univariate',
        'make_histogram': 'dsl.c10_working_with_data.e1001_univariate',
        'correlation_matrix': 'dsl.c10_working_with_data.e1003_multivariate',
        'random_normal': 'dsl.c10_working_with_data.e1002_bivariate',
        'demo_deque': 'dsl.c10_working_with_data.e1000_circular_buffer',
        'create_stock_price_namedtuple': 'dsl.c10_working_with_data.e1004_named_tuples',
        'create_stock_price': 'dsl.c10_working_with_data.e1004_named_tuples',
        'create_price_dict': 'dsl.c10_working_with_data.e1004_named_tuples',
        'parse_row': 'dsl.c10_working_with_data.e1006_cleaning',
        'try_parse_row': 'dsl.c10_working_with_data.e1006_cleaning',
        'process_csv': 'dsl.c10_working_with_data.e1006_cleaning',
        'max_stock_price': 'dsl.c10_working_with_data.e1007_manipulation',
        'max_prices_by_symbol': 'dsl.c10_working_with_data.e1007_manipulation',
        'pct_change': 'dsl.c10_working_with_data.e1007_manipulation',
        'day_over_day_changes': 'dsl.c10_working_with_data.e1007_manipulation',
        'group_prices_by_symbol': 'dsl.c10_working_with_data.e1007_manipulation',
        'find_largest_and_smallest_changes': 'dsl.c10_working_with_data.e1007_manipulation',
        'average_daily_change_by_month': 'dsl.c10_working_with_data.e1007_manipulation',
        'create_stock_price_dataclass': 'dsl.c10_working_with_data.e1005_dataclass',
        'vector_mean': 'dsl.c10_working_with_data.e1008_rescaling',
        'standard_deviation': 'dsl.c10_working_with_data.e1008_rescaling',
        'scale': 'dsl.c10_working_with_data.e1008_rescaling',
        'rescale': 'dsl.c10_working_with_data.e1008_rescaling',
        'simple_trange': 'dsl.c10_working_with_data.e1009_dimensionality_reduction',
        'de_mean': 'dsl.c10_working_with_data.e1009_dimensionality_reduction',
        'direction': 'dsl.c10_working_with_data.e1009_dimensionality_reduction',
        'directional_variance': 'dsl.c10_working_with_data.e1009_dimensionality_reduction',
        'directional_variance_gradient': 'dsl.c10_working_with_data.e1009_dimensionality_reduction',
        'first_principal_component': 'dsl.c10_working_with_data.e1009_dimensionality_reduction',
        'project': 'dsl.c10_working_with_data.e1009_dimensionality_reduction',
        'remove_projection_from_vector': 'dsl.c10_working_with_data.e1009_dimensionality_reduction',
        'remove_projection': 'dsl.c10_working_with_data.e1009_dimensionality_reduction',
        
        # Utility functions from crash course
        'mysqrt': 'dsl.c02_crash_course.e0203_functions',
        'strength': 'dsl.c06_probability.e0604_binom',
    }
    
    # Create dynamic strategies for all functions
    for func_name, module_path in module_mappings.items():
        try:
            functions[func_name] = create_dynamic_strategy(module_path, func_name)
        except ImportError as e:
            print(f"Warning: Could not import {func_name} from {module_path}: {e}")
    
    return functions


# Create all dynamic strategies
dynamic_strategies = get_all_library_functions()
