import logging
import operator
import random
from logging.config import dictConfig

from data_science_from_scratch import config
from data_science_from_scratch.library.linear_algebra import (
    distance,
    vector_subtract,
    scalar_multiply,
)


def sum_of_squares(v):
    """computes the sum of squared elements in v"""
    return sum(v_i ** 2 for v_i in v)


def difference_quotient(f, x, h):
    try:
        return (f(x + h) - f(x)) / h
    except TypeError:
        diff = map(operator.sub, f(x + h), f(x))
        return [_ / h for _ in diff]

    # purple *, hopefully


def partial_difference_quotient(f, v, i, h):
    # add h to just the i-th element of v
    w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)]
    try:
        return (f(w) - f(v)) / h
    except TypeError:
        diff = map(operator.sub, f(w), f(v))
        return [_ / h for _ in diff]


def estimate_gradient(f, v, h=0.00001):
    return [partial_difference_quotient(f, v, i, h) for i, _ in enumerate(v)]


def step(v, direction, step_size):
    """move step_size in the direction from v"""
    return [v_i + step_size * direction_i for v_i, direction_i in zip(v, direction)]


def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]


def safe(f):
    """define a new function that wraps f and return it"""

    # noinspection PyBroadException
    def safe_f(*args, **kwargs):
        # noinspection PyPep8
        try:
            return f(*args, **kwargs)
        except:
            return float("inf")  # this means "infinity" in Python

    return safe_f


#
#
# minimize / maximize batch
#
#


def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    """use gradient descent to find theta that minimizes target function"""

    step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]

    theta = theta_0  # set theta to initial value
    target_fn = safe(target_fn)  # safe version of target_fn
    value = target_fn(theta)  # value we're minimizing

    while True:
        gradient = gradient_fn(theta)
        next_thetas = [step(theta, gradient, -step_size) for step_size in step_sizes]

        # choose the one that minimizes the error function
        next_theta = min(next_thetas, key=target_fn)
        next_value = target_fn(next_theta)

        # stop if we're "converging"
        if abs(value - next_value) < tolerance:
            return theta
        else:
            theta, value = next_theta, next_value


def negate(f):
    """return a function that for any input x returns -f(x)"""
    return lambda *args, **kwargs: -f(*args, **kwargs)


def negate_all(f):
    """the same when f returns a list of numbers"""
    return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]


def maximize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    return minimize_batch(
        negate(target_fn), negate_all(gradient_fn), theta_0, tolerance
    )


#
# minimize / maximize stochastic
#


def in_random_order(data):
    """generator that returns the elements of data in random order"""
    indexes = [i for i, _ in enumerate(data)]  # create a list of indexes
    random.shuffle(indexes)  # shuffle them
    for i in indexes:  # return the data in that order
        yield data[i]


def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
    data = list(zip(x, y))
    theta = theta_0  # initial guess
    alpha = alpha_0  # initial step size
    min_theta, min_value = None, float("inf")  # the minimum so far
    iterations_with_no_improvement = 0

    # if we ever go 100 iterations with no improvement, stop
    while iterations_with_no_improvement < 100:
        value = sum(target_fn(x_i, y_i, theta) for x_i, y_i in data)

        if value < min_value:
            # if we've found a new minimum, remember it
            # and go back to the original step size
            min_theta, min_value = theta, value
            iterations_with_no_improvement = 0
            alpha = alpha_0
        else:
            # otherwise we're not improving, so try shrinking the step size
            iterations_with_no_improvement += 1
            alpha *= 0.9

        # and take a gradient step for each of the data points
        for x_i, y_i in in_random_order(data):
            gradient_i = gradient_fn(x_i, y_i, theta)
            theta = vector_subtract(theta, scalar_multiply(alpha, gradient_i))

    return min_theta


def maximize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
    return minimize_stochastic(
        negate(target_fn), negate_all(gradient_fn), x, y, theta_0, alpha_0
    )


def main():
    logging.info("using the gradient")

    _v = [random.randint(-10, 10) for _ in range(3)]

    _tolerance = 0.0000001

    while True:
        # print v, sum_of_squares(v)
        _gradient = sum_of_squares_gradient(_v)  # compute the gradient at v
        next_v = step(_v, _gradient, -0.01)  # take a negative gradient step
        if distance(next_v, _v) < _tolerance:  # stop if we're converging
            break
        _v = next_v  # continue if we're not

    logging.info("%r", "minimum v {}".format(_v))
    logging.info("%r", "minimum value {}".format(sum_of_squares(_v)))

    logging.info("using minimize_batch")

    _v = [random.randint(-10, 10) for _ in range(3)]

    _v = minimize_batch(sum_of_squares, sum_of_squares_gradient, _v)

    logging.info("%r", "minimum v  = {}".format(_v))
    logging.info("%r", "minimum value = {}".format(sum_of_squares(_v)))


if __name__ == "__main__":
    dictConfig(config.LOGGING_CONFIG_DICT)
    main()
