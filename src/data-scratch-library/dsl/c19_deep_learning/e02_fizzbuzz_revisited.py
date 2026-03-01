"""
Example: train a network to play FizzBuzz using the deep-learning framework.
"""

import logging
import random
from logging.config import dictConfig
from typing import List

from dsl.c19_deep_learning.layer import Sequential, Linear, Tanh, Sigmoid
from dsl.c19_deep_learning.metrics import Momentum, SSE, SoftmaxCrossEntropy
from dsl.c19_deep_learning.deep_learning import Tensor


def binary_encode(n: int) -> List[float]:
    """Encode *n* as a 10-bit binary vector."""
    return [float(n >> i & 1) for i in range(10)]


def fizz_buzz_encode(n: int) -> List[float]:
    """One-hot encode the FizzBuzz answer for *n*."""
    if n % 15 == 0:
        return [0.0, 0, 0, 1]
    if n % 5 == 0:
        return [0.0, 0, 1, 0]
    if n % 3 == 0:
        return [0.0, 1, 0, 0]
    return [1.0, 0, 0, 0]


def argmax(xs: List[float]) -> int:
    """Return the index of the largest element."""
    return max(range(len(xs)), key=lambda i: xs[i])


def fizzbuzz_accuracy(low: int, hi: int, net) -> float:
    """Fraction of correct FizzBuzz predictions in [low, hi)."""
    correct = sum(
        1
        for n in range(low, hi)
        if argmax(net.forward(binary_encode(n))) == argmax(fizz_buzz_encode(n))
    )
    return correct / (hi - low)


def main() -> None:
    xs = [binary_encode(n) for n in range(101, 1024)]
    ys = [fizz_buzz_encode(n) for n in range(101, 1024)]

    NUM_HIDDEN = 25
    random.seed(0)

    # -- SSE training --
    net = Sequential([
        Linear(input_dim=10, output_dim=NUM_HIDDEN, init="uniform"),
        Tanh(),
        Linear(input_dim=NUM_HIDDEN, output_dim=4, init="uniform"),
        Sigmoid(),
    ])
    optimizer = Momentum(learning_rate=0.1, momentum=0.9)
    loss = SSE()

    for epoch in range(1000):
        epoch_loss = 0.0
        for x, y in zip(xs, ys):
            predicted = net.forward(x)
            epoch_loss += loss.loss(predicted, y)
            gradient = loss.gradient(predicted, y)
            net.backward(gradient)
            optimizer.step(net)
        if epoch % 100 == 0:
            acc = fizzbuzz_accuracy(101, 1024, net)
            logging.info("SSE  epoch %d  loss %.2f  acc %.2f", epoch, epoch_loss, acc)

    logging.info("SSE test accuracy: %.2f", fizzbuzz_accuracy(1, 101, net))

    # -- Softmax cross-entropy training --
    random.seed(0)
    net2 = Sequential([
        Linear(input_dim=10, output_dim=NUM_HIDDEN, init="uniform"),
        Tanh(),
        Linear(input_dim=NUM_HIDDEN, output_dim=4, init="uniform"),
    ])
    optimizer2 = Momentum(learning_rate=0.1, momentum=0.9)
    loss2 = SoftmaxCrossEntropy()

    for epoch in range(100):
        epoch_loss = 0.0
        for x, y in zip(xs, ys):
            predicted = net2.forward(x)
            epoch_loss += loss2.loss(predicted, y)
            gradient = loss2.gradient(predicted, y)
            net2.backward(gradient)
            optimizer2.step(net2)
        if epoch % 10 == 0:
            acc = fizzbuzz_accuracy(101, 1024, net2)
            logging.info("CE   epoch %d  loss %.3f  acc %.2f", epoch, epoch_loss, acc)

    logging.info("CE test accuracy: %.2f", fizzbuzz_accuracy(1, 101, net2))


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
