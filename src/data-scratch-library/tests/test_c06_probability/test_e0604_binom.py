from math import comb
from random import seed

import pytest

from dsl.c06_probability.e0604_binom import bernoulli_trial, binomial, binom_pdf, binom_cdf, binom_ppf, strength


def test_bernoulli_trial():
    result = bernoulli_trial(0.5)
    expected = [0, 1]
    assert result in expected


@pytest.mark.parametrize(
    ("p", "n", "expected"), (
            (1, 120, pytest.approx(120, abs=0.01)),
            (1, 1, pytest.approx(1, abs=0.01)),
            (0.2, 100, pytest.approx(20, abs=10)),
            (0, 120, pytest.approx(0, abs=0.01))
    ))
def test_binomial(p, n, expected):
    result = binomial(p, n)
    assert result == expected


import pytest


def test_bernoulli_trial():
    # Test that bernoulli_trial returns 1 with probability p and 0 with probability 1-p
    p = 0.7
    trials = 10000
    successes = sum(bernoulli_trial(p) for _ in range(trials))
    assert (successes / trials) >= 0.65  # Check if it is close to p
    assert (successes / trials) <= 0.75  # Check if it is not too far from p


def test_binomial():
    # Test the binomial function
    p = 0.5
    n = 10
    successes = binomial(p, n)
    assert 0 <= successes <= n  # Number of successes should be between 0 and n


def test_binom_pdf():
    # Test the probability density function for specific values
    assert binom_pdf(0, 10, 0.5) == comb(10, 0) * (0.5 ** 0) * (0.5 ** 10)  # P(X=0)
    assert binom_pdf(5, 10, 0.5) == comb(10, 5) * (0.5 ** 5) * (0.5 ** 5)  # P(X=5)
    assert binom_pdf(10, 10, 0.5) == 0.5 ** 10  # P(X=10)


def test_binom_cdf():
    # Test the cumulative distribution function for specific values
    assert binom_cdf(0, 10, 0.5) == binom_pdf(0, 10, 0.5)  # CDF at 0
    assert binom_cdf(1, 10, 0.5) == binom_pdf(0, 10, 0.5) + binom_pdf(1, 10, 0.5)  # CDF at 1
    assert binom_cdf(10, 10, 0.5) == 1.0  # CDF at maximum k should be 1


def test_binom_ppf():
    # Test the percent point function for specific values
    seed(0)
    assert binom_ppf(0.5, 10, 0.5) == 5  # Median for n=10, p=0.5
    assert binom_ppf(0.95, 10, 0.5) == 8  # 95th percentile for n=10, p=0.5
    with pytest.raises(ValueError):
        binom_ppf(-0.1, 10, 0.5)  # q should be in [0, 1]
    with pytest.raises(ValueError):
        binom_ppf(1.1, 10, 0.5)  # q should be in [0, 1]
    with pytest.raises(ValueError):
        binom_ppf(0.5, -1, 0.5)  # n should be non-negative
    with pytest.raises(ValueError):
        binom_ppf(0.5, 10, 1.5)  # p should be in [0, 1]


def test_strength():
    # Test strength calculation
    assert strength(5, 10) >= 0.5  # Expected strength should be >= 0.5 for these inputs
    assert strength(10, 10) == 1.0  # Maximum successes should have maximum strength
