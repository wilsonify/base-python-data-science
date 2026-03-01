"""
Comprehensive tests for c07_hypothesis_and_inference - p-values
"""

import pytest
from dsl.c07_hypothesis_and_inference.e0703_pvalues import two_sided_p_value


class TestTwoSidedPValue:
    """Test two-sided p-value calculations"""

    def test_at_mean(self):
        """Test p-value at the mean"""
        p_value = two_sided_p_value(0)
        assert p_value == pytest.approx(1.0, abs=0.01)

    def test_one_sigma_above(self):
        """Test p-value at 1 standard deviation above mean"""
        p_value = two_sided_p_value(1)
        # Two-tailed: 2 * P(Z > 1) = 2 * 0.1587 = 0.3174
        assert p_value == pytest.approx(0.3174, abs=0.01)

    def test_one_sigma_below(self):
        """Test p-value at 1 standard deviation below mean"""
        p_value = two_sided_p_value(-1)
        # Two-tailed: 2 * P(Z < -1) = 2 * 0.1587 = 0.3174
        assert p_value == pytest.approx(0.3174, abs=0.01)

    def test_symmetry(self):
        """Test symmetry: p-value(x) == p-value(-x)"""
        x = 1.5
        p_above = two_sided_p_value(x)
        p_below = two_sided_p_value(-x)
        assert p_above == pytest.approx(p_below, abs=0.001)

    def test_two_sigma(self):
        """Test p-value at 2 standard deviations"""
        p_value = two_sided_p_value(2)
        # Two-tailed: 2 * P(Z > 2) = 2 * 0.0228 = 0.0456
        assert p_value == pytest.approx(0.0456, abs=0.01)

    def test_three_sigma(self):
        """Test p-value at 3 standard deviations"""
        p_value = two_sided_p_value(3)
        # Two-tailed: 2 * P(Z > 3) = 2 * 0.0013 = 0.0026
        assert p_value == pytest.approx(0.0026, abs=0.001)

    def test_custom_distribution_above(self):
        """Test with custom distribution, x above mean"""
        p_value = two_sided_p_value(525, mu=500, sigma=15.8)
        # Should be relatively high p-value (not extreme)
        assert 0.05 < p_value < 0.20

    def test_custom_distribution_below(self):
        """Test with custom distribution, x below mean"""
        p_value = two_sided_p_value(475, mu=500, sigma=15.8)
        # Should be relatively high p-value (not extreme)
        assert 0.05 < p_value < 0.20

    def test_extreme_value(self):
        """Test extreme value gives low p-value"""
        p_value = two_sided_p_value(5)
        # Very extreme value should have very low p-value
        assert p_value < 0.0001

    def test_book_example_524_5(self):
        """Test book's example: 524.5 heads in 1000 flips"""
        import math
        mu = 500
        sigma = math.sqrt(0.5 * 0.5 * 1000)
        p_value = two_sided_p_value(524.5, mu, sigma)
        # Book says upper_p_value = 0.061, so two-sided ≈ 0.122
        assert p_value == pytest.approx(0.122, abs=0.02)

    @pytest.mark.parametrize("x_value,expected_range", [
        (0, (0.95, 1.0)),      # At mean
        (0.5, (0.6, 0.7)),     # Close to mean
        (1.96, (0.04, 0.06)),  # 95% critical value
        (2.576, (0.009, 0.011)), # 99% critical value
    ])
    def test_parametrized_p_values(self, x_value, expected_range):
        """Test various x values with expected p-value ranges"""
        p_value = two_sided_p_value(x_value)
        assert expected_range[0] <= p_value <= expected_range[1]
