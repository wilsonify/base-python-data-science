"""
Example: word count, status-update analysis, and matrix multiplication.
"""

import logging
from datetime import datetime
from functools import partial
from logging.config import dictConfig

from dsl.c13_naive_bayes.naive_bayes import tokenize
from dsl.c25_mapreduce.data import A_entries, B_entries, status_updates
from dsl.c25_mapreduce.mapreduce import (
    count_distinct_reducer,
    liker_mapper,
    map_reduce,
    matrix_multiply_mapper,
    matrix_multiply_reducer,
    most_popular_word_reducer,
    sum_reducer,
    wc_mapper,
    wc_reducer,
    word_count,
)


def data_science_day_mapper(status_update):
    """Yield *(day_of_week, 1)* if the update mentions 'data science'."""
    if "data science" in status_update["text"].lower():
        yield (status_update["created_at"].weekday(), 1)


def words_per_user_mapper(status_update):
    """Yield *(username, (word, 1))* for every word."""
    user = status_update["username"]
    for word in tokenize(status_update["text"]):
        yield (user, (word, 1))


def main() -> None:
    documents = ["data science", "big data", "science fiction"]

    mapper_results = [r for doc in documents for r in wc_mapper(doc)]
    logging.info("wc_mapper results: %s", mapper_results)
    logging.info("word_count results: %s", word_count(documents))

    mr_word_count = map_reduce(documents, wc_mapper, wc_reducer)
    logging.info("map_reduce word count: %s", mr_word_count)

    ds_days = map_reduce(status_updates, data_science_day_mapper, sum_reducer)
    logging.info("data-science days: %s", ds_days)

    user_words = map_reduce(
        status_updates, words_per_user_mapper, most_popular_word_reducer
    )
    logging.info("user top words: %s", user_words)

    distinct_likers = map_reduce(
        status_updates, liker_mapper, count_distinct_reducer
    )
    logging.info("distinct likers: %s", distinct_likers)

    # Matrix multiplication
    entries = A_entries + B_entries
    mapper = partial(matrix_multiply_mapper, 2)
    reducer = partial(matrix_multiply_reducer, 2)
    result = map_reduce(entries, mapper, reducer)
    logging.info("matrix multiply entries: %s", entries)
    logging.info("matrix multiply result: %s", result)


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
