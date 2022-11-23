import logging
import random
from logging.config import dictConfig

from dsl.gradient_descent import sum_of_squares_gradient, step, sum_of_squares, minimize_batch
from dsl.linear_algebra import distance


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
    dictConfig(dict(
        version=1,
        formatters={"simple": {"format": """%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"""}},
        handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
        root={"handlers": ["console"], "level": logging.DEBUG},
    ))
    main()
