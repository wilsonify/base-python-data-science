import random
import pytest
from dsl.c04_linear_algebra import Vector
from dsl.c04_linear_algebra.e0401_vectors import vector_mean
from dsl.c08_gradient_descent.e0802_using_gradient import gradient_step
from dsl.c08_gradient_descent.e0803_fitting_models import linear_gradient


# Sample inputs for testing
inputs = [(x, 20 * x + 5) for x in range(-50, 50)]  # Generate inputs based on y = 20x + 5


# Test for linear_gradient function
def test_linear_gradient():
    theta = [20, 5]  # correct slope and intercept
    x, y = 10, 205  # y = 20 * 10 + 5 = 205
    result = linear_gradient(x, y, theta)
    expected = [0.0, 0.0]  # No error since prediction is accurate
    assert result == expected

    theta = [10, 0]  # wrong slope and intercept
    result = linear_gradient(x, y, theta)
    assert len(result) == 2  # Gradient should have 2 elements (for slope and intercept)


# Test gradient descent convergence
def test_gradient_descent_convergence():
    theta = [random.uniform(-1, 1), random.uniform(-1, 1)]
    learning_rate = 0.001

    for epoch in range(5000):
        grad = vector_mean([linear_gradient(x, y, theta) for x, y in inputs])
        theta = gradient_step(theta, grad, -learning_rate)

    slope, intercept = theta
    assert 19.9 < slope < 20.1, "Slope should converge to around 20"
    assert 4.9 < intercept < 5.1, "Intercept should converge to around 5"


# Test with fixed random seed for reproducibility
def test_gradient_descent_with_seed():
    random.seed(42)  # Fix the seed for reproducibility
    theta = [random.uniform(-1, 1), random.uniform(-1, 1)]
    learning_rate = 0.001

    for epoch in range(5000):
        grad = vector_mean([linear_gradient(x, y, theta) for x, y in inputs])
        theta = gradient_step(theta, grad, -learning_rate)

    slope, intercept = theta
    assert 19.9 < slope < 20.1, "Slope should converge to around 20 with fixed seed"
    assert 4.9 < intercept < 5.1, "Intercept should converge to around 5 with fixed seed"
