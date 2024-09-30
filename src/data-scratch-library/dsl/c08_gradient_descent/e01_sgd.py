import logging
import random
from logging.config import dictConfig

from dsl.c04_linear_algebra.e0401_vectors import distance, sum_of_squares
from dsl.c08_gradient_descent.e0802_using_gradient import sum_of_squares_gradient, gradient_step
from dsl.c08_gradient_descent.e0804_minibatch_gd import minimize_batch


def main():
    logging.info("using the gradient")
    _v = [random.randint(-10, 10) for _ in range(3)]
    _tolerance = 0.0000001
    max_iter = 1000
    for i in range(max_iter):
        # print v, sum_of_squares(v)
        _gradient = sum_of_squares_gradient(_v)  # compute the gradient at v
        next_v = gradient_step(_v, _gradient, -0.01)  # take a negative gradient step
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
    dictConfig(dict(
        version=1,
        formatters={"simple": {"format": """%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"""}},
        handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
        root={"handlers": ["console"], "level": logging.DEBUG},
    ))
    main()
