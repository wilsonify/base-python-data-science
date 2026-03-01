"""
Comprehensive tests for dispersion measures
Tests include: variance, standard deviation, range, interquartile range, etc.
"""
import pytest
import math
from dsl.c05_statistics.e0502_dispersion import (
    variance,
    standard_deviation,
    data_range,
    de_mean,
    interquartile_range
)
from dsl.c05_statistics.e0501_central_tendancy import mean


# ============================================================================
# data_range tests
# ============================================================================

class TestDataRange:
    """Test range calculation"""
    
    def test_basic_range(self):
        """Test basic range calculation"""
        assert data_range([1, 2, 3, 4, 5]) == 4
        assert data_range([10, 20, 30]) == 20
        
    def test_range_single_value(self):
        """Test range of single value is 0"""
        assert data_range([5]) == 0
        
    def test_range_two_values(self):
        """Test range with two values"""
        assert data_range([3, 7]) == 4
        
    def test_range_negative_values(self):
        """Test range with negative values"""
        assert data_range([-10, -5, 0, 5, 10]) == 20
        
    def test_range_constant_list(self, constant_list):
        """Test that range of constant list is 0"""
        assert data_range(constant_list) == 0
        
    def test_range_unsorted(self):
        """Test range with unsorted data"""
        assert data_range([5, 1, 9, 3, 7]) == 8
        
    @pytest.mark.parametrize("data,expected", [
        ([1, 2], 1),
        ([1, 2, 10], 9),
        ([1, 2, 3, 4, 5], 4),
        ([0, 0, 1], 1),
        ([-5, 5], 10),
    ])
    def test_parametrized_range(self, data, expected):
        """Parametrized range tests"""
        assert data_range(data) == expected


# ============================================================================
# de_mean tests
# ============================================================================

class TestDeMean:
    """Test mean centering (de-meaning)"""
    
    def test_basic_demean(self):
        """Test basic de-meaning"""
        result = de_mean([1, 2, 3])
        assert result == pytest.approx([-1, 0, 1])
        
    def test_demean_result_has_zero_mean(self):
        """Test that de-meaned data has mean of 0"""
        data = [1, 2, 3, 4, 5]
        result = de_mean(data)
        assert abs(mean(result)) < 1e-10
        
    def test_demean_constant_list(self, constant_list):
        """Test de-meaning constant list gives zeros"""
        result = de_mean(constant_list)
        assert all(x == pytest.approx(0) for x in result)
        
    def test_demean_negative_values(self):
        """Test de-meaning with negative values"""
        result = de_mean([-2, 0, 2])
        assert result == pytest.approx([-2, 0, 2])
        
    def test_demean_single_value(self):
        """Test de-meaning single value gives 0"""
        assert de_mean([5]) == pytest.approx([0])
        
    @pytest.mark.parametrize("data,expected", [
        ([1, 2], [-0.5, 0.5]),
        ([1, 2, 12], [-4.0, -3.0, 7.0]),
        ([1, 2, 3, 4, 5], [-2.0, -1.0, 0.0, 1.0, 2.0]),
        ([0, 0, 1], [-1/3, -1/3, 2/3]),
    ])
    def test_parametrized_demean(self, data, expected):
        """Parametrized de-mean tests"""
        result = de_mean(data)
        assert result == pytest.approx(expected, abs=1e-9)


# ============================================================================
# variance tests
# ============================================================================

class TestVariance:
    """Test variance calculation"""
    
    def test_basic_variance(self):
        """Test basic variance calculation"""
        # Data: [1, 2, 3, 4, 5], mean = 3
        # Deviations: [-2, -1, 0, 1, 2]
        # Squared: [4, 1, 0, 1, 4] = 10
        # Variance (n-1): 10/4 = 2.5
        assert variance([1, 2, 3, 4, 5]) == pytest.approx(2.5)
        
    def test_variance_constant_list(self, constant_list):
        """Test that variance of constant list is 0"""
        assert variance(constant_list) == pytest.approx(0)
        
    def test_variance_two_values(self):
        """Test variance with two values"""
        # variance([1, 5]) = ((1-3)^2 + (5-3)^2) / 1 = (4 + 4) / 1 = 8
        assert variance([1, 5]) == pytest.approx(8.0)
        
    def test_variance_negative_values(self):
        """Test variance with negative values"""
        # [-2, 0, 2], mean = 0
        # Squared deviations: [4, 0, 4] = 8
        # Variance: 8/2 = 4
        assert variance([-2, 0, 2]) == pytest.approx(4.0)
        
    def test_variance_small_dataset(self, small_dataset):
        """Test variance with small dataset"""
        # [2, 4, 6, 8], mean = 5
        # Deviations: [-3, -1, 1, 3]
        # Squared: [9, 1, 1, 9] = 20
        # Variance: 20/3 ≈ 6.667
        result = variance(small_dataset)
        assert result == pytest.approx(6.666667, abs=1e-5)
        
    def test_variance_uses_n_minus_1(self):
        """Test that variance uses n-1 (Bessel's correction)"""
        data = [1, 2, 3, 4]
        n = len(data)
        deviations = de_mean(data)
        sum_sq = sum(d**2 for d in deviations)
        expected = sum_sq / (n - 1)
        assert variance(data) == pytest.approx(expected)
        
    @pytest.mark.parametrize("data,expected", [
        ([1, 1, 1, 1], 0.0),
        ([1, 2, 3], 1.0),
        ([0, 0, 0, 6], 9.0),  # mean=1.5, deviations=[-1.5,-1.5,-1.5,4.5], sum_sq=27, var=27/3=9
    ])
    def test_parametrized_variance(self, data, expected):
        """Parametrized variance tests"""
        assert variance(data) == pytest.approx(expected)


