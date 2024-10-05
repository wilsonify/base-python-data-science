import logging
import math
import os
from inspect import getmembers, isfunction

import dsl.c05_statistics.e0501_central_tendancy
import dsl.c05_statistics.e0502_dispersion
import dsl.c05_statistics.e0503_correlation
import dsl.c10_working_with_data.e1001_univariate
import dsl.c10_working_with_data.working_with_data
from dsl.c04_linear_algebra.e0401_vectors import sum_of_squares

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def test_smoke():
    logging.info("is anything on fire")


def test_bucketize():
    point, bucket_size, expected = (25.4958, 5, 25)
    result = dsl.c10_working_with_data.e1001_univariate.bucketize(point, bucket_size)
    assert result == expected

    point, bucket_size, expected = (250.303, 5, 250)
    result = dsl.c10_working_with_data.e1001_univariate.bucketize(point, bucket_size)
    assert result == expected

    point, bucket_size, expected = (25.9, 25, 25)
    result = dsl.c10_working_with_data.e1001_univariate.bucketize(point, bucket_size)
    assert result == expected


def test_correlation():
    v1, v2, expected = ([1, 2], [2, 1], -1)
    result = dsl.c05_statistics.e0503_correlation.correlation(v1, v2)
    assert math.isclose(result, expected, abs_tol=0.01)

    v1, v2, expected = ([1, 2], [1, 2], 1)
    result = dsl.c05_statistics.e0503_correlation.correlation(v1, v2)
    assert math.isclose(result, expected, abs_tol=0.01)

    v1, v2, expected = ([1, 2, 3, 4, 5], [1, 1.5, 2, 2.5], 0.6)
    result = dsl.c05_statistics.e0503_correlation.correlation(v1, v2)
    assert math.isclose(result, expected, abs_tol=0.1)

    v1, v2, expected = ([1, 0, 0, 1], [1, 2, 3, 4], 0)
    result = dsl.c05_statistics.e0503_correlation.correlation(v1, v2)
    assert math.isclose(result, expected, abs_tol=0.01)


def test_covariance():
    v1, v2, expected = ([1, 2], [2, 1], -0.5)
    result = dsl.c05_statistics.e0503_correlation.covariance(v1, v2)
    assert math.isclose(result, expected, abs_tol=0.01)

    v1, v2, expected = ([1, 2], [1, 2], 0.5)
    result = dsl.c05_statistics.e0503_correlation.covariance(v1, v2)
    assert math.isclose(result, expected, abs_tol=0.01)

    v1, v2, expected = ([1, 2, 3, 4, 5], [1, 1.5, 2, 2.5], 0.6)
    result = dsl.c05_statistics.e0503_correlation.covariance(v1, v2)
    assert math.isclose(result, expected, abs_tol=0.1)

    v1, v2, expected = ([1, 0, 0, 1], [1, 2, 3, 4], 0)
    result = dsl.c05_statistics.e0503_correlation.covariance(v1, v2)
    assert math.isclose(result, expected, abs_tol=0.01)


def test_data_range():
    x, expected = ([1, 2], 1)
    result = dsl.c05_statistics.e0502_dispersion.data_range(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 2, 10], 9)
    result = dsl.c05_statistics.e0502_dispersion.data_range(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 2, 3, 4, 5], 4)
    result = dsl.c05_statistics.e0502_dispersion.data_range(x)
    assert math.isclose(result, expected, abs_tol=0.1)

    x, expected = ([1, 0, 0, 1], 1)
    result = dsl.c05_statistics.e0502_dispersion.data_range(x)
    assert math.isclose(result, expected, abs_tol=0.01)


def test_de_mean():
    x, expected = ([1, 2], [-0.5, 0.5])
    result = dsl.c05_statistics.e0502_dispersion.de_mean(x)
    assert result == expected
    x, expected = ([1, 2, 12], [-4.0, -3.0, 7.0])
    result = dsl.c05_statistics.e0502_dispersion.de_mean(x)
    assert result == expected
    x, expected = ([1, 2, 3, 4, 5], [-2.0, -1.0, 0.0, 1.0, 2.0])
    result = dsl.c05_statistics.e0502_dispersion.de_mean(x)
    assert result == expected
    x, expected = ([1, 0, 0, 1], [0.5, -0.5, -0.5, 0.5])
    result = dsl.c05_statistics.e0502_dispersion.de_mean(x)
    assert result == expected


