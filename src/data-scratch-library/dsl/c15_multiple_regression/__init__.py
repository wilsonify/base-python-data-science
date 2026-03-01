"""
Chapter 15: Multiple Regression

Linear regression with multiple independent variables.
"""

from .multiple_regression import (
    predict,
    error,
    squared_error,
    squared_error_gradient,
    estimate_beta,
    multiple_r_squared,
    bootstrap_sample,
    bootstrap_statistic,
    estimate_sample_beta,
    p_value,
    ridge_penalty,
    squared_error_ridge,
    ridge_penalty_gradient,
    squared_error_ridge_gradient,
    estimate_beta_ridge,
    lasso_penalty,
)
