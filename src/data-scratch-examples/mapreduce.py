"""
Analyzing Status Updates
"""
import logging
from datetime import datetime
from functools import partial
from logging.config import dictConfig

from dsl.mapreduce import (
    wc_mapper,
    word_count,
    wc_reducer,
    map_reduce,
    matrix_multiply_mapper,
    matrix_multiply_reducer,
    sum_reducer,
    most_popular_word_reducer,
    liker_mapper,
    count_distinct_reducer
)
from dsl.c13_naive_bayes.naive_bayes import tokenize

status_updates = [
    {
        "id": 1,
        "username": "joelgrus",
        "text": "Is anyone interested in a data science book?",
        "created_at": datetime(2013, 12, 21, 11, 47, 0),
        "liked_by": ["data_guy", "data_gal", "bill"],
    },
    # add your own
]


def data_science_day_mapper(status_update):
    """yields (day_of_week, 1) if status_update contains "data science" """
    if "data science" in status_update["text"].lower():
        day_of_week = status_update["created_at"].weekday()
        yield (day_of_week, 1)


def words_per_user_mapper(status_update):
    user = status_update["username"]
    for word in tokenize(status_update["text"]):
        yield (user, (word, 1))


A = [[3, 2]]
B = [[4, -2], [10, 0]]
A_entries = [("A", 0, 0, 3), ("A", 0, 1, 2), ]
B_entries = [("B", 0, 0, 4), ("B", 0, 1, -1), ("B", 1, 0, 10), ("B", 1, 1, 0)]
entries = A_entries + B_entries


def multipy(_entries):
    # matrix multiplication
    _mapper = partial(matrix_multiply_mapper, 3)
    _reducer = partial(matrix_multiply_reducer, 3)
    result = map_reduce(_entries, _mapper, _reducer)
    return result


def main():
    _documents = ["data science", "big data", "science fiction"]

    wc_mapper_results = [result for document in _documents for result in wc_mapper(document)]

    logging.info("%r", "wc_mapper results {}".format(wc_mapper_results))

    logging.info("%r", "word count results {}".format(word_count(_documents)))

    word_count_using_map_reduce = map_reduce(_documents, wc_mapper, wc_reducer)
    logging.info("%r", f"word count using map_reduce function {word_count_using_map_reduce}")

    data_science_days = map_reduce(status_updates, data_science_day_mapper, sum_reducer)

    user_words = map_reduce(
        status_updates,
        words_per_user_mapper,
        most_popular_word_reducer
    )
    distinct_likers_per_user = map_reduce(
        status_updates,
        liker_mapper,
        count_distinct_reducer
    )

    logging.info("%r", "data science days {}".format(data_science_days))
    logging.info("%r", "user words {}".format(user_words))
    logging.info("%r", "distinct likes {}".format(distinct_likers_per_user))

    result = multipy(entries)
    logging.info("map-reduce matrix multiplication")
    logging.info("%r", f"entries: {entries}")
    logging.info("%r", f"result: {result}")


if __name__ == "__main__":
    dictConfig(dict(
        version=1,
        formatters={"simple": {"format": """%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"""}},
        handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
        root={"handlers": ["console"], "level": logging.DEBUG},
    ))
    main()
