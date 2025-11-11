#!/usr/bin/env python3
"""
Simple test to verify the simplified MQTT system works correctly
"""

import os
import json
import pytest

def test_imports():
    """Test that all imports work correctly"""
    print("Testing imports...")
    
    # Test basic imports
    from data_scratch_mqtt import echo_strategy, Strategy, MQTT_HOST, MQTT_PORT
    print("✓ Basic imports successful")
    
    # Test dynamic strategies
    from data_scratch_mqtt import dynamic_strategies
    print(f"✓ Dynamic strategies loaded: {len(dynamic_strategies)} strategies")
    
    # Test that key strategies are available
    key_strategies = ['vector_add', 'mean', 'normal_cdf', 'accuracy']
    for strategy in key_strategies:
        assert strategy in dynamic_strategies, f"{strategy} strategy missing"
        print(f"✓ {strategy} strategy available")

def test_strategy_functionality():
    """Test that strategies work correctly"""
    print("\nTesting strategy functionality...")
    
    from data_scratch_mqtt import echo_strategy, Strategy
    
    # Mock MQTT client for testing
    class MockMQTTClient:
        def __init__(self):
            self.published_messages = []
        
        def publish(self, topic, payload, qos=0):
            self.published_messages.append({
                'topic': topic,
                'payload': payload.decode('utf-8') if isinstance(payload, bytes) else payload,
                'qos': qos
            })
    
    # Mock message
    class MockMessage:
        def __init__(self, payload):
            self.payload = json.dumps(payload).encode('utf-8')
    
    # Test echo strategy
    client = MockMQTTClient()
    msg = MockMessage({"test": "data", "strategy": "echo"})
    
    strategy = Strategy(echo_strategy, client, None, msg)
    strategy.execute()  # Don't pass arguments - Strategy class handles payload parsing
    
    # Verify the response
    assert len(client.published_messages) == 1, "Expected 1 published message"
    response = json.loads(client.published_messages[0]['payload'])
    assert response == {"test": "data", "strategy": "echo"}, f"Echo strategy response incorrect: {response}"
    print("✓ Echo strategy works correctly")

def test_dynamic_strategy_error_handling():
    """Test that dynamic strategies handle missing dependencies gracefully"""
    print("\nTesting dynamic strategy error handling...")
    
    from data_scratch_mqtt import dynamic_strategies, Strategy
    
    # Test a strategy that requires the dsl library
    if 'vector_add' in dynamic_strategies:
        # Mock MQTT client for testing
        class MockMQTTClient:
            def __init__(self):
                self.published_messages = []
            
            def publish(self, topic, payload, qos=0):
                self.published_messages.append({
                    'topic': topic,
                    'payload': payload.decode('utf-8') if isinstance(payload, bytes) else payload,
                    'qos': qos
                })
        
        # Mock message
        class MockMessage:
            def __init__(self, payload):
                self.payload = json.dumps(payload).encode('utf-8')
        
        client = MockMQTTClient()
        msg = MockMessage({"v": [1, 2, 3], "w": [4, 5, 6], "strategy": "vector_add"})
        
        strategy = Strategy(dynamic_strategies['vector_add'], client, None, msg)
        strategy.execute()  # Don't pass arguments - Strategy class handles payload parsing
        
        # Verify the error response
        assert len(client.published_messages) == 1, "Expected 1 published message"
        response = json.loads(client.published_messages[0]['payload'])
        assert 'error' in response and 'No module named' in response['error'], f"Unexpected response: {response}"
        print("✓ Dynamic strategy handles missing dependencies correctly")
    else:
        pytest.skip("vector_add strategy not available for testing")

def main():
    """Run all tests"""
    print("Testing Simplified MQTT System")
    print("=" * 50)
    
    success = True
    
    # Run tests
    success &= test_imports()
    success &= test_strategy_functionality()
    success &= test_dynamic_strategy_error_handling()
    
    print("\n" + "=" * 50)
    if success:
        print("🎉 All tests passed! MQTT system is simplified and working correctly.")
    else:
        print("⚠ Some tests failed. Please check the implementation.")
    
    return success

if __name__ == "__main__":
    main()
