"""
Simple linear regression: y = alpha + beta * x.
"""

from typing import List, Tuple

from dsl.c05_statistics.e0503_correlation import correlation
from dsl.c05_statistics.e0502_dispersion import de_mean, standard_deviation
from dsl.c05_statistics.e0501_central_tendancy import mean


def predict(alpha: float, beta: float, x_i: float) -> float:
    """Predict y given the linear model parameters."""
    return beta * x_i + alpha


def error(alpha: float, beta: float, x_i: float, y_i: float) -> float:
    """Residual for a single observation."""
    return y_i - predict(alpha, beta, x_i)


def sum_of_squared_errors(
    alpha: float, beta: float, x: List[float], y: List[float]
) -> float:
    """Total squared residuals for the model."""
    return sum(error(alpha, beta, x_i, y_i) ** 2 for x_i, y_i in zip(x, y))


def least_squares_fit(x: List[float], y: List[float]) -> Tuple[float, float]:
    """Return (alpha, beta) that minimise the sum of squared errors."""
    beta = correlation(x, y) * standard_deviation(y) / standard_deviation(x)
    alpha = mean(y) - beta * mean(x)
    return alpha, beta


def total_sum_of_squares(y: List[float]) -> float:
    """Total squared variation of y from its mean."""
    return sum(v ** 2 for v in de_mean(y))


def r_squared(
    alpha: float, beta: float, x: List[float], y: List[float]
) -> float:
    """Coefficient of determination (R²)."""
    return 1.0 - sum_of_squared_errors(alpha, beta, x, y) / total_sum_of_squares(y)


def squared_error(x_i: float, y_i: float, theta: List[float]) -> float:
    """Squared error as a function of theta = [alpha, beta]."""
    alpha, beta = theta
    return error(alpha, beta, x_i, y_i) ** 2


def squared_error_gradient(
    x_i: float, y_i: float, theta: List[float]
) -> List[float]:
    """Gradient of the squared error w.r.t. theta = [alpha, beta]."""
    alpha, beta = theta
    return [
        -2 * error(alpha, beta, x_i, y_i),
        -2 * error(alpha, beta, x_i, y_i) * x_i,
    ]
