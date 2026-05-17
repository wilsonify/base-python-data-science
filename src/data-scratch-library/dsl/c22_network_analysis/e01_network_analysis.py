"""
Example: compute centrality measures and PageRank on a small social graph.
"""

import logging
from logging.config import dictConfig

from dsl.c22_network_analysis.network_analysis import (
    populate_friends,
    populate_shortest_paths,
    populate_betweeness,
    populate_closeness,
    construct_adjacency,
    compute_eigenvectors,
    populate_endorsments,
    populate_endorsements,
    page_rank,
)
from dsl.c22_network_analysis.data import users_dict, friendships, endorsements


def main() -> None:
    users = populate_friends(users_dict, friendships)
    users = populate_shortest_paths(users)
    users = populate_betweeness(users)
    users = populate_closeness(users)

    logging.info("Betweenness Centrality")
    for u in users:
        logging.info("user %d  betweenness %.3f", u["id"], u["betweenness_centrality"])

    logging.info("Closeness Centrality")
    for u in users:
        logging.info("user %d  closeness %.4f", u["id"], u["closeness_centrality"])

    adj = construct_adjacency(users_dict, friendships)
    eig = compute_eigenvectors(adj)
    logging.info("Eigenvector Centrality")
    for uid, c in enumerate(eig):
        logging.info("user %d  eigenvector %.4f", uid, c)

    users = populate_endorsments(users, endorsements)
    pr = page_rank(users)
    logging.info("PageRank")
    for uid, rank in pr.items():
        logging.info("user %d  pagerank %.4f", uid, rank)

    endorsement_counts = sorted(
        populate_endorsements(users), key=lambda p: p[1], reverse=True
    )
    logging.info("endorsement counts: %s", endorsement_counts)


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
