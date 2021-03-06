import logging
import math
import os

from data_science_from_scratch.library import linear_algebra

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def test_smoke():
    logging.info("is anything on fire")


import pytest


@pytest.mark.parametrize(
    ("vec1", "vec2", "expected"), (
            ([0, 0, 0], [10, 10, 10], math.sqrt(300)),
            ([0, 0, 0], [-10, -10, -10], math.sqrt(300)))
)
def test_distance(vec1, vec2, expected):
    result = linear_algebra.distance(vec1, vec2)
    assert result == expected


@pytest.mark.parametrize(
    ("vec1", "vec2", "expected"), (
            ([1, 1, 1], [10, 10, 10], 30),
            ([1, 1, 1], [-10, -10, -10], -30))
)
def test_dot(vec1, vec2, expected):
    result = linear_algebra.dot(vec1, vec2)
    assert result == expected


@pytest.mark.parametrize(
    ("mat1", "col", "expected"), (
            ([[1, 2, 3]], 0, [1]),
            ([[1, 2, 3]], 2, [3]))
)
def test_get_column(mat1, col, expected):
    result = linear_algebra.get_column(mat1, col)
    assert result == expected


@pytest.mark.parametrize(
    ("mat1", "row", "expected"), (
            ([[1], [2], [3]], 0, [1]),
            ([[1], [2], [3]], 2, [3]))
)
def test_get_row(mat1, row, expected):
    result = linear_algebra.get_row(mat1, row)
    assert result == expected


@pytest.mark.parametrize(
    ("i", "j", "expected"), (
            (1, 1, True),
            (1, 2, False))
)
def test_is_diagonal(i, j, expected):
    result = linear_algebra.is_diagonal(i, j)
    assert result == expected


@pytest.mark.parametrize(
    ("vec1", "expected"), (
            ([10, 10, 10], math.sqrt(300)),
            ([-10, -10, -10], math.sqrt(300)))
)
def test_magnitude(vec1, expected):
    result = linear_algebra.magnitude(vec1)
    assert result == expected


@pytest.mark.parametrize(
    ("n", "m", "expected"), (
            (1, 1, [[1]]),
            (3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    ))
def test_make_matrix(n, m, expected):
    result = linear_algebra.make_matrix(n, m, linear_algebra.is_diagonal)
    assert result == expected


@pytest.mark.parametrize(
    ("mat1", "mat2", "expected"), (
            ([[1]], [[1]], [[2]]),
            ([[1, 0], [0, 1]], [[1, 2], [3, 4]], [[2, 2], [3, 5]])
    ))
def test_matrix_add(mat1, mat2, expected):
    result = linear_algebra.matrix_add(mat1, mat2)
    assert result == expected


def test_scalar_multiply():
    linear_algebra.scalar_multiply()


def test_shape():
    linear_algebra.shape()


def test_squared_distance():
    linear_algebra.squared_distance()


def test_sum_of_squares():
    linear_algebra.sum_of_squares()


def test_vector_add():
    linear_algebra.vector_add()


def test_vector_mean():
    linear_algebra.vector_mean()


def test_vector_subtract():
    linear_algebra.vector_subtract()


def test_vector_sum():
    linear_algebra.vector_sum()
