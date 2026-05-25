#include "hypothesis_and_inference.h"
#include <cmath>
#include <random>
#include <algorithm>
#include <numeric>

std::pair<double,double> normal_approximation_to_binomial(int n, double p) {
    double mu = p * n;
    double sigma = std::sqrt(p * (1.0 - p) * n);
    return {mu, sigma};
}

double normal_probability_below(double x, double mu, double sigma) {
    return normal_cdf(x, mu, sigma);
}

double normal_probability_above(double lo, double mu, double sigma) {
    return 1.0 - normal_cdf(lo, mu, sigma);
}

double normal_probability_between(double lo, double hi, double mu, double sigma) {
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma);
}

double normal_probability_outside(double lo, double hi, double mu, double sigma) {
    return 1.0 - normal_probability_between(lo, hi, mu, sigma);
}

double normal_upper_bound(double probability, double mu, double sigma) {
    return inverse_normal_cdf(probability, mu, sigma);
}

double normal_lower_bound(double probability, double mu, double sigma) {
    return inverse_normal_cdf(1.0 - probability, mu, sigma);
}

std::pair<double,double> normal_two_sided_bounds(double probability, double mu, double sigma) {
    double tail = (1.0 - probability) / 2.0;
    double lower = normal_upper_bound(tail, mu, sigma);
    double upper = normal_lower_bound(tail, mu, sigma);
    return {lower, upper};
}

double two_sided_p_value(double x, double mu, double sigma) {
    if (x >= mu)
        return 2.0 * normal_probability_above(x, mu, sigma);
    else
        return 2.0 * normal_probability_below(x, mu, sigma);
}

double upper_p_value(double x, double mu, double sigma) {
    return normal_probability_above(x, mu, sigma);
}

double lower_p_value(double x, double mu, double sigma) {
    return normal_probability_below(x, mu, sigma);
}

double count_extreme_values() {
    std::mt19937 rng(42);
    std::uniform_real_distribution<double> dist(0.0, 1.0);
    int extreme_value_count = 0;
    for (int i = 0; i < 100000; ++i) {
        int num_heads = 0;
        for (int j = 0; j < 1000; ++j) {
            if (dist(rng) < 0.5) ++num_heads;
        }
        if (num_heads >= 530 || num_heads <= 470)
            ++extreme_value_count;
    }
    return extreme_value_count / 100000.0;
}

std::vector<bool> run_experiment() {
    static std::mt19937 rng(std::random_device{}());
    std::uniform_real_distribution<double> dist(0.0, 1.0);
    std::vector<bool> flips(1000);
    for (int i = 0; i < 1000; ++i)
        flips[i] = dist(rng) < 0.5;
    return flips;
}

bool reject_fairness(const std::vector<bool>& experiment) {
    int num_heads = 0;
    for (bool flip : experiment) if (flip) ++num_heads;
    return num_heads < 469 || num_heads > 531;
}

std::pair<double,double> estimated_parameters(int n, int x) {
    double p = static_cast<double>(x) / n;
    double sigma = std::sqrt(p * (1.0 - p) / n);
    return {p, sigma};
}

double a_b_test_statistic(int n_a, int a_weight, int n_b, int b_weight) {
    auto [a_p, a_sig] = estimated_parameters(n_a, a_weight);
    auto [b_p, b_sig] = estimated_parameters(n_b, b_weight);
    return (b_p - a_p) / std::sqrt(a_sig * a_sig + b_sig * b_sig);
}

double normalizer(double alpha, double beta) {
    return std::tgamma(alpha) * std::tgamma(beta) / std::tgamma(alpha + beta);
}

double beta_pdf(double x, double alpha, double beta) {
    if (x < 0.0 || x > 1.0) return 0.0;
    return std::pow(x, alpha - 1.0) * std::pow(1.0 - x, beta - 1.0) / normalizer(alpha, beta);
}
