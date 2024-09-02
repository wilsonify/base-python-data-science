import logging
import math
import os
from inspect import getmembers, isfunction

from dsl.c04_linear_algebra import linear_algebra
from dsl.c04_linear_algebra.linear_algebra import distance, dot, get_column, get_row, is_diagonal, magnitude, \
    make_matrix, matrix_add, \
    scalar_multiply, shape, squared_distance, sum_of_squares, vector_add, vector_mean, vector_subtract, vector_sum
from dsl.c09_getting_data.random_matrix import random_matrix

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def test_smoke():
    logging.info("is anything on fire")
    for member in getmembers(linear_algebra):
        if isfunction(member[1]):
            print(member[0])


def test_distance():
    vec1, vec2, expected = ([0, 0, 0], [10, 10, 10], math.sqrt(300))
    result = distance(vec1, vec2)
    assert result == expected

    vec1, vec2, expected = ([0, 0, 0], [-10, -10, -10], math.sqrt(300))
    result = distance(vec1, vec2)
    assert result == expected


def test_dot():
    vec1, vec2, expected = ([1, 1, 1], [10, 10, 10], 30)
    result = dot(vec1, vec2)
    assert result == expected

    vec1, vec2, expected = ([1, 1, 1], [-10, -10, -10], -30)
    result = dot(vec1, vec2)
    assert result == expected


def test_get_column():
    mat1, col, expected = ([[1, 2, 3]], 0, [1])
    result = get_column(mat1, col)
    assert result == expected

    mat1, col, expected = ([[1, 2, 3]], 2, [3])
    result = get_column(mat1, col)
    assert result == expected


def test_get_row():
    mat1, row, expected = ([[1], [2], [3]], 0, [1])
    result = get_row(mat1, row)
    assert result == expected

    mat1, row, expected = ([[1], [2], [3]], 2, [3])
    result = get_row(mat1, row)
    assert result == expected


def test_is_diagonal():
    i, j, expected = (1, 1, True)
    result = is_diagonal(i, j)
    assert result == expected

    i, j, expected = (1, 2, False)
    result = is_diagonal(i, j)
    assert result == expected


def test_magnitude():
    vec1, expected = ([10, 10, 10], math.sqrt(300))
    result = magnitude(vec1)
    assert result == expected

    vec1, expected = ([-10, -10, -10], math.sqrt(300))
    result = magnitude(vec1)
    assert result == expected


def test_make_matrix():
    n, m, expected = (1, 1, [[1]])
    result = make_matrix(n, m, is_diagonal)
    assert result == expected

    n, m, expected = (3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    result = make_matrix(n, m, is_diagonal)
    assert result == expected


def test_matrix_add():
    mat1, mat2, expected = ([[1]], [[1]], [[2]])
    result = matrix_add(mat1, mat2)
    assert result == expected

    mat1, mat2, expected = ([[1, 0], [0, 1]], [[1, 2], [3, 4]], [[2, 2], [3, 5]])
    result = matrix_add(mat1, mat2)
    assert result == expected


def test_scalar_multiply():
    v, c, expected = ([2, 1], 1.87, [3.74, 1.87])
    result = scalar_multiply(c, v)
    assert result == expected

    v, c, expected = ([1, 2, 3, 4], 5, [5, 10, 15, 20])
    result = scalar_multiply(c, v)
    assert result == expected


def test_shape():
    num_rows, num_columns = shape(random_matrix())
    assert num_rows == 100
    assert num_columns == 4


def test_squared_distance():
    v1, v2, expected = ([1], [1], 0)
    result = squared_distance(v1, v2)
    assert result == expected

    v1, v2, expected = ([1, 0, 0, 1], [1, 2, 3, 4], 22)
    result = squared_distance(v1, v2)
    assert result == expected


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


def test_vector_add():
    v1, v2, expected = ([1], [1], [2])
    result = vector_add(v1, v2)
    assert result == expected

    v1, v2, expected = ([1, 0, 0, 1], [1, 2, 3, 4], [2, 2, 3, 5])
    result = vector_add(v1, v2)
    assert result == expected


def test_vector_mean():
    v1, v2, expected = ([1], [1], [1])
    result = vector_mean([v1, v2])
    assert result == expected

    v1, v2, expected = ([1, 0, 0, 1], [1, 2, 3, 4], [1, 1, 1.5, 2.5])
    result = vector_mean([v1, v2])
    assert result == expected


def test_vector_subtract():
    v1, v2, expected = ([1], [1], [0])
    result = vector_subtract(v1, v2)
    assert result == expected

    v1, v2, expected = ([1, 0, 0, 1], [1, 2, 3, 4], [0, -2, -3, -3])
    result = vector_subtract(v1, v2)
    assert result == expected


def test_vector_sum():
    v1, v2, expected = ([1], [1], [2])
    result = vector_sum([v1, v2])
    assert result == expected

    v1, v2, expected = ([1, 0, 0, 1], [1, 2, 3, 4], [2, 2, 3, 5])
    result = vector_sum([v1, v2])
    assert result == expected
