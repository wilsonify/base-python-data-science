import math

from dsl.c14_simple_linear_regression.simple_linear_regression import (
    predict,
    error,
    sum_of_squared_errors,
    least_squares_fit,
    total_sum_of_squares,
    r_squared,
    squared_error,
    squared_error_gradient,
)


# Perfect linear data: y = 2x + 1
X = [1, 2, 3, 4, 5]
Y = [3, 5, 7, 9, 11]


def test_predict():
    assert predict(1, 2, 3) == 7  # 2*3 + 1
    assert predict(0, 1, 5) == 5  # 1*5 + 0
    assert predict(1, 0, 5) == 1  # 0*5 + 1


def test_error():
    assert error(1, 2, 3, 7) == 0  # y_i - predict = 7 - 7
    assert error(0, 1, 5, 10) == 5  # 10 - 5


def test_sum_of_squared_errors():
    # Perfect fit: all errors are 0
    assert sum_of_squared_errors(1, 2, X, Y) == 0
    # Off by 1 on each: 5 * 1^2 = 5
    assert sum_of_squared_errors(2, 2, X, Y) == 5


def test_least_squares_fit():
    alpha, beta = least_squares_fit(X, Y)
    assert math.isclose(alpha, 1.0, abs_tol=1e-10)
    assert math.isclose(beta, 2.0, abs_tol=1e-10)


def test_total_sum_of_squares():
    result = total_sum_of_squares(Y)
    # mean of Y = 7, deviations: -4, -2, 0, 2, 4 => squares: 16+4+0+4+16 = 40
    assert math.isclose(result, 40.0, abs_tol=1e-10)


def test_r_squared():
    # Perfect fit => R^2 = 1.0
    r2 = r_squared(1, 2, X, Y)
    assert math.isclose(r2, 1.0, abs_tol=1e-10)


def test_squared_error():
    theta = (1, 2)
    # Perfect prediction at x=3, y=7 => error=0, squared=0
    assert squared_error(3, 7, theta) == 0
    # x=3, y=10 => predict=7, error=3, squared=9
    assert squared_error(3, 10, theta) == 9


def test_squared_error_gradient():
    theta = (1, 2)
    # x=3, y=10 => error=3, gradient = [-2*3, -2*3*3] = [-6, -18]
    grad = squared_error_gradient(3, 10, theta)
    assert math.isclose(grad[0], -6, abs_tol=1e-10)
    assert math.isclose(grad[1], -18, abs_tol=1e-10)

    # Perfect prediction => gradient = [0, 0]
    grad = squared_error_gradient(3, 7, theta)
    assert grad == [0, 0]
