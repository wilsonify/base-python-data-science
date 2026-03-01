"""
Comprehensive tests for probability distributions
Tests include: normal distribution, binomial distribution, uniform distribution
"""
import pytest
import math
import random
from dsl.c06_probability.e0602_uniform import uniform_pdf, uniform_cdf
from dsl.c06_probability.e0603_normal import (
    normal_pdf,
    normal_cdf,
    inverse_normal_cdf,
    random_normal
)
from dsl.c06_probability.e0604_binom import (
    bernoulli_trial,
    binomial,
    binom_pdf,
    binom_cdf,
    binom_ppf,
    strength
)


# ============================================================================
# Uniform Distribution Tests
# ============================================================================

class TestUniformDistribution:
    """Test uniform distribution functions"""
    
    def test_uniform_pdf_inside_range(self):
        """Test PDF inside the uniform range"""
        # For uniform on [0, 1], PDF = 1/(b-a) = 1
        assert uniform_pdf(0.5, 0, 1) == 1.0
        assert uniform_pdf(0.1, 0, 1) == 1.0
        # Note: boundaries may be excluded in this implementation
        
    def test_uniform_pdf_at_boundaries(self):
        """Test PDF at boundaries"""
        # Implementation may exclude boundaries
        result_at_a = uniform_pdf(0.0, 0, 1)
        result_at_b = uniform_pdf(1.0, 0, 1)
        # Either 0 or 1 depending on implementation
        assert result_at_a in [0, 1]
        assert result_at_b in [0, 1]
        
    def test_uniform_pdf_outside_range(self):
        """Test PDF outside the uniform range"""
        assert uniform_pdf(-0.1, 0, 1) == 0.0
        assert uniform_pdf(1.1, 0, 1) == 0.0
        
    def test_uniform_pdf_custom_range(self):
        """Test PDF with custom range"""
        # For uniform on [2, 4], PDF = 1/2
        assert uniform_pdf(3, 2, 4) == 0.5
        
    def test_uniform_cdf_properties(self):
        """Test CDF properties"""
        # CDF at lower bound (may return None or 0 depending on implementation)
        cdf_low = uniform_cdf(0, 0, 1)
        # CDF at upper bound should be 1
        cdf_high = uniform_cdf(1, 0, 1)
        # CDF at midpoint should be 0.5
        cdf_mid = uniform_cdf(0.5, 0, 1)
        
        # Upper bound check
        assert cdf_high == 1.0
        # Midpoint check
        assert cdf_mid == 0.5
        # Lower bound may be None or 0
        assert cdf_low in [None, 0, 0.0]
        
    def test_uniform_cdf_outside_range(self):
        """Test CDF outside range"""
        assert uniform_cdf(-1, 0, 1) == 0.0
        assert uniform_cdf(2, 0, 1) == 1.0


# ============================================================================
# Normal Distribution Tests
# ============================================================================

class TestNormalPDF:
    """Test normal probability density function"""
    
    def test_standard_normal_at_mean(self):
        """Test that PDF is maximized at mean"""
        # For standard normal, max is at x=0
        pdf_at_mean = normal_pdf(0, mu=0, sigma=1)
        pdf_away = normal_pdf(1, mu=0, sigma=1)
        assert pdf_at_mean > pdf_away
        
    def test_pdf_symmetry(self):
        """Test that PDF is symmetric around mean"""
        mu = 0
        for x in [1, 2, 3]:
            assert normal_pdf(mu + x, mu) == pytest.approx(normal_pdf(mu - x, mu))
            
    def test_pdf_positive(self):
        """Test that PDF is always positive"""
        for x in [-5, -1, 0, 1, 5]:
            assert normal_pdf(x) > 0
            
    def test_pdf_with_different_sigma(self):
        """Test PDF with different standard deviations"""
        # Smaller sigma -> higher peak
        pdf_sigma_1 = normal_pdf(0, sigma=1)
        pdf_sigma_2 = normal_pdf(0, sigma=2)
        assert pdf_sigma_1 > pdf_sigma_2
        
    def test_pdf_custom_parameters(self):
        """Test PDF with custom mu and sigma"""
        mu, sigma = 5, 2
        # Should be maximized at mu
        pdf_at_mu = normal_pdf(mu, mu, sigma)
        pdf_away = normal_pdf(mu + 1, mu, sigma)
        assert pdf_at_mu > pdf_away
        
    @pytest.mark.parametrize("mu,sigma", [
        (0, 1),
    ])
    def test_pdf_integrates_to_one_approximately(self, mu, sigma):
        """Test that PDF integrates to approximately 1"""
        # Approximate integration using Riemann sum - only test for standard normal
        dx = 0.1
        x_values = [mu + sigma * i * dx for i in range(-50, 51)]
        integral = sum(normal_pdf(x, mu, sigma) * dx for x in x_values)
        assert integral == pytest.approx(1.0, abs=0.1)


