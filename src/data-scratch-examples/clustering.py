import logging
import random
from logging.config import dictConfig

from dsl.clustering import KMeans, bottom_up_cluster, squared_clustering_errors, generate_clusters, get_values

inputs_list = [
    [-14, -5],
    [13, 13],
    [20, 23],
    [-19, -11],
    [-9, -16],
    [21, 27],
    [-49, 15],
    [26, 13],
    [-46, 5],
    [-34, -1],
    [11, 15],
    [-49, 0],
    [-22, -16],
    [19, 28],
    [-12, -8],
    [-13, -19],
    [-41, 8],
    [-11, -6],
    [-25, -9],
    [-18, -3],
]


def main():
    random.seed(0)  # so you get the same results as me
    _clusterer = KMeans(3)
    _clusterer.train(inputs_list)
    logging.info("%r", "3-means: {}".format(_clusterer.means))

    random.seed(0)
    _clusterer = KMeans(2)
    _clusterer.train(inputs_list)
    logging.info("%r", "2-means: {}".format(_clusterer.means))

    logging.info("compute errors as a function of k")
    for _k in range(1, len(inputs_list) + 1):
        logging.info("%r", "k = {}".format(_k))
        logging.info("%r", "squared_clustering_errors = {}".format(squared_clustering_errors(inputs_list, _k)))
    logging.info("done with errors as a function of k")

    logging.info("start bottom up hierarchical clustering")
    _base_cluster = bottom_up_cluster(inputs_list)
    logging.info("%r", "base_cluster = {}".format(_base_cluster))

    logging.info("three clusters, min")
    for cluster in generate_clusters(_base_cluster, 3):
        logging.debug("%r", "cluster = {}".format(cluster))
        logging.info("%r", "get_values(cluster) = {}".format(get_values(cluster)))

    logging.info("three clusters, max:")
    _base_cluster = bottom_up_cluster(inputs_list, max)
    for cluster in generate_clusters(_base_cluster, 3):
        logging.debug("%r", "cluster = {}".format(cluster))
        logging.info("%r", "get_values(cluster) = {}".format(get_values(cluster)))
    logging.info("done with bottom up hierarchical clustering")


if __name__ == "__main__":
    LOGGING_CONFIG_DICT = dict(
        version=1,
        formatters={"simple": {"format": """%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"""}},
        handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
        root={"handlers": ["console"], "level": logging.DEBUG},
    )
    dictConfig(LOGGING_CONFIG_DICT)
    main()