# ============================================================================
# standard_deviation tests
# ============================================================================

class TestStandardDeviation:
    """Test standard deviation calculation"""
    
    def test_basic_std(self):
        """Test basic standard deviation"""
        # variance([1, 2, 3, 4, 5]) = 2.5
        # std = sqrt(2.5) ≈ 1.58
        assert standard_deviation([1, 2, 3, 4, 5]) == pytest.approx(math.sqrt(2.5))
        
    def test_std_constant_list(self, constant_list):
        """Test that std of constant list is 0"""
        assert standard_deviation(constant_list) == pytest.approx(0)
        
    def test_std_equals_sqrt_variance(self):
        """Test that std = sqrt(variance)"""
        data = [1, 2, 3, 4, 5, 6]
        var = variance(data)
        std = standard_deviation(data)
        assert std == pytest.approx(math.sqrt(var))
        
    def test_std_positive(self):
        """Test that standard deviation is always non-negative"""
        data = [-10, -5, 0, 5, 10]
        assert standard_deviation(data) >= 0
        
    def test_std_small_dataset(self, small_dataset):
        """Test std with small dataset"""
        var = variance(small_dataset)
        expected = math.sqrt(var)
        assert standard_deviation(small_dataset) == pytest.approx(expected)
        
    @pytest.mark.parametrize("data", [
        [1, 2, 3, 4, 5],
        [10, 20, 30],
        [-5, 0, 5],
        [1.1, 2.2, 3.3],
    ])
    def test_std_variance_relationship(self, data):
        """Test std^2 = variance"""
        std = standard_deviation(data)
        var = variance(data)
        assert std ** 2 == pytest.approx(var)


# ============================================================================
# interquartile_range tests
# ============================================================================

class TestInterquartileRange:
    """Test interquartile range calculation"""
    
    def test_basic_iqr(self):
        """Test basic IQR calculation"""
        # For data 0-100, Q3=75, Q1=25, IQR=50
        data = list(range(101))
        assert interquartile_range(data) == pytest.approx(50)
        
    def test_iqr_constant_list(self, constant_list):
        """Test IQR of constant list is 0"""
        assert interquartile_range(constant_list) == 0
        
    def test_iqr_small_dataset(self):
        """Test IQR with small dataset"""
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = interquartile_range(data)
        # Q3 at 75% ≈ 7, Q1 at 25% ≈ 3
        assert result > 0
        
    def test_iqr_robust_to_outliers(self):
        """Test that IQR is robust to outliers"""
        normal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        with_outliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
        
        iqr_normal = interquartile_range(normal)
        iqr_outliers = interquartile_range(with_outliers)
        
        # IQR should be similar despite outlier
        assert abs(iqr_normal - iqr_outliers) < 2
        
    def test_iqr_unsorted(self):
        """Test that IQR handles unsorted data"""
        data = [9, 1, 5, 3, 7, 2, 8, 4, 6]
        result = interquartile_range(data)
        assert result > 0


# ============================================================================
# Integration and property tests
# ============================================================================

class TestDispersionProperties:
    """Test mathematical properties of dispersion measures"""
    
    def test_variance_nonnegative(self):
        """Test that variance is always non-negative"""
        test_cases = [
            [1, 2, 3, 4, 5],
            [-5, -4, -3, -2, -1],
            [0, 0, 0],
            [-10, 10],
        ]
        for data in test_cases:
            assert variance(data) >= 0
            
    def test_std_nonnegative(self):
        """Test that std is always non-negative"""
        test_cases = [
            [1, 2, 3, 4, 5],
            [-5, -4, -3, -2, -1],
            [0, 0, 0],
        ]
        for data in test_cases:
            assert standard_deviation(data) >= 0
            
    def test_adding_constant_doesnt_change_variance(self):
        """Test that adding a constant doesn't change variance"""
        data = [1, 2, 3, 4, 5]
        var_original = variance(data)
        
        data_plus_10 = [x + 10 for x in data]
        var_shifted = variance(data_plus_10)
        
        assert var_original == pytest.approx(var_shifted)
        
    def test_scaling_multiplies_std_by_scale(self):
        """Test that scaling by c multiplies std by |c|"""
        data = [1, 2, 3, 4, 5]
        std_original = standard_deviation(data)
        
        scale = 3
        data_scaled = [x * scale for x in data]
        std_scaled = standard_deviation(data_scaled)
        
        assert std_scaled == pytest.approx(abs(scale) * std_original)
        
    def test_zero_variance_implies_constant(self):
        """Test that zero variance implies all values are equal"""
        data = [5, 5, 5, 5, 5]
        assert variance(data) == pytest.approx(0)
        assert len(set(data)) == 1
        
    def test_range_bounds_other_measures(self):
        """Test that range >= std (rough relationship)"""
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        rng = data_range(data)
        std = standard_deviation(data)
        # Range is typically larger than std
        assert rng >= std
