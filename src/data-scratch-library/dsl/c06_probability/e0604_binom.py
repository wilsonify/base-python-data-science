import random
from math import comb


def bernoulli_trial(p):
    """Returns 1 with probability p and 0 with probability 1-p"""
    return 1 if random.random() < p else 0


def binomial(p, n):
    """Returns the sum of n bernoulli(p) trials"""
    return sum(bernoulli_trial(p) for _ in range(n))


def binom_pdf(k, n, p):
    """Calculate the probability density function for a binomial distribution.

    Args:
        k (int): Number of successes.
        n (int): Number of trials.
        p (float): Probability of success on each trial.

    Returns:
        float: The probability of obtaining exactly k successes in n trials.
    """
    if k < 0 or k > n:
        return 0.0  # Probability is 0 if k is out of bounds
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))


def binom_cdf(k, n, p):
    """Calculate the cumulative distribution function for a binomial distribution.

    Args:
        k (int): Number of successes.
        n (int): Number of trials.
        p (float): Probability of success on each trial.

    Returns:
        float: The cumulative probability of obtaining at most k successes in n trials.
    """
    return sum(comb(n, i) * (p ** i) * ((1 - p) ** (n - i)) for i in range(k + 1))


def binom_ppf(q, n, p):
    """Calculate the percent point function (PPF) for a binomial distribution.

    Args:
        q (float): The cumulative probability (0 <= q <= 1).
        n (int): Number of trials.
        p (float): Probability of success on each trial.

    Returns:
        int: The smallest number of successes k such that P(X <= k) >= q.
    """
    if q < 0 or q > 1:
        raise ValueError("q must be between 0 and 1")
    if n < 0 or p < 0 or p > 1:
        raise ValueError("n must be non-negative and p must be between 0 and 1")

    cumulative_prob = 0.0
    for k in range(n + 1):
        cumulative_prob += binom_pdf(k, n, p)
        if cumulative_prob >= q:
            return k

    return n  # If q = 1, return the maximum successes n


def strength(actual, expected):
    return binom_cdf(actual, expected, 0.5)
