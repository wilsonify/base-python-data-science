#include "logistic_regression.h"
#include <cmath>

double logistic(double x) {
    return 1.0 / (1.0 + std::exp(-x));
}

double logistic_prime(double x) {
    return logistic(x) * (1.0 - logistic(x));
}

double logistic_log_likelihood_i(const std::vector<double>& x_i, double y_i, const std::vector<double>& beta) {
    if (y_i == 1.0)
        return std::log(logistic(dot(x_i, beta)));
    else
        return std::log(1.0 - logistic(dot(x_i, beta)));
}

double logistic_log_likelihood(const std::vector<std::vector<double>>& x, const std::vector<double>& y, const std::vector<double>& beta) {
    double total = 0.0;
    for (size_t i = 0; i < x.size(); ++i)
        total += logistic_log_likelihood_i(x[i], y[i], beta);
    return total;
}

std::vector<double> logistic_log_partial_gradient_i(const std::vector<double>& x_i, double y_i, const std::vector<double>& beta) {
    double factor = y_i - logistic(dot(x_i, beta));
    std::vector<double> result(x_i.size());
    for (size_t j = 0; j < x_i.size(); ++j)
        result[j] = factor * x_i[j];
    return result;
}

std::vector<double> logistic_log_gradient(const std::vector<std::vector<double>>& x, const std::vector<double>& y, const std::vector<double>& beta) {
    std::vector<double> result(beta.size(), 0.0);
    for (size_t i = 0; i < x.size(); ++i) {
        auto grad_i = logistic_log_partial_gradient_i(x[i], y[i], beta);
        result = vector_add(result, grad_i);
    }
    return result;
}

LogisticScore score_logistic(const std::vector<double>& beta_hat,
                              const std::vector<std::vector<double>>& x_test,
                              const std::vector<double>& y_test) {
    int tp = 0, fp = 0, fn = 0;
    for (size_t i = 0; i < x_test.size(); ++i) {
        double predict = logistic(dot(beta_hat, x_test[i]));
        if (y_test[i] == 1.0 && predict >= 0.5)      ++tp;
        else if (y_test[i] == 1.0)                    ++fn;
        else if (predict >= 0.5)                      ++fp;
    }
    double precision = (tp + fp > 0) ? static_cast<double>(tp) / (tp + fp) : 0.0;
    double recall    = (tp + fn > 0) ? static_cast<double>(tp) / (tp + fn) : 0.0;
    return {precision, recall};
}

std::vector<double> logistic_fit(const std::vector<std::vector<double>>& x, const std::vector<double>& y) {
    std::vector<double> beta_0 = {1.0, 1.0, 1.0};

    auto fn = [&](const std::vector<double>& beta) {
        return logistic_log_likelihood(x, y, beta);
    };
    auto gradient_fn = [&](const std::vector<double>& beta) {
        return logistic_log_gradient(x, y, beta);
    };

    auto beta_1 = maximize_batch(fn, gradient_fn, beta_0);

    auto target_i = [](const std::vector<double>& x_i, double y_i, const std::vector<double>& beta) {
        return logistic_log_likelihood_i(x_i, y_i, beta);
    };
    auto gradient_i = [](const std::vector<double>& x_i, double y_i, const std::vector<double>& beta) {
        return logistic_log_partial_gradient_i(x_i, y_i, beta);
    };

    return maximize_stochastic(target_i, gradient_i, x, y, beta_1);
}
