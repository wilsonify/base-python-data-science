"""
Comprehensive tests for matrix operations
Tests cover: happy paths, edge cases, error handling, and mathematical properties
"""
import pytest
from dsl.c04_linear_algebra.e0402_matrices import (
    get_column,
    get_row,
    is_diagonal,
    make_matrix,
    matrix_add,
    matrix_multiply,
    shape,
    make_identity_matrix,
    make_random_matrix,
)


# ============================================================================
# shape tests
# ============================================================================

class TestShape:
    """Test matrix shape function"""
    
    def test_basic_shape(self):
        """Test basic shape calculation"""
        assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)
        assert shape([[1], [2], [3]]) == (3, 1)
        
    def test_single_row(self):
        """Test shape of single row matrix"""
        assert shape([[1, 2, 3, 4]]) == (1, 4)
        
    def test_square_matrix(self):
        """Test shape of square matrix"""
        assert shape([[1, 2], [3, 4]]) == (2, 2)
        
    def test_empty_matrix(self):
        """Test shape of empty matrix"""
        assert shape([]) == (0, 0)
        
    def test_random_matrix_shape(self):
        """Test shape of randomly generated matrix"""
        mat = make_random_matrix(num_points=100, num_columns=4)
        assert shape(mat) == (100, 4)


# ============================================================================
# get_row and get_column tests
# ============================================================================

class TestGetRowColumn:
    """Test row and column access"""
    
    def test_get_row_basic(self):
        """Test basic row access"""
        mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        assert get_row(mat, 0) == [1, 2, 3]
        assert get_row(mat, 1) == [4, 5, 6]
        assert get_row(mat, 2) == [7, 8, 9]
        
    def test_get_column_basic(self):
        """Test basic column access"""
        mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        assert get_column(mat, 0) == [1, 4, 7]
        assert get_column(mat, 1) == [2, 5, 8]
        assert get_column(mat, 2) == [3, 6, 9]
        
    def test_get_single_element(self):
        """Test accessing single element matrices"""
        mat = [[42]]
        assert get_row(mat, 0) == [42]
        assert get_column(mat, 0) == [42]
        
    @pytest.mark.parametrize("mat,row_idx,expected", [
        ([[1], [2], [3]], 0, [1]),
        ([[1], [2], [3]], 2, [3]),
        ([[1, 2, 3]], 0, [1, 2, 3]),
    ])
    def test_parametrized_get_row(self, mat, row_idx, expected):
        """Parametrized tests for get_row"""
        assert get_row(mat, row_idx) == expected


# ============================================================================
# is_diagonal tests
# ============================================================================

class TestIsDiagonal:
    """Test diagonal element check"""
    
    def test_diagonal_elements(self):
        """Test that diagonal elements return 1"""
        assert is_diagonal(0, 0) == 1
        assert is_diagonal(1, 1) == 1
        assert is_diagonal(5, 5) == 1
        
    def test_off_diagonal_elements(self):
        """Test that off-diagonal elements return 0"""
        assert is_diagonal(0, 1) == 0
        assert is_diagonal(1, 0) == 0
        assert is_diagonal(2, 5) == 0
        
    @pytest.mark.parametrize("i,j,expected", [
        (0, 0, 1),
        (1, 1, 1),
        (10, 10, 1),
        (0, 1, 0),
        (1, 0, 0),
        (5, 3, 0),
    ])
    def test_parametrized_is_diagonal(self, i, j, expected):
        """Parametrized diagonal tests"""
        assert is_diagonal(i, j) == expected


# ============================================================================
# make_matrix tests
# ============================================================================

