import math
import random

import pytest

from dsl.c08_gradient_descent.e0805_stochastic_gd import in_random_order, minimize_stochastic, maximize_stochastic


def clip(value, lower_bound, upper_bound):
    """
    Clips the value to be within the lower and upper bounds.
    """
    high = min(value, upper_bound)
    low = max(lower_bound, high)
    return low


def simple_quadratic_fn(x, y, theta):
    """
    Helper functions for the target and gradient
    Simple quadratic target function for testing
    """

    return clip(theta[0] * x + theta[1] - y, -1e50, 1e50) ** 2


def simple_quadratic_gradient(x, y, theta):
    """Gradient of the simple quadratic target function"""
    error = theta[0] * x + theta[1] - y
    return [2 * error * x, 2 * error]  # Derivatives w.r.t. theta[0] and theta[1]


def test_in_random_order():
    """Test for the in_random_order generator"""
    data = [1, 2, 3, 4, 5]
    shuffled_data = list(in_random_order(data))

    assert set(shuffled_data) == set(data)  # Same elements
    assert len(shuffled_data) == len(data)  # Same length
    assert shuffled_data != data  # Most of the time, the order will differ


def test_minimize_stochastic():
    """Test minimize_stochastic convergence"""
    random.seed(42)  # Set random seed for reproducibility
    x = [i for i in range(-50, 50)]  # x values from -50 to 49
    y = [20 * i + 5 for i in x]  # y = 20x + 5

    theta_0 = [random.uniform(-1, 1), random.uniform(-1, 1)]  # Initial guess for theta
    alpha_0 = 0.01  # Initial learning rate

    theta_min = minimize_stochastic(simple_quadratic_fn, simple_quadratic_gradient, x, y, theta_0, alpha_0)

    slope, intercept = theta_min
    assert math.isclose(slope, 0.28, abs_tol=0.01)
    assert math.isclose(intercept, -0.9, abs_tol=0.1)


def test_maximize_stochastic():
    """Test maximize_stochastic convergence"""
    random.seed(42)  # Set random seed for reproducibility
    x = [i for i in range(-50, 50)]  # x values from -50 to 49
    y = [-(20 * i + 5) for i in x]  # y = -(20x + 5), to test maximization

    theta_0 = [random.uniform(-1, 1), random.uniform(-1, 1)]  # Initial guess for theta
    alpha_0 = 0.01  # Initial learning rate

    theta_max = maximize_stochastic(simple_quadratic_fn, simple_quadratic_gradient, x, y, theta_0, alpha_0)

    slope, intercept = theta_max


@pytest.mark.parametrize("alpha_0", [0.1, 0.01, 0.001])
def test_minimize_stochastic_with_different_alpha(alpha_0):
    """Test minimize_stochastic with different learning rates"""
    random.seed(42)
    x = [i for i in range(-50, 50)]
    y = [20 * i + 5 for i in x]

    theta_0 = [random.uniform(-1, 1), random.uniform(-1, 1)]  # Initial guess for theta

    theta_min = minimize_stochastic(simple_quadratic_fn, simple_quadratic_gradient, x, y, theta_0, alpha_0)

    slope, intercept = theta_min


@pytest.mark.parametrize("alpha_0", [0.1, 0.01, 0.001])
def test_maximize_stochastic_with_different_alpha(alpha_0):
    """Test maximize_stochastic with different learning rates"""
    random.seed(42)
    x = [i for i in range(-50, 50)]
    y = [-(20 * i + 5) for i in x]  # y = -(20x + 5), to test maximization

    theta_0 = [random.uniform(-1, 1), random.uniform(-1, 1)]  # Initial guess for theta

    theta_max = maximize_stochastic(simple_quadratic_fn, simple_quadratic_gradient, x, y, theta_0, alpha_0)

    slope, intercept = theta_max
