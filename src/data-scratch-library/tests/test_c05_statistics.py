import logging
import math
import os
from inspect import getmembers, isfunction

from dsl.c05_statistics import stats

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def test_smoke():
    logging.info("is anything on fire")
    for member in getmembers(stats):
        if isfunction(member[1]):
            print(member[0])


def test_bucketize():
    point, bucket_size, expected = (25.4958, 5, 25)
    result = stats.bucketize(point, bucket_size)
    assert result == expected

    point, bucket_size, expected = (250.303, 5, 250)
    result = stats.bucketize(point, bucket_size)
    assert result == expected

    point, bucket_size, expected = (25.9, 25, 25)
    result = stats.bucketize(point, bucket_size)
    assert result == expected


def test_correlation():
    v1, v2, expected = ([1, 2], [2, 1], -1)
    result = stats.correlation(v1, v2)
    assert math.isclose(result, expected, abs_tol=0.01)

    v1, v2, expected = ([1, 2], [1, 2], 1)
    result = stats.correlation(v1, v2)
    assert math.isclose(result, expected, abs_tol=0.01)

    v1, v2, expected = ([1, 2, 3, 4, 5], [1, 1.5, 2, 2.5], 0.6)
    result = stats.correlation(v1, v2)
    assert math.isclose(result, expected, abs_tol=0.1)

    v1, v2, expected = ([1, 0, 0, 1], [1, 2, 3, 4], 0)
    result = stats.correlation(v1, v2)
    assert math.isclose(result, expected, abs_tol=0.01)


def test_covariance():
    v1, v2, expected = ([1, 2], [2, 1], -0.5)
    result = stats.covariance(v1, v2)
    assert math.isclose(result, expected, abs_tol=0.01)

    v1, v2, expected = ([1, 2], [1, 2], 0.5)
    result = stats.covariance(v1, v2)
    assert math.isclose(result, expected, abs_tol=0.01)

    v1, v2, expected = ([1, 2, 3, 4, 5], [1, 1.5, 2, 2.5], 0.6)
    result = stats.covariance(v1, v2)
    assert math.isclose(result, expected, abs_tol=0.1)

    v1, v2, expected = ([1, 0, 0, 1], [1, 2, 3, 4], 0)
    result = stats.covariance(v1, v2)
    assert math.isclose(result, expected, abs_tol=0.01)


def test_data_range():
    x, expected = ([1, 2], 1)
    result = stats.data_range(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 2, 10], 9)
    result = stats.data_range(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 2, 3, 4, 5], 4)
    result = stats.data_range(x)
    assert math.isclose(result, expected, abs_tol=0.1)

    x, expected = ([1, 0, 0, 1], 1)
    result = stats.data_range(x)
    assert math.isclose(result, expected, abs_tol=0.01)


def test_de_mean():
    x, expected = ([1, 2], [-0.5, 0.5])
    result = stats.de_mean(x)
    assert result == expected
    x, expected = ([1, 2, 12], [-4.0, -3.0, 7.0])
    result = stats.de_mean(x)
    assert result == expected
    x, expected = ([1, 2, 3, 4, 5], [-2.0, -1.0, 0.0, 1.0, 2.0])
    result = stats.de_mean(x)
    assert result == expected
    x, expected = ([1, 0, 0, 1], [0.5, -0.5, -0.5, 0.5])
    result = stats.de_mean(x)
    assert result == expected


def test_interquartile_range():
    x, expected = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
    result = stats.interquartile_range(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 2, 3, 4, 5, 100, 123], 98)
    result = stats.interquartile_range(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 3)
    result = stats.interquartile_range(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 0, 0, 1], 1)
    result = stats.interquartile_range(x)
    assert math.isclose(result, expected, abs_tol=0.01)


def test_mean():
    x, expected = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5)
    result = stats.mean(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 2, 3, 4, 5, 100, 123], 34)
    result = stats.mean(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 5.27)
    result = stats.mean(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 0, 0, 1], 0.5)
    result = stats.mean(x)
    assert math.isclose(result, expected, abs_tol=0.01)


def test_median():
    x, expected = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5)
    result = stats.median(x)
    assert result == expected
    x, expected = ([1, 2, 3, 4, 5, 100, 123], 4)
    result = stats.median(x)
    assert result == expected
    x, expected = ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 4)
    result = stats.median(x)
    assert result == expected
    x, expected = ([1, 0, 0, 1], 0.5)
    result = stats.median(x)
    assert result == expected


def test_mode():
    x, expected = ([1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10], [5])
    result = stats.mode(x)
    assert result == expected
    x, expected = ([1, 2, 3, 4, 5, 100, 123, 98, 98], [98])
    result = stats.mode(x)
    assert result == expected
    x, expected = ([1, 4, 6, 5, 4, 3, 3, 15, 4, 3, 6, 7, 3], [3])
    result = stats.mode(x)
    assert result == expected
    x, expected = ([1, 0, 0, 1], [1, 0])
    result = stats.mode(x)
    assert result == expected


def test_quantile():
    p, x, expected = (0.1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)
    result = stats.quantile(x, p)
    assert result == expected
    p, x, expected = (0.5, [1, 2, 3, 4, 5, 100, 123], 4)
    result = stats.quantile(x, p)
    assert result == expected
    p, x, expected = (0.75, [1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 6)
    result = stats.quantile(x, p)
    assert result == expected
    p, x, expected = (0.99, [1, 0, 0, 1], 1)
    result = stats.quantile(x, p)
    assert result == expected


def test_standard_deviation():
    x, expected = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3.03)
    result = stats.standard_deviation(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 2, 3, 4, 5, 100, 123], 53.37)
    result = stats.standard_deviation(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 3.64)
    result = stats.standard_deviation(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 0, 0, 1], 0.577)
    result = stats.standard_deviation(x)
    assert math.isclose(result, expected, abs_tol=0.01)


def test_sum_of_squares():
    x, expected = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 385)
    result = stats.sum_of_squares(x)
    assert result == expected
    x, expected = ([1, 2, 3, 4, 5, 100, 123], 25184)
    result = stats.sum_of_squares(x)
    assert result == expected
    x, expected = ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 438)
    result = stats.sum_of_squares(x)
    assert result == expected
    x, expected = ([1, 0, 0, 1], 2)
    result = stats.sum_of_squares(x)
    assert result == expected


def test_variance():
    x, expected = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9.17)
    result = stats.variance(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 2, 3, 4, 5, 100, 123], 2848.67)
    result = stats.variance(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 13.218)
    result = stats.variance(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 0, 0, 1], 0.33)
    result = stats.variance(x)
    assert math.isclose(result, expected, abs_tol=0.01)
