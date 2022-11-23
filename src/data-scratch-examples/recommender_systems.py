import logging
from logging.config import dictConfig

from dsl.recommender_systems import popular_interests, most_popular_new_interests, most_similar_users_to, \
    user_based_suggestions, most_similar_interests_to, item_based_suggestions


def main():
    logging.info("%r", "Popular Interests {}".format(popular_interests))

    logging.info("Most Popular New Interests")

    logging.info(
        "%r",
        "already like: NoSQL, MongoDB, Cassandra, HBase, Postgres {}".format(
            most_popular_new_interests(
                ["NoSQL", "MongoDB", "Cassandra", "HBase", "Postgres"]
            )
        ),
    )

    logging.info(
        "%r",
        "already like R,Python,statistics,regression,probability:  {}".format(
            most_popular_new_interests(
                ["R", "Python", "statistics", "regression", "probability"]
            )
        ),
    )

    logging.info("User based similarity")
    logging.info("%r", "most similar to 0 {}".format(most_similar_users_to(0)))
    logging.info("%r", "Suggestions for 0 {}".format(user_based_suggestions(0)))

    logging.info("Item based similarity")
    logging.info(
        "%r", "most similar to 'Big Data' {}".format(most_similar_interests_to(0))
    )
    logging.info("%r", "suggestions for user 0 {}".format(item_based_suggestions(0)))


if __name__ == "__main__":
    dictConfig(dict(
        version=1,
        formatters={"simple": {"format": """%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"""}},
        handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
        root={"handlers": ["console"], "level": logging.DEBUG},
    ))
    main()
