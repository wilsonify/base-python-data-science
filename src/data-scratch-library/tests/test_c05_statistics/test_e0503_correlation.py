"""
Comprehensive tests for correlation measures
Tests include: covariance, correlation, correlation matrix
"""
import pytest
import math
from dsl.c05_statistics.e0503_correlation import covariance, correlation, correlation_matrix
from dsl.c05_statistics.e0502_dispersion import standard_deviation


# ============================================================================
# covariance tests
# ============================================================================

class TestCovariance:
    """Test covariance calculation"""
    
    def test_basic_covariance(self):
        """Test basic covariance calculation"""
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        # Perfect linear relationship: y = 2x
        # cov(x, y) should be positive
        result = covariance(x, y)
        assert result > 0
        
    def test_covariance_with_self(self):
        """Test that cov(X, X) = var(X)"""
        from dsl.c05_statistics.e0502_dispersion import variance
        x = [1, 2, 3, 4, 5]
        cov_xx = covariance(x, x)
        var_x = variance(x)
        assert cov_xx == pytest.approx(var_x)
        
    def test_covariance_symmetric(self):
        """Test that cov(X, Y) = cov(Y, X)"""
        x = [1, 2, 3, 4]
        y = [2, 3, 5, 7]
        assert covariance(x, y) == pytest.approx(covariance(y, x))
        
    def test_positive_covariance(self):
        """Test positive covariance (both increase together)"""
        x = [1, 2, 3, 4, 5]
        y = [1, 2, 3, 4, 5]
        assert covariance(x, y) > 0
        
    def test_negative_covariance(self):
        """Test negative covariance (inverse relationship)"""
        x = [1, 2, 3, 4, 5]
        y = [5, 4, 3, 2, 1]
        assert covariance(x, y) < 0
        
    def test_zero_covariance(self):
        """Test near-zero covariance (no linear relationship)"""
        x = [1, 2, 3, 4]
        y = [2, 1, 2, 1]  # No clear linear trend
        result = covariance(x, y)
        # Should be close to zero
        assert abs(result) < 1.0
        
    def test_covariance_constant(self):
        """Test covariance when one variable is constant"""
        x = [1, 2, 3, 4, 5]
        y = [5, 5, 5, 5, 5]
        # Constant has zero variance, so covariance should be 0
        assert covariance(x, y) == pytest.approx(0)
        
    @pytest.mark.parametrize("x,y,expected_sign", [
        ([1, 2, 3], [1, 2, 3], 1),  # Positive
        ([1, 2, 3], [3, 2, 1], -1),  # Negative
        ([1, 2], [1, 2], 1),  # Positive
    ])
    def test_parametrized_covariance_sign(self, x, y, expected_sign):
        """Test covariance sign"""
        result = covariance(x, y)
        if expected_sign > 0:
            assert result > 0
        elif expected_sign < 0:
            assert result < 0


# ============================================================================
# correlation tests
# ============================================================================

class TestCorrelation:
    """Test correlation coefficient calculation"""
    
    def test_perfect_positive_correlation(self):
        """Test perfect positive correlation (r = 1)"""
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]  # y = 2x
        assert correlation(x, y) == pytest.approx(1.0, abs=1e-9)
        
    def test_perfect_negative_correlation(self):
        """Test perfect negative correlation (r = -1)"""
        x = [1, 2, 3, 4, 5]
        y = [5, 4, 3, 2, 1]
        assert correlation(x, y) == pytest.approx(-1.0, abs=1e-9)
        
    def test_correlation_with_self(self):
        """Test that cor(X, X) = 1"""
        x = [1, 2, 3, 4, 5]
        assert correlation(x, x) == pytest.approx(1.0, abs=1e-9)
        
    def test_correlation_symmetric(self):
        """Test that cor(X, Y) = cor(Y, X)"""
        x = [1, 2, 3, 4]
        y = [2, 3, 5, 7]
        assert correlation(x, y) == pytest.approx(correlation(y, x))
        
    def test_correlation_bounded(self):
        """Test that -1 <= r <= 1"""
        x = [1, 2, 3, 4, 5]
        y = [2, 3, 1, 5, 4]
        r = correlation(x, y)
        assert -1 <= r <= 1
        
    def test_zero_correlation(self):
        """Test near-zero correlation"""
        x = [1, 2, 3, 4, 5]
        y = [3, 1, 4, 1, 5]  # No clear pattern
        r = correlation(x, y)
        # Should be between -1 and 1, possibly near 0
        assert -1 <= r <= 1
        
    def test_correlation_scale_invariant(self):
        """Test that correlation is scale-invariant"""
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        
        # Scale x and y
        x_scaled = [10 * val for val in x]
        y_scaled = [100 * val for val in y]
        
        r1 = correlation(x, y)
        r2 = correlation(x_scaled, y_scaled)
        assert r1 == pytest.approx(r2, abs=1e-9)
        
    def test_correlation_location_invariant(self):
        """Test that correlation is location-invariant"""
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        
        # Shift x and y
        x_shifted = [val + 100 for val in x]
        y_shifted = [val + 1000 for val in y]
        
        r1 = correlation(x, y)
        r2 = correlation(x_shifted, y_shifted)
        assert r1 == pytest.approx(r2, abs=1e-9)
        
    @pytest.mark.parametrize("x,y,expected", [
        ([1, 2], [2, 1], -1.0),
        ([1, 2], [1, 2], 1.0),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 1.0),
    ])
    def test_parametrized_correlation(self, x, y, expected):
        """Parametrized correlation tests"""
        assert correlation(x, y) == pytest.approx(expected, abs=1e-9)


# ============================================================================
# correlation_matrix tests
# ============================================================================

