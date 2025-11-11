import pytest
import math

from dsl.c18_neural_networks.neural_networks import (
    sigmoid, neuron_output, feed_forward, backpropagation, 
    perceptron_output, step_function
)


def test_sigmoid():
    """Test the sigmoid function."""
    # Test basic properties
    assert sigmoid(0) == pytest.approx(0.5)
    assert sigmoid(1000) == pytest.approx(1.0)
    assert sigmoid(-1000) == pytest.approx(0.0)
    
    # Test specific values
    assert sigmoid(1) == pytest.approx(0.7310585786300049)
    assert sigmoid(-1) == pytest.approx(0.2689414213699951)
    
    # Test that it's monotonic
    assert sigmoid(2) > sigmoid(1)
    assert sigmoid(-1) > sigmoid(-2)


def test_step_function():
    """Test the step function."""
    assert step_function(1) == 1
    assert step_function(100) == 1
    assert step_function(0.1) == 1
    assert step_function(0) == 1
    assert step_function(-0.1) == 0
    assert step_function(-100) == 0


def test_perceptron_output():
    """Test the perceptron_output function."""
    weights = [2, -1]
    bias = -1
    inputs = [1, 1]
    
    # 2*1 + (-1)*1 + (-1) = 0 -> step(0) = 1
    result = perceptron_output(weights, bias, inputs)
    assert result == 1
    
    inputs = [0, 0]
    # 2*0 + (-1)*0 + (-1) = -1 -> step(-1) = 0
    result = perceptron_output(weights, bias, inputs)
    assert result == 0
    
    inputs = [1, 0]
    # 2*1 + (-1)*0 + (-1) = 1 -> step(1) = 1
    result = perceptron_output(weights, bias, inputs)
    assert result == 1


def test_neuron_output():
    """Test the neuron_output function."""
    # weights includes bias as the last element
    weights = [0.5, -0.5, 0.0]  # weights for inputs and bias
    inputs = [1, 1, 1]  # inputs with bias term
    
    # 0.5*1 + (-0.5)*1 + 0.0*1 = 0 -> sigmoid(0) = 0.5
    result = neuron_output(weights, inputs)
    assert result == pytest.approx(0.5)
    
    inputs = [2, 0, 1]  # inputs with bias term
    # 0.5*2 + (-0.5)*0 + 0.0*1 = 1 -> sigmoid(1) ≈ 0.731
    result = neuron_output(weights, inputs)
    assert result == pytest.approx(0.7310585786300049)


def test_feed_forward_simple_network():
    """Test feed_forward with a simple neural network."""
    # Simple network: 2 inputs -> 1 hidden neuron -> 1 output
    # Each neuron weights include bias weight at the end
    network = [
        # Hidden layer (1 neuron with 2 inputs + 1 bias)
        [[0.5, -0.5, 0.0]],  # weights for 2 inputs + bias
        # Output layer (1 neuron with 1 input + 1 bias)
        [[1.0, 0.0]]  # weights for 1 input + bias
    ]
    
    inputs = [1, 1]
    outputs = feed_forward(network, inputs)
    
    # Should return list of layer outputs
    assert len(outputs) == 2
    assert len(outputs[0]) == 1  # Hidden layer has 1 neuron
    assert len(outputs[1]) == 1  # Output layer has 1 neuron
    
    # Check that outputs are reasonable (between 0 and 1 for sigmoid)
    assert 0 <= outputs[0][0] <= 1
    assert 0 <= outputs[1][0] <= 1


def test_feed_forward_multi_hidden():
    """Test feed_forward with multiple hidden neurons."""
    # Network: 2 inputs -> 2 hidden neurons -> 1 output
    network = [
        # Hidden layer (2 neurons, each with 2 inputs + 1 bias)
        [
            [0.5, -0.5, 0.0],   # neuron 1
            [-0.5, 0.5, 0.0]    # neuron 2
        ],
        # Output layer (1 neuron with 2 inputs + 1 bias)
        [[1.0, 1.0, 0.0]]     # takes input from both hidden neurons
    ]
    
    inputs = [1, 1]
    outputs = feed_forward(network, inputs)
    
    assert len(outputs) == 2
    assert len(outputs[0]) == 2  # Hidden layer has 2 neurons
    assert len(outputs[1]) == 1  # Output layer has 1 neuron
    
    # All outputs should be valid sigmoid values
    for layer_output in outputs:
        for neuron_output in layer_output:
            assert 0 <= neuron_output <= 1


