"""
Example: fit multiple regression, bootstrap inference, and ridge regularisation.
"""

import logging
import random
from logging.config import dictConfig

from dsl.c04_linear_algebra.e0401_vectors import dot
from dsl.c05_statistics.e0502_dispersion import standard_deviation
from dsl.c05_statistics.e0501_central_tendancy import median
from dsl.c15_multiple_regression.multiple_regression import (
    estimate_beta,
    multiple_r_squared,
    bootstrap_statistic,
    estimate_sample_beta,
    p_value,
    estimate_beta_ridge,
)
from dsl.c15_multiple_regression.data import x, daily_minutes_good


def try_regularisation():
    """Try several ridge-penalty strengths."""
    for alpha in [0.0, 0.01, 0.1, 1, 10]:
        beta = estimate_beta_ridge(x, daily_minutes_good, alpha=alpha)
        logging.info(
            "alpha %s | beta %s | dot(beta[1:]) %s | R² %s",
            alpha, beta, dot(beta[1:], beta[1:]),
            multiple_r_squared(x, daily_minutes_good, beta),
        )


def run_bootstrap():
    """Bootstrap standard errors and p-values."""
    close_to_100 = [99.5 + random.random() for _ in range(101)]
    far_from_100 = (
        [99.5 + random.random()]
        + [random.random() for _ in range(50)]
        + [200 + random.random() for _ in range(50)]
    )
    logging.info("bootstrap close_to_100: %s", bootstrap_statistic(close_to_100, median, 100))
    logging.info("bootstrap far_from_100: %s", bootstrap_statistic(far_from_100, median, 100))

    bootstrap_betas = bootstrap_statistic(
        list(zip(x, daily_minutes_good)), estimate_sample_beta, 100
    )
    se = [standard_deviation([b[i] for b in bootstrap_betas]) for i in range(4)]
    logging.info("bootstrap standard errors: %s", se)
    logging.info("p_value(30.63, 1.174) = %s", p_value(30.63, 1.174))
    logging.info("p_value(0.972, 0.079) = %s", p_value(0.972, 0.079))
    logging.info("p_value(-1.868, 0.131) = %s", p_value(-1.868, 0.131))
    logging.info("p_value(0.911, 0.990) = %s", p_value(0.911, 0.990))


def main() -> None:
    random.seed(0)
    beta = estimate_beta(x, daily_minutes_good)
    logging.info("beta = %s", beta)
    logging.info("R² = %s", multiple_r_squared(x, daily_minutes_good, beta))

    run_bootstrap()
    try_regularisation()


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
