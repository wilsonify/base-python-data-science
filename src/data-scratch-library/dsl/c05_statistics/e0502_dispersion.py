import math

from dsl.c04_linear_algebra.e0401_vectors import sum_of_squares
from dsl.c05_statistics.e0501_central_tendancy import mean, quantile


def data_range(x):
    # "range" already means something in Python, so we'll use a different name
    return max(x) - min(x)


def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)


def standard_deviation(x):
    return math.sqrt(variance(x))


def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)
