import logging
import os

from data_science_from_scratch.library import stats

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def smoke():
    logging.info("is anything on fire")


def correlation(v1, v2, expected):
    result = stats.correlation(v1, v2)
    assert result == expected


def covariance(v1, v2, expected):
    result = stats.covariance(v1, v2)
    assert result == expected


def data_range(x, expected):
    result = stats.data_range(x)
    assert result == expected


def de_mean(x, expected):
    result = stats.de_mean(x)
    assert result == expected


def interquartile_range(x, expected):
    result = stats.interquartile_range(x)
    assert result == expected


def mean(x, expected):
    result = stats.mean(x)
    assert result == expected


def median(x, expected):
    result = stats.median(x)
    assert result == expected


def mode(x, expected):
    result = stats.mode(x)
    assert result == expected


def quantile(p, x, expected):
    result = stats.quantile(x, p)
    assert result == expected


def standard_deviation(x, expected):
    result = stats.standard_deviation(x)
    assert result == expected


def sum_of_squares(x, expected):
    result = stats.sum_of_squares(x)
    assert result == expected


def variance(x, expected):
    result = stats.variance(x)
    assert result == expected
