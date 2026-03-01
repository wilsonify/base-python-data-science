"""
Chapter 16: Logistic Regression

Binary classification via logistic regression fitted with gradient ascent.
"""

from .logistic_regression import (
    logistic,
    logistic_prime,
    logistic_log_likelihood_i,
    logistic_log_likelihood,
    logistic_log_partial_ij,
    logistic_log_gradient_i,
    logistic_log_gradient,
    score_logistic,
    logistic_fit,
)
