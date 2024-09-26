"""
functions for working with matrices
"""
from typing import Callable, Tuple

from dsl.c04_linear_algebra import Matrix, Vector


def shape(a_matrix: Matrix) -> Tuple[int, int]:
    num_rows = len(a_matrix)
    num_cols = len(a_matrix[0]) if a_matrix else 0
    return num_rows, num_cols


def get_row(a_matrix: Matrix, i: int) -> Vector:
    return a_matrix[i]


def get_column(a_matrix: Matrix, j: int) -> Vector:
    return [A_i[j] for A_i in a_matrix]


def make_matrix(num_rows: int, num_cols: int, entry_fn: Callable) -> Matrix:
    """
    returns a num_rows x num_cols matrix
    whose (i,j)-th entry is entry_fn(i, j)
    """
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]


def is_diagonal(i, j):
    """1's on the 'diagonal', 0's everywhere else"""
    return 1 if i == j else 0


def make_identity_matrix(n):
    return make_matrix(
        num_rows=n,
        num_cols=n,
        entry_fn=is_diagonal
    )


def matrix_add(a_matrix, b_matrix):
    assertmsg = "cannot add matrices with different shapes"
    assert shape(a_matrix) == shape(b_matrix), assertmsg
    num_rows, num_cols = shape(a_matrix)

    def entry_add(i, j):
        return a_matrix[i][j] + b_matrix[i][j]

    return make_matrix(num_rows, num_cols, entry_add)


def matrix_multiply(a_matrix, b_matrix):
    assertmsg = "Cannot multiply matrices: number of columns in A must equal the number of rows in B"
    num_rows_a, num_cols_a = shape(a_matrix)
    num_rows_b, num_cols_b = shape(b_matrix)
    assert num_cols_a == num_rows_b, assertmsg

    def entry_multiply(i, j):
        return sum(a_matrix[i][k] * b_matrix[k][j] for k in range(num_cols_a))

    return make_matrix(num_rows_a, num_cols_b, entry_multiply)
