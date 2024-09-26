"""
functions for working with vectors
"""
import math
from functools import reduce

from dsl.c04_linear_algebra import Vector


def vector_add(v: Vector, w: Vector) -> Vector:
    """
    adds two vectors component-wise
    List comprehensions are generally faster
    """
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def vector_subtract(v, w):
    """subtracts two vectors component-wise"""
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors):
    return reduce(vector_add, vectors)


def scalar_multiply(c, v):
    return [c * v_i for v_i in v]


def vector_mean(vectors):
    """compute the vector whose i-th element is the mean of the
    i-th elements of the input vectors"""
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)


def magnitude(v):
    return math.sqrt(sum_of_squares(v))


def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))


def distance(v: Vector, w: Vector) -> float:
    return math.sqrt(squared_distance(v, w))


def distance2(v: Vector, w: Vector) -> float:
    return magnitude(vector_subtract(v, w))
