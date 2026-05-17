"""
Example: logistic regression on paid-account data.
"""

import logging
import random
from logging.config import dictConfig

from dsl.c10_working_with_data.e1008_rescaling import rescale
from dsl.c11_machine_learning.machine_learning import train_test_split
from dsl.c15_multiple_regression.multiple_regression import estimate_beta
from dsl.c16_logistic_regression.logistic_regression import score_logistic, logistic_fit
from dsl.c16_logistic_regression.data import raw_data, get_x, get_y


def main() -> None:
    random.seed(0)
    data = [list(row) for row in raw_data]
    x = get_x(data)
    y = get_y(data)

    rescaled_x = rescale(x)

    logging.info("linear regression baseline")
    beta_linear = estimate_beta(rescaled_x, y)
    logging.info("beta = %s", beta_linear)

    logging.info("logistic regression")
    x_train, x_test, y_train, y_test = train_test_split(rescaled_x, y, 0.33)
    beta_hat = logistic_fit(x_train, y_train)

    prec, rec = score_logistic(beta_hat, x_test, y_test)
    logging.info("precision = %s", prec)
    logging.info("recall    = %s", rec)


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
