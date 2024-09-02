import logging
from logging.config import dictConfig

from dsl.c17_decision_trees.decision_trees import partition_entropy_by, build_tree_id3, classify


def main():
    inputs_list = [
        ({"level": "Senior", "lang": "Java", "tweets": "no", "phd": "no"}, False),
        ({"level": "Senior", "lang": "Java", "tweets": "no", "phd": "yes"}, False),
        ({"level": "Mid", "lang": "Python", "tweets": "no", "phd": "no"}, True),
        ({"level": "Junior", "lang": "Python", "tweets": "no", "phd": "no"}, True),
        ({"level": "Junior", "lang": "R", "tweets": "yes", "phd": "no"}, True),
        ({"level": "Junior", "lang": "R", "tweets": "yes", "phd": "yes"}, False),
        ({"level": "Mid", "lang": "R", "tweets": "yes", "phd": "yes"}, True),
        ({"level": "Senior", "lang": "Python", "tweets": "no", "phd": "no"}, False),
        ({"level": "Senior", "lang": "R", "tweets": "yes", "phd": "no"}, True),
        ({"level": "Junior", "lang": "Python", "tweets": "yes", "phd": "no"}, True),
        ({"level": "Senior", "lang": "Python", "tweets": "yes", "phd": "yes"}, True),
        ({"level": "Mid", "lang": "Python", "tweets": "no", "phd": "yes"}, True),
        ({"level": "Mid", "lang": "Java", "tweets": "yes", "phd": "no"}, True),
        ({"level": "Junior", "lang": "Python", "tweets": "no", "phd": "yes"}, False),
    ]

    for _key in ["level", "lang", "tweets", "phd"]:
        logging.info("%r", "key = {}".format(_key))
        partition_entropy_key = partition_entropy_by(inputs_list, _key)
        logging.info("%r", "partition_entropy = {}".format(partition_entropy_key))

    senior_inputs = [
        (in_put, label) for in_put, label in inputs_list if in_put["level"] == "Senior"
    ]

    for _key in ["lang", "tweets", "phd"]:
        logging.info("%r", "_key = {}".format(_key))
        partition_entropy2 = partition_entropy_by(senior_inputs, _key)
        logging.info("%r", "partition_entropy = {}".format(partition_entropy2))

    logging.info("building the tree")
    _tree = build_tree_id3(inputs_list)
    logging.info("%r", "tree = {}".format(_tree))

    logging.info(
        "%r",
        "Junior / Java / tweets / no phd {}".format(
            classify(
                _tree, {"level": "Junior", "lang": "Java", "tweets": "yes", "phd": "no"}
            ),
        ),
    )

    logging.info(
        "%r",
        "Junior / Java / tweets / phd {}".format(
            classify(
                _tree,
                {"level": "Junior", "lang": "Java", "tweets": "yes", "phd": "yes"},
            ),
        ),
    )

    logging.info("%r", "Intern {}".format(classify(_tree, {"level": "Intern"})))
    logging.info("%r", "Senior {}".format(classify(_tree, {"level": "Senior"})))


if __name__ == "__main__":
    dictConfig(dict(
        version=1,
        formatters={"simple": {"format": """%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"""}},
        handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
        root={"handlers": ["console"], "level": logging.DEBUG},
    ))
    main()
