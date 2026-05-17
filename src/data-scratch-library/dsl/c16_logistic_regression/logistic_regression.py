"""
Logistic regression via gradient ascent.
"""

import logging
import math
from functools import partial, reduce
from typing import List, Tuple

from dsl.c04_linear_algebra.e0401_vectors import dot, vector_add
from dsl.c08_gradient_descent.e0804_minibatch_gd import maximize_batch
from dsl.c08_gradient_descent.e0805_stochastic_gd import maximize_stochastic


def logistic(x: float) -> float:
    """Sigmoid function, clamped for numerical stability."""
    if x > 709:
        return 1.0
    if x < -709:
        return 0.0
    return 1.0 / (1 + math.exp(-x))


def logistic_prime(x: float) -> float:
    """Derivative of the sigmoid function."""
    return logistic(x) * (1 - logistic(x))


def logistic_log_likelihood_i(
    x_i: List[float], y_i: int, beta: List[float]
) -> float:
    """Log-likelihood contribution of observation *i*."""
    if y_i == 1:
        return math.log(logistic(dot(x_i, beta)))
    return math.log(1 - logistic(dot(x_i, beta)))


def logistic_log_likelihood(
    x: List[List[float]], y: List[int], beta: List[float]
) -> float:
    """Total log-likelihood."""
    return sum(
        logistic_log_likelihood_i(x_i, y_i, beta)
        for x_i, y_i in zip(x, y)
    )


def logistic_log_partial_ij(
    x_i: List[float], y_i: int, beta: List[float], j: int
) -> float:
    """Partial derivative of log-likelihood w.r.t. beta[j]."""
    return (y_i - logistic(dot(x_i, beta))) * x_i[j]


def logistic_log_gradient_i(
    x_i: List[float], y_i: int, beta: List[float]
) -> List[float]:
    """Gradient of log-likelihood for observation *i*."""
    return [
        logistic_log_partial_ij(x_i, y_i, beta, j) for j, _ in enumerate(beta)
    ]


def logistic_log_gradient(
    x: List[List[float]], y: List[int], beta: List[float]
) -> List[float]:
    """Total gradient of log-likelihood."""
    return reduce(
        vector_add,
        [logistic_log_gradient_i(x_i, y_i, beta) for x_i, y_i in zip(x, y)],
    )


def score_logistic(
    beta_hat: List[float],
    x_test: List[List[float]],
    y_test: List[int],
) -> Tuple[float, float]:
    """Return (precision, recall) on the test set."""
    tp = fp = tn = fn = 0
    for x_i, y_i in zip(x_test, y_test):
        pred = logistic(dot(beta_hat, x_i))
        if y_i == 1 and pred >= 0.5:
            tp += 1
        elif y_i == 1:
            fn += 1
        elif pred >= 0.5:
            fp += 1
        else:
            tn += 1
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    return precision, recall


def logistic_fit(
    x: List[List[float]], y: List[int]
) -> List[float]:
    """Fit logistic regression via batch then stochastic gradient ascent."""
    logging.info("fitting logistic regression")
    fn = partial(logistic_log_likelihood, x, y)
    gradient_fn = partial(logistic_log_gradient, x, y)
    beta_0 = [1.0, 1.0, 1.0]
    beta_1 = maximize_batch(fn, gradient_fn, beta_0)
    beta_hat = maximize_stochastic(
        logistic_log_likelihood_i, logistic_log_gradient_i, x, y, beta_1
    )
    logging.info("beta_hat = %s", beta_hat)
    return beta_hat
