"""
Comprehensive tests for the dynamic strategy system
"""

import os
import unittest
from unittest.mock import Mock, patch
import inspect

# Import from the built package (no sys.path manipulation)
from data_scratch_amqp.strategies_library.dynamic_strategy import (
    create_dynamic_strategy, 
    get_all_library_functions, 
    dynamic_strategies
)


class TestDynamicStrategy(unittest.TestCase):
    """Test the dynamic strategy creation and functionality"""

    def setUp(self):
        """Set up test fixtures"""
        self.mock_channel = Mock()
        self.mock_method = Mock()
        self.mock_props = Mock()
        self.mock_publish = Mock()
        
        # Create a mock strategy class with captured references
        mock_channel = self.mock_channel
        mock_method = self.mock_method
        mock_props = self.mock_props
        mock_publish = self.mock_publish
        
        class MockStrategy:
            def __init__(self):
                self.channel = mock_channel
                self.method = mock_method
                self.props = mock_props
                
            def publish(self, payload):
                mock_publish(payload)
        
        self.mock_strategy = MockStrategy()

    def test_create_dynamic_strategy_basic(self):
        """Test basic dynamic strategy creation"""
        # Test with a simple function
        def test_func(x, y=10):
            return x + y
        
        # Create a dynamic strategy
        strategy_func = create_dynamic_strategy("__main__", "test_func")
        
        # Mock the module import
        with patch('data_scratch_amqp.strategies_library.dynamic_strategy.importlib.import_module') as mock_import:
            mock_module = Mock()
            mock_module.test_func = test_func
            mock_import.return_value = mock_module
            
            # Bind the strategy to mock instance
            bound_strategy = strategy_func.__get__(self.mock_strategy, type(self.mock_strategy))
            
            # Test the strategy
            bound_strategy({"x": 5, "y": 3})
            
            # Check that publish was called with correct result
            self.mock_publish.assert_called_once_with(8)

    def test_create_dynamic_strategy_with_defaults(self):
        """Test dynamic strategy with default parameters"""
        def test_func(x, y=10, z=20):
            return x + y + z
        
        strategy_func = create_dynamic_strategy("__main__", "test_func")
        
        with patch('data_scratch_amqp.strategies_library.dynamic_strategy.importlib.import_module') as mock_import:
            mock_module = Mock()
            mock_module.test_func = test_func
            mock_import.return_value = mock_module
            
            bound_strategy = strategy_func.__get__(self.mock_strategy, type(self.mock_strategy))
            
            # Test with missing default parameter
            bound_strategy({"x": 5})
            self.mock_publish.assert_called_with(35)  # 5 + 10 + 20

    def test_create_dynamic_strategy_error_handling(self):
        """Test error handling in dynamic strategies"""
        strategy_func = create_dynamic_strategy("nonexistent.module", "nonexistent_func")
        
        bound_strategy = strategy_func.__get__(self.mock_strategy, type(self.mock_strategy))
        
        # Test with nonexistent module
        bound_strategy({"x": 5})
        
        # Should publish error information
        call_args = self.mock_publish.call_args[0][0]
        self.assertIn('error', call_args)
        self.assertIn('function', call_args)
        self.assertIn('module', call_args)

    def test_get_all_library_functions(self):
        """Test that all library functions are discovered"""
        functions = get_all_library_functions()
        
        # Check that we have a reasonable number of functions
        self.assertGreater(len(functions), 200)
        
        # Check that key functions are present
        key_functions = [
            'vector_add', 'dot', 'magnitude', 'mean', 'median',
            'normal_cdf', 'bernoulli_trial', 'accuracy', 'split_data',
            'knn_classify', 'logistic', 'entropy', 'page_rank'
        ]
        
        for func_name in key_functions:
            self.assertIn(func_name, functions)
        
        # Check that all functions are callable
        for func_name, func in functions.items():
            self.assertTrue(callable(func))

    def test_dynamic_strategies_global(self):
        """Test the global dynamic_strategies dictionary"""
        # Should be populated
        self.assertGreater(len(dynamic_strategies), 200)
        
        # Should contain key functions
        key_functions = ['vector_add', 'mean', 'normal_cdf', 'accuracy']
        for func_name in key_functions:
            self.assertIn(func_name, dynamic_strategies)

    def test_strategy_signature_detection(self):
        """Test that strategy signatures are correctly detected"""
        def test_func(a, b, c=10, *args, **kwargs):
            return a + b + c
        
        strategy_func = create_dynamic_strategy("__main__", "test_func")
        
        with patch('data_scratch_amqp.strategies_library.dynamic_strategy.importlib.import_module') as mock_import:
            mock_module = Mock()
            mock_module.test_func = test_func
            mock_import.return_value = mock_module
            
            bound_strategy = strategy_func.__get__(self.mock_strategy, type(self.mock_strategy))
            
            # Should handle positional and keyword arguments
            bound_strategy({"a": 1, "b": 2})
            self.mock_publish.assert_called_with(13)  # 1 + 2 + 10

    def test_strategy_parameter_extraction(self):
        """Test parameter extraction from request body"""
        def test_func(required_param, optional_param="default", another_optional=42):
            return f"{required_param}-{optional_param}-{another_optional}"
        
        strategy_func = create_dynamic_strategy("__main__", "test_func")
        
        with patch('data_scratch_amqp.strategies_library.dynamic_strategy.importlib.import_module') as mock_import:
            mock_module = Mock()
            mock_module.test_func = test_func
            mock_import.return_value = mock_module
            
            bound_strategy = strategy_func.__get__(self.mock_strategy, type(self.mock_strategy))
            
            # Test with only required parameter
            bound_strategy({"required_param": "test"})
            self.mock_publish.assert_called_with("test-default-42")
            
            # Test with some optional parameters
            bound_strategy({"required_param": "test", "optional_param": "custom"})
            self.mock_publish.assert_called_with("test-custom-42")

    def test_module_mapping_coverage(self):
        """Test that module mappings cover major categories"""
        functions = get_all_library_functions()
        
        # Count functions by category (based on module paths)
        categories = {}
        for func_name in functions.keys():
            # This is a simplified categorization based on function names
            if any(word in func_name for word in ['vector', 'matrix', 'dot', 'magnitude', 'distance']):
                categories['linear_algebra'] = categories.get('linear_algebra', 0) + 1
            elif any(word in func_name for word in ['mean', 'median', 'variance', 'correlation', 'covariance']):
                categories['statistics'] = categories.get('statistics', 0) + 1
            elif any(word in func_name for word in ['normal', 'bernoulli', 'binomial', 'uniform']):
                categories['probability'] = categories.get('probability', 0) + 1
            elif any(word in func_name for word in ['gradient', 'minimize', 'maximize']):
                categories['gradient_descent'] = categories.get('gradient_descent', 0) + 1
            elif any(word in func_name for word in ['accuracy', 'precision', 'recall', 'f1', 'split_data']):
                categories['machine_learning'] = categories.get('machine_learning', 0) + 1
        
        # Should have functions from major categories
        expected_categories = ['linear_algebra', 'statistics', 'probability', 'gradient_descent', 'machine_learning']
        for category in expected_categories:
            self.assertIn(category, categories)
            self.assertGreater(categories[category], 0, f"Should have functions in {category}")


class TestStrategyIntegration(unittest.TestCase):
    """Test integration with the AMQP system"""

    def test_strategy_binding(self):
        """Test that strategies can be properly bound to strategy instances"""
        # Test that dynamic strategies can be bound like instance methods
        sample_func = list(dynamic_strategies.values())[0]
        
        class TestStrategy:
            def publish(self, payload):
                self.published = payload
        
        strategy = TestStrategy()
        bound_func = sample_func.__get__(strategy, TestStrategy)
        
        # Should be callable
        self.assertTrue(callable(bound_func))

    def test_error_handling_integration(self):
        """Test error handling in the full integration"""
        strategy_func = create_dynamic_strategy("nonexistent.module", "nonexistent_func")
        
        class TestStrategy:
            def __init__(self):
                self.published = None
                
            def publish(self, payload):
                self.published = payload
        
        strategy = TestStrategy()
        bound_func = strategy_func.__get__(strategy, TestStrategy)
        
        # Execute with error
        bound_func({"test": "data"})
        
        # Should have published error info
        self.assertIsNotNone(strategy.published)
        self.assertIn('error', strategy.published)


if __name__ == '__main__':
    unittest.main()
