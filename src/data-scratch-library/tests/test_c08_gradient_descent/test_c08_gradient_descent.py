import logging
import math
import os
import random
from typing import List

from dsl.c04_linear_algebra.e0401_vectors import distance
from dsl.c08_gradient_descent.e0801_estimating_gradient import (
    difference_quotient,
    partial_difference_quotient,
    estimate_gradient
)
from dsl.c08_gradient_descent.e0805_stochastic_gd import in_random_order

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def naive_square(x: float) -> float:
    return x * x


def naive_square_comprehension(x: List[float]) -> float:
    return x[0] * x[1]


def test_smoke():
    logging.info("is anything on fire")


def test_difference_quotient():
    x = 5
    h = 1
    result = difference_quotient(
        f=naive_square,
        x=x,
        h=h
    )
    assert result == (naive_square(x + h) - naive_square(x)) / h


def test_partial_difference_quotient():
    output = partial_difference_quotient(
        f=naive_square_comprehension,
        v=[10.0, 2.0],
        i=0,
        h=1
    )

    assert math.isclose(output, 2.0)


def test_distance():
    v, w, expected = ([63, 150], [67, 160], 10.77)
    result = distance(v=v, w=w)
    assert math.isclose(result, expected, abs_tol=0.01)

    v, w, expected = ([63, 150], [70, 171], 22.14)
    result = distance(v=v, w=w)
    assert math.isclose(result, expected, abs_tol=0.01)

    v, w, expected = ([67, 160], [70, 171], 11.40)
    result = distance(v=v, w=w)
    assert math.isclose(result, expected, abs_tol=0.01)


def test_estimate_gradient():
    output = estimate_gradient(
        f=naive_square_comprehension,
        v=[10.0, 2.0],
        h=1
    )
    assert output == [2.0, 10.0]


def test_in_random_order():
    random.seed(0)
    output = in_random_order(data=[1, 2, 3, 4, 5, 6])
    assert [_ for _ in output] == [5, 3, 2, 1, 6, 4]


