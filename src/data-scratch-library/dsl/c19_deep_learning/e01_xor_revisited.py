"""
Example: train a small network to solve XOR using the deep-learning framework.
"""

import logging
import random
from logging.config import dictConfig
from typing import List

from dsl.c19_deep_learning.layer import Sequential, Linear, Sigmoid
from dsl.c19_deep_learning.metrics import GradientDescent, SSE


def main() -> None:
    random.seed(0)

    xs: List[List[float]] = [[0.0, 0], [0.0, 1], [1.0, 0], [1.0, 1]]
    ys: List[List[float]] = [[0.0], [1.0], [1.0], [0.0]]

    net = Sequential([
        Linear(input_dim=2, output_dim=2),
        Sigmoid(),
        Linear(input_dim=2, output_dim=1),
    ])

    optimizer = GradientDescent(learning_rate=0.1)
    loss = SSE()

    for epoch in range(3000):
        epoch_loss = 0.0
        for x, y in zip(xs, ys):
            predicted = net.forward(x)
            epoch_loss += loss.loss(predicted, y)
            gradient = loss.gradient(predicted, y)
            net.backward(gradient)
            optimizer.step(net)
        if epoch % 500 == 0:
            logging.info("epoch %d  loss %.4f", epoch, epoch_loss)

    for x, y in zip(xs, ys):
        logging.info("x=%s  predicted=%s  target=%s", x, net.forward(x), y)

    for param in net.params():
        logging.info("param: %s", param)


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
