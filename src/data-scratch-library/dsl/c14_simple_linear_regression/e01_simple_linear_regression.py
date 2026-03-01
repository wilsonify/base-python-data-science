"""
Example: fit a simple linear model with least squares and gradient descent.
"""

import logging
import random
from logging.config import dictConfig

from dsl.c08_gradient_descent.e0805_stochastic_gd import minimize_stochastic
from dsl.c14_simple_linear_regression.simple_linear_regression import (
    least_squares_fit,
    r_squared,
    squared_error,
    squared_error_gradient,
)
from dsl.c14_simple_linear_regression.data import (
    num_friends_good,
    daily_minutes_good,
)


def main() -> None:
    alpha, beta = least_squares_fit(num_friends_good, daily_minutes_good)
    logging.info("alpha = %s", alpha)
    logging.info("beta  = %s", beta)
    logging.info("r-squared = %s", r_squared(alpha, beta, num_friends_good, daily_minutes_good))

    # gradient-descent approach
    random.seed(0)
    theta = [random.random(), random.random()]
    alpha, beta = minimize_stochastic(
        squared_error,
        squared_error_gradient,
        num_friends_good,
        daily_minutes_good,
        theta,
        0.0001,
    )
    logging.info("GD alpha = %s", alpha)
    logging.info("GD beta  = %s", beta)


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
