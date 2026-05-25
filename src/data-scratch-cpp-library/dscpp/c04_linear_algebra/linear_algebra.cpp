// Linear Algebra Implementation - C++ Data Science Library
// Port from TypeScript implementation

#include "linear_algebra.h"
#include <algorithm>
#include <numeric>
double scalar_add(double a, double b) {
    return a + b;
}

// Vector operations
std::vector<double> vector_add(const std::vector<double>& v, const std::vector<double>& w) {
    if (v.size() != w.size()) {
        throw std::invalid_argument("Vectors must be the same length");
    }
    
    std::vector<double> result(v.size());
    for (size_t i = 0; i < v.size(); ++i) {
        result[i] = v[i] + w[i];
    }
    return result;
}

std::vector<double> vector_subtract(const std::vector<double>& v, const std::vector<double>& w) {
    if (v.size() != w.size()) {
        throw std::invalid_argument("Vectors must be the same length");
    }
    
    std::vector<double> result(v.size());
    for (size_t i = 0; i < v.size(); ++i) {
        result[i] = v[i] - w[i];
    }
    return result;
}

std::vector<double> vector_sum(const std::vector<std::vector<double>>& vectors) {
    if (vectors.empty()) {
        return {};
    }
    
    if (vectors.size() == 1) {
        return vectors[0];
    }
    
    // Start with the first vector
    std::vector<double> result = vectors[0];
    
    // Add all remaining vectors
    for (size_t i = 1; i < vectors.size(); ++i) {
        result = vector_add(result, vectors[i]);
    }
    
    return result;
}

std::vector<double> scalar_multiply(double c, const std::vector<double>& v) {
    std::vector<double> result(v.size());
    for (size_t i = 0; i < v.size(); ++i) {
        result[i] = c * v[i];
    }
    return result;
}

std::vector<double> vector_mean(const std::vector<std::vector<double>>& vectors) {
    // compute the vector whose i-th element is the mean of the i-th elements of the input vectors
    double n = static_cast<double>(vectors.size());
    return scalar_multiply(1.0 / n, vector_sum(vectors));
}

// Vector math operations
double dot(const std::vector<double>& v, const std::vector<double>& w) {
    if (v.size() != w.size()) {
        throw std::invalid_argument("Vectors must be the same length");
    }
    
    double result = 0.0;
    for (size_t i = 0; i < v.size(); ++i) {
        result += v[i] * w[i];
    }
    return result;
}

double sum_of_squares(const std::vector<double>& v) {
    return dot(v, v);
}

double magnitude(const std::vector<double>& v) {
    return std::sqrt(sum_of_squares(v));
}

double squared_distance(const std::vector<double>& v, const std::vector<double>& w) {
    return sum_of_squares(vector_subtract(v, w));
}

double distance(const std::vector<double>& v, const std::vector<double>& w) {
    return std::sqrt(squared_distance(v, w));
}

// Matrix operations
std::pair<int, int> shape(const std::vector<std::vector<double>>& a_matrix) {
    int num_rows = static_cast<int>(a_matrix.size());
    int num_cols = a_matrix.empty() ? 0 : static_cast<int>(a_matrix[0].size());
    return {num_rows, num_cols};
}

std::vector<double> get_row(const std::vector<std::vector<double>>& a_matrix, int i) {
    if (i < 0 || i >= static_cast<int>(a_matrix.size())) {
        throw std::out_of_range("Row index out of range");
    }
    return a_matrix[i];
}

std::vector<double> get_column(const std::vector<std::vector<double>>& a_matrix, int j) {
    if (a_matrix.empty()) {
        throw std::invalid_argument("Matrix is empty");
    }
    if (j < 0 || j >= static_cast<int>(a_matrix[0].size())) {
        throw std::out_of_range("Column index out of range");
    }
    
    std::vector<double> result;
    for (const auto& row : a_matrix) {
        if (j >= static_cast<int>(row.size())) {
            throw std::out_of_range("Column index out of range");
        }
        result.push_back(row[j]);
    }
    return result;
}

double is_diagonal(int i, int j) {
    // 1's on the 'diagonal', 0's everywhere else
    return (i == j) ? 1.0 : 0.0;
}

// Define the identity matrix
const std::vector<std::vector<double>> identity_matrix = make_matrix(5, 5, is_diagonal);

std::vector<std::vector<double>> matrix_add(const std::vector<std::vector<double>>& a_matrix, 
                                           const std::vector<std::vector<double>>& b_matrix) {
    auto shape_a = shape(a_matrix);
    auto shape_b = shape(b_matrix);
    
    if (shape_a != shape_b) {
        throw std::invalid_argument("cannot add matrices with different shapes");
    }
    
    int num_rows = shape_a.first;
    int num_cols = shape_a.second;
    
    auto entry_fn = [&a_matrix, &b_matrix](int i, int j) {
        return a_matrix[i][j] + b_matrix[i][j];
    };
    
    return make_matrix(num_rows, num_cols, entry_fn);
}
