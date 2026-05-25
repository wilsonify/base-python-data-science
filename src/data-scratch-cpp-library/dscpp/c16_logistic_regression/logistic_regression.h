#pragma once
#include <vector>
#include <functional>
#include "../c08_gradient_descent/gradient_descent.h"
#include "../c04_linear_algebra/linear_algebra.h"

double logistic(double x);
double logistic_prime(double x);
double logistic_log_likelihood_i(const std::vector<double>& x_i, double y_i, const std::vector<double>& beta);
double logistic_log_likelihood(const std::vector<std::vector<double>>& x, const std::vector<double>& y, const std::vector<double>& beta);
std::vector<double> logistic_log_partial_gradient_i(const std::vector<double>& x_i, double y_i, const std::vector<double>& beta);
std::vector<double> logistic_log_gradient(const std::vector<std::vector<double>>& x, const std::vector<double>& y, const std::vector<double>& beta);
struct LogisticScore { double precision; double recall; };
LogisticScore score_logistic(const std::vector<double>& beta_hat, const std::vector<std::vector<double>>& x_test, const std::vector<double>& y_test);
std::vector<double> logistic_fit(const std::vector<std::vector<double>>& x, const std::vector<double>& y);
