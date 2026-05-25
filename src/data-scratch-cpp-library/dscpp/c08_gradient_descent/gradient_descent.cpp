#include "gradient_descent.h"
#include <cmath>
#include <algorithm>
#include <numeric>
#include <random>

double grad_sum_of_squares(const std::vector<double>& v) {
    double result = 0.0;
    for (double vi : v) result += vi * vi;
    return result;
}

double difference_quotient(std::function<double(double)> f, double x, double h) {
    return (f(x + h) - f(x)) / h;
}

double partial_difference_quotient(std::function<double(const std::vector<double>&)> f,
                                    const std::vector<double>& v, int i, double h) {
    std::vector<double> w = v;
    w[i] += h;
    return (f(w) - f(v)) / h;
}

std::vector<double> estimate_gradient(std::function<double(const std::vector<double>&)> f,
                                       const std::vector<double>& v, double h) {
    std::vector<double> result(v.size());
    for (size_t i = 0; i < v.size(); ++i)
        result[i] = partial_difference_quotient(f, v, static_cast<int>(i), h);
    return result;
}

std::vector<double> grad_step(const std::vector<double>& v, const std::vector<double>& direction, double step_size) {
    return vector_add(v, scalar_multiply(step_size, direction));
}

std::vector<double> sum_of_squares_gradient(const std::vector<double>& v) {
    std::vector<double> result(v.size());
    for (size_t i = 0; i < v.size(); ++i)
        result[i] = 2.0 * v[i];
    return result;
}

std::vector<double> minimize_batch(
    std::function<double(const std::vector<double>&)> target_fn,
    std::function<std::vector<double>(const std::vector<double>&)> gradient_fn,
    std::vector<double> theta_0,
    double tolerance) {

    const std::vector<double> step_sizes = {100.0, 10.0, 1.0, 0.1, 0.01, 0.001, 0.0001, 0.00001};
    std::vector<double> theta = theta_0;
    double value = target_fn(theta);

    while (true) {
        std::vector<double> gradient = gradient_fn(theta);
        std::vector<double> next_theta = theta;
        double next_value = std::numeric_limits<double>::infinity();

        for (double step_size : step_sizes) {
            std::vector<double> candidate = grad_step(theta, gradient, -step_size);
            double candidate_value = target_fn(candidate);
            if (candidate_value < next_value) {
                next_value = candidate_value;
                next_theta = candidate;
            }
        }

        if (std::abs(value - next_value) < tolerance)
            return theta;

        theta = next_theta;
        value = next_value;
    }
}

std::vector<double> maximize_batch(
    std::function<double(const std::vector<double>&)> target_fn,
    std::function<std::vector<double>(const std::vector<double>&)> gradient_fn,
    std::vector<double> theta_0,
    double tolerance) {

    auto neg_target = [&](const std::vector<double>& v) { return -target_fn(v); };
    auto neg_gradient = [&](const std::vector<double>& v) {
        auto g = gradient_fn(v);
        for (auto& x : g) x = -x;
        return g;
    };
    return minimize_batch(neg_target, neg_gradient, theta_0, tolerance);
}

std::vector<double> minimize_stochastic(
    std::function<double(const std::vector<double>&, double, const std::vector<double>&)> target_fn,
    std::function<std::vector<double>(const std::vector<double>&, double, const std::vector<double>&)> gradient_fn,
    const std::vector<std::vector<double>>& x,
    const std::vector<double>& y,
    std::vector<double> theta_0,
    double alpha_0) {

    std::mt19937 rng(42);
    std::vector<double> theta = theta_0;
    double alpha = alpha_0;
    std::vector<double> min_theta = theta;
    double min_value = std::numeric_limits<double>::infinity();
    int iterations_with_no_improvement = 0;

    std::vector<size_t> indices(x.size());
    std::iota(indices.begin(), indices.end(), 0);

    while (iterations_with_no_improvement < 100) {
        double value = 0.0;
        for (size_t i = 0; i < x.size(); ++i)
            value += target_fn(x[i], y[i], theta);

        if (value < min_value) {
            min_theta = theta;
            min_value = value;
            iterations_with_no_improvement = 0;
            alpha = alpha_0;
        } else {
            ++iterations_with_no_improvement;
            alpha *= 0.9;
        }

        std::shuffle(indices.begin(), indices.end(), rng);
        for (size_t idx : indices) {
            auto gradient_i = gradient_fn(x[idx], y[idx], theta);
            theta = vector_subtract(theta, scalar_multiply(alpha, gradient_i));
        }
    }
    return min_theta;
}

std::vector<double> maximize_stochastic(
    std::function<double(const std::vector<double>&, double, const std::vector<double>&)> target_fn,
    std::function<std::vector<double>(const std::vector<double>&, double, const std::vector<double>&)> gradient_fn,
    const std::vector<std::vector<double>>& x,
    const std::vector<double>& y,
    std::vector<double> theta_0,
    double alpha_0) {

    auto neg_target = [&](const std::vector<double>& xi, double yi, const std::vector<double>& t) {
        return -target_fn(xi, yi, t);
    };
    auto neg_gradient = [&](const std::vector<double>& xi, double yi, const std::vector<double>& t) {
        auto g = gradient_fn(xi, yi, t);
        for (auto& v : g) v = -v;
        return g;
    };
    return minimize_stochastic(neg_target, neg_gradient, x, y, theta_0, alpha_0);
}
