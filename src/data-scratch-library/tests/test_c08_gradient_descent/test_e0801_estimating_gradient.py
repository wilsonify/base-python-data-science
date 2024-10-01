import math
from random import seed

from dsl.c08_gradient_descent.e0801_estimating_gradient import (
    difference_quotient,
    partial_difference_quotient,
    estimate_gradient
)


# Test difference_quotient with scalar function
def test_difference_quotient_scalar():
    # f(x) = x^2, the derivative at x = 3 should be 2 * 3 = 6
    f = lambda x: x ** 2
    x = 3.0
    h = 1e-5
    result = difference_quotient(f, x, h)
    expected = 2 * x
    assert math.isclose(result, expected, rel_tol=1e-5)


# Test difference_quotient with vector function
def test_difference_quotient_vector():
    seed(0)
    # f(x) = [x + 1, x - 1], vector function
    f = lambda x: [x + 1, x - 1]
    x = 2.0
    h = 1e-5
    result = difference_quotient(f, x, h)
    assert math.isclose(result[0], 1.0, abs_tol=0.01)
    assert math.isclose(result[1], 1.0, abs_tol=0.01)


# Test partial_difference_quotient
def test_partial_difference_quotient():
    # f(v) = v[0]^2 + v[1]^2, the partial derivative wrt v[0] at (3, 4) should be 2 * 3 = 6
    f = lambda v: v[0] ** 2 + v[1] ** 2
    v = [3.0, 4.0]
    i = 0
    h = 1e-5
    result = partial_difference_quotient(f, v, i, h)
    expected = 2 * v[0]
    assert math.isclose(result, expected, rel_tol=1e-5)


# Test estimate_gradient
def test_estimate_gradient():
    # f(v) = v[0]^2 + v[1]^2, the gradient at (3, 4) should be [6, 8]
    f = lambda v: v[0] ** 2 + v[1] ** 2
    v = [3.0, 4.0]
    h = 1e-5
    result = estimate_gradient(f, v, h)
    expected = [6.0, 8.0]
    assert all(math.isclose(r, e, rel_tol=1e-5) for r, e in zip(result, expected))
