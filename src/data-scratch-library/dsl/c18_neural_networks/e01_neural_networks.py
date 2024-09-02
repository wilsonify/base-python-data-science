import logging
import random
from logging.config import dictConfig

from dsl.c18_neural_networks.neural_networks import backpropagation, feed_forward

random.seed(0)  # to get repeatable results
input_size = 25  # each input is a vector of length 25
num_hidden = 5  # we'll have 5 neurons in the hidden layer
output_size = 10  # we need 10 outputs for each input

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
    return [1 if c == "1" else 0 for row in raw_digit.split("\n") for c in row.strip()]


def create_network():
    logging.info("each hidden neuron has one weight per input, plus a bias weight")
    hidden_layer = [[random.random() for _ in range(input_size + 1)] for _ in range(num_hidden)]

    logging.info("each output neuron has one weight per hidden neuron, plus a bias weight")
    output_layer = [[random.random() for _ in range(num_hidden + 1)] for _ in range(output_size)]

    logging.info("the network starts out with random weights")
    network = [hidden_layer, output_layer]
    return network


def fit_network(network, inputs, targets):
    logging.info("fit_network backpropagate 10,000 iterations; should converge")
    for _ in range(10000):
        for input_vector, target_vector in zip(inputs, targets):
            backpropagation(network, input_vector, target_vector)


def predict(network, in_put):
    return feed_forward(network, in_put)[-1]


def predict_vector(network, new_input):
    return [round(x, 2) for x in predict(network, new_input)]


def predict_batch(network, input_batch):
    output_batch = []
    for i, input_i in enumerate(input_batch):
        rounded_outputs = predict_vector(network, input_i)
        output_batch.append(rounded_outputs)
    return output_batch


def main():
    logging.info("main")
    inputs_ = list(map(make_digit, raw_digits))
    targets_ = [[1 if i == j else 0 for i in range(10)] for j in range(10)]
    _network = create_network()
    fit_network(_network, inputs_, targets_)
    output_batch_ = predict_batch(_network, inputs_)
    logging.info("%r", f"output_batch_ = {output_batch_}")

    new_x = [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, ]
    rounded_predictions = predict_vector(_network, new_x)
    logging.info("%r", f"rounded predictions {rounded_predictions}")  # .@@@.

    new_x = [0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, ]
    rounded_predictions = predict_vector(_network, new_x)
    logging.info("%r", f"rounded predictions {rounded_predictions}")


if __name__ == "__main__":
    dictConfig(dict(
        version=1,
        formatters={"simple": {"format": """%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"""}},
        handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
        root={"handlers": ["console"], "level": logging.DEBUG},
    ))
    main()
