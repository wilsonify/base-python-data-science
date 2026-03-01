"""
Comprehensive tests for vector operations
Tests cover: happy paths, edge cases, error handling, and mathematical properties
"""
import pytest
import math
from dsl.c04_linear_algebra.e0401_vectors import (
    distance,
    distance2,
    dot,
    magnitude,
    scalar_multiply,
    squared_distance,
    sum_of_squares,
    vector_add,
    vector_mean,
    vector_subtract,
    vector_sum
)


# ============================================================================
# vector_add tests
# ============================================================================

class TestVectorAdd:
    """Test vector addition"""
    
    def test_basic_addition(self):
        """Test basic vector addition"""
        assert vector_add([1, 2], [3, 4]) == [4, 6]
        assert vector_add([1], [1]) == [2]
        
    def test_addition_with_zeros(self, zero_vector):
        """Test that v + 0 = v (additive identity)"""
        v = [1, 2, 3]
        assert vector_add(v, zero_vector) == v
        
    def test_addition_commutative(self):
        """Test that v + w = w + v"""
        v, w = [1, 2, 3], [4, 5, 6]
        assert vector_add(v, w) == vector_add(w, v)
        
    def test_negative_values(self):
        """Test addition with negative values"""
        assert vector_add([1, -2, 3], [-1, 2, -3]) == [0, 0, 0]
        
    def test_floating_point(self):
        """Test with floating point numbers"""
        result = vector_add([1.5, 2.5], [0.5, 0.5])
        assert result == pytest.approx([2.0, 3.0])
        
    def test_single_element(self):
        """Test with single element vectors"""
        assert vector_add([5], [3]) == [8]
        
    def test_mismatched_lengths_raises_error(self):
        """Test that mismatched vector lengths raise AssertionError"""
        with pytest.raises(AssertionError, match="same length"):
            vector_add([1, 2], [1, 2, 3])
            
    def test_empty_vectors_edge_case(self):
        """Test with empty vectors"""
        assert vector_add([], []) == []


# ============================================================================
# vector_subtract tests
# ============================================================================

class TestVectorSubtract:
    """Test vector subtraction"""
    
    def test_basic_subtraction(self):
        """Test basic vector subtraction"""
        assert vector_subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]
        
    def test_subtract_from_self_gives_zero(self):
        """Test that v - v = 0"""
        v = [1, 2, 3]
        assert vector_subtract(v, v) == [0, 0, 0]
        
    def test_subtract_zero(self, zero_vector):
        """Test that v - 0 = v"""
        v = [1, 2, 3]
        assert vector_subtract(v, zero_vector) == v
        
    def test_negative_results(self):
        """Test subtraction producing negative results"""
        assert vector_subtract([1, 2], [3, 4]) == [-2, -2]


# ============================================================================
# scalar_multiply tests
# ============================================================================

class TestScalarMultiply:
    """Test scalar multiplication"""
    
    def test_basic_multiplication(self):
        """Test basic scalar multiplication"""
        assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]
        
    def test_multiply_by_zero(self):
        """Test that 0 * v = 0"""
        v = [1, 2, 3]
        assert scalar_multiply(0, v) == [0, 0, 0]
        
    def test_multiply_by_one(self):
        """Test that 1 * v = v"""
        v = [1, 2, 3]
        assert scalar_multiply(1, v) == v
        
    def test_multiply_by_negative(self):
        """Test multiplication by negative scalar"""
        assert scalar_multiply(-2, [1, 2, 3]) == [-2, -4, -6]
        
    def test_multiply_empty_vector(self):
        """Test scalar multiplication with empty vector"""
        assert scalar_multiply(5, []) == []
        
    @pytest.mark.parametrize("scalar,vector,expected", [
        (2, [1, 2, 3], [2, 4, 6]),
        (0.5, [2, 4, 6], [1, 2, 3]),
        (-1, [1, 2], [-1, -2]),
        (3, [0, 0], [0, 0]),
    ])
    def test_parametrized_multiply(self, scalar, vector, expected):
        """Parametrized tests for scalar multiplication"""
        assert scalar_multiply(scalar, vector) == pytest.approx(expected)


