import math

from dsl.linear_algebra import dot


def step_function(x):
    return 1 if x >= 0 else 0


def perceptron_output(weights, bias, x):
    """returns 1 if the perceptron 'fires', 0 if not"""
    return step_function(dot(weights, x) + bias)


def sigmoid(t):
    return 1 / (1 + math.exp(-t))


def neuron_output(weights, inputs):
    return sigmoid(dot(weights, inputs))


def feed_forward(neural_network, input_vector):
    """takes in a neural network (represented as a list of lists of lists of weights)
    and returns the output from forward-propagating the input"""

    outputs = []

    for layer in neural_network:
        input_with_bias = input_vector + [1]  # add a bias input
        output = [
            neuron_output(neuron, input_with_bias)  # compute the output
            for neuron in layer
        ]  # for this layer
        outputs.append(output)  # and remember it

        # the input to the next layer is the output of this one
        input_vector = output

    return outputs


def backpropagate(network, input_vector, target):
    hidden_outputs, outputs = feed_forward(network, input_vector)

    # the output * (1 - output) is from the derivative of sigmoid
    output_deltas = [
        output * (1 - output) * (output - target[i]) for i, output in enumerate(outputs)
    ]

    # adjust weights for output layer (network[-1])
    for i, output_neuron in enumerate(network[-1]):
        for j, hidden_output in enumerate(hidden_outputs + [1]):
            output_neuron[j] -= output_deltas[i] * hidden_output

    # back-propagate errors to hidden layer
    hidden_deltas = [
        hidden_output
        * (1 - hidden_output)
        * dot(output_deltas, [n[i] for n in network[-1]])
        for i, hidden_output in enumerate(hidden_outputs)
    ]

    # adjust weights for hidden layer (network[0])
    for i, hidden_neuron in enumerate(network[0]):
        for j, input_j in enumerate(input_vector + [1]):
            hidden_neuron[j] -= hidden_deltas[i] * input_j