class TestMakeMatrix:
    """Test matrix creation"""
    
    def test_make_identity(self):
        """Test creating identity matrix with make_matrix"""
        result = make_matrix(3, 3, is_diagonal)
        expected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        assert result == expected
        
    def test_make_zeros(self):
        """Test creating zero matrix"""
        result = make_matrix(2, 3, lambda i, j: 0)
        expected = [[0, 0, 0], [0, 0, 0]]
        assert result == expected
        
    def test_make_ones(self):
        """Test creating matrix of all ones"""
        result = make_matrix(2, 2, lambda i, j: 1)
        expected = [[1, 1], [1, 1]]
        assert result == expected
        
    def test_make_custom_function(self):
        """Test creating matrix with custom entry function"""
        result = make_matrix(3, 3, lambda i, j: i + j)
        expected = [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
        assert result == expected
        
    def test_make_single_element(self):
        """Test creating 1x1 matrix"""
        result = make_matrix(1, 1, lambda i, j: 42)
        assert result == [[42]]
        
    def test_make_rectangular(self):
        """Test creating rectangular matrices"""
        result = make_matrix(2, 4, lambda i, j: i * 4 + j)
        assert shape(result) == (2, 4)


# ============================================================================
# make_identity_matrix tests
# ============================================================================

class TestMakeIdentityMatrix:
    """Test identity matrix creation"""
    
    def test_identity_2x2(self):
        """Test 2x2 identity matrix"""
        assert make_identity_matrix(2) == [[1, 0], [0, 1]]
        
    def test_identity_3x3(self):
        """Test 3x3 identity matrix"""
        assert make_identity_matrix(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        
    def test_identity_5x5(self):
        """Test 5x5 identity matrix"""
        expected = [
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1]
        ]
        assert make_identity_matrix(5) == expected
        
    def test_identity_diagonal_sum(self):
        """Test that diagonal sums to n"""
        n = 7
        identity = make_identity_matrix(n)
        diagonal_sum = sum(identity[i][i] for i in range(n))
        assert diagonal_sum == n
        
    def test_identity_off_diagonal_sum(self):
        """Test that off-diagonal elements sum to 0"""
        n = 4
        identity = make_identity_matrix(n)
        off_diagonal_sum = sum(
            identity[i][j] 
            for i in range(n) 
            for j in range(n) 
            if i != j
        )
        assert off_diagonal_sum == 0


# ============================================================================
# matrix_add tests
# ============================================================================

class TestMatrixAdd:
    """Test matrix addition"""
    
    def test_basic_addition(self):
        """Test basic matrix addition"""
        mat1 = [[1, 2], [3, 4]]
        mat2 = [[5, 6], [7, 8]]
        expected = [[6, 8], [10, 12]]
        assert matrix_add(mat1, mat2) == expected
        
    def test_add_identity(self, identity_matrix_2x2):
        """Test adding identity matrix"""
        mat = [[1, 2], [3, 4]]
        result = matrix_add(mat, identity_matrix_2x2)
        expected = [[2, 2], [3, 5]]
        assert result == expected
        
    def test_add_zeros(self):
        """Test that A + 0 = A"""
        mat = [[1, 2], [3, 4]]
        zeros = [[0, 0], [0, 0]]
        assert matrix_add(mat, zeros) == mat
        
    def test_addition_commutative(self):
        """Test that A + B = B + A"""
        mat1 = [[1, 2], [3, 4]]
        mat2 = [[5, 6], [7, 8]]
        assert matrix_add(mat1, mat2) == matrix_add(mat2, mat1)
        
    def test_single_element(self):
        """Test adding 1x1 matrices"""
        assert matrix_add([[1]], [[1]]) == [[2]]
        
    def test_mismatched_shapes_raise_error(self):
        """Test that adding matrices with different shapes raises error"""
        mat1 = [[1, 2], [3, 4]]
        mat2 = [[1, 2, 3]]
        with pytest.raises(AssertionError, match="different shapes"):
            matrix_add(mat1, mat2)
            
    @pytest.mark.parametrize("mat1,mat2,expected", [
        ([[1]], [[1]], [[2]]),
        ([[1, 0], [0, 1]], [[1, 2], [3, 4]], [[2, 2], [3, 5]]),
        ([[0, 0], [0, 0]], [[1, 2], [3, 4]], [[1, 2], [3, 4]]),
    ])
    def test_parametrized_addition(self, mat1, mat2, expected):
        """Parametrized matrix addition tests"""
        assert matrix_add(mat1, mat2) == expected


# ============================================================================
# matrix_multiply tests
# ============================================================================

class TestMatrixMultiply:
    """Test matrix multiplication"""
    
    def test_basic_multiplication(self):
        """Test basic matrix multiplication"""
        mat1 = [[1, 2], [3, 4]]
        mat2 = [[5, 6], [7, 8]]
        expected = [[19, 22], [43, 50]]
        assert matrix_multiply(mat1, mat2) == expected
        
    def test_multiply_by_identity(self, identity_matrix_2x2):
        """Test that A * I = A"""
        mat = [[1, 2], [3, 4]]
        result = matrix_multiply(mat, identity_matrix_2x2)
        assert result == mat
        
    def test_identity_times_matrix(self, identity_matrix_2x2):
        """Test that I * A = A"""
        mat = [[1, 2], [3, 4]]
        result = matrix_multiply(identity_matrix_2x2, mat)
        assert result == mat
        
    def test_rectangular_multiplication(self):
        """Test multiplying rectangular matrices"""
        # 2x3 * 3x2 = 2x2
        mat1 = [[1, 2, 3], [4, 5, 6]]
        mat2 = [[1, 2], [3, 4], [5, 6]]
        result = matrix_multiply(mat1, mat2)
        assert shape(result) == (2, 2)
        expected = [[22, 28], [49, 64]]
        assert result == expected
        
    def test_single_element(self):
        """Test 1x1 matrix multiplication"""
        assert matrix_multiply([[2]], [[3]]) == [[6]]
        
    def test_vector_as_matrix(self):
        """Test multiplying matrix by column vector"""
        mat = [[1, 2], [3, 4]]
        vec = [[5], [6]]  # column vector
        result = matrix_multiply(mat, vec)
        expected = [[17], [39]]
        assert result == expected
        
    def test_incompatible_shapes_raise_error(self):
        """Test that incompatible dimensions raise error"""
        mat1 = [[1, 2], [3, 4]]  # 2x2
        mat2 = [[1, 2, 3]]  # 1x3
        with pytest.raises(AssertionError, match="Cannot multiply"):
            matrix_multiply(mat1, mat2)
            
    def test_multiplication_not_commutative(self):
        """Test that AB != BA in general"""
        mat1 = [[1, 2], [3, 4]]
        mat2 = [[0, 1], [1, 0]]
        ab = matrix_multiply(mat1, mat2)
        ba = matrix_multiply(mat2, mat1)
        assert ab != ba
        
    def test_associative_property(self):
        """Test that (AB)C = A(BC)"""
        A = [[1, 2], [3, 4]]
        B = [[2, 0], [1, 2]]
        C = [[1, 1], [0, 1]]
        
        ab_c = matrix_multiply(matrix_multiply(A, B), C)
        a_bc = matrix_multiply(A, matrix_multiply(B, C))
        assert ab_c == a_bc


# ============================================================================
# Mathematical Property Tests
# ============================================================================

class TestMatrixProperties:
    """Test mathematical properties of matrices"""
    
    def test_identity_is_multiplicative_identity(self):
        """Test I * I = I"""
        identity = make_identity_matrix(3)
        result = matrix_multiply(identity, identity)
        assert result == identity
        
    def test_zero_matrix_property(self):
        """Test A + (-A) would equal zero (testing addition inverse concept)"""
        mat = [[1, 2], [3, 4]]
        neg_mat = [[-1, -2], [-3, -4]]
        zeros = [[0, 0], [0, 0]]
        assert matrix_add(mat, neg_mat) == zeros
        
    def test_distributive_left(self):
        """Test A(B + C) = AB + AC"""
        A = [[1, 2], [3, 4]]
        B = [[1, 0], [0, 1]]
        C = [[2, 1], [1, 2]]
        
        bc = matrix_add(B, C)
        left = matrix_multiply(A, bc)
        
        ab = matrix_multiply(A, B)
        ac = matrix_multiply(A, C)
        right = matrix_add(ab, ac)
        
        assert left == right


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
