#include "gradient_descent.h"
#include "linear_algebra.h"

double logistic(x);
double logistic_prime(x);
double logistic_log_likelihood_i(x_i, y_i, beta);
double logistic_log_likelihood(x, y, beta);
double logistic_log_partial_ij(x_i, y_i, beta, j);
double logistic_log_gradient_i(x_i, y_i, beta);
double logistic_log_gradient(x, y, beta);
double score_logistic(beta_hat, x_test, y_test);
double logistic_fit(x, y);
