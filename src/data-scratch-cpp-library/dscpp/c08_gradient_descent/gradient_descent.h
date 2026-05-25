#pragma once
#include <vector>
#include <functional>
#include <limits>
#include "../c04_linear_algebra/linear_algebra.h"

double grad_sum_of_squares(const std::vector<double>& v);
double difference_quotient(std::function<double(double)> f, double x, double h);
double partial_difference_quotient(std::function<double(const std::vector<double>&)> f, const std::vector<double>& v, int i, double h);
std::vector<double> estimate_gradient(std::function<double(const std::vector<double>&)> f, const std::vector<double>& v, double h=0.00001);
std::vector<double> grad_step(const std::vector<double>& v, const std::vector<double>& direction, double step_size);
std::vector<double> sum_of_squares_gradient(const std::vector<double>& v);
std::vector<double> minimize_batch(
    std::function<double(const std::vector<double>&)> target_fn,
    std::function<std::vector<double>(const std::vector<double>&)> gradient_fn,
    std::vector<double> theta_0,
    double tolerance=1e-6);
std::vector<double> maximize_batch(
    std::function<double(const std::vector<double>&)> target_fn,
    std::function<std::vector<double>(const std::vector<double>&)> gradient_fn,
    std::vector<double> theta_0,
    double tolerance=1e-6);
using DataPoint = std::pair<std::vector<double>, double>;
std::vector<double> minimize_stochastic(
    std::function<double(const std::vector<double>&, double, const std::vector<double>&)> target_fn,
    std::function<std::vector<double>(const std::vector<double>&, double, const std::vector<double>&)> gradient_fn,
    const std::vector<std::vector<double>>& x,
    const std::vector<double>& y,
    std::vector<double> theta_0,
    double alpha_0=0.01);
std::vector<double> maximize_stochastic(
    std::function<double(const std::vector<double>&, double, const std::vector<double>&)> target_fn,
    std::function<std::vector<double>(const std::vector<double>&, double, const std::vector<double>&)> gradient_fn,
    const std::vector<std::vector<double>>& x,
    const std::vector<double>& y,
    std::vector<double> theta_0,
    double alpha_0=0.01);
