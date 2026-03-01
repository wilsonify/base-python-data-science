"""
Example: evaluate classification metrics on a sample confusion matrix.
"""

import logging
from logging.config import dictConfig

from dsl.c11_machine_learning.machine_learning import (
    accuracy,
    precision,
    recall,
    f1_score,
)


def main() -> None:
    tp, fp, fn, tn = 70, 4930, 13930, 981070
    logging.info("accuracy  = %s", accuracy(tp, fp, fn, tn))
    logging.info("precision = %s", precision(tp, fp, fn, tn))
    logging.info("recall    = %s", recall(tp, fp, fn, tn))
    logging.info("f1_score  = %s", f1_score(tp, fp, fn, tn))


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
