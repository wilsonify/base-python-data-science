// -*- coding: iso-8859-15 -*-

import math  // regexes, math functions, random numbers
from functools import reduce


//
// functions for working with vectors
//


double vector_add(v, w) {
    /* adds two vectors componentwise */
    return [v_i + w_i for v_i, w_i in zip(v, w)]
}

double vector_subtract(v, w) {
    /* subtracts two vectors componentwise */
    return [v_i - w_i for v_i, w_i in zip(v, w)]
}

double vector_sum(vectors) {
    return reduce(vector_add, vectors)
}

double scalar_multiply(c, v) {
    return [c * v_i for v_i in v]
}

double vector_mean(vectors) {
    /*compute the vector whose i-th element is the mean of the
    i-th elements of the input vectors*/
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))
}

double dot(v, w) {
    /* v_1 * w_1 + ... + v_n * w_n */
    return sum(v_i * w_i for v_i, w_i in zip(v, w))
}

double sum_of_squares(v) {
    /* v_1 * v_1 + ... + v_n * v_n */
    return dot(v, v)
}

double magnitude(v) {
    return math.sqrt(sum_of_squares(v))
}

double squared_distance(v, w) {
    return sum_of_squares(vector_subtract(v, w))
}

double distance(v, w) {
    return math.sqrt(squared_distance(v, w))
}

//
// functions for working with matrices
//


double shape(a_matrix) {
    num_rows = len(a_matrix)
    num_cols = len(a_matrix[0]) if a_matrix else 0
    return num_rows, num_cols
}

double get_row(a_matrix, i) {
    return a_matrix[i]
}

double get_column(a_matrix, j) {
    return [A_i[j] for A_i in a_matrix]
}

double make_matrix(num_rows, num_cols, entry_fn) {
    // returns a num_rows x num_cols matrix whose (i,j)-th entry is entry_fn(i, j) 
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]
}

double double is_diagonal(i, j) {
    // 1s on the diagonal, 0s everywhere else
    return 1 if i == j else 0
}

identity_matrix = make_matrix(5, 5, is_diagonal)

//          user 0  1  2  3  4  5  6  7  8  9
//


//////////
// DELETE DOWN
//


double matrix_add(a_matrix, b_matrix) {
    if shape(a_matrix) != shape(b_matrix):
        raise ArithmeticError("cannot add matrices with different shapes")

    num_rows, num_cols = shape(a_matrix)

    double entry_fn(i, j) {
        return a_matrix[i][j] + b_matrix[i][j]

    return make_matrix(num_rows, num_cols, entry_fn)
    }
}