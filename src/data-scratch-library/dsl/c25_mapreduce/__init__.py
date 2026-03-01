"""
Chapter 25: MapReduce

A simple MapReduce framework with word-count and matrix-multiply examples.
"""

from .mapreduce import (
    wc_mapper,
    wc_reducer,
    word_count,
    map_reduce,
    reduce_with,
    values_reducer,
    sum_reducer,
    max_reducer,
    min_reducer,
    count_distinct_reducer,
    most_popular_word_reducer,
    liker_mapper,
    matrix_multiply_mapper,
    matrix_multiply_reducer,
)
