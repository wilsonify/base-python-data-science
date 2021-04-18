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


def test_dot():
    linear_algebra.dot()


def test_get_column():
    linear_algebra.get_column()


def test_get_row():
    linear_algebra.get_row()


def test_identity_matrix():
    linear_algebra.identity_matrix()


def test_is_diagonal():
    linear_algebra.is_diagonal()


def test_magnitude():
    linear_algebra.magnitude()


def test_make_matrix():
    linear_algebra.make_matrix()


def test_math():
    linear_algebra.math()


def test_matrix_add():
    linear_algebra.matrix_add()


def test_reduce():
    linear_algebra.reduce()


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
