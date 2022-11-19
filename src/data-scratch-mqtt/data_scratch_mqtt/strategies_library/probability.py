import os

from data_science_from_scratch.library import probability

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def bernoulli_trial(self, body):
    p = body["p"]
    result = probability.bernoulli_trial(p)
    self.publish(result)


def binomial(self, body):
    p = body["p"]
    n = body["n"]
    result = probability.binomial(p, n)
    self.publish(result)


def inverse_normal_cdf(self, body):
    p = body["p"]
    mu = body["mu"]
    sigma = body["sigma"]
    result = probability.inverse_normal_cdf(p, mu, sigma)
    self.publish(result)


def normal_cdf(self, body):
    x = body["x"]
    mu = body["mu"]
    sigma = body["sigma"]
    result = probability.normal_cdf(x, mu, sigma)
    self.publish(result)


def normal_pdf(self, body):
    x = body["x"]
    mu = body["mu"]
    sigma = body["sigma"]
    result = probability.normal_pdf(x, mu, sigma)
    self.publish(result)


def random_kid(self, body):
    result = probability.random_kid()
    self.publish(result)


def uniform_cdf(self, body):
    x = body["x"]
    result = probability.uniform_cdf(x)
    self.publish(result)


def uniform_pdf(self, body):
    x = body["x"]
    result = probability.uniform_pdf(x)
    self.publish(result)
