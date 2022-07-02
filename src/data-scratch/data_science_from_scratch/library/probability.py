import logging
import math
import random
from logging.config import dictConfig

from data_science_from_scratch import config


def random_normal():
    """returns a random draw from a standard normal distribution"""
    return inverse_normal_cdf(random.random())


def random_kid():
    return random.choice(["boy", "girl"])


def uniform_pdf(x, a=0, b=1):
    assert b > a, "maximum,b, must be greater than minimum,a"
    return 1 / (b - a) if a <= x < b else 0


def uniform_cdf(x, a=0, b=1):
    """returns the probability that a uniform random variable is less than x"""
    if x < a:
        return 0
    if a < x < b:
        return (x - a) / (b - a)  # e.g. P(X < 0.4) = 0.4
    if b <= x:
        return 1


def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return math.exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma)


def normal_cdf(x, mu=0.0, sigma=1.0):
    return (1.0 + math.erf((x - mu) / math.sqrt(2.0) / sigma)) / 2.0


def plot_normal_cdfs(plt):
    xs = [x / 10.0 for x in range(-50, 50)]
    plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs], "-", label="mu=0,sigma=1")
    plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], "--", label="mu=0,sigma=2")
    plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ":", label="mu=0,sigma=0.5")
    plt.plot(xs, [normal_cdf(x, mu=-1) for x in xs], "-.", label="mu=-1,sigma=1")
    plt.legend(loc=4)  # bottom right
    plt.show()


def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """find approximate inverse using binary search"""

    # if not standard, compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z, low_p = -10.0, 0  # normal_cdf(-10) is (very close to) 0
    hi_z, hi_p = 10.0, 1  # normal_cdf(10)  is (very close to) 1
    mid_z = (low_z + hi_z) / 2
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2  # consider the midpoint
        mid_p = normal_cdf(mid_z)  # and the cdf's value there
        if mid_p < p:
            # midpoint is still too low, search above it
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            # midpoint is still too high, search below it
            hi_z, hi_p = mid_z, mid_p
        else:
            break

    return mid_z


def bernoulli_trial(p):
    return 1 if random.random() < p else 0


def binomial(p, n):
    return sum(bernoulli_trial(p) for _ in range(n))


def mysqrt(x: float) -> float:  # noqa: E501
    """ square root """
    return math.sqrt(x)


def mystrength(actual: float, expected: float) -> float:  # noqa: E501
    """ signal strength """
    eps = 0.001
    strength = actual / (expected + eps)
    return strength


if __name__ == "__main__":
    dictConfig(config.LOGGING_CONFIG_DICT)  #
    # CONDITIONAL PROBABILITY
    #

    both_girls = 0
    older_girl = 0
    either_girl = 0

    random.seed(0)
    for _ in range(10000):
        younger = random_kid()
        older = random_kid()
        if older == "girl":
            older_girl += 1
        if older == "girl" and younger == "girl":
            both_girls += 1
        if older == "girl" or younger == "girl":
            either_girl += 1

    logging.info(
        "%r", "P(both | older): {}".format(both_girls / older_girl)
    )  # 0.514 ~ 1/2)
    logging.info(
        "%r", "P(both | either): {}".format(both_girls / either_girl)
    )  # 0.342 ~ 1/3)