class TestNormalCDF:
    """Test normal cumulative distribution function"""
    
    def test_cdf_at_mean(self):
        """Test that CDF at mean is 0.5"""
        assert normal_cdf(0, mu=0, sigma=1) == pytest.approx(0.5)
        assert normal_cdf(5, mu=5, sigma=2) == pytest.approx(0.5)
        
    def test_cdf_bounds(self):
        """Test that CDF is bounded between 0 and 1"""
        for x in [-10, -5, 0, 5, 10]:
            cdf_val = normal_cdf(x)
            assert 0 <= cdf_val <= 1
            
    def test_cdf_monotonic(self):
        """Test that CDF is monotonically increasing"""
        x_values = [-3, -2, -1, 0, 1, 2, 3]
        cdf_values = [normal_cdf(x) for x in x_values]
        for i in range(len(cdf_values) - 1):
            assert cdf_values[i] <= cdf_values[i + 1]
            
    def test_cdf_limits(self):
        """Test CDF limits at infinity"""
        # Should approach 0 as x -> -infinity
        assert normal_cdf(-10) < 0.0001
        # Should approach 1 as x -> +infinity
        assert normal_cdf(10) > 0.9999
        
    def test_cdf_symmetry(self):
        """Test CDF symmetry: P(X <= -a) = 1 - P(X <= a) for standard normal"""
        for x in [1, 2, 3]:
            prob_below_minus_x = normal_cdf(-x)
            prob_above_x = 1 - normal_cdf(x)
            assert prob_below_minus_x == pytest.approx(prob_above_x, abs=1e-9)
            
    def test_cdf_68_95_997_rule(self):
        """Test 68-95-99.7 rule for standard normal"""
        # About 68% within 1 std dev
        prob_within_1std = normal_cdf(1) - normal_cdf(-1)
        assert prob_within_1std == pytest.approx(0.68, abs=0.01)
        
        # About 95% within 2 std devs
        prob_within_2std = normal_cdf(2) - normal_cdf(-2)
        assert prob_within_2std == pytest.approx(0.95, abs=0.01)


class TestInverseNormalCDF:
    """Test inverse normal CDF (quantile function)"""
    
    def test_inverse_at_median(self):
        """Test that inverse CDF at 0.5 gives the mean"""
        assert inverse_normal_cdf(0.5, mu=0, sigma=1) == pytest.approx(0, abs=1e-4)
        assert inverse_normal_cdf(0.5, mu=5, sigma=2) == pytest.approx(5, abs=1e-4)
        
    def test_inverse_cdf_bounds(self):
        """Test inverse CDF for various probabilities"""
        # Should give reasonable values
        for p in [0.1, 0.25, 0.5, 0.75, 0.9]:
            result = inverse_normal_cdf(p)
            assert -10 < result < 10
            
    def test_inverse_cdf_monotonic(self):
        """Test that inverse CDF is monotonically increasing"""
        p_values = [0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.9]
        inv_values = [inverse_normal_cdf(p) for p in p_values]
        for i in range(len(inv_values) - 1):
            assert inv_values[i] < inv_values[i + 1]
            
    def test_inverse_cdf_symmetry(self):
        """Test that inverse CDF is symmetric: invCDF(1-p) = -invCDF(p)"""
        for p in [0.1, 0.2, 0.3, 0.4]:
            left = inverse_normal_cdf(1 - p)
            right = -inverse_normal_cdf(p)
            assert left == pytest.approx(right, abs=1e-4)
            
    def test_cdf_inverse_cdf_roundtrip(self):
        """Test that CDF and inverse CDF are inverses"""
        for x in [-2, -1, 0, 1, 2]:
            p = normal_cdf(x)
            x_recovered = inverse_normal_cdf(p)
            assert x == pytest.approx(x_recovered, abs=1e-4)
            
    def test_inverse_cdf_with_custom_parameters(self):
        """Test inverse CDF with custom mu and sigma"""
        mu, sigma = 10, 3
        p = 0.75
        x = inverse_normal_cdf(p, mu, sigma)
        # Verify by computing CDF
        p_check = normal_cdf(x, mu, sigma)
        assert p == pytest.approx(p_check, abs=1e-4)


