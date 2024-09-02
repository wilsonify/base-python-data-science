import logging
import math
import os
from inspect import getmembers, isfunction

import pytest

from dsl.c04_linear_algebra import linear_algebra
from dsl.c04_linear_algebra.linear_algebra import distance, dot, get_column, get_row, is_diagonal, magnitude, \
    make_matrix, matrix_add, \
    scalar_multiply, shape, squared_distance, sum_of_squares, vector_add, vector_mean, vector_subtract, vector_sum
from dsl.c06_probability.probability import random_normal

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


@pytest.fixture(name="random_matrix")
def random_matrix_fixture():
    num_points = 100
    data = []
    for _ in range(num_points):
        row = [None, None, None, None]
        row[0] = random_normal()
        row[1] = -5 * row[0] + random_normal()
        row[2] = row[0] + row[1] + 5 * random_normal()
        row[3] = 6 if row[2] > -2 else 0
        data.append(row)
    return data


def test_smoke():
    logging.info("is anything on fire")
    for member in getmembers(linear_algebra):
        if isfunction(member[1]):
            print(member[0])


@pytest.mark.parametrize(
    ("vec1", "vec2", "expected"), (
            ([0, 0, 0], [10, 10, 10], math.sqrt(300)),
            ([0, 0, 0], [-10, -10, -10], math.sqrt(300)))
)
def test_distance(vec1, vec2, expected):
    result = distance(vec1, vec2)
    assert result == expected


@pytest.mark.parametrize(
    ("vec1", "vec2", "expected"), (
            ([1, 1, 1], [10, 10, 10], 30),
            ([1, 1, 1], [-10, -10, -10], -30))
)
def test_dot(vec1, vec2, expected):
    result = dot(vec1, vec2)
    assert result == expected


@pytest.mark.parametrize(
    ("mat1", "col", "expected"), (
            ([[1, 2, 3]], 0, [1]),
            ([[1, 2, 3]], 2, [3]))
)
def test_get_column(mat1, col, expected):
    result = get_column(mat1, col)
    assert result == expected


@pytest.mark.parametrize(
    ("mat1", "row", "expected"), (
            ([[1], [2], [3]], 0, [1]),
            ([[1], [2], [3]], 2, [3]))
)
def test_get_row(mat1, row, expected):
    result = get_row(mat1, row)
    assert result == expected


@pytest.mark.parametrize(
    ("i", "j", "expected"), (
            (1, 1, True),
            (1, 2, False))
)
def test_is_diagonal(i, j, expected):
    result = is_diagonal(i, j)
    assert result == expected


@pytest.mark.parametrize(
    ("vec1", "expected"), (
            ([10, 10, 10], math.sqrt(300)),
            ([-10, -10, -10], math.sqrt(300)))
)
def test_magnitude(vec1, expected):
    result = magnitude(vec1)
    assert result == expected


@pytest.mark.parametrize(
    ("n", "m", "expected"), (
            (1, 1, [[1]]),
            (3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    ))
def test_make_matrix(n, m, expected):
    result = make_matrix(n, m, is_diagonal)
    assert result == expected


@pytest.mark.parametrize(
    ("mat1", "mat2", "expected"), (
            ([[1]], [[1]], [[2]]),
            ([[1, 0], [0, 1]], [[1, 2], [3, 4]], [[2, 2], [3, 5]])
    ))
def test_matrix_add(mat1, mat2, expected):
    result = matrix_add(mat1, mat2)
    assert result == expected


@pytest.mark.parametrize(
    ("v", "c", "expected"), (
            ([2, 1], 1.87, [3.74, 1.87]),
            ([1, 2, 3, 4], 5, [5, 10, 15, 20])
    ))
def test_scalar_multiply(v, c, expected):
    result = scalar_multiply(c, v)
    assert result == expected


def test_shape(random_matrix):
    num_rows, num_columns = shape(random_matrix)
    assert num_rows == 100
    assert num_columns == 4


@pytest.mark.parametrize(
    ("v1", "v2", "expected"), (
            ([1], [1], 0),
            ([1, 0, 0, 1], [1, 2, 3, 4], 22)
    ))
def test_squared_distance(v1, v2, expected):
    result = squared_distance(v1, v2)
    assert result == expected


@pytest.mark.parametrize(
    ("v1", "expected"), (
            ([1], 1),
            ([1, 0, 0, 1], 2),
            ([1, 2, 3, 4], 30)
    ))
def test_sum_of_squares(v1, expected):
    result = sum_of_squares(v1)
    assert result == expected


@pytest.mark.parametrize(
    ("v1", "v2", "expected"), (
            ([1], [1], [2]),
            ([1, 0, 0, 1], [1, 2, 3, 4], [2, 2, 3, 5])
    ))
def test_vector_add(v1, v2, expected):
    result = vector_add(v1, v2)
    assert result == expected


@pytest.mark.parametrize(
    ("v1", "v2", "expected"), (
            ([1], [1], [1]),
            ([1, 0, 0, 1], [1, 2, 3, 4], [1, 1, 1.5, 2.5])
    ))
def test_vector_mean(v1, v2, expected):
    result = vector_mean([v1, v2])
    assert result == expected


@pytest.mark.parametrize(
    ("v1", "v2", "expected"), (
            ([1], [1], [0]),
            ([1, 0, 0, 1], [1, 2, 3, 4], [0, -2, -3, -3])
    ))
def test_vector_subtract(v1, v2, expected):
    result = vector_subtract(v1, v2)
    assert result == expected


@pytest.mark.parametrize(
    ("v1", "v2", "expected"), (
            ([1], [1], [2]),
            ([1, 0, 0, 1], [1, 2, 3, 4], [2, 2, 3, 5])
    ))
def test_vector_sum(v1, v2, expected):
    result = vector_sum([v1, v2])
    assert result == expected
