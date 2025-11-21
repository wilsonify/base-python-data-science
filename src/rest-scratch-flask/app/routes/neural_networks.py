from flask import Blueprint, request, jsonify
import random

from dsl.c18_neural_networks.neural_networks import (
    sigmoid, step_function, perceptron_output, neuron_output,
    feed_forward, backpropagation
)

neural_networks_bp = Blueprint('neural_networks', __name__)

# Common response messages
ERR_NO_JSON = 'No JSON data provided'
INPUTS_MUST_BE_LIST = 'inputs must be a list'


def _validate_layer(i, layer):
    """Validate a single layer description and return flattened neuron weights with bias.

    Expected layer format: [weights, bias]
    """
    if not isinstance(layer, list) or len(layer) != 2:
        raise ValueError(f'Layer {i} must be [weights, bias]')

    weights, bias = layer
    if not isinstance(weights, list):
        raise ValueError(f'Weights in layer {i} must be a list')

    if not isinstance(bias, (int, float)):
        raise ValueError(f'Bias in layer {i} must be a number')

    return list(weights) + [bias]

@neural_networks_bp.route('/sigmoid', methods=['POST'])
def calculate_sigmoid():
    """
    Calculate sigmoid activation function.
    
    Request body:
    {
        "x": 1.0
    }
    """
    try:
        data = request.get_json(silent=True)
        
        if not data:
            return jsonify({'error': ERR_NO_JSON}), 400
        
        if 'x' not in data:
            return jsonify({'error': 'Missing required field: x'}), 400
        
        x = data['x']
        
        if not isinstance(x, (int, float)):
            return jsonify({'error': 'x must be a number'}), 400
        
        result = sigmoid(x)
        
        return jsonify({
            'input': x,
            'sigmoid': result,
            'function': 'sigmoid(x) = 1 / (1 + e^(-x))'
        })
        
    except Exception as e:
        return jsonify({'error': f'Sigmoid calculation failed: {str(e)}'}), 500


@neural_networks_bp.route('/step', methods=['POST'])
def calculate_step():
    """
    Calculate step activation function.
    
    Request body:
    {
        "x": 1.0
    }
    """
    try:
        data = request.get_json(silent=True)
        
        if not data:
            return jsonify({'error': ERR_NO_JSON}), 400
        
        if 'x' not in data:
            return jsonify({'error': 'Missing required field: x'}), 400
        
        x = data['x']
        
        if not isinstance(x, (int, float)):
            return jsonify({'error': 'x must be a number'}), 400
        
        result = step_function(x)
        
        return jsonify({
            'input': x,
            'step': result,
            'function': 'step(x) = 1 if x >= 0 else 0'
        })
        
    except Exception as e:
        return jsonify({'error': f'Step function calculation failed: {str(e)}'}), 500


@neural_networks_bp.route('/perceptron', methods=['POST'])
def perceptron_predict():
    """
    Make prediction using a perceptron.
    
    Request body:
    {
        "weights": [0.5, -0.5],
        "bias": -0.1,
        "inputs": [1.0, 0.5]
    }
    """
    try:
        data = request.get_json(silent=True)
        
        if not data:
            return jsonify({'error': ERR_NO_JSON}), 400
        
        if 'weights' not in data or 'bias' not in data or 'inputs' not in data:
            return jsonify({'error': 'Missing required fields: weights, bias, inputs'}), 400
        
        weights = data['weights']
        bias = data['bias']
        inputs = data['inputs']
        
        # Validate data types
        if not isinstance(weights, list):
            return jsonify({'error': 'weights must be a list'}), 400
        
        if not isinstance(bias, (int, float)):
            return jsonify({'error': 'bias must be a number'}), 400
        
        if not isinstance(inputs, list):
            return jsonify({'error': INPUTS_MUST_BE_LIST}), 400
        
        if len(weights) != len(inputs):
            return jsonify({'error': 'weights and inputs must have the same length'}), 400
        
        # Calculate perceptron output
        result = perceptron_output(weights, bias, inputs)
        
        # Calculate weighted sum for debugging
        weighted_sum = sum(w * i for w, i in zip(weights, inputs)) + bias
        
        return jsonify({
            'inputs': inputs,
            'weights': weights,
            'bias': bias,
            'weighted_sum': weighted_sum,
            'output': result,
            'activation': 'step_function'
        })
        
    except Exception as e:
        return jsonify({'error': f'Perceptron prediction failed: {str(e)}'}), 500