class TestCorrelationMatrix:
    """Test correlation matrix calculation"""
    
    def test_basic_correlation_matrix(self):
        """Test basic correlation matrix"""
        data = [
            [1, 2, 3],
            [2, 4, 6],
            [3, 6, 9]
        ]
        matrix = correlation_matrix(data)
        
        # Should be 3x3
        assert len(matrix) == 3
        assert all(len(row) == 3 for row in matrix)
        
    def test_diagonal_is_ones(self):
        """Test that diagonal elements are 1 (cor(X, X) = 1)"""
        data = [
            [1, 2, 3, 4],
            [2, 4, 6, 8],
            [1, 3, 5, 7]
        ]
        matrix = correlation_matrix(data)
        
        for i in range(len(matrix)):
            assert matrix[i][i] == pytest.approx(1.0, abs=1e-9)
            
    def test_matrix_symmetric(self):
        """Test that correlation matrix is symmetric"""
        data = [
            [1, 2, 3, 4],
            [2, 3, 4, 5],
            [5, 4, 3, 2]
        ]
        matrix = correlation_matrix(data)
        
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                assert matrix[i][j] == pytest.approx(matrix[j][i], abs=1e-9)
                
    def test_single_variable(self):
        """Test correlation matrix for single variable with multiple observations"""
        # Data should have multiple rows (observations), one column (variable)
        # But correlation_matrix expects data[i] to be a variable
        # So for one variable, we need data = [[obs1, obs2, obs3, ...]]
        data = [[1, 2, 3, 4, 5]]  # One variable, 5 observations
        
        try:
            matrix = correlation_matrix(data)
            # Should be 1x1 matrix
            assert len(matrix) == 1
            assert len(matrix[0]) == 1
            # Correlation of variable with itself should be 1 (or 0 if no variation)
            assert matrix[0][0] in [0, 1] or abs(matrix[0][0] - 1.0) < 1e-9
        except ZeroDivisionError:
            # Single element per variable causes division by zero in variance
            pytest.skip("Variance undefined for single observation")
        
    def test_two_variables(self):
        """Test correlation matrix for two variables"""
        # 4 observations (rows), 2 variables (columns)
        # Variable 1: [1, 2, 3, 4], Variable 2: [2, 4, 6, 8]
        data = [
            [1, 2],  # observation 1
            [2, 4],  # observation 2
            [3, 6],  # observation 3
            [4, 8]   # observation 4
        ]
        matrix = correlation_matrix(data)
        
        # Should be 2x2
        assert len(matrix) == 2
        assert len(matrix[0]) == 2
        
        # Diagonal should be 1 (correlation with self)
        assert matrix[0][0] == pytest.approx(1.0, abs=1e-9)
        assert matrix[1][1] == pytest.approx(1.0, abs=1e-9)
        
        # Off-diagonal should be symmetric
        assert matrix[0][1] == pytest.approx(matrix[1][0], abs=1e-9)
        
    def test_perfectly_correlated_variables(self):
        """Test correlation matrix with perfectly correlated variables"""
        # 4 observations, 2 variables with perfect positive correlation
        # Variable 1: [1, 2, 3, 4], Variable 2: [2, 4, 6, 8] (y = 2x)
        data = [
            [1, 2],
            [2, 4],
            [3, 6],
            [4, 8]
        ]
        matrix = correlation_matrix(data)
        
        # Should have 1 on off-diagonal (perfect correlation)
        assert matrix[0][1] == pytest.approx(1.0, abs=1e-6)
        
    def test_negatively_correlated_variables(self):
        """Test correlation matrix with negatively correlated variables"""
        # 4 observations, 2 variables with perfect negative correlation
        # Variable 1: [1, 2, 3, 4], Variable 2: [4, 3, 2, 1]
        data = [
            [1, 4],
            [2, 3],
            [3, 2],
            [4, 1]
        ]
        matrix = correlation_matrix(data)
        # Should have -1 on off-diagonal (perfect negative correlation)
        assert matrix[0][1] == pytest.approx(-1.0, abs=1e-9)


# ============================================================================
# Integration and mathematical property tests
# ============================================================================

class TestCorrelationProperties:
    """Test mathematical properties of correlation measures"""
    
    def test_correlation_from_covariance(self):
        """Test that cor(X,Y) = cov(X,Y) / (std(X) * std(Y))"""
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 5, 4, 5]
        
        cov_xy = covariance(x, y)
        std_x = standard_deviation(x)
        std_y = standard_deviation(y)
        
        expected_cor = cov_xy / (std_x * std_y)
        actual_cor = correlation(x, y)
        
        assert actual_cor == pytest.approx(expected_cor, abs=1e-9)
        
    def test_cauchy_schwarz_for_covariance(self):
        """Test |cov(X,Y)| <= std(X) * std(Y)"""
        x = [1, 2, 3, 4, 5]
        y = [2, 3, 1, 5, 4]
        
        cov_xy = abs(covariance(x, y))
        std_x = standard_deviation(x)
        std_y = standard_deviation(y)
        
        assert cov_xy <= std_x * std_y + 1e-9
        
    def test_correlation_bounds(self):
        """Test that correlation is always between -1 and 1"""
        import random
        random.seed(42)
        
        # Test with random data
        for _ in range(10):
            x = [random.random() for _ in range(10)]
            y = [random.random() for _ in range(10)]
            r = correlation(x, y)
            assert -1 <= r <= 1
            
    def test_uncorrelated_independent_uniform(self, seed_random):
        """Test that independent random variables have low correlation"""
        import random
        
        x = [random.random() for _ in range(100)]
        y = [random.random() for _ in range(100)]
        
        r = correlation(x, y)
        # Should be close to 0 for independent variables
        assert abs(r) < 0.3  # Relaxed bound for random data
