"""
Comprehensive tests for c07_hypothesis_and_inference - A/B testing
"""

import pytest
from dsl.c07_hypothesis_and_inference.e0705_a_b import (
    estimated_parameters,
    a_b_test_statistic
)


class TestEstimatedParameters:
    """Test parameter estimation for proportions"""

    def test_fifty_percent(self):
        """Test 50% proportion"""
        p, sigma = estimated_parameters(1000, 500)
        assert p == pytest.approx(0.5)
        assert sigma == pytest.approx(0.0158, abs=0.001)

    def test_twenty_percent(self):
        """Test 20% proportion"""
        p, sigma = estimated_parameters(1000, 200)
        assert p == pytest.approx(0.2)
        assert sigma == pytest.approx(0.0126, abs=0.001)

    def test_small_sample(self):
        """Test small sample size"""
        p, sigma = estimated_parameters(100, 25)
        assert p == pytest.approx(0.25)
        # sigma = sqrt(0.25 * 0.75 / 100) = sqrt(0.001875)
        assert sigma == pytest.approx(0.0433, abs=0.001)

    def test_extreme_proportion_high(self):
        """Test extreme high proportion"""
        p, sigma = estimated_parameters(100, 95)
        assert p == pytest.approx(0.95)
        assert sigma == pytest.approx(0.0218, abs=0.001)

    def test_extreme_proportion_low(self):
        """Test extreme low proportion"""
        p, sigma = estimated_parameters(100, 5)
        assert p == pytest.approx(0.05)
        assert sigma == pytest.approx(0.0218, abs=0.001)

    def test_all_successes(self):
        """Test 100% success rate"""
        p, sigma = estimated_parameters(100, 100)
        assert p == pytest.approx(1.0)
        assert sigma == pytest.approx(0.0)

    def test_no_successes(self):
        """Test 0% success rate"""
        p, sigma = estimated_parameters(100, 0)
        assert p == pytest.approx(0.0)
        assert sigma == pytest.approx(0.0)


class TestABTestStatistic:
    """Test A/B test z-statistic calculations"""

    def test_identical_groups(self):
        """Test identical groups should have z ≈ 0"""
        z = a_b_test_statistic(1000, 200, 1000, 200)
        assert z == pytest.approx(0.0, abs=0.01)

    def test_book_example_1(self):
        """Test book's example: 200 vs 180"""
        z = a_b_test_statistic(1000, 200, 1000, 180)
        # Book says z = -1.14
        assert z == pytest.approx(-1.14, abs=0.02)

    def test_book_example_2(self):
        """Test book's example: 200 vs 150"""
        z = a_b_test_statistic(1000, 200, 1000, 150)
        # Book says z = -2.94
        assert z == pytest.approx(-2.94, abs=0.02)

    def test_significant_difference(self):
        """Test significant difference (|z| > 1.96)"""
        z = a_b_test_statistic(1000, 300, 1000, 200)
        # Large difference should have |z| > 1.96
        assert abs(z) > 1.96

    def test_non_significant_difference(self):
        """Test non-significant difference (|z| < 1.96)"""
        z = a_b_test_statistic(1000, 205, 1000, 195)
        # Small difference should have |z| < 1.96
        assert abs(z) < 1.96

    def test_b_greater_than_a(self):
        """Test when B has higher rate than A"""
        z = a_b_test_statistic(1000, 150, 1000, 200)
        # B > A should give positive z
        assert z > 0

    def test_a_greater_than_b(self):
        """Test when A has higher rate than B"""
        z = a_b_test_statistic(1000, 250, 1000, 200)
        # A > B should give negative z
        assert z < 0

    def test_small_samples(self):
        """Test with smaller sample sizes"""
        z = a_b_test_statistic(100, 30, 100, 20)
        # Should still compute reasonably
        assert -5 < z < 5

    def test_large_samples(self):
        """Test with larger sample sizes"""
        z = a_b_test_statistic(10000, 2100, 10000, 1900)
        # Larger samples make differences more significant
        assert abs(z) > 2

    @pytest.mark.parametrize("n_a,a_clicks,n_b,b_clicks,significant", [
        (1000, 200, 1000, 200, False),  # Same rates
        (1000, 200, 1000, 220, False),  # Small difference
        (1000, 200, 1000, 250, True),   # Large difference
        (1000, 150, 1000, 200, True),   # Large difference
        (100, 10, 100, 15, False),      # Small sample, small diff
    ])
    def test_parametrized_significance(self, n_a, a_clicks, n_b, b_clicks, significant):
        """Test various scenarios for significance"""
        z = a_b_test_statistic(n_a, a_clicks, n_b, b_clicks)
        if significant:
            assert abs(z) > 1.96, f"Expected significant z-score, got {z}"
        else:
            assert abs(z) <= 2.0, f"Expected non-significant z-score, got {z}"
