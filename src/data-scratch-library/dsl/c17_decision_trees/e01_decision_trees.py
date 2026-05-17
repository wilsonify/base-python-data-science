"""
Example: build a decision tree on interview data and make predictions.
"""

import logging
from logging.config import dictConfig

from dsl.c17_decision_trees.decision_trees import (
    partition_entropy_by,
    build_tree_id3,
    classify,
)
from dsl.c17_decision_trees.data import inputs_list


def main() -> None:
    for key in ["level", "lang", "tweets", "phd"]:
        ent = partition_entropy_by(inputs_list, key)
        logging.info("partition entropy by %s = %s", key, ent)

    senior_inputs = [
        (attrs, label) for attrs, label in inputs_list if attrs["level"] == "Senior"
    ]
    for key in ["lang", "tweets", "phd"]:
        ent = partition_entropy_by(senior_inputs, key)
        logging.info("senior partition entropy by %s = %s", key, ent)

    logging.info("building the tree")
    tree = build_tree_id3(inputs_list)
    logging.info("tree = %s", tree)

    logging.info(
        "Junior / Java / tweets / no phd => %s",
        classify(tree, {"level": "Junior", "lang": "Java", "tweets": "yes", "phd": "no"}),
    )
    logging.info(
        "Junior / Java / tweets / phd => %s",
        classify(tree, {"level": "Junior", "lang": "Java", "tweets": "yes", "phd": "yes"}),
    )
    logging.info("Intern => %s", classify(tree, {"level": "Intern"}))
    logging.info("Senior => %s", classify(tree, {"level": "Senior"}))


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
