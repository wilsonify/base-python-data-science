import logging
import os
import random
from functools import partial

import pytest
from data_science_from_scratch.library import gradient_descent

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def test_smoke():
    logging.info("is anything on fire")


def test_difference_quotient(naive_square):
    x = 5
    h = 1
    result = gradient_descent.difference_quotient(
        f=naive_square,
        x=x,
        h=h
    )
    assert result == (naive_square(x + h) - naive_square(x)) / h


def test_partial_difference_quotient(naive_square_comprehension):
    output = gradient_descent.partial_difference_quotient(
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
    result = gradient_descent.distance(v=v, w=w)
    assert result - expected == pytest.approx(0, abs=0.01)


def test_estimate_gradient(naive_square_comprehension):
    output = gradient_descent.estimate_gradient(
        f=naive_square_comprehension,
        v=[10.0, 2.0],
        h=1
    )
    assert output == [[21.0, 0.0], [0.0, 5.0]]


def test_in_random_order():
    random.seed(0)
    output = gradient_descent.in_random_order(data=[1, 2, 3, 4, 5, 6])
    assert [_ for _ in output] == [5, 3, 2, 1, 6, 4]


def test_maximize_batch():
    X = [[1, 2, 3], [2, 3, 4], [5, 6, 7]]
    gradient_descent.maximize_batch(
        target_fn=partial(gradient_descent.directional_variance, X),
        gradient_fn=partial(gradient_descent.directional_variance_gradient, X),
        theta_0=[1 for _ in X[0]],
        tolerance=0.000001
    )


def test_maximize_stochastic():
    gradient_descent.maximize_stochastic()


def test_minimize_batch():
    gradient_descent.minimize_batch()


def test_minimize_stochastic():
    gradient_descent.minimize_stochastic()


def test_negate():
    gradient_descent.negate()


def test_negate_all():
    gradient_descent.negate_all()


def test_random():
    gradient_descent.random()


def test_safe():
    gradient_descent.safe()


def test_scalar_multiply():
    gradient_descent.scalar_multiply()


def test_step():
    gradient_descent.step()


def test_sum_of_squares():
    gradient_descent.sum_of_squares()


def test_sum_of_squares_gradient():
    gradient_descent.sum_of_squares_gradient()


def test_vector_subtract():
    gradient_descent.vector_subtract()
