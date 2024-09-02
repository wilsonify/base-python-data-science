import logging
import math
from collections import defaultdict, Counter
from functools import partial

from dsl.c13_naive_bayes.naive_bayes import tokenize


def word_count_old(documents):
    """word count not using MapReduce"""
    return Counter(word for document in documents for word in tokenize(document))


def wc_mapper(document):
    """for each word in the document, emit (word,1)"""
    for word in tokenize(document):
        yield (word, 1)


def wc_reducer(word, counts):
    """sum up the counts for a word"""
    yield (word, sum(counts))


def word_count(documents):
    """count the words in the input documents using MapReduce"""

    # place to store grouped values
    collector = defaultdict(list)

    for document in documents:
        for word, count in wc_mapper(document):
            collector[word].append(count)

    return [
        output
        for word, counts in collector.items()
        for output in wc_reducer(word, counts)
    ]


def map_reduce(inputs, mapper, reducer):
    """runs MapReduce on the inputs using mapper and reducer"""
    collector = defaultdict(list)

    for in_put in inputs:
        for key, value in mapper(in_put):
            collector[key].append(value)

    return [
        output for key, values in collector.items() for output in reducer(key, values)
    ]


def reduce_with(aggregation_fn, key, values):
    """reduces a key-values pair by applying aggregation_fn to the values"""
    yield (key, aggregation_fn(values))


def values_reducer(aggregation_fn):
    """turns a function (values -> output) into a reducer"""
    return partial(reduce_with, aggregation_fn)


sum_reducer = values_reducer(sum)
max_reducer = values_reducer(max)
min_reducer = values_reducer(min)
count_distinct_reducer = values_reducer(lambda values: len(set(values)))


def most_popular_word_reducer(user, words_and_counts):
    """given a sequence of (word, count) pairs,
    return the word with the highest total count"""

    word_counts = Counter()
    for word, count in words_and_counts:
        word_counts[word] += count

    word, count = word_counts.most_common(1)[0]

    yield (user, (word, count))


def most_popular_word_reducer(user, words_and_counts):
    """given a sequence of (word, count) pairs,
    return the word with the highest total count"""

    word_counts = Counter()
    for word, count in words_and_counts:
        word_counts[word] += count

    word, count = word_counts.most_common(1)[0]

    yield (user, (word, count))


def liker_mapper(status_update):
    user = status_update["username"]
    for liker in status_update["liked_by"]:
        yield (user, liker)


#
# matrix multiplication
#


def matrix_multiply_mapper(m, element):
    """
    m is the common dimension (columns of A, rows of B)
    element is a tuple (matrix_name, i, j, value)
    """
    matrix, i, j, value = element

    if matrix == "A":
        for column in range(m):
            # A_ij is the jth entry in the sum for each C_i_column
            yield ((i, column), (j, value))
    else:
        for row in range(m):
            # B_ij is the ith entry in the sum for each C_row_j
            yield ((row, j), (i, value))


def matrix_multiply_reducer(m, key, indexed_values):
    logging.debug("%s", "m = {}".format(m))
    results_by_index = defaultdict(list)
    for index, value in indexed_values:
        results_by_index[index].append(value)

    # sum up all the products of the positions with two results
    sum_product = sum(
        results[0] * results[1]
        for results in results_by_index.values()
        if len(results) == 2
    )

    if not math.isclose(sum_product, 0.0, abs_tol=0.0001):
        yield (key, sum_product)