def test_interquartile_range():
    x, expected = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
    result = dsl.c05_statistics.e0502_dispersion.interquartile_range(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 2, 3, 4, 5, 100, 123], 98)
    result = dsl.c05_statistics.e0502_dispersion.interquartile_range(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 3)
    result = dsl.c05_statistics.e0502_dispersion.interquartile_range(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 0, 0, 1], 1)
    result = dsl.c05_statistics.e0502_dispersion.interquartile_range(x)
    assert math.isclose(result, expected, abs_tol=0.01)


def test_mean():
    x, expected = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5)
    result = dsl.c05_statistics.e0501_central_tendancy.mean(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 2, 3, 4, 5, 100, 123], 34)
    result = dsl.c05_statistics.e0501_central_tendancy.mean(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 5.27)
    result = dsl.c05_statistics.e0501_central_tendancy.mean(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 0, 0, 1], 0.5)
    result = dsl.c05_statistics.e0501_central_tendancy.mean(x)
    assert math.isclose(result, expected, abs_tol=0.01)


def test_median():
    x, expected = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5)
    result = dsl.c05_statistics.e0501_central_tendancy.median(x)
    assert result == expected
    x, expected = ([1, 2, 3, 4, 5, 100, 123], 4)
    result = dsl.c05_statistics.e0501_central_tendancy.median(x)
    assert result == expected
    x, expected = ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 4)
    result = dsl.c05_statistics.e0501_central_tendancy.median(x)
    assert result == expected
    x, expected = ([1, 0, 0, 1], 0.5)
    result = dsl.c05_statistics.e0501_central_tendancy.median(x)
    assert result == expected


def test_mode():
    x, expected = ([1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10], [5])
    result = dsl.c05_statistics.e0501_central_tendancy.mode(x)
    assert result == expected
    x, expected = ([1, 2, 3, 4, 5, 100, 123, 98, 98], [98])
    result = dsl.c05_statistics.e0501_central_tendancy.mode(x)
    assert result == expected
    x, expected = ([1, 4, 6, 5, 4, 3, 3, 15, 4, 3, 6, 7, 3], [3])
    result = dsl.c05_statistics.e0501_central_tendancy.mode(x)
    assert result == expected
    x, expected = ([1, 0, 0, 1], [1, 0])
    result = dsl.c05_statistics.e0501_central_tendancy.mode(x)
    assert result == expected


def test_quantile():
    p, x, expected = (0.1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)
    result = dsl.c05_statistics.e0501_central_tendancy.quantile(x, p)
    assert result == expected
    p, x, expected = (0.5, [1, 2, 3, 4, 5, 100, 123], 4)
    result = dsl.c05_statistics.e0501_central_tendancy.quantile(x, p)
    assert result == expected
    p, x, expected = (0.75, [1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 6)
    result = dsl.c05_statistics.e0501_central_tendancy.quantile(x, p)
    assert result == expected
    p, x, expected = (0.99, [1, 0, 0, 1], 1)
    result = dsl.c05_statistics.e0501_central_tendancy.quantile(x, p)
    assert result == expected


def test_standard_deviation():
    x, expected = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3.03)
    result = dsl.c05_statistics.e0502_dispersion.standard_deviation(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 2, 3, 4, 5, 100, 123], 53.37)
    result = dsl.c05_statistics.e0502_dispersion.standard_deviation(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 3.64)
    result = dsl.c05_statistics.e0502_dispersion.standard_deviation(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 0, 0, 1], 0.577)
    result = dsl.c05_statistics.e0502_dispersion.standard_deviation(x)
    assert math.isclose(result, expected, abs_tol=0.01)


def test_sum_of_squares():
    x, expected = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 385)
    result = sum_of_squares(x)
    assert result == expected
    x, expected = ([1, 2, 3, 4, 5, 100, 123], 25184)
    result = sum_of_squares(x)
    assert result == expected
    x, expected = ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 438)
    result = sum_of_squares(x)
    assert result == expected
    x, expected = ([1, 0, 0, 1], 2)
    result = sum_of_squares(x)
    assert result == expected


def test_variance():
    x, expected = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9.17)
    result = dsl.c05_statistics.e0502_dispersion.variance(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 2, 3, 4, 5, 100, 123], 2848.67)
    result = dsl.c05_statistics.e0502_dispersion.variance(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 13.218)
    result = dsl.c05_statistics.e0502_dispersion.variance(x)
    assert math.isclose(result, expected, abs_tol=0.01)

    x, expected = ([1, 0, 0, 1], 0.33)
    result = dsl.c05_statistics.e0502_dispersion.variance(x)
    assert math.isclose(result, expected, abs_tol=0.01)
