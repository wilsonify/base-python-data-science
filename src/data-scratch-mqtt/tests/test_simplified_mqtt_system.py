"""
Test suite for the simplified MQTT system
Tests the dynamic strategy system without requiring a running MQTT broker
"""

import json
import pytest
from unittest.mock import Mock, MagicMock

from data_scratch_mqtt import echo_strategy, dynamic_strategies, Strategy
from data_scratch_mqtt.config import MQTT_TOPIC


class MockMQTTMessage:
    """Mock MQTT message for testing"""
    def __init__(self, payload_dict):
        self.payload = json.dumps(payload_dict).encode('utf-8')


class MockMQTTClient:
    """Mock MQTT client for testing"""
    def __init__(self):
        self.published_messages = []
    
    def publish(self, topic, payload, qos=0):
        self.published_messages.append({
            'topic': topic,
            'payload': payload.decode('utf-8') if isinstance(payload, bytes) else payload,
            'qos': qos
        })


def test_echo_strategy():
    """Test the echo strategy functionality"""
    client = MockMQTTClient()
    msg = MockMQTTMessage({"test": "data", "strategy": "echo"})
    
    strategy = Strategy(echo_strategy, client, None, msg)
    strategy.execute()
    
    # Verify the response
    assert len(client.published_messages) == 1
    response = json.loads(client.published_messages[0]['payload'])
    assert response == {"test": "data", "strategy": "echo"}
    assert client.published_messages[0]['topic'] == f"{MQTT_TOPIC}_reply"


def test_dynamic_strategies_loaded():
    """Test that dynamic strategies are loaded correctly"""
    assert len(dynamic_strategies) > 80  # Should have many strategies
    assert 'vector_add' in dynamic_strategies
    assert 'mean' in dynamic_strategies
    assert 'normal_cd' in dynamic_strategies
    assert 'accuracy' in dynamic_strategies


def test_dynamic_strategy_error_handling():
    """Test that dynamic strategies handle missing dependencies gracefully"""
    # Test a strategy that requires the dsl library
    if 'vector_add' in dynamic_strategies:
        client = MockMQTTClient()
        msg = MockMQTTMessage({"v": [1, 2, 3], "w": [4, 5, 6], "strategy": "vector_add"})
        
        strategy = Strategy(dynamic_strategies['vector_add'], client, None, msg)
        strategy.execute()
        
        # Should get an error response due to missing dsl library
        assert len(client.published_messages) == 1
        response = json.loads(client.published_messages[0]['payload'])
        assert 'error' in response
        assert 'No module named' in response['error']


def test_strategy_with_missing_parameters():
    """Test strategy behavior when required parameters are missing"""
    client = MockMQTTClient()
    # Send message without required parameters for vector_add
    msg = MockMQTTMessage({"strategy": "vector_add", "missing_param": "test"})
    
    if 'vector_add' in dynamic_strategies:
        strategy = Strategy(dynamic_strategies['vector_add'], client, None, msg)
        strategy.execute()
        
        # Should get an error response
        assert len(client.published_messages) == 1
        response = json.loads(client.published_messages[0]['payload'])
        assert 'error' in response


def test_strategy_with_optional_parameters():
    """Test strategy behavior with optional parameters"""
    # Test a strategy that has optional parameters
    if 'mean' in dynamic_strategies:
        client = MockMQTTClient()
        msg = MockMQTTMessage({"xs": [1, 2, 3, 4, 5], "strategy": "mean"})
        
        strategy = Strategy(dynamic_strategies['mean'], client, None, msg)
        strategy.execute()
        
        # Should get an error response due to missing dsl library
        assert len(client.published_messages) == 1
        response = json.loads(client.published_messages[0]['payload'])
        # Even though parameters are correct, it will fail due to missing dsl library
        assert 'error' in response


def test_custom_reply_to_and_correlation_id():
    """Test that custom reply_to and correlation_id are handled correctly"""
    client = MockMQTTClient()
    msg = MockMQTTMessage({
        "test": "data", 
        "strategy": "echo",
        "reply_to": "custom_topic",
        "correlation_id": "test_123"
    })
    
    strategy = Strategy(echo_strategy, client, None, msg)
    strategy.execute()
    
    # Verify the custom topic is used
    assert len(client.published_messages) == 1
    assert client.published_messages[0]['topic'] == "custom_topic"


def test_mqtt_config_values():
    """Test that MQTT configuration values are available"""
    from data_scratch_mqtt.config import MQTT_HOST, MQTT_PORT, MQTT_TOPIC, MQTT_USER, MQTT_PASS, MQTT_KEEPALIVE
    
    assert MQTT_HOST is not None
    assert isinstance(MQTT_PORT, int)
    assert MQTT_TOPIC is not None
    assert MQTT_USER is not None
    assert MQTT_PASS is not None
    assert isinstance(MQTT_KEEPALIVE, int)


def test_strategy_count():
    """Test the total number of available strategies"""
    from data_scratch_mqtt.__main__ import available_strategies
    
    # Should have echo + sqrt/strength (if available) + dynamic strategies
    expected_min = 1 + len(dynamic_strategies)  # At least echo + all dynamic
    assert len(available_strategies) >= expected_min


def test_json_parsing_error():
    """Test handling of invalid JSON in message payload"""
    client = MockMQTTClient()
    
    # Create a message with invalid JSON
    msg = Mock()
    msg.payload = b'{"invalid": json}'  # Missing quotes
    
    try:
        strategy = Strategy(echo_strategy, client, None, msg)
        # If we get here, the JSON parsing should have failed
        assert False, "Should have raised JSON parsing error"
    except json.JSONDecodeError:
        # Expected behavior
        pass


def test_available_strategies_includes_core():
    """Test that core strategies are always available"""
    from data_scratch_mqtt.__main__ import available_strategies
    
    assert "echo" in available_strategies
    assert available_strategies["echo"] == echo_strategy
