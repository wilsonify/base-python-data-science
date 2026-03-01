"""
Example: k-means and hierarchical clustering on 2-D data.
"""

import logging
import random
from logging.config import dictConfig

from dsl.c20_clustering.clustering import (
    KMeans,
    bottom_up_cluster,
    squared_clustering_errors,
    generate_clusters,
    get_values,
)
from dsl.c20_clustering.data import inputs_list


def main() -> None:
    random.seed(0)

    clusterer = KMeans(3)
    clusterer.train(inputs_list)
    logging.info("3-means: %s", clusterer.means)

    random.seed(0)
    clusterer2 = KMeans(2)
    clusterer2.train(inputs_list)
    logging.info("2-means: %s", clusterer2.means)

    logging.info("squared errors by k")
    for k in range(1, len(inputs_list) + 1):
        err = squared_clustering_errors(inputs_list, k)
        logging.info("k=%d  error=%s", k, err)

    logging.info("bottom-up hierarchical clustering (min linkage)")
    base = bottom_up_cluster(inputs_list)
    for cluster in generate_clusters(base, 3):
        logging.info("cluster: %s", get_values(cluster))

    logging.info("bottom-up hierarchical clustering (max linkage)")
    base_max = bottom_up_cluster(inputs_list, max)
    for cluster in generate_clusters(base_max, 3):
        logging.info("cluster: %s", get_values(cluster))


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
