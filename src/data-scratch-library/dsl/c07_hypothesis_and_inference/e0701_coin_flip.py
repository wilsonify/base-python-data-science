#####
#
# probabilities a normal lies in an interval
#
# the normal cdf _is_ the probability the variable is below a threshold
# it's above the threshold if it's not below the threshold
# it's between if it's less than hi, but not less than lo
# it's outside if it's not between

######

import math
from typing import Tuple

from dsl.c06_probability.e0603_normal import normal_cdf

normal_probability_below = normal_cdf


def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
    """finds mu and sigma corresponding to a Binomial(n, p)"""
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma


def normal_probability_above(lo, mu=0.0, sigma=1.0):
    return 1 - normal_cdf(lo, mu, sigma)


def normal_probability_between(lo, hi, mu=0.0, sigma=1.0):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)


def normal_probability_outside(lo, hi, mu=0.0, sigma=1.0):
    return 1 - normal_probability_between(lo, hi, mu, sigma)


if __name__ == "__main__":
    mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)



