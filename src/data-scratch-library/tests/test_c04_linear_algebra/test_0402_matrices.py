"""
functions for working with matrices
"""
from dsl.c04_linear_algebra.e0402_matrices import (
    get_column,
    get_row,
    is_diagonal,
    make_matrix,
    matrix_add,
    shape,
    make_identity_matrix, matrix_multiply, make_random_matrix,
)

A = [[1, 2, 3], [4, 5, 6]]  # A has 2 rows and 3 columns
B = [[1, 2], [3, 4], [5, 6]]  # B has 3 rows and 2 columns


def test_shape():
    assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)
    num_rows, num_columns = shape(
        make_random_matrix(
            num_points=100,
            num_columns=4
        ))
    assert num_rows == 100
    assert num_columns == 4


def test_make_identity_matrix():
    assert make_identity_matrix(5) == [
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1]
    ]


def test_get_column():
    mat1, col, expected = ([[1, 2, 3]], 0, [1])
    result = get_column(mat1, col)
    assert result == expected

    mat1, col, expected = ([[1, 2, 3]], 2, [3])
    result = get_column(mat1, col)
    assert result == expected


def test_get_row():
    mat1, row, expected = ([[1], [2], [3]], 0, [1])
    result = get_row(mat1, row)
    assert result == expected

    mat1, row, expected = ([[1], [2], [3]], 2, [3])
    result = get_row(mat1, row)
    assert result == expected


def test_is_diagonal():
    i, j, expected = (1, 1, True)
    result = is_diagonal(i, j)
    assert result == expected

    i, j, expected = (1, 2, False)
    result = is_diagonal(i, j)
    assert result == expected


def test_make_matrix():
    n, m, expected = (1, 1, [[1]])
    result = make_matrix(n, m, is_diagonal)
    assert result == expected

    n, m, expected = (3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    result = make_matrix(n, m, is_diagonal)
    assert result == expected


def test_matrix_add():
    mat1, mat2, expected = ([[1]], [[1]], [[2]])
    result = matrix_add(mat1, mat2)
    assert result == expected

    mat1, mat2, expected = ([[1, 0], [0, 1]], [[1, 2], [3, 4]], [[2, 2], [3, 5]])
    result = matrix_add(mat1, mat2)
    assert result == expected


def test_matrix_multiply():
    # Test 1: Multiply two 1x1 matrices
    mat1, mat2, expected = ([[2]], [[3]], [[6]])
    result = matrix_multiply(mat1, mat2)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test 2: Multiply two 2x2 matrices
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6], [7, 8]]
    expected = [[19, 22], [43, 50]]  # Result of multiplying mat1 and mat2
    result = matrix_multiply(mat1, mat2)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test 3: Multiply a 2x3 matrix with a 3x2 matrix
    mat1 = [[1, 2, 3], [4, 5, 6]]
    mat2 = [[7, 8], [9, 10], [11, 12]]
    expected = [[58, 64], [139, 154]]  # Result of multiplying mat1 and mat2
    result = matrix_multiply(mat1, mat2)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test 4: Multiply identity matrix
    mat1 = [[1, 0], [0, 1]]
    mat2 = [[5, 6], [7, 8]]
    expected = [[5, 6], [7, 8]]  # Multiplying by identity matrix should return the same matrix
    result = matrix_multiply(mat1, mat2)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test 5: Multiply two non-square matrices
    mat1 = [[1, 2], [3, 4], [5, 6]]
    mat2 = [[7, 8, 9], [10, 11, 12]]
    expected = [[27, 30, 33], [61, 68, 75], [95, 106, 117]]
    result = matrix_multiply(mat1, mat2)
    assert result == expected, f"Expected {expected}, but got {result}"
