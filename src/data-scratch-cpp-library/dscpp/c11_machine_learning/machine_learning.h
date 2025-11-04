#pragma once

#include <vector>
#include <map>

// Data splitting structures
struct SplitData {
    std::vector<std::vector<double>> train;
    std::vector<std::vector<double>> test;
};

struct TrainTestSplit {
    std::vector<std::vector<double>> x_train;
    std::vector<double> y_train;
    std::vector<std::vector<double>> x_test;
    std::vector<double> y_test;
};

// Data splitting functions
SplitData split_data(const std::vector<std::vector<double>>& data, double prob);
TrainTestSplit train_test_split(const std::vector<std::vector<double>>& x, 
                               const std::vector<double>& y, 
                               double test_pct);

// Performance metrics
double accuracy(double tp, double fp, double fn, double tn);
double precision(double tp, double fp, double fn, double tn);
double recall(double tp, double fp, double fn, double tn);
double f1_score(double tp, double fp, double fn, double tn);