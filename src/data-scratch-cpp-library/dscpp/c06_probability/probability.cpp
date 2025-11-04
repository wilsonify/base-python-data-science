// Probability Implementation - C++ Data Science Library
// Port from TypeScript implementation

#include "probability.h"
#include <cmath>
#include <algorithm>
#include <random>
#include <chrono>

// Random number generator
static std::random_device rd;
static std::mt19937 gen(rd());

// Error function and normal distribution
double erf(double x) {
    double a1 = 0.254829592;
    double a2 = -0.284496736;
    double a3 = 1.421413741;
    double a4 = -1.453152027;
    double a5 = 1.061405429;
    double p = 0.3275911;
    double sign = 1;
    if (x < 0) { sign = -1; }
    x = std::abs(x);
    double t = 1.0 / (1.0 + p * x);
    double y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * std::exp(-x * x);
    return sign * y;
}

double uniform_pdf(double x, double a, double b) {
    return (a <= x && x < b) ? 1.0 / (b - a) : 0.0;
}

double uniform_cdf(double x, double a, double b) {
    /* returns the probability that a uniform random variable is less than x */
    if (x < a) {
        return 0.0;
    }
    if (a < x && x < b) {
        return (x - a) / (b - a);
    }
    if (b <= x) {
        return 1.0;
    }
    return 0.0; // Should not reach here
}

double normal_pdf(double x, double mu, double sigma) {
    double sqrt_two_pi = std::sqrt(2.0 * M_PI);
    return std::exp(-std::pow(x - mu, 2.0) / 2.0 / std::pow(sigma, 2.0)) / (sqrt_two_pi * sigma);
}

double normal_cdf(double x, double mu, double sigma) {
    return (1.0 + erf((x - mu) / std::sqrt(2.0) / sigma)) / 2.0;
}

double inverse_normal_cdf(double p, double mu, double sigma, double tolerance) {
    /* find approximate inverse using binary search */
    double low_z = -10.0;
    double low_p = 0.0;
    double hi_z = 10.0;
    double hi_p = 1.0;
    double mid_z = (low_z + hi_z) / 2.0;

    while (hi_z - low_z > tolerance) {
        mid_z = (low_z + hi_z) / 2.0;
        double mid_p = normal_cdf(mid_z);

        if (mid_p < p) {
            low_z = mid_z;
            low_p = mid_p;
        } else if (mid_p > p) {
            hi_z = mid_z;
            hi_p = mid_p;
        } else {
            break;
        }
    }

    return mid_z;
}

// Random functions
std::string random_choice(const std::vector<std::string>& choices) {
    if (choices.empty()) {
        return "";
    }
    std::uniform_int_distribution<> dis(0, choices.size() - 1);
    return choices[dis(gen)];
}

std::string random_kid() {
    static std::vector<std::string> choices = {"boy", "girl"};
    return random_choice(choices);
}

double random_normal() {
    // returns a random draw from a standard normal distribution
    std::uniform_real_distribution<> dis(0.0, 1.0);
    return inverse_normal_cdf(dis(gen));
}

// Probability distributions
int bernoulli_trial(double p) {
    std::uniform_real_distribution<> dis(0.0, 1.0);
    return (dis(gen) < p) ? 1 : 0;
}

int binomial(double p, int n) {
    int result = 0;
    for (int i = 0; i < n; ++i) {
        result += bernoulli_trial(p);
    }
    return result;
}
