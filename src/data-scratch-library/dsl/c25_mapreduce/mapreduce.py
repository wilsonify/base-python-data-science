"""
A minimal MapReduce framework: mapper → group → reducer.
"""

import logging
import math
from collections import Counter, defaultdict
from functools import partial
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    Iterator,
    List,
    Sequence,
    Tuple,
    TypeVar,
)

from dsl.c13_naive_bayes.naive_bayes import tokenize

K = TypeVar("K")
V = TypeVar("V")


# ---------- word count ----------

def wc_mapper(document: str) -> Iterator[Tuple[str, int]]:
    """Emit *(word, 1)* for every word in *document*."""
    for word in tokenize(document):
        yield (word, 1)


def wc_reducer(word: str, counts: List[int]) -> Iterator[Tuple[str, int]]:
    """Sum counts for *word*."""
    yield (word, sum(counts))


def word_count(documents: Iterable[str]) -> List[Tuple[str, int]]:
    """Count words in *documents* using a simple local MapReduce."""
    collector: Dict[str, List[int]] = defaultdict(list)
    for document in documents:
        for word, count in wc_mapper(document):
            collector[word].append(count)
    return [
        output
        for word, counts in collector.items()
        for output in wc_reducer(word, counts)
    ]


# ---------- generic MapReduce ----------

def map_reduce(
    inputs: Iterable[Any],
    mapper: Callable[[Any], Iterable[Tuple[Any, Any]]],
    reducer: Callable[..., Iterable[Tuple[Any, Any]]],
) -> List[Tuple[Any, Any]]:
    """Run a single-machine MapReduce over *inputs*."""
    collector: Dict[Any, List[Any]] = defaultdict(list)
    for inp in inputs:
        for key, value in mapper(inp):
            collector[key].append(value)
    return [
        output
        for key, values in collector.items()
        for output in reducer(key, values)
    ]


# ---------- generic reducers ----------

def reduce_with(
    aggregation_fn: Callable[[List[Any]], Any],
    key: Any,
    values: List[Any],
) -> Iterator[Tuple[Any, Any]]:
    """Reduce *key*/*values* by applying *aggregation_fn*."""
    yield (key, aggregation_fn(values))


def values_reducer(
    aggregation_fn: Callable[[List[Any]], Any],
) -> Callable[..., Iterator[Tuple[Any, Any]]]:
    """Turn an aggregation function into a reducer."""
    return partial(reduce_with, aggregation_fn)


sum_reducer = values_reducer(sum)
max_reducer = values_reducer(max)
min_reducer = values_reducer(min)
count_distinct_reducer = values_reducer(lambda vals: len(set(vals)))


def most_popular_word_reducer(
    user: str, words_and_counts: List[Tuple[str, int]]
) -> Iterator[Tuple[str, Tuple[str, int]]]:
    """Return the word with the highest total count for *user*."""
    word_counts: Counter = Counter()
    for word, count in words_and_counts:
        word_counts[word] += count
    word, count = word_counts.most_common(1)[0]
    yield (user, (word, count))


# ---------- social-media helpers ----------

def liker_mapper(
    status_update: Dict[str, Any],
) -> Iterator[Tuple[str, str]]:
    """Emit *(username, liker)* for each like."""
    user = status_update["username"]
    for liker in status_update["liked_by"]:
        yield (user, liker)


# ---------- matrix multiplication ----------

def matrix_multiply_mapper(
    m: int, element: Tuple[str, int, int, float]
) -> Iterator[Tuple[Tuple[int, int], Tuple[int, float]]]:
    """
    Emit entries for matrix multiplication.

    *m* is the shared dimension (columns of A / rows of B).
    *element* is *(matrix_name, i, j, value)*.
    """
    matrix, i, j, value = element
    if matrix == "A":
        for column in range(m):
            yield ((i, column), (j, value))
    else:
        for row in range(m):
            yield ((row, j), (i, value))


def matrix_multiply_reducer(
    m: int,
    key: Tuple[int, int],
    indexed_values: List[Tuple[int, float]],
) -> Iterator[Tuple[Tuple[int, int], float]]:
    """Sum the element-wise products for cell *key*."""
    logging.debug("m = %s", m)
    by_index: Dict[int, List[float]] = defaultdict(list)
    for index, value in indexed_values:
        by_index[index].append(value)
    total = sum(
        vals[0] * vals[1]
        for vals in by_index.values()
        if len(vals) == 2
    )
    if not math.isclose(total, 0.0, abs_tol=1e-4):
        yield (key, total)
