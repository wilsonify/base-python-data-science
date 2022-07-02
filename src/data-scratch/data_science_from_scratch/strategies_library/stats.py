import logging
import os

from data_science_from_scratch.library import stats

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def smoke():
    logging.info("is anything on fire")


def correlation(v1, v2, expected):
    result = stats.correlation(v1, v2)
    self.publish(payload)


def covariance(v1, v2, expected):
    result = stats.covariance(v1, v2)
    self.publish(payload)


def data_range(x, expected):
    result = stats.data_range(x)
    self.publish(payload)


def de_mean(x, expected):
    result = stats.de_mean(x)
    self.publish(payload)


def interquartile_range(x, expected):
    result = stats.interquartile_range(x)
    self.publish(payload)


def mean(x, expected):
    result = stats.mean(x)
    self.publish(payload)


def median(x, expected):
    result = stats.median(x)
    self.publish(payload)


def mode(x, expected):
    result = stats.mode(x)
    self.publish(payload)


def quantile(p, x, expected):
    result = stats.quantile(x, p)
    self.publish(payload)


def standard_deviation(x, expected):
    result = stats.standard_deviation(x)
    self.publish(payload)


def sum_of_squares(x, expected):
    result = stats.sum_of_squares(x)
    self.publish(payload)


def variance(x, expected):
    result = stats.variance(x)
    self.publish(payload)
