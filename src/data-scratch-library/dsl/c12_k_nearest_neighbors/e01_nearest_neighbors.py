"""
Example: classify cities by favourite language & explore the curse of dimensionality.
"""

import logging
import random
from logging.config import dictConfig

from dsl.c05_statistics.e0501_central_tendancy import mean
from dsl.c12_k_nearest_neighbors.nearest_neighbors import (
    knn_classify,
    random_distances,
)
from dsl.c12_k_nearest_neighbors.data import cities


def try_several_k(city_data, ks=(1, 3, 5, 7)):
    """Leave-one-out evaluation for several values of k."""
    for k in ks:
        num_correct = sum(
            knn_classify(
                k,
                [c for c in city_data if c != (loc, lang)],
                loc,
            )
            == lang
            for loc, lang in city_data
        )
        logging.info("%d neighbor(s): %d correct out of %d", k, num_correct, len(city_data))


def explore_dimensionality():
    """Show how distances behave as dimensions increase."""
    for dim in range(1, 101, 5):
        distances = random_distances(dim, 10_000)
        logging.info(
            "dim %3d | min %.4f | mean %.4f | ratio %.4f",
            dim,
            min(distances),
            mean(distances),
            min(distances) / mean(distances),
        )


def main() -> None:
    random.seed(0)
    try_several_k(cities)
    explore_dimensionality()


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
