import random
from dsl.c06_probability.e0603_normal import inverse_normal_cdf


def random_normal() -> float:
    """
    Returns a random draw from a standard normal distribution (mean=0, std=1).

    This uses inverse transform sampling, where we map a uniformly distributed random number
    from [0, 1) to a corresponding value from the standard normal distribution using the
    inverse CDF (cumulative distribution function).
    """
    return inverse_normal_cdf(random.random())


