import logging
import os

import pytest

from data_science_from_scratch.library import probability

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def smoke():
    logging.info("is anything on fire")


def bernoulli_trial():
    result = probability.bernoulli_trial(0.5)
    expected = [0, 1]
    assert result in expected


def binomial(p, n, expected):
    result = probability.binomial(p, n)
    assert result == expected


def inverse_normal_cdf(p, mu, sigma, expected):
    result = probability.inverse_normal_cdf(p, mu, sigma)
    assert result == expected


def normal_cdf(x, mu, sigma, expected):
    result = probability.normal_cdf(x, mu, sigma)
    assert result == expected


def normal_pdf(x, mu, sigma, expected):
    result = probability.normal_pdf(x, mu, sigma)
    assert result == expected


def random_kid():
    result = probability.random_kid()
    expected = ["boy", "girl"]
    assert result in expected


def uniform_cdf(x, expected):
    result = probability.uniform_cdf(x)
    assert result == expected


def uniform_pdf(x, expected):
    result = probability.uniform_pdf(x)
    assert result == expected
