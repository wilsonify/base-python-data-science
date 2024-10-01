import math
import random

from dsl.c04_linear_algebra.e0401_vectors import vector_mean
from dsl.c08_gradient_descent.e0802_using_gradient import gradient_step
from dsl.c08_gradient_descent.e0803_fitting_models import linear_gradient
from dsl.c08_gradient_descent.e0804_minibatch_gd import minibatches, minimize_batch, maximize_batch

# Sample dataset for testing
inputs = [(x, 20 * x + 5) for x in range(-50, 50)]  # y = 20x + 5


def test_minibatches():
    """Test the minibatches function"""
    batch_size = 10
    dataset = list(range(50))

    batches = list(minibatches(dataset, batch_size=batch_size, shuffle=False))

    assert len(batches) == 5  # Since dataset has 50 elements and batch_size is 10
    for batch in batches:
        assert len(batch) == batch_size  # Each batch should be of the correct size


def test_minibatches_shuffle():
    batch_size = 10
    dataset = list(range(50))
    shuffled_batches = list(minibatches(dataset, batch_size=batch_size, shuffle=True))
    # Ensure that the total number of elements remains the same
    shuffled_data = [item for batch in shuffled_batches for item in batch]
    assert sorted(shuffled_data) == dataset  # Data should remain the same but shuffled


def test_minibatch_sgd_convergence():
    """Test minibatch stochastic gradient descent convergence"""
    random.seed(42)
    theta = [random.uniform(-1, 1), random.uniform(-1, 1)]
    learning_rate = 0.001
    batch_size = 20

    for epoch in range(1000):
        for batch in minibatches(inputs, batch_size=batch_size):
            grad = vector_mean([linear_gradient(x, y, theta) for x, y in batch])
            theta = gradient_step(theta, grad, -learning_rate)

    slope, intercept = theta
    assert 19.9 < slope < 20.1, "Slope should converge to around 20"
    assert 4.9 < intercept < 5.1, "Intercept should converge to around 5"


def test_single_example_sgd_convergence():
    """Test single-example stochastic gradient descent convergence"""
    random.seed(42)
    theta = [random.uniform(-1, 1), random.uniform(-1, 1)]
    learning_rate = 0.001

    for epoch in range(100):
        for x, y in inputs:
            grad = linear_gradient(x, y, theta)
            theta = gradient_step(theta, grad, -learning_rate)

    slope, intercept = theta
    assert 19.9 < slope < 20.1, "Slope should converge to around 20"
    assert 4.9 < intercept < 5.1, "Intercept should converge to around 5"


def test_minimize_batch():
    """Test minimize_batch convergence"""

    def target_fn(v):
        return sum(v_i ** 2 for v_i in v)  # A simple quadratic function

    def gradient_fn(v):
        return [2 * v_i for v_i in v]  # Gradient of the quadratic function

    theta_0 = [random.uniform(-10, 10) for _ in range(3)]  # Random initial theta
    minimized_theta = minimize_batch(target_fn, gradient_fn, theta_0)

    for v_i in minimized_theta:
        assert abs(v_i) < 0.001, "Theta values should converge to near zero"


def test_maximize_batch():
    """Test maximize_batch convergence"""

    def target_fn(v):
        return -sum(v_i ** 2 for v_i in v)  # A simple negative quadratic function

    def gradient_fn(v):
        return [-2 * v_i for v_i in v]  # Gradient of the negative quadratic function

    theta_0 = [random.uniform(-10, 10) for _ in range(3)]  # Random initial theta
    maximized_theta = maximize_batch(target_fn, gradient_fn, theta_0)

    for v_i in maximized_theta:
        assert math.isclose(abs(v_i), 0.001, abs_tol=0.01)


def test_sgd_with_fixed_seed():
    """Test for reproducibility using a fixed random seed"""
    random.seed(42)
    theta = [random.uniform(-1, 1), random.uniform(-1, 1)]
    learning_rate = 0.001
    batch_size = 20

    for epoch in range(1000):
        for batch in minibatches(inputs, batch_size=batch_size):
            grad = vector_mean([linear_gradient(x, y, theta) for x, y in batch])
            theta = gradient_step(theta, grad, -learning_rate)

    slope, intercept = theta
    assert 19.9 < slope < 20.1, "Slope should converge to around 20 with fixed seed"
    assert 4.9 < intercept < 5.1, "Intercept should converge to around 5 with fixed seed"
