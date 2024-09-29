import os

import dsl.c05_statistics.e0501_central_tendancy
import dsl.c05_statistics.e0502_dispersion
import dsl.c05_statistics.e0503_correlation
import dsl.c10_working_with_data.working_with_data
from dsl import stats

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def bucketize(self, body):
    point = body["point"]
    bucket_size = body["bucket_size"]
    result = dsl.c10_working_with_data.working_with_data.bucketize(point, bucket_size)
    self.publish(result)


def correlation_matrix(self, body):
    data = body["data"]
    result = dsl.c05_statistics.e0503_correlation.correlation_matrix(data)
    self.publish(result)


def correlation(self, body):
    x = body["x"]
    y = body["y"]
    result = dsl.c05_statistics.e0503_correlation.correlation(x, y)
    self.publish(result)


def covariance(self, body):
    x = body["x"]
    y = body["y"]
    result = dsl.c05_statistics.e0503_correlation.covariance(x, y)
    self.publish(result)


def data_range(self, body):
    x = body["x"]
    result = dsl.c05_statistics.e0502_dispersion.data_range(x)
    self.publish(result)


def de_mean(self, body):
    x = body["x"]
    result = dsl.c05_statistics.e0502_dispersion.de_mean(x)
    self.publish(result)


def interquartile_range(self, body):
    x = body["x"]
    result = dsl.c05_statistics.e0502_dispersion.interquartile_range(x)
    self.publish(result)


def mean(self, body):
    x = body["x"]
    result = dsl.c05_statistics.e0501_central_tendancy.mean(x)
    self.publish(result)


def median(self, body):
    x = body["x"]
    result = dsl.c05_statistics.e0501_central_tendancy.median(x)
    self.publish(result)


def mode(self, body):
    x = body["x"]
    result = dsl.c05_statistics.e0501_central_tendancy.mode(x)
    self.publish(result)


def quantile(self, body):
    x = body["x"]
    p = body["p"]
    result = dsl.c05_statistics.e0501_central_tendancy.quantile(x, p)
    self.publish(result)


def standard_deviation(self, body):
    x = body["x"]
    result = dsl.c05_statistics.e0502_dispersion.standard_deviation(x)
    self.publish(result)


def sum_of_squares(self, body):
    x = body["x"]
    result = stats.sum_of_squares(x)
    self.publish(result)


def variance(self, body):
    x = body["x"]
    result = dsl.c05_statistics.e0502_dispersion.variance(x)
    self.publish(result)
