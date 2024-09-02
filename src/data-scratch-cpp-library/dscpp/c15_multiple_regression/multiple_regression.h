
#include "gradient_descent.h"
#include "linear_algebra.h"
#include "probability.h"
#include "simple_linear_regression.h"

double predict(x_i, beta);
double error(x_i, y_i, beta);
double squared_error(x_i, y_i, beta);
double squared_error_gradient(x_i, y_i, beta);
double estimate_beta(x, y);
double multiple_r_squared(x, y, beta);
double bootstrap_sample(data);
double bootstrap_statistic(data, stats_fn, num_samples);
double estimate_sample_beta(sample);
double p_value(beta_hat_j, sigma_hat_j);
double ridge_penalty(beta, alpha);
double squared_error_ridge(x_i, y_i, beta, alpha);
double ridge_penalty_gradient(beta, alpha);
double squared_error_ridge_gradient(x_i, y_i, beta, alpha);
double estimate_beta_ridge(x, y, alpha);
double lasso_penalty(beta, alpha);