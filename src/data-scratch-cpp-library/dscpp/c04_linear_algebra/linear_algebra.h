#pragma once

#include <vector>
#include <functional>
#include <stdexcept>
#include <cmath>

// Type alias for bivariate function
using BivariateFunction = std::function<double(int, int)>;

// Scalar operations
double scalar_add(double a, double b);

// Vector operations
std::vector<double> vector_add(const std::vector<double>& v, const std::vector<double>& w);
std::vector<double> vector_subtract(const std::vector<double>& v, const std::vector<double>& w);
std::vector<double> vector_sum(const std::vector<std::vector<double>>& vectors);
std::vector<double> scalar_multiply(double c, const std::vector<double>& v);
std::vector<double> vector_mean(const std::vector<std::vector<double>>& vectors);

// Vector math operations
double dot(const std::vector<double>& v, const std::vector<double>& w);
double sum_of_squares(const std::vector<double>& v);
double magnitude(const std::vector<double>& v);
double squared_distance(const std::vector<double>& v, const std::vector<double>& w);
double distance(const std::vector<double>& v, const std::vector<double>& w);

// Matrix operations
std::pair<int, int> shape(const std::vector<std::vector<double>>& a_matrix);
std::vector<double> get_row(const std::vector<std::vector<double>>& a_matrix, int i);
std::vector<double> get_column(const std::vector<std::vector<double>>& a_matrix, int j);
std::vector<std::vector<double>> make_matrix(int num_rows, int num_cols, BivariateFunction entry_fn);
double is_diagonal(int i, int j);
extern const std::vector<std::vector<double>> identity_matrix;
std::vector<std::vector<double>> matrix_add(const std::vector<std::vector<double>>& a_matrix, const std::vector<std::vector<double>>& b_matrix);