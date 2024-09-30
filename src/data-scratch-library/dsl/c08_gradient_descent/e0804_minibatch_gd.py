"""
compute the gradient
(and take a gradient step)
based on a “minibatch” sampled from the
larger dataset
"""
import random
from typing import List, Iterator

from dsl.c04_linear_algebra.e0401_vectors import vector_mean
from dsl.c08_gradient_descent import T, safe, negate, negate_all
from dsl.c08_gradient_descent.e0802_using_gradient import gradient_step
from dsl.c08_gradient_descent.e0803_fitting_models import linear_gradient


def minibatches(
        dataset: List[T],
        batch_size: int,
        shuffle: bool = True) -> Iterator[List[T]]:
    """Generates `batch_size`-sized minibatches from the dataset"""
    # start indexes 0, batch_size, 2 * batch_size, ...
    batch_starts = [start for start in range(0, len(dataset), batch_size)]
    if shuffle:
        # shuffle the batches
        random.shuffle(batch_starts)
    for start in batch_starts:
        end = start + batch_size
        yield dataset[start:end]


def e0804_minibatch_sgd_main():
    # x ranges from -50 to 49,
    # y is always 20 * x + 5
    inputs = [(x, 20 * x + 5) for x in range(-50, 50)]
    learning_rate = 0.001

    theta = [random.uniform(-1, 1), random.uniform(-1, 1)]
    for epoch in range(1000):
        for batch in minibatches(inputs, batch_size=20):
            grad = vector_mean([linear_gradient(x, y, theta) for x, y in batch])
            theta = gradient_step(theta, grad, -learning_rate)
        print(epoch, theta)

    slope, intercept = theta
    assert 19.9 < slope < 20.1, "slope should be about 20"
    assert 4.9 < intercept < 5.1, "intercept should be about 5"


def e0805_minibatch_sgd_main():
    """
    take gradient steps based on one training example at a time
    just another variation.
    """
    # x ranges from -50 to 49,
    # y is always 20 * x + 5
    inputs = [(x, 20 * x + 5) for x in range(-50, 50)]
    learning_rate = 0.001

    theta = [random.uniform(-1, 1), random.uniform(-1, 1)]
    for epoch in range(100):
        for x, y in inputs:
            grad = linear_gradient(x, y, theta)
            theta = gradient_step(theta, grad, -learning_rate)
        print(epoch, theta)
    slope, intercept = theta
    assert 19.9 < slope < 20.1, "slope should be about 20"
    assert 4.9 < intercept < 5.1, "intercept should be about 5"


#
# minimize / maximize batch
#


def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    """
    use gradient descent to find theta that minimizes target function
    """

    step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]

    theta = theta_0  # set theta to initial value
    target_fn = safe(target_fn)  # safe version of target_fn
    value = target_fn(theta)  # value we're minimizing

    while True:
        gradient = gradient_fn(theta)
        next_thetas = [gradient_step(theta, gradient, -step_size) for step_size in step_sizes]

        # choose the one that minimizes the error function
        next_theta = min(next_thetas, key=target_fn)
        next_value = target_fn(next_theta)

        # stop if we're "converging"
        if abs(value - next_value) < tolerance:
            return theta
        else:
            theta, value = next_theta, next_value


def maximize_batch(
        target_fn,
        gradient_fn,
        theta_0,
        tolerance=0.000001):
    return minimize_batch(
        negate(target_fn),
        negate_all(gradient_fn), theta_0, tolerance
    )


if __name__ == "__main__":
    e0804_minibatch_sgd_main()
    e0805_minibatch_sgd_main()