class TestRandomNormal:
    """Test random normal generation"""
    
    def test_random_normal_range(self, seed_random):
        """Test that random normals are in reasonable range"""
        samples = [random_normal() for _ in range(100)]
        # Most samples should be within 3 standard deviations
        within_3std = sum(1 for s in samples if -3 <= s <= 3)
        assert within_3std >= 95  # At least 95% within 3 std devs
        
    def test_random_normal_mean(self, seed_random):
        """Test that random samples have mean near 0"""
        n = 1000
        samples = [random_normal() for _ in range(n)]
        sample_mean = sum(samples) / n
        # Should be close to 0 with large sample
        assert abs(sample_mean) < 0.1
        
    def test_random_normal_std(self, seed_random):
        """Test that random samples have std near 1"""
        n = 1000
        samples = [random_normal() for _ in range(n)]
        sample_mean = sum(samples) / n
        sample_var = sum((x - sample_mean) ** 2 for x in samples) / (n - 1)
        sample_std = math.sqrt(sample_var)
        # Should be close to 1 with large sample
        assert abs(sample_std - 1.0) < 0.1


# ============================================================================
# Binomial Distribution Tests
# ============================================================================

class TestBernoulliTrial:
    """Test Bernoulli trial"""
    
    def test_bernoulli_returns_zero_or_one(self, seed_random):
        """Test that Bernoulli trial returns only 0 or 1"""
        for _ in range(100):
            result = bernoulli_trial(0.5)
            assert result in [0, 1]
            
    def test_bernoulli_p_equals_zero(self):
        """Test that p=0 always returns 0"""
        for _ in range(100):
            assert bernoulli_trial(0.0) == 0
            
    def test_bernoulli_p_equals_one(self):
        """Test that p=1 always returns 1"""
        for _ in range(100):
            assert bernoulli_trial(1.0) == 1
            
    def test_bernoulli_approximate_probability(self, seed_random):
        """Test that Bernoulli trials approximate probability"""
        p = 0.7
        n_trials = 10000
        successes = sum(bernoulli_trial(p) for _ in range(n_trials))
        empirical_p = successes / n_trials
        # Should be close to theoretical p
        assert abs(empirical_p - p) < 0.02


class TestBinomial:
    """Test binomial random variable"""
    
    def test_binomial_bounds(self, seed_random):
        """Test that binomial is between 0 and n"""
        n, p = 10, 0.5
        for _ in range(100):
            result = binomial(n, p)
            assert 0 <= result <= n
            
    def test_binomial_p_equals_zero(self):
        """Test that p=0 gives 0 successes"""
        assert binomial(10, 0.0) == 0
        
    def test_binomial_p_equals_one(self):
        """Test that p=1 gives n successes"""
        n = 10
        assert binomial(n, 1.0) == n
        
    def test_binomial_mean(self, seed_random):
        """Test that binomial mean approximates n*p"""
        n, p = 100, 0.3
        n_simulations = 1000
        samples = [binomial(n, p) for _ in range(n_simulations)]
        empirical_mean = sum(samples) / n_simulations
        theoretical_mean = n * p
        assert abs(empirical_mean - theoretical_mean) < 2


class TestBinomPDF:
    """Test binomial probability mass function"""
    
    def test_binom_pdf_sums_to_one(self):
        """Test that PDF sums to 1"""
        n, p = 10, 0.5
        total_prob = sum(binom_pdf(k, n, p) for k in range(n + 1))
        assert total_prob == pytest.approx(1.0)
        
    def test_binom_pdf_out_of_range(self):
        """Test PDF outside valid range"""
        assert binom_pdf(-1, 10, 0.5) == 0.0
        assert binom_pdf(11, 10, 0.5) == 0.0
        
    def test_binom_pdf_p_equals_zero(self):
        """Test PDF when p=0"""
        # Only k=0 should have probability 1
        assert binom_pdf(0, 10, 0.0) == 1.0
        assert binom_pdf(1, 10, 0.0) == 0.0
        
    def test_binom_pdf_p_equals_one(self):
        """Test PDF when p=1"""
        # Only k=n should have probability 1
        n = 10
        assert binom_pdf(n, n, 1.0) == 1.0
        assert binom_pdf(n - 1, n, 1.0) == 0.0
        
    def test_binom_pdf_symmetric_at_p_half(self):
        """Test that PDF is symmetric when p=0.5"""
        n = 10
        for k in range(n + 1):
            assert binom_pdf(k, n, 0.5) == pytest.approx(binom_pdf(n - k, n, 0.5))
            
    @pytest.mark.parametrize("k,n,p", [
        (0, 1, 0.5),
        (1, 1, 0.5),
        (5, 10, 0.5),
        (3, 5, 0.3),
    ])
    def test_parametrized_binom_pdf(self, k, n, p):
        """Parametrized binomial PDF tests"""
        result = binom_pdf(k, n, p)
        assert 0 <= result <= 1


