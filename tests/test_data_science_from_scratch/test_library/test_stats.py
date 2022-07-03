import logging
import os
from inspect import getmembers, isfunction

import pytest

from data_science_from_scratch.library import stats

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def test_smoke():
    logging.info("is anything on fire")
    for member in getmembers(stats):
        if isfunction(member[1]):
            print(member[0])


@pytest.mark.parametrize(
    ("point", "bucket_size", "expected"), (
            (25.4958, 5, 25),
            (250.303, 5, 250),
            (25.9, 25, 25),
    ))
def test_bucketize(point, bucket_size, expected):
    result = stats.bucketize(point, bucket_size)
    assert result == expected


@pytest.mark.parametrize(
    ("v1", "v2", "expected"), (
            ([1, 2], [2, 1], pytest.approx(-1, abs=0.01)),
            ([1, 2], [1, 2], pytest.approx(1, abs=0.01)),
            ([1, 2, 3, 4, 5], [1, 1.5, 2, 2.5], pytest.approx(0.6, abs=0.1)),
            ([1, 0, 0, 1], [1, 2, 3, 4], pytest.approx(0, abs=0.01))
    ))
def test_correlation(v1, v2, expected):
    result = stats.correlation(v1, v2)
    assert result == expected


@pytest.mark.parametrize(
    ("v1", "v2", "expected"), (
            ([1, 2], [2, 1], pytest.approx(-0.5, abs=0.01)),
            ([1, 2], [1, 2], pytest.approx(0.5, abs=0.01)),
            ([1, 2, 3, 4, 5], [1, 1.5, 2, 2.5], pytest.approx(0.6, abs=0.1)),
            ([1, 0, 0, 1], [1, 2, 3, 4], pytest.approx(0, abs=0.01))
    ))
def test_covariance(v1, v2, expected):
    result = stats.covariance(v1, v2)
    assert result == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            ([1, 2], pytest.approx(1, abs=0.01)),
            ([1, 2, 10], pytest.approx(9, abs=0.01)),
            ([1, 2, 3, 4, 5], pytest.approx(4, abs=0.1)),
            ([1, 0, 0, 1], pytest.approx(1, abs=0.01))
    ))
def test_data_range(x, expected):
    result = stats.data_range(x)
    assert result == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            ([1, 2], [-0.5, 0.5]),
            ([1, 2, 12], [-4.0, -3.0, 7.0]),
            ([1, 2, 3, 4, 5], [-2.0, -1.0, 0.0, 1.0, 2.0]),
            ([1, 0, 0, 1], [0.5, -0.5, -0.5, 0.5])
    ))
def test_de_mean(x, expected):
    result = stats.de_mean(x)
    assert result == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5),
            ([1, 2, 3, 4, 5, 100, 123], 98),
            ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 3),
            ([1, 0, 0, 1], pytest.approx(1, abs=0.01))
    ))
def test_interquartile_range(x, expected):
    result = stats.interquartile_range(x)
    assert result == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5),
            ([1, 2, 3, 4, 5, 100, 123], 34),
            ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], pytest.approx(5.27, abs=0.01)),
            ([1, 0, 0, 1], pytest.approx(0.5, abs=0.01))
    ))
def test_mean(x, expected):
    result = stats.mean(x)
    assert result == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5),
            ([1, 2, 3, 4, 5, 100, 123], 4),
            ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 4),
            ([1, 0, 0, 1], 0.5)
    ))
def test_median(x, expected):
    result = stats.median(x)
    assert result == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            ([1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10], [5]),
            ([1, 2, 3, 4, 5, 100, 123, 98, 98], [98]),
            ([1, 4, 6, 5, 4, 3, 3, 15, 4, 3, 6, 7, 3], [3]),
            ([1, 0, 0, 1], [1, 0])
    ))
def test_mode(x, expected):
    result = stats.mode(x)
    assert result == expected


@pytest.mark.parametrize(
    ("p", "x", "expected"), (
            (0.1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2),
            (0.5, [1, 2, 3, 4, 5, 100, 123], 4),
            (0.75, [1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 6),
            (0.99, [1, 0, 0, 1], 1)
    ))
def test_quantile(p, x, expected):
    result = stats.quantile(x, p)
    assert result == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], pytest.approx(3.03, abs=0.01)),
            ([1, 2, 3, 4, 5, 100, 123], pytest.approx(53.37, abs=0.01)),
            ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], pytest.approx(3.64, abs=0.01)),
            ([1, 0, 0, 1], pytest.approx(0.577, abs=0.01))
    ))
def test_standard_deviation(x, expected):
    result = stats.standard_deviation(x)
    assert result == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 385),
            ([1, 2, 3, 4, 5, 100, 123], 25184),
            ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 438),
            ([1, 0, 0, 1], 2)
    ))
def test_sum_of_squares(x, expected):
    result = stats.sum_of_squares(x)
    assert result == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], pytest.approx(9.17, abs=0.01)),
            ([1, 2, 3, 4, 5, 100, 123], pytest.approx(2848.67, abs=0.01)),
            ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], pytest.approx(13.218, abs=0.01)),
            ([1, 0, 0, 1], pytest.approx(0.33, abs=0.01))
    ))
def test_variance(x, expected):
    result = stats.variance(x)
    assert result == expected
