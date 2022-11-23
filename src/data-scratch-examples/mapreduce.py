import logging
from functools import partial
from logging.config import dictConfig

from dsl.mapreduce import wc_mapper, word_count, wc_reducer, map_reduce, data_science_days, user_words, \
    distinct_likers_per_user, matrix_multiply_mapper, matrix_multiply_reducer


def main():
    _documents = ["data science", "big data", "science fiction"]

    wc_mapper_results = [
        result for document in _documents for result in wc_mapper(document)
    ]

    logging.info("%r", "wc_mapper results {}".format(wc_mapper_results))

    logging.info("%r", "word count results {}".format(word_count(_documents)))

    logging.info(
        "%r",
        "word count using map_reduce function {}".format(
            map_reduce(_documents, wc_mapper, wc_reducer)
        ),
    )

    logging.info("%r", "data science days {}".format(data_science_days))

    logging.info("%r", "user words {}".format(user_words))

    logging.info("%r", "distinct likers {}".format(distinct_likers_per_user))

    # matrix multiplication

    entries = [
        ("A", 0, 0, 3),
        ("A", 0, 1, 2),
        ("B", 0, 0, 4),
        ("B", 0, 1, -1),
        ("B", 1, 0, 10),
    ]
    _mapper = partial(matrix_multiply_mapper, 3)
    _reducer = partial(matrix_multiply_reducer, 3)

    logging.info("map-reduce matrix multiplication")
    logging.info("%r", "entries: {}".format(entries))
    logging.info("%r", "result: {}".format(map_reduce(entries, _mapper, _reducer)))


if __name__ == "__main__":
    dictConfig(dict(
        version=1,
        formatters={"simple": {"format": """%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"""}},
        handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
        root={"handlers": ["console"], "level": logging.DEBUG},
    ))
    main()