# ============================================================================
# vector_sum tests
# ============================================================================

class TestVectorSum:
    """Test summing multiple vectors"""
    
    def test_sum_two_vectors(self):
        """Test summing two vectors"""
        assert vector_sum([[1, 2], [3, 4]]) == [4, 6]
        
    def test_sum_multiple_vectors(self):
        """Test summing many vectors"""
        vectors = [[1, 2], [3, 4], [5, 6], [7, 8]]
        assert vector_sum(vectors) == [16, 20]
        
    def test_sum_with_single_vector(self):
        """Test sum of single vector returns that vector"""
        v = [1, 2, 3]
        assert vector_sum([v]) == v


# ============================================================================
# vector_mean tests
# ============================================================================

class TestVectorMean:
    """Test vector mean calculation"""
    
    def test_mean_of_two(self):
        """Test mean of two vectors"""
        assert vector_mean([[1, 2], [3, 4]]) == [2, 3]
        
    def test_mean_of_identical_vectors(self):
        """Test that mean of identical vectors equals that vector"""
        v = [1, 2, 3]
        assert vector_mean([v, v, v]) == v
        
    def test_mean_three_vectors(self):
        """Test mean of three vectors"""
        assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]
        
    def test_mean_with_floating_point(self):
        """Test mean with floating point results"""
        result = vector_mean([[1, 0, 0, 1], [1, 2, 3, 4]])
        assert result == pytest.approx([1, 1, 1.5, 2.5])


# ============================================================================
# dot product tests
# ============================================================================

class TestDot:
    """Test dot product"""
    
    def test_basic_dot_product(self):
        """Test basic dot product calculation"""
        assert dot([1, 2, 3], [4, 5, 6]) == 32
        
    def test_dot_with_zero_vector(self, zero_vector):
        """Test that dot(v, 0) = 0"""
        v = [1, 2, 3]
        assert dot(v, zero_vector) == 0
        
    def test_dot_commutative(self):
        """Test that dot(v, w) = dot(w, v)"""
        v, w = [1, 2, 3], [4, 5, 6]
        assert dot(v, w) == dot(w, v)
        
    def test_dot_with_self(self):
        """Test dot product of vector with itself"""
        assert dot([3, 4], [3, 4]) == 25
        
    def test_orthogonal_vectors(self):
        """Test that orthogonal vectors have dot product = 0"""
        assert dot([1, 0], [0, 1]) == 0
        
    @pytest.mark.parametrize("v,w,expected", [
        ([1, 1, 1], [10, 10, 10], 30),
        ([1, 1, 1], [-10, -10, -10], -30),
        ([1, 0, 0], [0, 1, 0], 0),
        ([2, 3], [4, 5], 23),
    ])
    def test_parametrized_dot(self, v, w, expected):
        """Parametrized dot product tests"""
        assert dot(v, w) == expected


# ============================================================================
# sum_of_squares tests
# ============================================================================

class TestSumOfSquares:
    """Test sum of squares calculation"""
    
    def test_basic_sum_of_squares(self):
        """Test basic sum of squares"""
        assert sum_of_squares([1, 2, 3]) == 14
        assert sum_of_squares([3, 4]) == 25
        
    def test_zero_vector(self, zero_vector):
        """Test sum of squares of zero vector is 0"""
        assert sum_of_squares(zero_vector) == 0
        
    def test_single_element(self):
        """Test with single element"""
        assert sum_of_squares([5]) == 25
        
    def test_negative_values(self):
        """Test that negative values square to positive"""
        assert sum_of_squares([-3, -4]) == 25
        
    @pytest.mark.parametrize("vector,expected", [
        ([1], 1),
        ([1, 0, 0, 1], 2),
        ([1, 2, 3, 4], 30),
        ([0, 0, 0], 0),
    ])
    def test_parametrized_sum_of_squares(self, vector, expected):
        """Parametrized sum of squares tests"""
        assert sum_of_squares(vector) == expected


# ============================================================================
# magnitude tests
# ============================================================================

