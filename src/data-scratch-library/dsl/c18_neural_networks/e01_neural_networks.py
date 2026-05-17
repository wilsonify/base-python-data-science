"""
Example: train a two-layer network to recognise hand-drawn digits.
"""

import logging
import random
from logging.config import dictConfig
from typing import List

from dsl.c18_neural_networks.neural_networks import backpropagation, feed_forward
from dsl.c18_neural_networks.data import (
    raw_digits,
    make_digit,
    INPUT_SIZE,
    NUM_HIDDEN,
    OUTPUT_SIZE,
)


def create_network() -> List[List[List[float]]]:
    """Create a random two-layer network."""
    hidden_layer = [
        [random.random() for _ in range(INPUT_SIZE + 1)] for _ in range(NUM_HIDDEN)
    ]
    output_layer = [
        [random.random() for _ in range(NUM_HIDDEN + 1)] for _ in range(OUTPUT_SIZE)
    ]
    return [hidden_layer, output_layer]


def fit_network(
    network: List[List[List[float]]],
    inputs: List[List[int]],
    targets: List[List[int]],
    num_epochs: int = 10000,
) -> None:
    """Train the network with backpropagation for *num_epochs*."""
    logging.info("backpropagating %d epochs", num_epochs)
    for _ in range(num_epochs):
        for input_vector, target_vector in zip(inputs, targets):
            backpropagation(network, input_vector, target_vector)


def predict(network: List[List[List[float]]], x: List[float]) -> List[float]:
    """Return the final-layer output for input *x*."""
    return feed_forward(network, x)[-1]


def predict_vector(network: List[List[List[float]]], x: List[float]) -> List[float]:
    """Return rounded predictions for input *x*."""
    return [round(v, 2) for v in predict(network, x)]


def main() -> None:
    random.seed(0)

    inputs = [make_digit(raw) for raw in raw_digits]
    targets = [[1 if i == j else 0 for i in range(10)] for j in range(10)]

    network = create_network()
    fit_network(network, inputs, targets)

    for i, inp in enumerate(inputs):
        logging.info("digit %d => %s", i, predict_vector(network, inp))

    # Test with a hand-drawn 3 (slightly different from training)
    new_3 = [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0]
    logging.info("hand-drawn 3 => %s", predict_vector(network, new_3))

    new_8 = [0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0]
    logging.info("hand-drawn 8 => %s", predict_vector(network, new_8))


if __name__ == "__main__":
    dictConfig(
        {
            "version": 1,
            "formatters": {
                "simple": {
                    "format": "%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "simple",
                }
            },
            "root": {"handlers": ["console"], "level": logging.DEBUG},
        }
    )
    main()
