"""
Example: popularity, user-based, and item-based recommendations.
"""

import logging
from logging.config import dictConfig

from dsl.c23_recommender_systems.recommender_systems import (
    most_popular_new_interests,
    most_similar_users_to,
    user_based_suggestions,
    most_similar_interests_to,
    item_based_suggestions,
)


def main() -> None:
    logging.info("Most popular new interests for a NoSQL user:")
    logging.info(
        "%s",
        most_popular_new_interests(
            ["NoSQL", "MongoDB", "Cassandra", "HBase", "Postgres"]
        ),
    )
    logging.info("Most popular new interests for an R/Python user:")
    logging.info(
        "%s",
        most_popular_new_interests(
            ["R", "Python", "statistics", "regression", "probability"]
        ),
    )

    logging.info("Users most similar to user 0: %s", most_similar_users_to(0))
    logging.info("User-based suggestions for user 0: %s", user_based_suggestions(0))

    logging.info("Interests most similar to 'Big Data' (index 0): %s", most_similar_interests_to(0))
    logging.info("Item-based suggestions for user 0: %s", item_based_suggestions(0))


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
