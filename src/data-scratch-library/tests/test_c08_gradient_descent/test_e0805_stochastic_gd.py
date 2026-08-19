import math
import random

import pytest

from dsl.c08_gradient_descent.e0805_stochastic_gd import in_random_order, minimize_stochastic, maximize_stochastic


def clip(value, lower_bound, upper_bound):
    """Clips the value to be within the lower and upper bounds."""
    high = min(value, upper_bound)
    low = max(lower_bound, high)
    return low


def simple_quadratic_fn(x, y, theta):
    """Simple quadratic target function for testing"""
    return clip(theta[0] * x + theta[1] - y, -1e50, 1e50) ** 2


def simple_quadratic_gradient(x, y, theta):
    """Gradient of the simple quadratic target function"""
    error = theta[0] * x + theta[1] - y
    return [2 * error * x, 2 * error]


def negated_quadratic_fn(x, y, theta):
    """Negative quadratic: has a maximum at the correct solution"""
    return -simple_quadratic_fn(x, y, theta)


def negated_quadratic_gradient(x, y, theta):
    """Gradient of the negative quadratic"""
    error = theta[0] * x + theta[1] - y
    return [-2 * error * x, -2 * error]


def test_in_random_order():
    """Test for the in_random_order generator"""
    data = [1, 2, 3, 4, 5]
    shuffled_data = list(in_random_order(data))

    assert set(shuffled_data) == set(data)
    assert len(shuffled_data) == len(data)
    assert shuffled_data != data


def test_minimize_stochastic():
    """Test minimize_stochastic convergence"""
    random.seed(42)
    x = [i * 0.1 for i in range(-50, 50)]
    y = [20 * xi + 5 for xi in x]

    theta_0 = [random.uniform(-1, 1), random.uniform(-1, 1)]
    alpha_0 = 0.01

    theta_min = minimize_stochastic(simple_quadratic_fn, simple_quadratic_gradient, x, y, theta_0, alpha_0)

    slope, intercept = theta_min
    assert math.isclose(slope, 20, abs_tol=0.5)
    assert math.isclose(intercept, 5, abs_tol=0.5)


def test_maximize_stochastic():
    """Test maximize_stochastic convergence"""
    random.seed(42)
    x = [i * 0.1 for i in range(-50, 50)]
    y = [20 * xi + 5 for xi in x]

    theta_0 = [random.uniform(-1, 1), random.uniform(-1, 1)]
    alpha_0 = 0.01

    theta_max = maximize_stochastic(negated_quadratic_fn, negated_quadratic_gradient, x, y, theta_0, alpha_0)

    slope, intercept = theta_max
    assert math.isclose(slope, 20, abs_tol=0.5)
    assert math.isclose(intercept, 5, abs_tol=0.5)


@pytest.mark.parametrize("alpha_0", [0.1, 0.01, 0.001])
def test_minimize_stochastic_with_different_alpha(alpha_0):
    """Test minimize_stochastic with different learning rates"""
    random.seed(42)
    x = [i * 0.1 for i in range(-50, 50)]
    y = [20 * xi + 5 for xi in x]

    theta_0 = [random.uniform(-1, 1), random.uniform(-1, 1)]

    theta_min = minimize_stochastic(simple_quadratic_fn, simple_quadratic_gradient, x, y, theta_0, alpha_0)

    slope, intercept = theta_min
    assert math.isclose(slope, 20, abs_tol=0.5), f"Slope should converge to around 20 with alpha {alpha_0}"
    assert math.isclose(intercept, 5, abs_tol=0.5), f"Intercept should converge to around 5 with alpha {alpha_0}"


@pytest.mark.parametrize("alpha_0", [0.1, 0.01, 0.001])
def test_maximize_stochastic_with_different_alpha(alpha_0):
    """Test maximize_stochastic with different learning rates"""
    random.seed(42)
    x = [i * 0.1 for i in range(-50, 50)]
    y = [20 * xi + 5 for xi in x]

    theta_0 = [random.uniform(-1, 1), random.uniform(-1, 1)]

    theta_max = maximize_stochastic(negated_quadratic_fn, negated_quadratic_gradient, x, y, theta_0, alpha_0)

    slope, intercept = theta_max
    assert math.isclose(slope, 20, abs_tol=0.5), f"Slope should converge to around 20 with alpha {alpha_0}"
    assert math.isclose(intercept, 5, abs_tol=0.5), f"Intercept should converge to around 5 with alpha {alpha_0}"
