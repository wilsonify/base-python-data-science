"""
Multiple linear regression with bootstrap inference and regularisation.
"""

import random
from functools import partial
from typing import List, Callable, Tuple

from dsl.c04_linear_algebra.e0401_vectors import dot, vector_add
from dsl.c06_probability.e0603_normal import normal_cdf
from dsl.c08_gradient_descent.e0805_stochastic_gd import minimize_stochastic
from dsl.c14_simple_linear_regression.simple_linear_regression import total_sum_of_squares


def predict(x_i: List[float], beta: List[float]) -> float:
    """Predicted value for observation *x_i*."""
    return dot(x_i, beta)


def error(x_i: List[float], y_i: float, beta: List[float]) -> float:
    """Residual for observation *x_i*."""
    return y_i - predict(x_i, beta)


def squared_error(x_i: List[float], y_i: float, beta: List[float]) -> float:
    """Squared residual for observation *x_i*."""
    return error(x_i, y_i, beta) ** 2


def squared_error_gradient(
    x_i: List[float], y_i: float, beta: List[float]
) -> List[float]:
    """Gradient of the squared error w.r.t. *beta*."""
    return [-2 * x_ij * error(x_i, y_i, beta) for x_ij in x_i]


def estimate_beta(x: List[List[float]], y: List[float]) -> List[float]:
    """Estimate *beta* via stochastic gradient descent."""
    beta_initial = [random.random() for _ in x[0]]
    return minimize_stochastic(
        squared_error, squared_error_gradient, x, y, beta_initial, 0.001
    )


def multiple_r_squared(
    x: List[List[float]], y: List[float], beta: List[float]
) -> float:
    """Coefficient of determination for multiple regression."""
    sse = sum(error(x_i, y_i, beta) ** 2 for x_i, y_i in zip(x, y))
    return 1.0 - sse / total_sum_of_squares(y)


# ── Bootstrap ────────────────────────────────────────────────────────


def bootstrap_sample(data: list) -> list:
    """Randomly sample len(data) elements **with** replacement."""
    return [random.choice(data) for _ in data]


def bootstrap_statistic(
    data: list, stats_fn: Callable, num_samples: int
) -> list:
    """Evaluate *stats_fn* on *num_samples* bootstrap resamples."""
    return [stats_fn(bootstrap_sample(data)) for _ in range(num_samples)]


def estimate_sample_beta(sample: list) -> List[float]:
    """Estimate beta from a bootstrap sample of (x, y) pairs."""
    x_sample, y_sample = list(zip(*sample))
    return estimate_beta(list(x_sample), list(y_sample))


def p_value(beta_hat_j: float, sigma_hat_j: float) -> float:
    """Two-sided p-value for a coefficient estimate."""
    if beta_hat_j > 0:
        return 2 * (1 - normal_cdf(beta_hat_j / sigma_hat_j))
    return 2 * normal_cdf(beta_hat_j / sigma_hat_j)


# ── Regularised regression ───────────────────────────────────────────


def ridge_penalty(beta: List[float], alpha: float) -> float:
    """L2 penalty (excludes intercept)."""
    return alpha * dot(beta[1:], beta[1:])


def squared_error_ridge(
    x_i: List[float], y_i: float, beta: List[float], alpha: float
) -> float:
    """Squared error plus ridge penalty."""
    return error(x_i, y_i, beta) ** 2 + ridge_penalty(beta, alpha)


def ridge_penalty_gradient(beta: List[float], alpha: float) -> List[float]:
    """Gradient of the ridge penalty."""
    return [0.0] + [2 * alpha * beta_j for beta_j in beta[1:]]


def squared_error_ridge_gradient(
    x_i: List[float], y_i: float, beta: List[float], alpha: float
) -> List[float]:
    """Gradient of the squared error + ridge penalty."""
    return vector_add(
        squared_error_gradient(x_i, y_i, beta),
        ridge_penalty_gradient(beta, alpha),
    )


def estimate_beta_ridge(
    x: List[List[float]], y: List[float], alpha: float
) -> List[float]:
    """Estimate *beta* with ridge (L2) regularisation."""
    beta_initial = [random.random() for _ in x[0]]
    return minimize_stochastic(
        partial(squared_error_ridge, alpha=alpha),
        partial(squared_error_ridge_gradient, alpha=alpha),
        x, y, beta_initial, 0.001,
    )


def lasso_penalty(beta: List[float], alpha: float) -> float:
    """L1 penalty (excludes intercept)."""
    return alpha * sum(abs(beta_i) for beta_i in beta[1:])