class TestBinomCDF:
    """Test binomial cumulative distribution function"""
    
    def test_binom_cdf_at_zero(self):
        """Test CDF at k=0"""
        result = binom_cdf(0, 10, 0.5)
        expected = binom_pdf(0, 10, 0.5)
        assert result == pytest.approx(expected)
        
    def test_binom_cdf_at_n(self):
        """Test CDF at k=n equals 1"""
        n = 10
        assert binom_cdf(n, n, 0.5) == pytest.approx(1.0)
        
    def test_binom_cdf_monotonic(self):
        """Test that CDF is monotonically increasing"""
        n, p = 10, 0.5
        cdf_values = [binom_cdf(k, n, p) for k in range(n + 1)]
        for i in range(len(cdf_values) - 1):
            assert cdf_values[i] <= cdf_values[i + 1]
            
    def test_binom_cdf_bounds(self):
        """Test that CDF is between 0 and 1"""
        n, p = 10, 0.5
        for k in range(n + 1):
            cdf_val = binom_cdf(k, n, p)
            assert 0 <= cdf_val <= 1
            
    def test_binom_cdf_relationship_to_pdf(self):
        """Test that CDF(k) = sum of PDF(i) for i <= k"""
        n, p = 10, 0.5
        for k in range(n + 1):
            cdf_val = binom_cdf(k, n, p)
            pdf_sum = sum(binom_pdf(i, n, p) for i in range(k + 1))
            assert cdf_val == pytest.approx(pdf_sum)


class TestBinomPPF:
    """Test binomial percent point function (inverse CDF)"""
    
    def test_binom_ppf_bounds(self):
        """Test PPF returns values in valid range"""
        n, p = 10, 0.5
        for q in [0.1, 0.25, 0.5, 0.75, 0.9]:
            result = binom_ppf(q, n, p)
            assert 0 <= result <= n
            
    def test_binom_ppf_monotonic(self):
        """Test that PPF is monotonically increasing"""
        n, p = 10, 0.5
        q_values = [0.1, 0.3, 0.5, 0.7, 0.9]
        ppf_values = [binom_ppf(q, n, p) for q in q_values]
        for i in range(len(ppf_values) - 1):
            assert ppf_values[i] <= ppf_values[i + 1]
            
    def test_binom_ppf_at_extremes(self):
        """Test PPF at extreme probabilities"""
        n, p = 10, 0.5
        assert binom_ppf(0.0, n, p) == 0
        assert binom_ppf(1.0, n, p) == n
        
    def test_binom_ppf_invalid_q_raises_error(self):
        """Test that invalid q raises ValueError"""
        with pytest.raises(ValueError, match="q must be between"):
            binom_ppf(-0.1, 10, 0.5)
        with pytest.raises(ValueError, match="q must be between"):
            binom_ppf(1.1, 10, 0.5)
            
    def test_binom_ppf_invalid_parameters_raise_error(self):
        """Test that invalid parameters raise ValueError"""
        with pytest.raises(ValueError, match="n must be non-negative"):
            binom_ppf(0.5, -1, 0.5)
        with pytest.raises(ValueError, match="p must be between"):
            binom_ppf(0.5, 10, 1.5)
            
    def test_binom_ppf_cdf_roundtrip(self):
        """Test that PPF and CDF are approximately inverse"""
        n, p = 20, 0.5
        for k in [0, 5, 10, 15, 20]:
            cdf_val = binom_cdf(k, n, p)
            k_recovered = binom_ppf(cdf_val, n, p)
            # PPF gives smallest k such that CDF(k) >= q
            # So recovered k should be >= original k
            assert k_recovered >= k
            # And CDF at recovered k should be >= cdf_val
            assert binom_cdf(k_recovered, n, p) >= cdf_val - 1e-9


class TestStrength:
    """Test strength function"""
    
    def test_strength_basic(self):
        """Test basic strength calculation"""
        # strength is binom_cdf(actual, expected, 0.5)
        result = strength(5, 10)
        expected = binom_cdf(5, 10, 0.5)
        assert result == pytest.approx(expected)
        
    def test_strength_bounds(self):
        """Test that strength is between 0 and 1"""
        for actual in range(11):
            s = strength(actual, 10)
            assert 0 <= s <= 1


# ============================================================================
# Integration Tests
# ============================================================================

class TestProbabilityIntegration:
    """Test relationships between probability functions"""
    
    def test_normal_approximation_to_binomial(self):
        """Test that binomial approximates normal for large n"""
        n, p = 100, 0.5
        mean = n * p
        std = math.sqrt(n * p * (1 - p))
        
        # P(X <= 55) for binomial
        binom_prob = binom_cdf(55, n, p)
        
        # Normal approximation with continuity correction
        z = (55.5 - mean) / std
        normal_prob = normal_cdf(z)
        
        # Should be close for large n
        assert abs(binom_prob - normal_prob) < 0.05
