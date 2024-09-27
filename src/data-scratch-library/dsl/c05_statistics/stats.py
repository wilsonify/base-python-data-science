import math
from collections import Counter
from typing import List

from dsl.c04_linear_algebra.e0401_vectors import (
    sum_of_squares,
    dot
)
from dsl.c04_linear_algebra.e0402_matrices import (
    shape,
    get_column,
    make_matrix
)


def bucketize(point, bucket_size):
    """floor the point to the next lower multiple of bucket_size"""
    return bucket_size * math.floor(point / bucket_size)


def make_histogram(points, bucket_size):
    """buckets the points and counts how many in each bucket"""
    return Counter(bucketize(point, bucket_size) for point in points)


def correlation_matrix(data):
    """returns the num_columns x num_columns matrix whose (i, j)th entry
    is the correlation between columns i and j of data"""

    _, num_columns = shape(data)

    def matrix_entry(i, j):
        return correlation(get_column(data, i), get_column(data, j))

    return make_matrix(num_columns, num_columns, matrix_entry)


def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)


def median(v: List[float]) -> float:
    """finds the 'middle-most' value of v"""
    n = len(v)
    assert n > 0, "Cannot compute median of an empty list"
    if n % 2 == 1:
        # if odd, return the middle value
        sorted_v = sorted(v)
        midpoint = n // 2
        return sorted_v[midpoint]
    else:
        # if even, return the average of two middle values
        sorted_v = sorted(v)
        midpoint = n // 2
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2.0


def quantile(x, p):
    """returns the pth-percentile value in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]


def mode(x):
    """returns a list, might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]


# "range" already means something in Python, so we'll use a different name
def data_range(x):
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


####
#
# CORRELATION
#
#####


def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)


def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0  # if no variation, correlation is zero