class TestMagnitude:
    """Test vector magnitude"""
    
    def test_pythagorean_triple(self):
        """Test with Pythagorean triple"""
        assert magnitude([3, 4]) == 5
        assert magnitude([5, 12]) == 13
        
    def test_zero_vector(self, zero_vector):
        """Test magnitude of zero vector is 0"""
        assert magnitude(zero_vector) == 0
        
    def test_unit_vectors(self, unit_vectors):
        """Test that unit vectors have magnitude 1"""
        for vec in unit_vectors.values():
            assert magnitude(vec) == pytest.approx(1.0)
            
    def test_negative_values(self):
        """Test that magnitude handles negative values correctly"""
        assert magnitude([-3, -4]) == 5
        
    def test_magnitude_consistency(self):
        """Test magnitude equals sqrt(dot(v, v))"""
        v = [1, 2, 3]
        assert magnitude(v) == pytest.approx(math.sqrt(dot(v, v)))


# ============================================================================
# distance tests
# ============================================================================

class TestDistance:
    """Test distance calculations"""
    
    def test_basic_distance(self):
        """Test basic distance calculation"""
        assert distance([0, 0], [3, 4]) == 5
        
    def test_distance_to_self_is_zero(self):
        """Test that distance(v, v) = 0"""
        v = [1, 2, 3]
        assert distance(v, v) == 0
        
    def test_distance_symmetric(self):
        """Test that distance(v, w) = distance(w, v)"""
        v, w = [1, 2, 3], [4, 5, 6]
        assert distance(v, w) == distance(w, v)
        
    def test_distance_with_negatives(self):
        """Test distance with negative coordinates"""
        d = distance([0, 0, 0], [-10, -10, -10])
        assert d == pytest.approx(math.sqrt(300))
        
    def test_distance_and_distance2_agree(self):
        """Test that distance and distance2 give same results"""
        v, w = [1, 2, 3], [4, 5, 6]
        assert distance(v, w) == pytest.approx(distance2(v, w))


# ============================================================================
# squared_distance tests
# ============================================================================

class TestSquaredDistance:
    """Test squared distance"""
    
    def test_basic_squared_distance(self):
        """Test basic squared distance"""
        assert squared_distance([0, 0], [3, 4]) == 25
        
    def test_squared_distance_to_self(self):
        """Test that squared_distance(v, v) = 0"""
        v = [1, 2, 3]
        assert squared_distance(v, v) == 0
        
    def test_squared_distance_consistency(self):
        """Test that squared_distance = distance^2"""
        v, w = [1, 2, 3], [4, 5, 6]
        assert squared_distance(v, w) == pytest.approx(distance(v, w) ** 2)
        
    @pytest.mark.parametrize("v,w,expected", [
        ([1], [1], 0),
        ([1, 0, 0, 1], [1, 2, 3, 4], 22),
        ([0, 0], [3, 4], 25),
    ])
    def test_parametrized_squared_distance(self, v, w, expected):
        """Parametrized squared distance tests"""
        assert squared_distance(v, w) == expected


# ============================================================================
# Mathematical Property Tests
# ============================================================================

class TestMathematicalProperties:
    """Test mathematical properties and invariants"""
    
    def test_triangle_inequality(self):
        """Test that |v + w| <= |v| + |w|"""
        v, w = [1, 2, 3], [4, 5, 6]
        sum_vec = vector_add(v, w)
        assert magnitude(sum_vec) <= magnitude(v) + magnitude(w) + 1e-10
        
    def test_cauchy_schwarz(self):
        """Test Cauchy-Schwarz inequality: |dot(v,w)| <= |v| * |w|"""
        v, w = [1, 2, 3], [4, 5, 6]
        assert abs(dot(v, w)) <= magnitude(v) * magnitude(w) + 1e-10
        
    def test_scalar_distributive(self):
        """Test that c(v + w) = cv + cw"""
        c = 2
        v, w = [1, 2], [3, 4]
        left = scalar_multiply(c, vector_add(v, w))
        right = vector_add(scalar_multiply(c, v), scalar_multiply(c, w))
        assert left == right



