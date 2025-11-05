"""
Test to ensure the circular import issue is resolved
"""

import unittest
import sys
import os

# Add the src directory to the path for testing
sys.path.insert(0, os.path.dirname(__file__))

class TestCircularImportFix(unittest.TestCase):
    """Test that the circular import issue is completely resolved"""
    
    def test_import_routing_key_from_main_module(self):
        """Test the original failing import"""
        # This was the original failing import
        from data_scratch_amqp import routing_key
        self.assertIsNotNone(routing_key)
        self.assertIsInstance(routing_key, str)
    
    def test_import_all_main_exports(self):
        """Test that all main module exports work"""
        try:
            from data_scratch_amqp import (
                Strategy, 
                echo_strategy, 
                routing_key, 
                amqp_host, 
                amqp_port, 
                heartbeat, 
                timeout
            )
            self.assertIsNotNone(Strategy)
            self.assertIsNotNone(echo_strategy)
            self.assertIsNotNone(routing_key)
            self.assertIsNotNone(amqp_host)
            self.assertIsNotNone(amqp_port)
            self.assertIsNotNone(heartbeat)
            self.assertIsNotNone(timeout)
        except ImportError as e:
            self.fail(f"Import failed: {e}")
    
    def test_dynamic_strategies_import(self):
        """Test that dynamic strategies can be imported (even if empty due to missing dsl)"""
        try:
            from data_scratch_amqp.strategies_library.dynamic_strategy import (
                create_dynamic_strategy,
                get_all_library_functions,
                dynamic_strategies
            )
            self.assertIsNotNone(create_dynamic_strategy)
            self.assertIsNotNone(get_all_library_functions)
            self.assertIsInstance(dynamic_strategies, dict)
        except ImportError as e:
            self.fail(f"Dynamic strategy import failed: {e}")
    
    def test_strategy_class_can_be_instantiated(self):
        """Test that Strategy class can be imported and used"""
        from data_scratch_amqp.strategies_library.abstract import Strategy
        
        # Mock the required parameters
        class MockChannel:
            def basic_publish(self, **kwargs):
                pass
        
        class MockMethod:
            pass
        
        class MockProps:
            def __init__(self):
                self.reply_to = "test_exchange"
                self.correlation_id = "test_id"
        
        def dummy_strategy(self, body):
            self.publish({"result": "test"})
        
        # Should be able to create Strategy instance
        strategy = Strategy(dummy_strategy, MockChannel(), MockMethod(), MockProps())
        self.assertIsNotNone(strategy)
        self.assertEqual(strategy.name, "Default Strategy")
    
    def test_no_circular_import_in_publish_method(self):
        """Test that the publish method can access routing_key without circular import"""
        from data_scratch_amqp.strategies_library.abstract import Strategy
        
        # Mock the required parameters
        published_payload = None
        
        class MockChannel:
            def basic_publish(self, exchange, routing_key, properties, body):
                nonlocal published_payload
                published_payload = {
                    'exchange': exchange,
                    'routing_key': routing_key,
                    'properties': properties,
                    'body': body
                }
        
        class MockMethod:
            pass
        
        class MockProps:
            def __init__(self):
                self.reply_to = "test_exchange"
                self.correlation_id = "test_id"
        
        def dummy_strategy(self, body):
            self.publish({"result": "test"})
        
        strategy = Strategy(dummy_strategy, MockChannel(), MockMethod(), MockProps())
        
        # This should work without circular import
        strategy.publish({"test": "data"})
        
        # Verify the publish was called with correct routing_key
        self.assertIsNotNone(published_payload)
        self.assertEqual(published_payload['routing_key'], "dsfs")  # default value

if __name__ == '__main__':
    unittest.main()
