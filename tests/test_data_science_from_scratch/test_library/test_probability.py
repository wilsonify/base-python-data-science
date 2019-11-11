import logging
import os

from data_science_from_scratch.library import probability

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def test_smoke():
    logging.info("is anything on fire")


def test_bernoulli_trial():
    probability.bernoulli_trial()


def test_binomial():
    probability.binomial()


def test_config():
    probability.config()


def test_dictConfig():
    probability.dictConfig()


def test_inverse_normal_cdf():
    probability.inverse_normal_cdf()


def test_logging():
    probability.logging()


def test_math():
    probability.math()


def test_normal_cdf():
    probability.normal_cdf()


def test_normal_pdf():
    probability.normal_pdf()


def test_plot_normal_cdfs():
    probability.plot_normal_cdfs()


def test_random():
    probability.random()


def test_random_kid():
    probability.random_kid()


def test_uniform_cdf():
    probability.uniform_cdf()


def test_uniform_pdf():
    probability.uniform_pdf()
