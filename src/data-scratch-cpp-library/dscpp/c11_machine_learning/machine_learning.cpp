// Machine Learning Implementation - C++ Data Science Library
// Port from TypeScript implementation

#include "machine_learning.h"
#include <random>
#include <stdexcept>

// Random number generator
static std::random_device rd;
static std::mt19937 gen(rd());

// Data splitting functions
SplitData split_data(const std::vector<std::vector<double>>& data, double prob) {
    // split data into fractions [prob, 1 - prob]
    SplitData results;
    std::uniform_real_distribution dis(0.0, 1.0);
    
    for (const auto& row : data) {
        if (dis(gen) < prob) {
            results.test.push_back(row);
        } else {
            results.train.push_back(row);
        }
    }
    return results;
}

TrainTestSplit train_test_split(const std::vector<std::vector<double>>& x, 
                               const std::vector<double>& y, 
                               double test_pct) {
    if (x.size() != y.size()) {
        throw std::invalid_argument("x and y must have the same length");
    }
    
    TrainTestSplit results;
    std::uniform_real_distribution dis(0.0, 1.0);
    
    for (size_t i = 0; i < x.size(); ++i) {
        if (dis(gen) < test_pct) {
            results.x_test.push_back(x[i]);
            results.y_test.push_back(y[i]);
        } else {
            results.x_train.push_back(x[i]);
            results.y_train.push_back(y[i]);
        }
    }
    return results;
}

// Performance metrics
double accuracy(double tp, double fp, double fn, double tn) {
    double correct = tp + tn;
    double total = tp + fp + fn + tn;
    return (total == 0) ? 0.0 : correct / total;
}

double precision(double tp, double fp, [[maybe_unused]] double fn, [[maybe_unused]] double tn) {
    double denominator = tp + fp;
    return (denominator == 0) ? 0.0 : tp / denominator;
}

double recall(double tp, [[maybe_unused]] double fp, double fn, [[maybe_unused]] double tn) {
    double denominator = tp + fn;
    return (denominator == 0) ? 0.0 : tp / denominator;
}

double f1_score(double tp, double fp, double fn, double tn) {
    double p = precision(tp, fp, fn, tn);
    double r = recall(tp, fp, fn, tn);
    double denominator = p + r;
    return (denominator == 0) ? 0.0 : 2.0 * p * r / denominator;
}
