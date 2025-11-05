import os
import inspect
import importlib
from typing import Any, Dict

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def create_dynamic_strategy(module_path: str, function_name: str):
    """Dynamically create a strategy function that wraps a library function"""
    
    def dynamic_strategy(self, body: Dict[str, Any]):
        try:
            # Import the module and get the function
            module = importlib.import_module(module_path)
            func = getattr(module, function_name)
            
            # Get function signature to extract parameters
            sig = inspect.signature(func)
            parameters = list(sig.parameters.keys())
            
            # Extract arguments from body, handling defaults
            kwargs = {}
            for param in parameters:
                if param in body:
                    kwargs[param] = body[param]
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
    
    # Define the module mappings
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
        
        # Hypothesis and Inference
        'normal_upper_bound': 'dsl.c07_hypothesis_and_inference.e0702_normal_bounds',
        'normal_lower_bound': 'dsl.c07_hypothesis_and_inference.e0702_normal_bounds',
        'normal_two_sided_bounds': 'dsl.c07_hypothesis_and_inference.e0702_normal_bounds',
        'normal_approximation_to_binomial': 'dsl.c07_hypothesis_and_inference.e0701_coin_flip',
        'normal_probability_above': 'dsl.c07_hypothesis_and_inference.e0701_coin_flip',
        'normal_probability_between': 'dsl.c07_hypothesis_and_inference.e0701_coin_flip',
        'normal_probability_outside': 'dsl.c07_hypothesis_and_inference.e0701_coin_flip',
        'two_sided_p_value': 'dsl.c07_hypothesis_and_inference.e0703_pvalues',
        'count_extreme_values': 'dsl.c07_hypothesis_and_inference.e0703_pvalues',
        'estimated_parameters': 'dsl.c07_hypothesis_and_inference.e0705_a_b',
        'a_b_test_statistic': 'dsl.c07_hypothesis_and_inference.e0705_a_b',
        'normalizer': 'dsl.c07_hypothesis_and_inference.e0706_bayesian_inference',
        'beta_pdf': 'dsl.c07_hypothesis_and_inference.e0706_bayesian_inference',
        
        # K Nearest Neighbors
        'raw_majority_vote': 'dsl.c12_k_nearest_neighbors.nearest_neighbors',
        'majority_vote': 'dsl.c12_k_nearest_neighbors.nearest_neighbors',
        'knn_classify': 'dsl.c12_k_nearest_neighbors.nearest_neighbors',
        'random_point': 'dsl.c12_k_nearest_neighbors.nearest_neighbors',
        'random_distances': 'dsl.c12_k_nearest_neighbors.nearest_neighbors',
        'get_distances': 'dsl.c12_k_nearest_neighbors.nearest_neighbors',
        'try_several_k': 'dsl.c12_k_nearest_neighbors.nearest_neighbors',
        
        # Simple Linear Regression
        'predict': 'dsl.c14_simple_linear_regression.simple_linear_regression',
        'error': 'dsl.c14_simple_linear_regression.simple_linear_regression',
        'sum_of_squared_errors': 'dsl.c14_simple_linear_regression.simple_linear_regression',
        'least_squares_fit': 'dsl.c14_simple_linear_regression.simple_linear_regression',
        'total_sum_of_squares': 'dsl.c14_simple_linear_regression.simple_linear_regression',
        'r_squared': 'dsl.c14_simple_linear_regression.simple_linear_regression',
        'squared_error': 'dsl.c14_simple_linear_regression.simple_linear_regression',
        'squared_error_gradient': 'dsl.c14_simple_linear_regression.simple_linear_regression',
        
        # Multiple Regression
        'predict_multiple': 'dsl.c15_multiple_regression.multiple_regression',
        'error_multiple': 'dsl.c15_multiple_regression.multiple_regression',
        'squared_error_multiple': 'dsl.c15_multiple_regression.multiple_regression',
        'squared_error_gradient_multiple': 'dsl.c15_multiple_regression.multiple_regression',
        'estimate_beta': 'dsl.c15_multiple_regression.multiple_regression',
        'multiple_r_squared': 'dsl.c15_multiple_regression.multiple_regression',
        'bootstrap_sample': 'dsl.c15_multiple_regression.multiple_regression',
        'bootstrap_statistic': 'dsl.c15_multiple_regression.multiple_regression',
        'estimate_sample_beta': 'dsl.c15_multiple_regression.multiple_regression',
        'p_value': 'dsl.c15_multiple_regression.multiple_regression',
        'ridge_penalty': 'dsl.c15_multiple_regression.multiple_regression',
        'squared_error_ridge': 'dsl.c15_multiple_regression.multiple_regression',
        'ridge_penalty_gradient': 'dsl.c15_multiple_regression.multiple_regression',
        'squared_error_ridge_gradient': 'dsl.c15_multiple_regression.multiple_regression',
        'estimate_beta_ridge': 'dsl.c15_multiple_regression.multiple_regression',
        'lasso_penalty': 'dsl.c15_multiple_regression.multiple_regression',
        
        # Logistic Regression
        'logistic': 'dsl.c16_logistic_regression.logistic_regression',
        'logistic_prime': 'dsl.c16_logistic_regression.logistic_regression',
        'logistic_log_likelihood_i': 'dsl.c16_logistic_regression.logistic_regression',
        'logistic_log_likelihood': 'dsl.c16_logistic_regression.logistic_regression',
        'logistic_log_partial_ij': 'dsl.c16_logistic_regression.logistic_regression',
        'logistic_log_gradient_i': 'dsl.c16_logistic_regression.logistic_regression',
        'logistic_log_gradient': 'dsl.c16_logistic_regression.logistic_regression',
        'score_logistic': 'dsl.c16_logistic_regression.logistic_regression',
        'logistic_fit': 'dsl.c16_logistic_regression.logistic_regression',
        
        # Decision Trees
        'entropy': 'dsl.c17_decision_trees.decision_trees',
        'get_class_probabilities': 'dsl.c17_decision_trees.decision_trees',
        'data_entropy': 'dsl.c17_decision_trees.decision_trees',
        'partition_entropy': 'dsl.c17_decision_trees.decision_trees',
        'group_by': 'dsl.c17_decision_trees.decision_trees',
        'partition_by': 'dsl.c17_decision_trees.decision_trees',
        'partition_entropy_by': 'dsl.c17_decision_trees.decision_trees',
        'classify_tree': 'dsl.c17_decision_trees.decision_trees',
        'build_tree_id3': 'dsl.c17_decision_trees.decision_trees',
        'forest_classify': 'dsl.c17_decision_trees.decision_trees',
        
        # Neural Networks
        'step_function': 'dsl.c18_neural_networks.neural_networks',
        'perceptron_output': 'dsl.c18_neural_networks.neural_networks',
        'sigmoid': 'dsl.c18_neural_networks.neural_networks',
        'neuron_output': 'dsl.c18_neural_networks.neural_networks',
        'feed_forward': 'dsl.c18_neural_networks.neural_networks',
        'backpropagation': 'dsl.c18_neural_networks.neural_networks',
        
        # Deep Learning
        'make_digit': 'dsl.c19_deep_learning.e01_neural_networks',
        'create_network': 'dsl.c19_deep_learning.e01_neural_networks',
        'fit_network': 'dsl.c19_deep_learning.e01_neural_networks',
        'predict_network': 'dsl.c19_deep_learning.e01_neural_networks',
        'predict_vector': 'dsl.c19_deep_learning.e01_neural_networks',
        'predict_batch': 'dsl.c19_deep_learning.e01_neural_networks',
        
        # Clustering
        'squared_clustering_errors': 'dsl.c20_clustering.clustering',
        'is_leaf': 'dsl.c20_clustering.clustering',
        'get_children': 'dsl.c20_clustering.clustering',
        'get_values': 'dsl.c20_clustering.clustering',
        'cluster_distance': 'dsl.c20_clustering.clustering',
        'get_merge_order': 'dsl.c20_clustering.clustering',
        'bottom_up_cluster': 'dsl.c20_clustering.clustering',
        'generate_clusters': 'dsl.c20_clustering.clustering',
        
        # Natural Language Processing
        'tokenize': 'dsl.c21_natural_language_processing.naive_bayes',
        
        # Network Analysis
        'populate_endorsements': 'dsl.c22_network_analysis.network_analysis',
        'get_page_ranks': 'dsl.c22_network_analysis.network_analysis',
        'get_eigenvector_centrality': 'dsl.c22_network_analysis.network_analysis',
        'populate_endorsments': 'dsl.c22_network_analysis.network_analysis',
        'compute_eigenvectors': 'dsl.c22_network_analysis.network_analysis',
        'construct_adjacency': 'dsl.c22_network_analysis.network_analysis',
        'get_closeness': 'dsl.c22_network_analysis.network_analysis',
        'get_betweeness': 'dsl.c22_network_analysis.network_analysis',
        'populate_closeness': 'dsl.c22_network_analysis.network_analysis',
        'populate_shortest_paths': 'dsl.c22_network_analysis.network_analysis',
        'populate_betweeness_v1': 'dsl.c22_network_analysis.network_analysis',
        'initialize_centrality': 'dsl.c22_network_analysis.network_analysis',
        'process_shortest_paths': 'dsl.c22_network_analysis.network_analysis',
        'update_centrality': 'dsl.c22_network_analysis.network_analysis',
        'populate_betweeness': 'dsl.c22_network_analysis.network_analysis',
        'populate_friends': 'dsl.c22_network_analysis.network_analysis',
        'shortest_paths_from': 'dsl.c22_network_analysis.network_analysis',
        'farness': 'dsl.c22_network_analysis.network_analysis',
        'matrix_product_entry': 'dsl.c22_network_analysis.network_analysis',
        'matrix_multiply': 'dsl.c22_network_analysis.network_analysis',
        'vector_as_matrix': 'dsl.c22_network_analysis.network_analysis',
        'vector_from_matrix': 'dsl.c22_network_analysis.network_analysis',
        'matrix_operate': 'dsl.c22_network_analysis.network_analysis',
        'find_eigenvector': 'dsl.c22_network_analysis.network_analysis',
        'page_rank': 'dsl.c22_network_analysis.network_analysis',
        
        # Recommender Systems
        'most_popular_new_interests': 'dsl.c23_recommender_systems.recommender_systems',
        'cosine_similarity': 'dsl.c23_recommender_systems.recommender_systems',
        'make_user_interest_vector': 'dsl.c23_recommender_systems.recommender_systems',
        'most_similar_users_to': 'dsl.c23_recommender_systems.recommender_systems',
        'user_based_suggestions': 'dsl.c23_recommender_systems.recommender_systems',
        'most_similar_interests_to': 'dsl.c23_recommender_systems.recommender_systems',
        'item_based_suggestions': 'dsl.c23_recommender_systems.recommender_systems',
        
        # Databases
        'word_count_old': 'dsl.c25_mapreduce.mapreduce',
        'wc_mapper': 'dsl.c25_mapreduce.mapreduce',
        'wc_reducer': 'dsl.c25_mapreduce.mapreduce',
        'word_count': 'dsl.c25_mapreduce.mapreduce',
        'map_reduce': 'dsl.c25_mapreduce.mapreduce',
        'reduce_with': 'dsl.c25_mapreduce.mapreduce',
        'values_reducer': 'dsl.c25_mapreduce.mapreduce',
        'most_popular_word_reducer': 'dsl.c25_mapreduce.mapreduce',
        'liker_mapper': 'dsl.c25_mapreduce.mapreduce',
        'matrix_multiply_mapper': 'dsl.c25_mapreduce.mapreduce',
        'matrix_multiply_reducer': 'dsl.c25_mapreduce.mapreduce',
        
        # Naive Bayes
        'word_counter': 'dsl.c13_naive_bayes.naive_bayes',
        'predict_batch': 'dsl.c13_naive_bayes.naive_bayes',
        'read_classifier': 'dsl.c13_naive_bayes.naive_bayes',
        'count_words': 'dsl.c13_naive_bayes.naive_bayes',
        'word_probabilities': 'dsl.c13_naive_bayes.naive_bayes',
        'get_spam_probability': 'dsl.c13_naive_bayes.naive_bayes',
        'get_subject_data': 'dsl.c13_naive_bayes.naive_bayes',
        'p_spam_given_word': 'dsl.c13_naive_bayes.naive_bayes',
        
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
