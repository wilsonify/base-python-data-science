#pragma once

#include "../c04_linear_algebra/linear_algebra.h"
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include <limits>

// Basic statistics functions
double bucketize(double point, double bucket_size);
std::map<std::string, int> Counter(const std::vector<double>& array);
std::map<std::string, int> make_histogram(const std::vector<double>& points, double bucket_size);
std::vector<std::vector<double>> correlation_matrix(const std::vector<std::vector<double>>& data);

// Central tendency
double summation(const std::vector<double>& x);
double mean(const std::vector<double>& x);
double median(std::vector<double> v);
double quantile(std::vector<double> x, double p);
std::vector<double> mode(const std::vector<double>& x);
double data_range(const std::vector<double>& x);

// Dispersion measures
std::vector<double> de_mean(const std::vector<double>& x);
double variance(const std::vector<double>& x);
double standard_deviation(const std::vector<double>& x);
double interquartile_range(const std::vector<double>& x);

// Correlation and covariance
double covariance(const std::vector<double>& x, const std::vector<double>& y);
double correlation(const std::vector<double>& x, const std::vector<double>& y);