@neural_networks_bp.route('/neuron', methods=['POST'])
def neuron_activate():
    """
    Calculate neuron output with sigmoid activation.
    
    Request body:
    {
        "weights": [0.5, -0.5],
        "inputs": [1.0, 0.5]
    }
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': ERR_NO_JSON}), 400
        
        if 'weights' not in data or 'inputs' not in data:
            return jsonify({'error': 'Missing required fields: weights, inputs'}), 400
        
        weights = data['weights']
        inputs = data['inputs']
        
        # Validate data types
        if not isinstance(weights, list):
            return jsonify({'error': 'weights must be a list'}), 400
        
        if not isinstance(inputs, list):
            return jsonify({'error': INPUTS_MUST_BE_LIST}), 400
        
        if len(weights) != len(inputs):
            return jsonify({'error': 'weights and inputs must have the same length'}), 400
        
        # Calculate neuron output
        result = neuron_output(weights, inputs)
        
        # Calculate weighted sum for debugging
        weighted_sum = sum(w * i for w, i in zip(weights, inputs))
        
        return jsonify({
            'inputs': inputs,
            'weights': weights,
            'weighted_sum': weighted_sum,
            'output': result,
            'activation': 'sigmoid'
        })
        
    except Exception as e:
        return jsonify({'error': f'Neuron activation failed: {str(e)}'}), 500


def _validate_and_convert_network_payload(data, require_target=False):
    """Validate network payload and return converted network and inputs (and target if required)."""
    if not data:
        raise ValueError(ERR_NO_JSON)

    if 'network' not in data or 'inputs' not in data:
        raise ValueError('Missing required fields: network, inputs')

    network = data['network']
    inputs = data['inputs']

    if not isinstance(network, list):
        raise ValueError('network must be a list')

    if not isinstance(inputs, list):
        raise ValueError(INPUTS_MUST_BE_LIST)

    if require_target and 'target' not in data:
        raise ValueError('Missing required field: target')

    # Validate structure and types; convert to internal format
    converted_network = []
    for i, layer in enumerate(network):
        neuron_weights = _validate_layer(i, layer)
        converted_network.append([neuron_weights])

    if require_target:
        return converted_network, inputs, data['target']

    return converted_network, inputs


@neural_networks_bp.route('/feed_forward', methods=['POST'])
def network_feed_forward():
    """
    Perform feed-forward propagation through a neural network.
    
    Request body:
    {
        "network": [
            [[0.5, -0.5], 0.0],  # Hidden layer: [weights, bias]
            [[1.0, 1.0], 0.0]    # Output layer: [weights, bias]
        ],
        "inputs": [1.0, 1.0]
    }
    """
    data = request.get_json()
    try:
        result = _feed_forward_route(data)
        return jsonify(result)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Feed-forward propagation failed: {str(e)}'}), 500


def _feed_forward_route(data):
    if not data:
        raise ValueError(ERR_NO_JSON)

    converted_network, inputs = _validate_and_convert_network_payload(data)
    outputs = feed_forward(converted_network, inputs)

    return {
        'inputs': inputs,
        'network_structure': [len(layer) for layer in converted_network],
        'layer_outputs': outputs,
        'final_output': outputs[-1] if outputs else [],
        'num_layers': len(converted_network)
    }


@neural_networks_bp.route('/backpropagation', methods=['POST'])
def calculate_backpropagation():
    """
    Calculate gradients using backpropagation.
    
    Request body:
    {
        "network": [
            [[0.5, -0.5], 0.0],  # Hidden layer: [weights, bias]
            [[1.0, 1.0], 0.0]    # Output layer: [weights, bias]
        ],
        "inputs": [1.0, 1.0],
        "target": [1.0]
    }
    """
    data = request.get_json()
    try:
        result = _backprop_route(data)
        return jsonify(result)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Backpropagation failed: {str(e)}'}), 500


def _backprop_route(data):
    if not data:
        raise ValueError(ERR_NO_JSON)

    converted_network, inputs, target = _validate_and_convert_network_payload(data, require_target=True)

    gradients = backpropagation(converted_network, inputs, target)
    outputs = feed_forward(converted_network, inputs)

    return {
        'inputs': inputs,
        'target': target,
        'network_output': outputs[-1] if outputs else [],
        'gradients': gradients,
        'num_layers': len(converted_network),
        'note': 'Gradients are returned as [weight_gradients, bias_gradient] for each layer'
    }


def _init_network(input_dim: int, hidden_neurons: int, output_dim: int):
    """Initialize a simple random network: hidden neurons followed by output neurons.

    Returns a list of [weights, bias] for each neuron.
    """
    net = []
    for _ in range(hidden_neurons):
        weights = [random.uniform(-1, 1) for _ in range(input_dim)]
        bias = random.uniform(-1, 1)
        net.append([weights, bias])
    for _ in range(output_dim):
        weights = [random.uniform(-1, 1) for _ in range(hidden_neurons)]
        bias = random.uniform(-1, 1)
        net.append([weights, bias])
    return net


def _run_simple_training(net, data, epochs_count):
    """Run the simplified training loop used for the demo.

    For each epoch compute per-sample squared error and return list of epoch-average errors.
    This intentionally does not update weights (keeps original demo behaviour).
    """
    errs = []
    for _ in range(epochs_count):
        epoch_error = _compute_epoch_error(net, data)
        errs.append(epoch_error / len(data) if data else 0)

    return errs


def _compute_epoch_error(net, data):
    """Compute total squared error for a single epoch (helper to reduce nesting)."""
    epoch_error = 0
    for sample in data:
        inputs = sample.get('inputs')
        target = sample.get('target')

        outputs = feed_forward(net, inputs)
        if outputs and target:
            epoch_error += sum((o - t) ** 2 for o, t in zip(outputs[-1], target))

    return epoch_error


@neural_networks_bp.route('/simple_train', methods=['POST'])
def simple_training():
    """
    Simple neural network training demonstration.
    
    Request body:
    {
        "training_data": [
            {"inputs": [0, 0], "target": [0]},
            {"inputs": [0, 1], "target": [1]},
            {"inputs": [1, 0], "target": [1]},
            {"inputs": [1, 1], "target": [0]}
        ],
        "hidden_neurons": 2,
        "learning_rate": 0.1,
        "epochs": 100
    }
    """
    data = request.get_json()

    try:
        training_data, hidden_neurons, learning_rate, epochs = _validate_simple_training_payload(data)

        # Get input/output dimensions
        input_dim = len(training_data[0]['inputs'])
        output_dim = len(training_data[0]['target'])

        payload = {
            'training_data': training_data,
            'hidden_neurons': hidden_neurons,
            'learning_rate': learning_rate,
            'epochs': epochs
        }

        result = _simple_training_route(payload, input_dim, output_dim)
        return jsonify(result)

    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Training failed: {str(e)}'}), 500


def _simple_training_route(data, input_dim, output_dim):
    training_data = data.get('training_data')
    hidden_neurons = data.get('hidden_neurons', 2)
    learning_rate = data.get('learning_rate', 0.1)
    epochs = data.get('epochs', 100)

    if not isinstance(training_data, list):
        raise ValueError('training_data must be a list')

    if not isinstance(hidden_neurons, int) or hidden_neurons <= 0:
        raise ValueError('hidden_neurons must be a positive integer')

    if not isinstance(learning_rate, (int, float)) or learning_rate <= 0:
        raise ValueError('learning_rate must be a positive number')

    if not isinstance(epochs, int) or epochs <= 0:
        raise ValueError('epochs must be a positive integer')

    if not training_data:
        raise ValueError('training_data cannot be empty')

    network = _init_network(input_dim, hidden_neurons, output_dim)
    training_errors = _run_simple_training(network, training_data, epochs)

    return {
        'status': 'training_completed',
        'network_structure': {
            'input_dim': input_dim,
            'hidden_neurons': hidden_neurons,
            'output_dim': output_dim
        },
        'training_parameters': {
            'learning_rate': learning_rate,
            'epochs': epochs
        },
        'training_samples': len(training_data),
        'final_error': training_errors[-1] if training_errors else 0,
        'note': 'This is a demonstration. Actual weight updates not implemented in this simple version.'
    }


def _validate_simple_training_payload(data):
    """Validate payload for /simple_train and return validated values.

    Raises ValueError on invalid input.
    """
    if not data:
        raise ValueError(ERR_NO_JSON)

    if 'training_data' not in data:
        raise ValueError('Missing required field: training_data')

    training_data = data['training_data']
    hidden_neurons = data.get('hidden_neurons', 2)
    learning_rate = data.get('learning_rate', 0.1)
    epochs = data.get('epochs', 100)

    # Validate data types
    if not isinstance(training_data, list):
        raise ValueError('training_data must be a list')

    if not isinstance(hidden_neurons, int) or hidden_neurons <= 0:
        raise ValueError('hidden_neurons must be a positive integer')

    if not isinstance(learning_rate, (int, float)) or learning_rate <= 0:
        raise ValueError('learning_rate must be a positive number')

    if not isinstance(epochs, int) or epochs <= 0:
        raise ValueError('epochs must be a positive integer')

    if not training_data:
        raise ValueError('training_data cannot be empty')

    return training_data, hidden_neurons, learning_rate, epochs


@neural_networks_bp.route('/info', methods=['GET'])
def neural_networks_info():
    """Get information about neural network algorithms and parameters."""
    return jsonify({
        'algorithms': ['Feed-forward Neural Networks', 'Backpropagation', 'Perceptron'],
        'description': 'Neural networks are computational models inspired by biological neural networks',
        'functions': {
            'sigmoid': {
                'description': 'S-shaped activation function',
                'formula': 'sigmoid(x) = 1 / (1 + e^(-x))',
                'range': '(0, 1)'
            },
            'step_function': {
                'description': 'Binary activation function',
                'formula': 'step(x) = 1 if x >= 0 else 0',
                'range': '{0, 1}'
            },
            'perceptron': {
                'description': 'Linear classifier with step activation',
                'parameters': 'weights, bias, inputs'
            },
            'neuron_output': {
                'description': 'Neuron with sigmoid activation',
                'parameters': 'weights, inputs'
            },
            'feed_forward': {
                'description': 'Forward propagation through neural network',
                'parameters': 'network, inputs'
            },
            'backpropagation': {
                'description': 'Gradient calculation for training',
                'parameters': 'network, inputs, target'
            }
        },
        'endpoints': {
            'sigmoid': 'POST /api/neural-networks/sigmoid',
            'step': 'POST /api/neural-networks/step',
            'perceptron': 'POST /api/neural-networks/perceptron',
            'neuron': 'POST /api/neural-networks/neuron',
            'feed_forward': 'POST /api/neural-networks/feed_forward',
            'backpropagation': 'POST /api/neural-networks/backpropagation',
            'simple_train': 'POST /api/neural-networks/simple_train'
        },
        'notes': [
            'Network format: [[weights, bias], [weights, bias], ...]',
            'Weights and inputs must have matching dimensions',
            'Backpropagation returns gradients for each layer',
            'Training requires iterative weight updates with gradients'
        ]
    })
