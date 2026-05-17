"""
Feed-forward neural network with backpropagation.
"""

import math
from typing import List

from dsl.c04_linear_algebra.e0401_vectors import dot


def step_function(x: float) -> int:
    """Return 1 if *x* >= 0, else 0."""
    return 1 if x >= 0 else 0


def perceptron_output(weights: List[float], bias: float, x: List[float]) -> int:
    """Return 1 if the perceptron fires, 0 otherwise."""
    return step_function(dot(weights, x) + bias)


def sigmoid(t: float) -> float:
    """Logistic sigmoid, safe against overflow."""
    try:
        return 1 / (1 + math.exp(-t))
    except OverflowError:
        return 0.0 if t < 0 else 1.0


def neuron_output(weights: List[float], inputs: List[float]) -> float:
    """Compute sigmoid(dot(weights, inputs))."""
    return sigmoid(dot(weights, inputs))


def feed_forward(
    neural_network: List[List[List[float]]], input_vector: List[float]
) -> List[List[float]]:
    """
    Forward-propagate *input_vector* through a network represented as
    a list of layers, where each layer is a list of neuron weight vectors.

    Returns the list of per-layer outputs (including the final layer).
    """
    outputs: List[List[float]] = []
    for layer in neural_network:
        input_with_bias = input_vector + [1]
        output = [neuron_output(neuron, input_with_bias) for neuron in layer]
        outputs.append(output)
        input_vector = output
    return outputs


def backpropagation(
    network: List[List[List[float]]],
    input_vector: List[float],
    target: List[float],
) -> None:
    """
    One step of backpropagation.  Updates *network* weights **in-place**.
    Assumes a two-layer network (hidden + output).
    """
    hidden_outputs, outputs = feed_forward(network, input_vector)

    output_deltas = [
        output * (1 - output) * (output - target[i])
        for i, output in enumerate(outputs)
    ]

    for i, output_neuron in enumerate(network[-1]):
        for j, hidden_output in enumerate(hidden_outputs + [1]):
            output_neuron[j] -= output_deltas[i] * hidden_output

    hidden_deltas = [
        hidden_output
        * (1 - hidden_output)
        * dot(output_deltas, [n[i] for n in network[-1]])
        for i, hidden_output in enumerate(hidden_outputs)
    ]

    for i, hidden_neuron in enumerate(network[0]):
        for j, input_j in enumerate(input_vector + [1]):
            hidden_neuron[j] -= hidden_deltas[i] * input_j
