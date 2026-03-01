import math
import random

from dsl.c15_multiple_regression.multiple_regression import (
    predict,
    error,
    squared_error,
    squared_error_gradient,
    multiple_r_squared,
    bootstrap_sample,
    bootstrap_statistic,
    p_value,
    ridge_penalty,
    squared_error_ridge,
    ridge_penalty_gradient,
    squared_error_ridge_gradient,
    lasso_penalty,
)


# Simple data: y = 1 + 2*x1 + 3*x2
# x_i = [1, x1, x2] (first element is intercept term)
BETA = [1, 2, 3]
X_I = [1, 4, 5]  # predict = 1 + 2*4 + 3*5 = 24
Y_I = 24


def test_predict():
    assert predict(X_I, BETA) == 24
    assert predict([1, 0, 0], BETA) == 1


def test_error():
    assert error(X_I, Y_I, BETA) == 0  # perfect prediction
    assert error(X_I, 30, BETA) == 6  # 30 - 24


def test_squared_error():
    assert squared_error(X_I, Y_I, BETA) == 0
    assert squared_error(X_I, 30, BETA) == 36  # 6^2


def test_squared_error_gradient():
    # error = 0 for perfect prediction => gradient all zeros
    grad = squared_error_gradient(X_I, Y_I, BETA)
    assert grad == [0, 0, 0]

    # error = 6 for y=30: gradient = [-2 * x_ij * 6]
    grad = squared_error_gradient(X_I, 30, BETA)
    assert grad == [-2 * 1 * 6, -2 * 4 * 6, -2 * 5 * 6]


def test_multiple_r_squared():
    x = [[1, 1], [1, 2], [1, 3]]
    y = [3, 5, 7]  # y = 1 + 2*x1
    beta = [1, 2]
    r2 = multiple_r_squared(x, y, beta)
    assert math.isclose(r2, 1.0, abs_tol=1e-10)


def test_bootstrap_sample():
    random.seed(42)
    data = [1, 2, 3, 4, 5]
    sample = bootstrap_sample(data)
    assert len(sample) == len(data)
    # All elements should be from the original data
    assert all(s in data for s in sample)


def test_bootstrap_statistic():
    random.seed(42)
    data = [1, 2, 3, 4, 5]
    results = bootstrap_statistic(data, sum, num_samples=10)
    assert len(results) == 10
    # Each result should be a sum of 5 elements drawn from data
    for r in results:
        assert 5 <= r <= 25  # min=5*1, max=5*5


def test_p_value_positive():
    # Large positive beta_hat_j => small p-value
    p = p_value(3.0, 1.0)
    assert 0 < p < 0.01


def test_p_value_negative():
    # Large negative beta_hat_j => small p-value
    p = p_value(-3.0, 1.0)
    assert 0 < p < 0.01


def test_p_value_zero():
    # beta_hat_j = 0 => p-value = 1.0 (not significant)
    p = p_value(0.0, 1.0)
    assert math.isclose(p, 1.0, abs_tol=0.01)


def test_ridge_penalty():
    beta = [5, 2, 3]
    alpha = 0.1
    # Penalty = alpha * (beta[1]^2 + beta[2]^2) = 0.1 * (4 + 9) = 1.3
    assert math.isclose(ridge_penalty(beta, alpha), 1.3, abs_tol=1e-10)


def test_squared_error_ridge():
    result = squared_error_ridge(X_I, Y_I, BETA, 0.1)
    # squared_error = 0, ridge_penalty = 0.1 * (4 + 9) = 1.3
    assert math.isclose(result, 1.3, abs_tol=1e-10)


def test_ridge_penalty_gradient():
    beta = [5, 2, 3]
    alpha = 0.1
    grad = ridge_penalty_gradient(beta, alpha)
    # [0, 2*0.1*2, 2*0.1*3] = [0, 0.4, 0.6]
    assert grad[0] == 0
    assert math.isclose(grad[1], 0.4, abs_tol=1e-10)
    assert math.isclose(grad[2], 0.6, abs_tol=1e-10)


def test_squared_error_ridge_gradient():
    grad = squared_error_ridge_gradient(X_I, Y_I, BETA, 0.1)
    # squared_error_gradient is [0,0,0] (perfect fit)
    # ridge_penalty_gradient is [0, 0.4, 0.6]
    assert math.isclose(grad[0], 0, abs_tol=1e-10)
    assert math.isclose(grad[1], 0.4, abs_tol=1e-10)
    assert math.isclose(grad[2], 0.6, abs_tol=1e-10)


def test_lasso_penalty():
    beta = [5, -2, 3]
    alpha = 0.1
    # Penalty = 0.1 * (|-2| + |3|) = 0.1 * 5 = 0.5
    assert math.isclose(lasso_penalty(beta, alpha), 0.5, abs_tol=1e-10)
