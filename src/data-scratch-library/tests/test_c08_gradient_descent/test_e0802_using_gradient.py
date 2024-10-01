import random
import pytest
from dsl.c04_linear_algebra import Vector
from dsl.c04_linear_algebra.e0401_vectors import scalar_multiply, vector_add, distance
from dsl.c08_gradient_descent.e0802_using_gradient import gradient_step, sum_of_squares_gradient


# Test for gradient_step
def test_gradient_step():
    v = [1.0, 2.0, 3.0]
    gradient = [0.1, 0.2, 0.3]
    step_size = 0.1
    result = gradient_step(v, gradient, step_size)
    expected = vector_add(v, scalar_multiply(step_size, gradient))
    assert result == expected


# Test for sum_of_squares_gradient
def test_sum_of_squares_gradient():
    v = [1.0, -2.0, 3.0]
    result = sum_of_squares_gradient(v)
    expected = [2 * v_i for v_i in v]
    assert result == expected


# Test the gradient descent process (main logic) without randomness
def test_gradient_descent_convergence():
    v = [0.1, -0.2, 0.3]
    for epoch in range(1000):
        grad = sum_of_squares_gradient(v)
        v = gradient_step(v, grad, -0.01)

    # The vector should converge close to [0, 0, 0]
    assert distance(v, [0, 0, 0]) < 0.001


# Test the gradient descent process with fixed seed
def test_gradient_descent_with_seed():
    random.seed(42)
    v = [random.uniform(-10, 10) for _ in range(3)]

    for epoch in range(1000):
        grad = sum_of_squares_gradient(v)
        v = gradient_step(v, grad, -0.01)

    # After 1000 steps, the result should be near [0, 0, 0]
    assert distance(v, [0, 0, 0]) < 0.001
