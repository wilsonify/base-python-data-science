import pytest

from dsl.c06_probability.e0602_uniform import uniform_cdf, uniform_pdf


@pytest.mark.parametrize(
    ("x", "expected"), (
            (0.1, pytest.approx(0.1, abs=0.01)),
            (0.5, pytest.approx(0.5, abs=0.01)),
            (0.9, pytest.approx(0.9, abs=0.01)),
            (2, pytest.approx(1, abs=0.1))
    ))
def test_uniform_cdf(x, expected):
    result = uniform_cdf(x)
    assert result == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            (-0.1, pytest.approx(0, abs=0.01)),
            (0.5, pytest.approx(1, abs=0.01)),
            (0.9, pytest.approx(1, abs=0.01)),
            (2, pytest.approx(0, abs=0.1))
    ))
def test_uniform_pdf(x, expected):
    result = uniform_pdf(x)
    assert result == expected
