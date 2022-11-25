import logging
from logging.config import dictConfig

from dsl.recommender_systems import (
    popular_interests,
    most_popular_new_interests,
    most_similar_users_to,
    user_based_suggestions,
    most_similar_interests_to,
    item_based_suggestions
)


def main():
    logging.info("%r", f"Popular Interests {popular_interests}")
    logging.info("Most Popular New Interests")
    most_pop = most_popular_new_interests(["NoSQL", "MongoDB", "Cassandra", "HBase", "Postgres"])
    most_pop2 = most_popular_new_interests(["R", "Python", "statistics", "regression", "probability"])
    logging.info("%r", f"already like: NoSQL, MongoDB, Cassandra, HBase, Postgres {most_pop}")
    logging.info("%r", f"already like R,Python,statistics,regression,probability:  {most_pop2}")

    logging.info("User based similarity")
    logging.info("%r", f"most similar to 0 {most_similar_users_to(0)}")
    logging.info("%r", f"Suggestions for 0 {user_based_suggestions(0)}")

    logging.info("Item based similarity")
    logging.info("%r", f"most similar to 'Big Data' {most_similar_interests_to(0)}" )
    logging.info("%r", f"suggestions for user 0 {item_based_suggestions(0)}")


if __name__ == "__main__":
    dictConfig(dict(
        version=1,
        formatters={"simple": {"format": """%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"""}},
        handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
        root={"handlers": ["console"], "level": logging.DEBUG},
    ))
    main()
