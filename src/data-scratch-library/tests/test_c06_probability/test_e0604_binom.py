from math import comb
from random import seed

import pytest

from dsl.c06_probability.e0604_binom import bernoulli_trial, binomial, binom_pdf, binom_cdf, binom_ppf, strength


def test_bernoulli_trial():
    result = bernoulli_trial(0.5)
    expected = [0, 1]
    assert result in expected


@pytest.mark.parametrize(
    ("n", "p", "expected"), (
            (120, 1, pytest.approx(120, abs=0.01)),
            (1, 1, pytest.approx(1, abs=0.01)),
            (100, 0.2, pytest.approx(20, abs=10)),
            (120, 0, pytest.approx(0, abs=0.01))
    ))
def test_binomial_parametrized(n, p, expected):
    result = binomial(n, p)
    assert result == expected


def test_bernoulli_trial_statistical():
    # Test that bernoulli_trial returns 1 with probability p and 0 with probability 1-p
    p = 0.7
    trials = 10000
    successes = sum(bernoulli_trial(p) for _ in range(trials))
    assert (successes / trials) >= 0.65
    assert (successes / trials) <= 0.75


def test_binomial():
    # Test the binomial function
    p = 0.5
    n = 10
    successes = binomial(n, p)
    assert 0 <= successes <= n


def test_binom_pdf():
    assert binom_pdf(0, 10, 0.5) == comb(10, 0) * (0.5 ** 0) * (0.5 ** 10)
    assert binom_pdf(5, 10, 0.5) == comb(10, 5) * (0.5 ** 5) * (0.5 ** 5)
    assert binom_pdf(10, 10, 0.5) == 0.5 ** 10


def test_binom_cdf():
    assert binom_cdf(0, 10, 0.5) == binom_pdf(0, 10, 0.5)
    assert binom_cdf(1, 10, 0.5) == binom_pdf(0, 10, 0.5) + binom_pdf(1, 10, 0.5)
    assert binom_cdf(10, 10, 0.5) == 1.0


def test_binom_ppf():
    seed(0)
    assert binom_ppf(0.5, 10, 0.5) == 5
    assert binom_ppf(0.95, 10, 0.5) == 8
    with pytest.raises(ValueError):
        binom_ppf(-0.1, 10, 0.5)
    with pytest.raises(ValueError):
        binom_ppf(1.1, 10, 0.5)
    with pytest.raises(ValueError):
        binom_ppf(0.5, -1, 0.5)
    with pytest.raises(ValueError):
        binom_ppf(0.5, 10, 1.5)


def test_strength():
    assert strength(5, 10) >= 0.5
    assert strength(10, 10) == 1.0
