// Statistics Implementation - C++ Data Science Library
// Port from TypeScript implementation

#include "stats.h"
#include <algorithm>
#include <numeric>
#include <cmath>
#include <string>

// Basic statistics functions
double bucketize(double point, double bucket_size) {
    // floor the point to the next lower multiple of bucket_size
    return bucket_size * std::floor(point / bucket_size);
}

std::map<std::string, int> Counter(const std::vector<double>& array) {
    std::map<std::string, int> count;
    for (double val : array) {
        std::string key = std::to_string(val);
        count[key]++;
    }
    return count;
}

std::map<std::string, int> make_histogram(const std::vector<double>& points, double bucket_size) {
    // buckets the points and counts how many in each bucket
    std::vector<double> counting;
    for (double point : points) {
        counting.push_back(bucketize(point, bucket_size));
    }
    return Counter(counting);
}

std::vector<std::vector<double>> correlation_matrix(const std::vector<std::vector<double>>& data) {
    // returns the num_columns x num_columns matrix whose (i, j)th entry is the correlation between columns i and j of data
    auto shape_info = shape(data);
    int num_columns = shape_info.second;

    auto matrix_entry = [&data](int i, int j) {
        return correlation(get_column(data, i), get_column(data, j));
    };

    return make_matrix(num_columns, num_columns, matrix_entry);
}

// Central tendency
double summation(const std::vector<double>& x) {
    return std::accumulate(x.begin(), x.end(), 0.0);
}

double mean(const std::vector<double>& x) {
    if (x.empty()) {
        return std::numeric_limits<double>::quiet_NaN();
    }
    return summation(x) / static_cast<double>(x.size());
}

double median(std::vector<double> v) {
    if (v.empty()) {
        return std::numeric_limits<double>::quiet_NaN();
    }
    
    // finds the 'middle-most' value of v
    std::sort(v.begin(), v.end());
    int n = static_cast<int>(v.size());
    int midpoint = n / 2;

    if (n % 2 == 1) {
        return v[midpoint];
    } else {
        int lo = midpoint - 1;
        int hi = midpoint;
        return (v[lo] + v[hi]) / 2.0;
    }
}

double quantile(std::vector<double> x, double p) {
    if (x.empty()) {
        return std::numeric_limits<double>::quiet_NaN();
    }
    
    // returns the pth-percentile value in x
    std::sort(x.begin(), x.end());
    int p_index = static_cast<int>(std::floor(p * x.size()));
    p_index = std::max(0, std::min(p_index, static_cast<int>(x.size()) - 1));
    return x[p_index];
}

std::vector<double> mode(const std::vector<double>& x) {
    // returns a list, might be more than one mode
    auto counts = Counter(x);
    
    if (counts.empty()) {
        return {};
    }
    
    int max_count = 0;
    for (const auto& pair : counts) {
        max_count = std::max(max_count, pair.second);
    }
    
    std::vector<double> result;
    for (const auto& pair : counts) {
        if (pair.second == max_count) {
            result.push_back(std::stod(pair.first));
        }
    }
    return result;
}

double data_range(const std::vector<double>& x) {
    if (x.empty()) {
        return std::numeric_limits<double>::quiet_NaN();
    }
    
    auto minmax = std::minmax_element(x.begin(), x.end());
    return *minmax.second - *minmax.first;
}

// Dispersion measures
std::vector<double> de_mean(const std::vector<double>& x) {
    // translate x by subtracting its mean (so the result has mean 0)
    double x_bar = mean(x);
    std::vector<double> result(x.size());
    for (size_t i = 0; i < x.size(); ++i) {
        result[i] = x[i] - x_bar;
    }
    return result;
}

double variance(const std::vector<double>& x) {
    int n = static_cast<int>(x.size());
    if (n < 2) {
        return std::numeric_limits<double>::quiet_NaN();
    }
    auto deviations = de_mean(x);
    return sum_of_squares(deviations) / static_cast<double>(n - 1);
}

double standard_deviation(const std::vector<double>& x) {
    return std::sqrt(variance(x));
}

double interquartile_range(const std::vector<double>& x) {
    return quantile(x, 0.75) - quantile(x, 0.25);
}

// Correlation and covariance
double covariance(const std::vector<double>& x, const std::vector<double>& y) {
    int n = static_cast<int>(x.size());
    if (n < 2 || n != static_cast<int>(y.size())) {
        return std::numeric_limits<double>::quiet_NaN();
    }
    return dot(de_mean(x), de_mean(y)) / static_cast<double>(n - 1);
}

double correlation(const std::vector<double>& x, const std::vector<double>& y) {
    int n = static_cast<int>(x.size());
    if (n < 2 || n != static_cast<int>(y.size())) {
        return std::numeric_limits<double>::quiet_NaN();
    }
    
    double eps = 0.0001;
    double stdev_x = standard_deviation(x);
    double stdev_y = standard_deviation(y);
    double divisor = (stdev_x * stdev_y) + eps;
    return covariance(x, y) / divisor;
}
