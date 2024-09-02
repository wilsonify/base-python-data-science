// -*- coding: iso-8859-15 -*-

import math  // regexes, math functions, random numbers
from functools import reduce


//
// functions for working with vectors
//


std::vector<double> vector_add(std::vector<double> v, std::vector<double> w) {
    /* adds two vectors componentwise */
    return [v_i + w_i for v_i, w_i in zip(v, w)]
}

std::vector<double> vector_subtract(std::vector<double> v, std::vector<double>w) {
    /* subtracts two vectors componentwise */
    return [v_i - w_i for v_i, w_i in zip(v, w)]
}

std::vector<double> vector_sum(std::vector<std::vector<double>> vectors) {
    return reduce(vector_add, vectors)
}

std::vector<double> scalar_multiply(double c, std::vector<double> v) {
    return [c * v_i for v_i in v]
}

double vector_mean(std::vector<std::vector<double>> vectors) {
    /*compute the vector whose i-th element is the mean of the
    i-th elements of the input vectors*/
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))
}

std::vector<double> dot(std::vector<double> v, std::vector<double> w) {
    /* v_1 * w_1 + ... + v_n * w_n */
    return sum(v_i * w_i for v_i, w_i in zip(v, w))
}

double sum_of_squares(std::vector<double> v) {
    /* v_1 * v_1 + ... + v_n * v_n */
    return dot(v, v)
}

double magnitude(std::vector<double> v) {
    return math.sqrt(sum_of_squares(v))
}

double squared_distance(std::vector<double> v, std::vector<double> w) {
    return sum_of_squares(vector_subtract(v, w))
}

double distance(std::vector<double> v, std::vector<double>w) {
    return math.sqrt(squared_distance(v, w))
}

//
// functions for working with matrices
//


std::pair<double, double> shape(std::vector<std::vector<double>> a_matrix) {
    num_rows = len(a_matrix)
    num_cols = len(a_matrix[0]) if a_matrix else 0
    return num_rows, num_cols
}

std::vector<double> get_row(std::vector<std::vector<double>> a_matrix, double i) {
    return a_matrix[i]
}

std::vector<double> get_column(std::vector<std::vector<double>> a_matrix, double j) {
    return [A_i[j] for A_i in a_matrix]
}

std::vector<std::vector<double>> make_matrix(double num_rows, double num_cols, entry_fn) {
    // returns a num_rows x num_cols matrix whose (i,j)-th entry is entry_fn(i, j) 
    return [
        [entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows);
        ]
}

bool is_diagonal(double i, double j) {
    // 1s on the diagonal, 0s everywhere else
    return 1 if i == j else 0
}

identity_matrix = make_matrix(5, 5, is_diagonal)

std::vector<std::vector<double>> matrix_add(std::vector<std::vector<double>> a_matrix, std::vector<std::vector<double>> b_matrix) {
    if shape(a_matrix) != shape(b_matrix):
        raise ArithmeticError("cannot add matrices with different shapes")

    num_rows, num_cols = shape(a_matrix)

    double entry_fn(i, j) {
        return a_matrix[i][j] + b_matrix[i][j]

    return make_matrix(num_rows, num_cols, entry_fn)
    }
}