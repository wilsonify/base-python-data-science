"""
1. Start with a random value for theta.
2. Compute the mean of the gradients.
3. Adjust theta in that direction.
4. Repeat.
"""
import random

from dsl.c04_linear_algebra import Vector
from dsl.c04_linear_algebra.e0401_vectors import vector_mean
from dsl.c08_gradient_descent.e0802_using_gradient import gradient_step


def linear_gradient(x: float, y: float, theta: Vector) -> Vector:
    slope, intercept = theta
    predicted = slope * x + intercept  # The prediction of the model.
    error = (predicted - y)  # error is (predicted - actual).
    squared_error = error ** 2
    grad = [2 * error * x, 2 * error]
    return grad


def main():

    # Start with random values for slope and intercept
    theta = [random.uniform(-1, 1), random.uniform(-1, 1)]
    learning_rate = 0.001
    for epoch in range(5000):
        # Compute the mean of the gradients
        grad = vector_mean([linear_gradient(x, y, theta) for x, y in inputs])
        # Take a step in that direction
        theta = gradient_step(theta, grad, -learning_rate)
        print(epoch, theta)

    slope, intercept = theta
    assert 19.9 < slope < 20.1, "slope should be about 20"
    assert 4.9 < intercept < 5.1, "intercept should be about 5"


if __name__ == "__main__":
    main()
