import math
import random

from data_science_from_scratch.linear_algebra import dot


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


if __name__ == "__main__":

    raw_digits = [
        """11111
           1...1
           1...1
           1...1
           11111""",
        """..1..
           ..1..
           ..1..
           ..1..
           ..1..""",
        """11111
           ....1
           11111
           1....
           11111""",
        """11111
           ....1
           11111
           ....1
           11111""",
        """1...1
           1...1
           11111
           ....1
           ....1""",
        """11111
           1....
           11111
           ....1
           11111""",
        """11111
           1....
           11111
           1...1
           11111""",
        """11111
           ....1
           ....1
           ....1
           ....1""",
        """11111
           1...1
           11111
           1...1
           11111""",
        """11111
           1...1
           11111
           ....1
           11111""",
    ]


    def make_digit(raw_digit):
        return [
            1 if c == "1" else 0 for row in raw_digit.split("\n") for c in row.strip()
        ]


    inputs_ = list(map(make_digit, raw_digits))

    targets = [[1 if i == j else 0 for i in range(10)] for j in range(10)]

    random.seed(0)  # to get repeatable results
    input_size = 25  # each input is a vector of length 25
    num_hidden = 5  # we'll have 5 neurons in the hidden layer
    output_size = 10  # we need 10 outputs for each input

    # each hidden neuron has one weight per input, plus a bias weight
    hidden_layer = [
        [random.random() for _ in range(input_size + 1)] for _ in range(num_hidden)
    ]

    # each output neuron has one weight per hidden neuron, plus a bias weight
    output_layer = [
        [random.random() for _ in range(num_hidden + 1)] for _ in range(output_size)
    ]

    # the network starts out with random weights
    _network = [hidden_layer, output_layer]

    # 10,000 iterations seems enough to converge
    for _ in range(10000):
        for input_vector_, target_vector in zip(inputs_, targets):
            backpropagate(_network, input_vector_, target_vector)


    def predict(in_put):
        return feed_forward(_network, in_put)[-1]


    for i, input_i in enumerate(inputs_):
        outputs_ = predict(input_i)
        print(i, [round(p, 2) for p in outputs_])

    print(""".@@@....@@..@@....@@.@@@.""")
    print(
        [round(x, 2) for x in predict([
            0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0,
        ])])  # .@@@.
    print()

    print(
        """.@@@.@..@@.@@@.@..@@.@@@."""
    )
    print([round(x, 2) for x in predict([
        0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0
    ])])
    print()
