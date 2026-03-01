"""
Comprehensive tests for c07_hypothesis_and_inference - coin flip probabilities
"""

import pytest
from dsl.c07_hypothesis_and_inference.e0701_coin_flip import (
    normal_approximation_to_binomial,
    normal_probability_above,
    normal_probability_below,
    normal_probability_between,
    normal_probability_outside
)


class TestNormalApproximationToBinomial:
    """Test binomial approximation with normal distribution"""

    def test_fair_coin(self):
        """Test fair coin with n=1000"""
        mu, sigma = normal_approximation_to_binomial(1000, 0.5)
        assert mu == pytest.approx(500.0)
        assert sigma == pytest.approx(15.811, abs=0.001)

    def test_biased_coin_high_p(self):
        """Test biased coin with p=0.7"""
        mu, sigma = normal_approximation_to_binomial(100, 0.7)
        assert mu == pytest.approx(70.0)
        assert sigma == pytest.approx(4.583, abs=0.001)

    def test_biased_coin_low_p(self):
        """Test biased coin with p=0.3"""
        mu, sigma = normal_approximation_to_binomial(100, 0.3)
        assert mu == pytest.approx(30.0)
        assert sigma == pytest.approx(4.583, abs=0.001)

    def test_single_trial(self):
        """Test single trial"""
        mu, sigma = normal_approximation_to_binomial(1, 0.5)
        assert mu == pytest.approx(0.5)
        assert sigma == pytest.approx(0.5)

    def test_extreme_probabilities(self):
        """Test extreme p values"""
        mu, sigma = normal_approximation_to_binomial(100, 0.99)
        assert mu == pytest.approx(99.0)
        assert sigma == pytest.approx(0.995, abs=0.01)


class TestNormalProbabilityAbove:
    """Test probability above threshold"""

    def test_standard_normal_at_zero(self):
        """Test standard normal at mean"""
        prob = normal_probability_above(0)
        assert prob == pytest.approx(0.5, abs=0.01)

    def test_standard_normal_at_one_sigma(self):
        """Test standard normal at 1 standard deviation"""
        prob = normal_probability_above(1)
        assert prob == pytest.approx(0.1587, abs=0.01)

    def test_standard_normal_at_two_sigma(self):
        """Test standard normal at 2 standard deviations"""
        prob = normal_probability_above(2)
        assert prob == pytest.approx(0.0228, abs=0.01)

    def test_custom_distribution(self):
        """Test custom mu and sigma"""
        prob = normal_probability_above(100, mu=100, sigma=10)
        assert prob == pytest.approx(0.5, abs=0.01)


class TestNormalProbabilityBelow:
    """Test probability below threshold"""

    def test_standard_normal_at_zero(self):
        """Test standard normal at mean"""
        prob = normal_probability_below(0)
        assert prob == pytest.approx(0.5, abs=0.01)

    def test_standard_normal_at_negative_one(self):
        """Test standard normal at -1"""
        prob = normal_probability_below(-1)
        assert prob == pytest.approx(0.1587, abs=0.01)

    def test_complementary_property(self):
        """Test that above + below = 1"""
        x = 1.5
        above = normal_probability_above(x)
        below = normal_probability_below(x)
        assert above + below == pytest.approx(1.0)


class TestNormalProbabilityBetween:
    """Test probability in interval"""

    def test_symmetric_interval(self):
        """Test symmetric interval around mean"""
        prob = normal_probability_between(-1, 1)
        assert prob == pytest.approx(0.6827, abs=0.01)  # 68% rule

    def test_two_sigma_interval(self):
        """Test two sigma interval"""
        prob = normal_probability_between(-2, 2)
        assert prob == pytest.approx(0.9545, abs=0.01)  # 95% rule

    def test_three_sigma_interval(self):
        """Test three sigma interval"""
        prob = normal_probability_between(-3, 3)
        assert prob == pytest.approx(0.9973, abs=0.01)  # 99.7% rule

    def test_one_sided_interval(self):
        """Test one-sided interval"""
        prob = normal_probability_between(0, 1)
        assert prob == pytest.approx(0.3413, abs=0.01)

    def test_custom_distribution_interval(self):
        """Test custom distribution"""
        prob = normal_probability_between(90, 110, mu=100, sigma=10)
        assert prob == pytest.approx(0.6827, abs=0.01)


class TestNormalProbabilityOutside:
    """Test probability outside interval"""

    def test_outside_one_sigma(self):
        """Test probability outside ±1 sigma"""
        prob = normal_probability_outside(-1, 1)
        assert prob == pytest.approx(0.3173, abs=0.01)

    def test_outside_two_sigma(self):
        """Test probability outside ±2 sigma"""
        prob = normal_probability_outside(-2, 2)
        assert prob == pytest.approx(0.0455, abs=0.01)

    def test_complementary_property(self):
        """Test that inside + outside = 1"""
        lo, hi = -1.5, 2.5
        inside = normal_probability_between(lo, hi)
        outside = normal_probability_outside(lo, hi)
        assert inside + outside == pytest.approx(1.0)

    def test_custom_distribution(self):
        """Test custom distribution"""
        prob = normal_probability_outside(90, 110, mu=100, sigma=10)
        assert prob == pytest.approx(0.3173, abs=0.01)
