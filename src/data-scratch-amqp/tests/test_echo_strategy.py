"""
Test for the basic echo strategy
"""

import unittest
import sys
import os
from unittest.mock import Mock

# Add the src directory to the path for testing
sys.path.insert(0, os.path.dirname(__file__))

class TestEchoStrategy(unittest.TestCase):
    """Test the echo strategy functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.mock_channel = Mock()
        self.mock_method = Mock()
        self.mock_props = Mock()
        self.mock_publish = Mock()
        
        # Create a mock strategy class
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
    
    def test_echo_strategy_import(self):
        """Test that echo_strategy can be imported"""
        from data_scratch_amqp import echo_strategy
        self.assertIsNotNone(echo_strategy)
        self.assertTrue(callable(echo_strategy))
    
    def test_echo_strategy_functionality(self):
        """Test that echo_strategy works correctly"""
        from data_scratch_amqp import echo_strategy
        
        # Bind the strategy to mock instance
        bound_strategy = echo_strategy.__get__(self.mock_strategy, type(self.mock_strategy))
        
        # Test data
        test_data = {"message": "hello", "value": 42}
        
        # Execute the strategy
        bound_strategy(test_data)
        
        # Verify publish was called with the echo data
        self.mock_publish.assert_called_once_with(test_data)
    
    def test_echo_strategy_with_different_data_types(self):
        """Test echo_strategy with various data types"""
        from data_scratch_amqp import echo_strategy
        
        # Bind the strategy to mock instance
        bound_strategy = echo_strategy.__get__(self.mock_strategy, type(self.mock_strategy))
        
        test_cases = [
            {"string": "test"},
            {"number": 123},
            {"list": [1, 2, 3]},
            {"nested": {"inner": "value"}},
            {"mixed": [1, "two", {"three": 3}]}
        ]
        
        for test_data in test_cases:
            with self.subTest(test_data=test_data):
                self.mock_publish.reset_mock()
                bound_strategy(test_data)
                self.mock_publish.assert_called_once_with(test_data)

if __name__ == '__main__':
    unittest.main()
