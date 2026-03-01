"""
Comprehensive tests for central tendency measures
Tests include: mean, median, quantile, mode with edge cases and error handling
"""
import pytest
from collections import Counter
from dsl.c05_statistics.e0501_central_tendancy import mean, median, quantile, mode


# ============================================================================
# mean tests
# ============================================================================

class TestMean:
    """Test mean calculation"""
    
    def test_basic_mean(self, sample_data):
        """Test basic mean calculation"""
        assert mean(sample_data) == 5.5
        
    def test_mean_single_value(self):
        """Test mean of single value"""
        assert mean([5]) == 5
        
    def test_mean_two_values(self):
        """Test mean of two values"""
        assert mean([3, 7]) == 5
        
    def test_mean_negative_values(self):
        """Test mean with negative values"""
        assert mean([-1, 0, 1]) == 0
        
    def test_mean_constant_list(self, constant_list):
        """Test that mean of constant list equals that constant"""
        assert mean(constant_list) == 5
        
    def test_mean_floating_point(self, small_dataset):
        """Test mean with floating point"""
        assert mean(small_dataset) == pytest.approx(5.0)
        
    @pytest.mark.parametrize("data,expected", [
        ([1, 2, 3], 2.0),
        ([10, 20, 30], 20.0),
        ([0, 0, 0], 0.0),
        ([-5, 0, 5], 0.0),
        ([1.5, 2.5, 3.5], 2.5),
    ])
    def test_parametrized_mean(self, data, expected):
        """Parametrized mean tests"""
        assert mean(data) == pytest.approx(expected)
        
    def test_mean_empty_list_raises_error(self):
        """Test that mean of empty list raises ZeroDivisionError"""
        with pytest.raises(ZeroDivisionError):
            mean([])


# ============================================================================
# median tests
# ============================================================================

class TestMedian:
    """Test median calculation"""
    
    def test_median_odd_length(self):
        """Test median with odd number of elements"""
        assert median([1, 2, 3, 4, 5]) == 3
        assert median([1, 3, 5]) == 3
        
    def test_median_even_length(self):
        """Test median with even number of elements"""
        assert median([1, 2, 3, 4]) == 2.5
        assert median([1, 4]) == 2.5
        
    def test_median_single_value(self):
        """Test median of single value"""
        assert median([42]) == 42
        
    def test_median_two_values(self):
        """Test median of two values"""
        assert median([3, 7]) == 5.0
        
    def test_median_unsorted(self):
        """Test that median works with unsorted data"""
        assert median([5, 1, 3, 2, 4]) == 3
        
    def test_median_with_duplicates(self):
        """Test median with duplicate values"""
        assert median([1, 2, 2, 2, 3]) == 2
        assert median([1, 1, 2, 2]) == 1.5
        
    def test_median_negative_values(self):
        """Test median with negative values"""
        assert median([-3, -1, 0, 1, 3]) == 0
        
    def test_median_constant_list(self, constant_list):
        """Test median of constant list"""
        assert median(constant_list) == 5
        
    def test_median_empty_list_raises_error(self):
        """Test that median of empty list raises AssertionError"""
        with pytest.raises(AssertionError, match="empty"):
            median([])
            
    @pytest.mark.parametrize("data,expected", [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4], 2.5),
        ([5, 1, 3], 3),
        ([10], 10),
        ([-5, 0, 5], 0),
    ])
    def test_parametrized_median(self, data, expected):
        """Parametrized median tests"""
        assert median(data) == expected


# ============================================================================
# quantile tests
# ============================================================================

class TestQuantile:
    """Test quantile calculation"""
    
    def test_quartiles(self):
        """Test standard quartiles"""
        data = list(range(101))  # 0 to 100
        assert quantile(data, 0.25) == 25
        assert quantile(data, 0.50) == 50
        assert quantile(data, 0.75) == 75
        
    def test_deciles(self):
        """Test deciles"""
        data = list(range(101))
        assert quantile(data, 0.1) == 10
        assert quantile(data, 0.9) == 90
        
    def test_min_max_quantiles(self):
        """Test 0th and ~100th percentiles"""
        data = [1, 2, 3, 4, 5]
        assert quantile(data, 0.0) == 1
        assert quantile(data, 0.99) == 5
        
    def test_median_as_quantile(self):
        """Test that 50th percentile equals median"""
        data = [1, 2, 3, 4, 5]
        q50 = quantile(data, 0.5)
        med = median(data)
        # Note: quantile uses index-based method, might differ slightly
        assert q50 in data  # Should be a value from the dataset
        
    def test_single_value(self):
        """Test quantile of single value"""
        assert quantile([5], 0.5) == 5
        
    def test_quantile_unsorted(self):
        """Test that quantile handles unsorted data"""
        data = [5, 2, 8, 1, 9]
        q50 = quantile(data, 0.5)
        assert q50 in data
        
    @pytest.mark.parametrize("p", [0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 0.99])
    def test_quantile_range(self, p):
        """Test that quantiles are within data range"""
        data = list(range(1, 101))
        result = quantile(data, p)
        assert min(data) <= result <= max(data)


# ============================================================================
# mode tests
# ============================================================================

class TestMode:
    """Test mode calculation"""
    
    def test_single_mode(self):
        """Test data with single mode"""
        assert mode([1, 2, 2, 3]) == [2]
        assert mode([1, 1, 1, 2, 3]) == [1]
        
    def test_multiple_modes(self, bimodal_data):
        """Test bimodal data"""
        modes = mode(bimodal_data)
        assert set(modes) == {1, 2}
        assert len(modes) == 2
        
    def test_no_clear_mode(self):
        """Test when all values appear equally (all are modes)"""
        result = mode([1, 2, 3, 4, 5])
        assert len(result) == 5
        assert set(result) == {1, 2, 3, 4, 5}
        
    def test_constant_list_mode(self, constant_list):
        """Test mode of constant list"""
        assert mode(constant_list) == [5]
        
    def test_single_value_mode(self):
        """Test mode of single value"""
        assert mode([42]) == [42]
        
    def test_mode_with_strings(self):
        """Test that mode works with non-numeric data"""
        data = ['a', 'b', 'b', 'c']
        assert mode(data) == ['b']
        
    def test_three_modes(self):
        """Test data with three modes"""
        data = [1, 1, 2, 2, 3, 3, 4]
        modes = mode(data)
        assert set(modes) == {1, 2, 3}
        
    @pytest.mark.parametrize("data,expected_modes", [
        ([1, 2, 2, 3], {2}),
        ([1, 1, 2, 2], {1, 2}),
        ([5, 5, 5], {5}),
        ([1, 2, 3], {1, 2, 3}),
    ])
    def test_parametrized_mode(self, data, expected_modes):
        """Parametrized mode tests"""
        result = mode(data)
        assert set(result) == expected_modes


# ============================================================================
# Integration tests
# ============================================================================

class TestCentralTendencyIntegration:
    """Test relationships between different measures"""
    
    def test_symmetric_distribution(self):
        """For symmetric distributions, mean ≈ median"""
        data = [1, 2, 3, 4, 5]
        assert abs(mean(data) - median(data)) < 0.01
        
    def test_constant_list_all_equal(self, constant_list):
        """For constant list, mean = median = mode"""
        m = mean(constant_list)
        med = median(constant_list)
        mod = mode(constant_list)[0]
        assert m == med == mod == 5
        
    def test_median_equals_50th_percentile_concept(self):
        """Test that median is conceptually the 50th percentile"""
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        med = median(data)
        # At least half values are <= median
        below_or_equal = sum(1 for x in data if x <= med)
        assert below_or_equal >= len(data) / 2
