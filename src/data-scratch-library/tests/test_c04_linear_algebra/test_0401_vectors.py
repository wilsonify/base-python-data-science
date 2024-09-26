import logging
import math
import os

from dsl.c04_linear_algebra.e0401_vectors import (
    distance,
    dot,
    magnitude,
    scalar_multiply,
    squared_distance,
    sum_of_squares,
    vector_add,
    vector_mean,
    vector_subtract,
    vector_sum
)

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)

height_weight_age = [
    70,  # inches,
    170,  # pounds,
    40  # years
]
grades = [
    95,  # exam1
    80,  # exam2
    75,  # exam3
    62  # exam4
]


def test_smoke():
    logging.info("is anything on fire")


def test_vector_add():
    v1, v2, expected = ([1], [1], [2])
    result = vector_add(v1, v2)
    assert result == expected

    v1, v2, expected = ([1, 0, 0, 1], [1, 2, 3, 4], [2, 2, 3, 5])
    result = vector_add(v1, v2)
    assert result == expected

    v1, v2, expected = [1, 2], [2, 1], [3, 3]
    result = vector_add(v1, v2)
    assert result == expected


def test_vector_subtract():
    v1, v2, expected = ([1], [1], [0])
    result = vector_subtract(v1, v2)
    assert result == expected

    v1, v2, expected = ([1, 0, 0, 1], [1, 2, 3, 4], [0, -2, -3, -3])
    result = vector_subtract(v1, v2)
    assert result == expected

    v1, v2, expected = [5, 7, 9], [4, 5, 6], [1, 2, 3]
    result = vector_subtract(v1, v2)
    assert result == expected


def test_vector_mean():
    v1, v2, expected = ([1], [1], [1])
    result = vector_mean([v1, v2])
    assert result == expected

    v1, v2, expected = ([1, 0, 0, 1], [1, 2, 3, 4], [1, 1, 1.5, 2.5])
    result = vector_mean([v1, v2])
    assert result == expected

    assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]


def test_vector_sum():
    v1, v2, expected = ([1], [1], [2])
    result = vector_sum([v1, v2])
    assert result == expected

    v1, v2, expected = ([1, 0, 0, 1], [1, 2, 3, 4], [2, 2, 3, 5])
    result = vector_sum([v1, v2])
    assert result == expected

    result = vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]])
    expected = [16, 20]
    assert result == expected


def test_scalar_multiply():
    v, c, expected = ([2, 1], 1.87, [3.74, 1.87])
    result = scalar_multiply(c, v)
    assert result == expected

    v, c, expected = ([1, 2, 3, 4], 5, [5, 10, 15, 20])
    result = scalar_multiply(c, v)
    assert result == expected

    assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


def test_dot():
    vec1, vec2, expected = ([1, 1, 1], [10, 10, 10], 30)
    result = dot(vec1, vec2)
    assert result == expected

    vec1, vec2, expected = ([1, 1, 1], [-10, -10, -10], -30)
    result = dot(vec1, vec2)
    assert result == expected

    assert dot([1, 2, 3], [4, 5, 6]) == 32


def test_sum_of_squares():
    v1, expected = ([1], 1)
    result = sum_of_squares(v1)
    assert result == expected

    v1, expected = ([1, 0, 0, 1], 2)
    result = sum_of_squares(v1)
    assert result == expected

    v1, expected = ([1, 2, 3, 4], 30)
    result = sum_of_squares(v1)
    assert result == expected

    assert sum_of_squares([1, 2, 3]) == 14



def test_magnitude():
    vec1, expected = ([10, 10, 10], math.sqrt(300))
    result = magnitude(vec1)
    assert result == expected

    vec1, expected = ([-10, -10, -10], math.sqrt(300))
    result = magnitude(vec1)
    assert result == expected

    assert magnitude([3, 4]) == 5


def test_squared_distance():
    v1, v2, expected = ([1], [1], 0)
    result = squared_distance(v1, v2)
    assert result == expected

    v1, v2, expected = ([1, 0, 0, 1], [1, 2, 3, 4], 22)
    result = squared_distance(v1, v2)
    assert result == expected

def test_distance():
    vec1, vec2, expected = ([0, 0, 0], [10, 10, 10], math.sqrt(300))
    result = distance(vec1, vec2)
    assert result == expected

    vec1, vec2, expected = ([0, 0, 0], [-10, -10, -10], math.sqrt(300))
    result = distance(vec1, vec2)
    assert result == expected


