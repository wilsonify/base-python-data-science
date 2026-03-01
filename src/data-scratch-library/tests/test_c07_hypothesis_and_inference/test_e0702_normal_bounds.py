"""
Comprehensive tests for c07_hypothesis_and_inference - normal bounds
"""

import pytest
from dsl.c07_hypothesis_and_inference.e0702_normal_bounds import (
    normal_upper_bound,
    normal_lower_bound,
    normal_two_sided_bounds
)


class TestNormalUpperBound:
    """Test upper bound (percentile) calculations"""

    def test_median_standard_normal(self):
        """Test 50th percentile of standard normal"""
        bound = normal_upper_bound(0.5)
        assert bound == pytest.approx(0.0, abs=0.01)

    def test_75th_percentile(self):
        """Test 75th percentile"""
        bound = normal_upper_bound(0.75)
        assert bound == pytest.approx(0.674, abs=0.01)

    def test_95th_percentile(self):
        """Test 95th percentile"""
        bound = normal_upper_bound(0.95)
        assert bound == pytest.approx(1.645, abs=0.01)

    def test_99th_percentile(self):
        """Test 99th percentile"""
        bound = normal_upper_bound(0.99)
        assert bound == pytest.approx(2.326, abs=0.01)

    def test_custom_distribution(self):
        """Test with custom mu and sigma"""
        bound = normal_upper_bound(0.5, mu=100, sigma=15)
        assert bound == pytest.approx(100.0, abs=0.5)


class TestNormalLowerBound:
    """Test lower bound calculations"""

    def test_median_standard_normal(self):
        """Test 50th percentile from below"""
        bound = normal_lower_bound(0.5)
        assert bound == pytest.approx(0.0, abs=0.01)

    def test_relationship_with_upper_bound(self):
        """Test relationship: lower_bound(p) and upper_bound(p) for standard normal"""
        p = 0.25
        lower = normal_lower_bound(p)
        upper = normal_upper_bound(p)
        # For standard normal, lower_bound(p) gives z where P(Z >= z) = p
        # which means P(Z <= z) = 1-p, so it's the (1-p) percentile
        # upper_bound(p) gives z where P(Z <= z) = p, so it's the p percentile
        # For symmetry: percentile(1-p) = -percentile(p)
        assert lower == pytest.approx(-upper, abs=0.01)

    def test_05_probability(self):
        """Test 5% lower bound"""
        bound = normal_lower_bound(0.05)
        assert bound == pytest.approx(1.645, abs=0.01)

    def test_custom_distribution(self):
        """Test with custom distribution"""
        bound = normal_lower_bound(0.5, mu=50, sigma=5)
        assert bound == pytest.approx(50.0, abs=0.5)


class TestNormalTwoSidedBounds:
    """Test two-sided confidence intervals"""

    def test_95_percent_confidence(self):
        """Test 95% confidence interval for standard normal"""
        lower, upper = normal_two_sided_bounds(0.95)
        assert lower == pytest.approx(-1.96, abs=0.01)
        assert upper == pytest.approx(1.96, abs=0.01)

    def test_90_percent_confidence(self):
        """Test 90% confidence interval"""
        lower, upper = normal_two_sided_bounds(0.90)
        assert lower == pytest.approx(-1.645, abs=0.01)
        assert upper == pytest.approx(1.645, abs=0.01)

    def test_99_percent_confidence(self):
        """Test 99% confidence interval"""
        lower, upper = normal_two_sided_bounds(0.99)
        assert lower == pytest.approx(-2.576, abs=0.01)
        assert upper == pytest.approx(2.576, abs=0.01)

    def test_symmetry(self):
        """Test that bounds are symmetric around mean"""
        lower, upper = normal_two_sided_bounds(0.95, mu=0)
        assert lower == pytest.approx(-upper, abs=0.01)

    def test_custom_distribution(self):
        """Test with custom mu and sigma"""
        mu, sigma = 500, 15.8
        lower, upper = normal_two_sided_bounds(0.95, mu, sigma)
        # Should be approximately mu ± 1.96*sigma
        assert lower == pytest.approx(mu - 1.96 * sigma, abs=1.0)
        assert upper == pytest.approx(mu + 1.96 * sigma, abs=1.0)

    def test_coin_flip_example(self):
        """Test the book's coin flip example: n=1000, p=0.5"""
        import math
        mu = 500
        sigma = math.sqrt(0.5 * 0.5 * 1000)
        lower, upper = normal_two_sided_bounds(0.95, mu, sigma)
        # Book says (469, 531)
        assert lower == pytest.approx(469, abs=2)
        assert upper == pytest.approx(531, abs=2)

    def test_bounds_contain_probability(self):
        """Test that bounds contain specified probability"""
        from dsl.c07_hypothesis_and_inference.e0701_coin_flip import normal_probability_between
        
        mu, sigma = 100, 15
        prob = 0.90
        lower, upper = normal_two_sided_bounds(prob, mu, sigma)
        
        # Calculate actual probability between bounds
        actual_prob = normal_probability_between(lower, upper, mu, sigma)
        assert actual_prob == pytest.approx(prob, abs=0.01)
