import logging
import os
import random
from functools import partial
from inspect import getmembers, isfunction

import pytest

from dsl import gradient_descent
from dsl.linear_algebra import distance
from dsl.gradient_descent import (
    difference_quotient,
    partial_difference_quotient,
    estimate_gradient,
    in_random_order,
    maximize_batch,
    maximize_stochastic,
    negate,
    negate_all
)
from dsl.manipulation import directional_variance, directional_variance_gradient
from dsl.multiple_regression import squared_error, squared_error_gradient

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def test_smoke():
    logging.info("is anything on fire")
    for member in getmembers(gradient_descent):
        if isfunction(member[1]):
            print(member[0])


def test_difference_quotient(naive_square):
    x = 5
    h = 1
    result = difference_quotient(
        f=naive_square,
        x=x,
        h=h
    )
    assert result == (naive_square(x + h) - naive_square(x)) / h


def test_partial_difference_quotient(naive_square_comprehension):
    output = partial_difference_quotient(
        f=naive_square_comprehension,
        v=[10.0, 2.0],
        i=0,
        h=1
    )
    assert output == [pytest.approx(21.0), pytest.approx(0.0)]


@pytest.mark.parametrize(
    ('v', 'w', 'expected'),
    (
            ([63, 150], [67, 160], 10.77),
            ([63, 150], [70, 171], 22.14),
            ([67, 160], [70, 171], 11.40)
    )
)
def test_distance(v, w, expected):
    result = distance(v=v, w=w)
    assert result - expected == pytest.approx(0, abs=0.01)


def test_estimate_gradient(naive_square_comprehension):
    output = estimate_gradient(
        f=naive_square_comprehension,
        v=[10.0, 2.0],
        h=1
    )
    assert output == [[21.0, 0.0], [0.0, 5.0]]


def test_in_random_order():
    random.seed(0)
    output = in_random_order(data=[1, 2, 3, 4, 5, 6])
    assert [_ for _ in output] == [5, 3, 2, 1, 6, 4]


def test_maximize_batch():
    x = [[1, 2, 3], [2, 3, 4], [5, 6, 7]]
    maximize_batch(
        target_fn=partial(directional_variance, x),
        gradient_fn=partial(directional_variance_gradient, x),
        theta_0=[1 for _ in x[0]],
        tolerance=0.000001
    )


def test_maximize_stochastic():
    x = [
        [1, 49, 4, 0], [1, 41, 9, 0], [1, 40, 8, 0],
        [1, 25, 6, 0], [1, 21, 1, 0], [1, 21, 0, 0],
        [1, 19, 3, 0], [1, 19, 0, 0], [1, 18, 9, 0], [1, 18, 8, 0]
    ]
    y = [
        68.77, 51.25, 52.08,
        38.36, 44.54, 57.13,
        51.4, 41.42, 31.22, 34.76,
    ]
    maximize_stochastic(
        target_fn=negate(squared_error),
        gradient_fn=negate_all(squared_error_gradient),
        x=x,
        y=y,
        theta_0=[random.random() for _ in x[0]],
        alpha_0=0.01
    )
