import logging
from logging.config import dictConfig

from dsl.network_analysis import users_dict, eigenvector_centralities, page_rank


def main():
    logging.info("Betweenness Centrality")
    for _user in users_dict:
        logging.info(
            "%r",
            "user {}, betweenness {}".format(
                _user["id"], _user["betweenness_centrality"]
            ),
        )

    logging.info("Closeness Centrality")
    for _user in users_dict:
        logging.info(
            "%r",
            "user {}, closeness_centrality {}".format(
                _user["id"], _user["closeness_centrality"]
            ),
        )

    logging.info("Eigenvector Centrality")
    for _user_id, centrality in enumerate(eigenvector_centralities):
        logging.info("%r", "user_id {}, centrality {}".format(_user_id, centrality))

    logging.info("PageRank")
    for _user_id, _pr in page_rank(users_dict).items():
        logging.info("%r", "user_id {}, pr{}".format(_user_id, _pr))


if __name__ == "__main__":
    dictConfig(dict(
        version=1,
        formatters={"simple": {"format": """%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"""}},
        handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
        root={"handlers": ["console"], "level": logging.DEBUG},
    ))
    main()
