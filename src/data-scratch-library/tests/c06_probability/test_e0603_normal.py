import pytest

from dsl.c06_probability.e0603_normal import random_normal, inverse_normal_cdf, normal_cdf, normal_pdf


def test_random_normal():
    result = random_normal()
    assert len([result]) == 1


@pytest.mark.parametrize(
    ("p", "mu", "sigma", "expected"), (
            (0.01, 100, 5, pytest.approx(88.36, abs=0.01)),
            (0.10, 100, 5, pytest.approx(93.59, abs=0.01)),
            (0.5, 100, 5, pytest.approx(100, abs=0.01)),
            (0.95, 100, 5, pytest.approx(108, abs=1))
    ))
def test_inverse_normal_cdf(p, mu, sigma, expected):
    result = inverse_normal_cdf(p, mu, sigma)
    assert result == expected


@pytest.mark.parametrize(
    ("x", "mu", "sigma", "expected"), (
            (0.1, 100, 5, pytest.approx(0, abs=0.01)),
            (95, 100, 5, pytest.approx(0.16, abs=0.01)),
            (100, 100, 5, pytest.approx(0.5, abs=0.01)),
            (105, 100, 5, pytest.approx(0.84, abs=1))
    ))
def test_normal_cdf(x, mu, sigma, expected):
    result = normal_cdf(x, mu, sigma)
    assert result == expected


@pytest.mark.parametrize(
    ("x", "mu", "sigma", "expected"), (
            (0.1, 100, 5, pytest.approx(0, abs=0.01)),
            (95, 100, 5, pytest.approx(0.05, abs=0.01)),
            (100, 100, 5, pytest.approx(0.08, abs=0.01)),
            (105, 100, 5, pytest.approx(0.84, abs=1))
    ))
def test_normal_pdf(x, mu, sigma, expected):
    result = normal_pdf(x, mu, sigma)
    assert result == expected
