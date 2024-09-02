import os

from dsl.c05_statistics import stats

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def bucketize(self, body):
    point = body["point"]
    bucket_size = body["bucket_size"]
    result = stats.bucketize(point, bucket_size)
    self.publish(result)


def correlation_matrix(self, body):
    data = body["data"]
    result = stats.correlation_matrix(data)
    self.publish(result)


def correlation(self, body):
    x = body["x"]
    y = body["y"]
    result = stats.correlation(x, y)
    self.publish(result)


def covariance(self, body):
    x = body["x"]
    y = body["y"]
    result = stats.covariance(x, y)
    self.publish(result)


def data_range(self, body):
    x = body["x"]
    result = stats.data_range(x)
    self.publish(result)


def de_mean(self, body):
    x = body["x"]
    result = stats.de_mean(x)
    self.publish(result)


def interquartile_range(self, body):
    x = body["x"]
    result = stats.interquartile_range(x)
    self.publish(result)


def mean(self, body):
    x = body["x"]
    result = stats.mean(x)
    self.publish(result)


def median(self, body):
    x = body["x"]
    result = stats.median(x)
    self.publish(result)


def mode(self, body):
    x = body["x"]
    result = stats.mode(x)
    self.publish(result)


def quantile(self, body):
    x = body["x"]
    p = body["p"]
    result = stats.quantile(x, p)
    self.publish(result)


def standard_deviation(self, body):
    x = body["x"]
    result = stats.standard_deviation(x)
    self.publish(result)


def sum_of_squares(self, body):
    x = body["x"]
    result = stats.sum_of_squares(x)
    self.publish(result)


def variance(self, body):
    x = body["x"]
    result = stats.variance(x)
    self.publish(result)
