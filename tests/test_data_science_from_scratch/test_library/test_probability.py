import logging
import os
from inspect import getmembers, isfunction

import pytest

from dsl.c06_probability import probability

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def test_smoke():
    logging.info("is anything on fire")
    for member in getmembers(probability):
        if isfunction(member[1]):
            print(member[0])


def test_random_normal():
    result = probability.random_normal()
    assert len([result]) == 1


def test_bernoulli_trial():
    result = probability.bernoulli_trial(0.5)
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
    result = probability.binomial(p, n)
    assert result == expected


@pytest.mark.parametrize(
    ("p", "mu", "sigma", "expected"), (
            (0.01, 100, 5, pytest.approx(88.36, abs=0.01)),
            (0.10, 100, 5, pytest.approx(93.59, abs=0.01)),
            (0.5, 100, 5, pytest.approx(100, abs=0.01)),
            (0.95, 100, 5, pytest.approx(108, abs=1))
    ))
def test_inverse_normal_cdf(p, mu, sigma, expected):
    result = probability.inverse_normal_cdf(p, mu, sigma)
    assert result == expected


@pytest.mark.parametrize(
    ("x", "mu", "sigma", "expected"), (
            (0.1, 100, 5, pytest.approx(0, abs=0.01)),
            (95, 100, 5, pytest.approx(0.16, abs=0.01)),
            (100, 100, 5, pytest.approx(0.5, abs=0.01)),
            (105, 100, 5, pytest.approx(0.84, abs=1))
    ))
def test_normal_cdf(x, mu, sigma, expected):
    result = probability.normal_cdf(x, mu, sigma)
    assert result == expected


@pytest.mark.parametrize(
    ("x", "mu", "sigma", "expected"), (
            (0.1, 100, 5, pytest.approx(0, abs=0.01)),
            (95, 100, 5, pytest.approx(0.05, abs=0.01)),
            (100, 100, 5, pytest.approx(0.08, abs=0.01)),
            (105, 100, 5, pytest.approx(0.84, abs=1))
    ))
def test_normal_pdf(x, mu, sigma, expected):
    result = probability.normal_pdf(x, mu, sigma)
    assert result == expected


def test_random_kid():
    result = probability.random_kid()
    expected = ["boy", "girl"]
    assert result in expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            (0.1, pytest.approx(0.1, abs=0.01)),
            (0.5, pytest.approx(0.5, abs=0.01)),
            (0.9, pytest.approx(0.9, abs=0.01)),
            (2, pytest.approx(1, abs=0.1))
    ))
def test_uniform_cdf(x, expected):
    result = probability.uniform_cdf(x)
    assert result == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            (-0.1, pytest.approx(0, abs=0.01)),
            (0.5, pytest.approx(1, abs=0.01)),
            (0.9, pytest.approx(1, abs=0.01)),
            (2, pytest.approx(0, abs=0.1))
    ))
def test_uniform_pdf(x, expected):
    result = probability.uniform_pdf(x)
    assert result == expected