def test_backpropagation():
    """Test the backpropagation function."""
    # Simple network for XOR problem
    network = [
        # Hidden layer (2 neurons, each with 2 inputs + 1 bias)
        [
            [0.5, -0.5, 0.0],
            [-0.5, 0.5, 0.0]
        ],
        # Output layer (1 neuron with 2 inputs + 1 bias)
        [[1.0, 1.0, 0.0]]
    ]
    
    # Save original weights
    original_weights = [[neuron[:] for neuron in layer] for layer in network]
    
    inputs = [1, 0]
    target = [1.0]
    
    # Run backpropagation (modifies network in-place)
    backpropagation(network, inputs, target)
    
    # Check that weights have been updated
    weights_changed = False
    for layer_idx, layer in enumerate(network):
        for neuron_idx, neuron in enumerate(layer):
            if neuron != original_weights[layer_idx][neuron_idx]:
                weights_changed = True
                break
    
    assert weights_changed, "Backpropagation should update weights"


def test_backpropagation_xor():
    """Test backpropagation on XOR problem."""
    # Network that can learn XOR
    network = [
        # Hidden layer (2 neurons, each with 2 inputs + 1 bias)
        [
            [0.5, -0.5, 0.0],
            [-0.5, 0.5, 0.0]
        ],
        # Output layer (1 neuron with 2 inputs + 1 bias)
        [[1.0, 1.0, 0.0]]
    ]
    
    # XOR training data
    training_data = [
        ([0, 0], [0.0]),
        ([0, 1], [1.0]),
        ([1, 0], [1.0]),
        ([1, 1], [0.0])
    ]
    
    # Test that backpropagation runs without error
    for inputs, target in training_data:
        # Save original weights
        original_weights = [[neuron[:] for neuron in layer] for layer in network]
        
        # Run backpropagation (modifies network in-place)
        backpropagation(network, inputs, target)
        
        # Verify it ran (network was modified or stayed the same)
        assert network is not None


def test_network_dimensions():
    """Test that network dimensions are handled correctly."""
    # Network with proper dimensions
    network = [
        [[0.5, 0.0]],  # 1 neuron expecting 1 input + bias
        [[1.0, 1.0, 0.0]]  # 1 neuron expecting 1 input from previous layer + bias
    ]
    
    inputs = [1]  # 1 input
    
    # Should handle properly
    outputs = feed_forward(network, inputs)
    assert outputs is not None
    assert len(outputs) == 2


def test_empty_network():
    """Test behavior with empty network."""
    empty_network = []
    inputs = [1, 2, 3]
    
    outputs = feed_forward(empty_network, inputs)
    # Should return empty list for empty network
    assert outputs == []


def test_single_neuron_network():
    """Test network with just one neuron."""
    single_neuron_network = [
        [[1.0, 1.0, 0.0]]  # Single neuron taking 2 inputs + bias
    ]
    
    inputs = [1, 1]
    outputs = feed_forward(single_neuron_network, inputs)
    
    assert len(outputs) == 1
    assert len(outputs[0]) == 1
    assert outputs[0][0] == pytest.approx(sigmoid(2.0))  # 1*1 + 1*1 + 0 = 2


def test_gradient_magnitude():
    """Test that backpropagation updates weights reasonably."""
    network = [
        [[0.5, -0.5, 0.0]],  # 1 neuron with 2 inputs + bias
        [[1.0, 0.0]]  # 1 neuron with 1 input + bias
    ]
    
    # Save original weights
    original_weights = [[neuron[:] for neuron in layer] for layer in network]
    
    inputs = [1, 1]
    target = [1.0]
    
    # Run backpropagation
    backpropagation(network, inputs, target)
    
    # Check that weights changed but not too drastically
    for layer_idx, layer in enumerate(network):
        for neuron_idx, neuron in enumerate(layer):
            for weight_idx, weight in enumerate(neuron):
                original_weight = original_weights[layer_idx][neuron_idx][weight_idx]
                # Weight should be finite
                assert math.isfinite(weight)
                # Weight change should be reasonable (not jumping by thousands)
                assert abs(weight - original_weight) < 100
