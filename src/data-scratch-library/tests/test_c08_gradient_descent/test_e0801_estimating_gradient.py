import math
from random import seed

from dsl.c08_gradient_descent.e0801_estimating_gradient import (
    difference_quotient,
    partial_difference_quotient,
    estimate_gradient
)


def test_difference_quotient_scalar():
    """Test difference_quotient with scalar function"""
    # f(x) = x^2, the derivative at x = 3 should be 2 * 3 = 6
    result = difference_quotient(f=lambda x: x ** 2, x=3.0, h=1e-5)
    expected = 2 * 3
    assert math.isclose(result, expected, rel_tol=0.01)


def test_difference_quotient_vector():
    """Test difference_quotient with vector function"""
    seed(0)
    # f(x) = [x + 1, x - 1], vector function
    result = difference_quotient(f=lambda x: [x + 1, x - 1], x=2.0, h=1e-5)
    assert math.isclose(result[0], 1.0, abs_tol=0.01)
    assert math.isclose(result[1], 1.0, abs_tol=0.01)


def test_partial_difference_quotient():
    """Test partial_difference_quotient"""
    # f(v) = v[0]^2 + v[1]^2, the partial derivative wrt v[0] at (3, 4) should be 2 * 3 = 6

    result = partial_difference_quotient(
        f=lambda v: v[0] ** 2 + v[1] ** 2,
        v=[3.0, 4.0],
        i=0,
        h=1e-5
    )
    expected = 2.0 * 3.0
    assert math.isclose(result, expected, rel_tol=1e-5)


def test_estimate_gradient():
    """Test estimate_gradient"""
    # f(v) = v[0]^2 + v[1]^2, the gradient at (3, 4) should be [6, 8]
    result = estimate_gradient(
        f=lambda v: v[0] ** 2 + v[1] ** 2,
        v=[3.0, 4.0],
        h=1e-5
    )
    expected = [6.0, 8.0]
    assert math.isclose(result[0], expected[0], rel_tol=1e-5)
    assert math.isclose(result[1], expected[1], rel_tol=1e-5)
