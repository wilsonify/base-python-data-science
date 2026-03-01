"""
Comprehensive tests for c07_hypothesis_and_inference - Bayesian inference
"""

import pytest
import math
from dsl.c07_hypothesis_and_inference.e0706_bayesian_inference import (
    normalizer,
    beta_pdf
)


class TestNormalizer:
    """Test beta distribution normalizer (beta function)"""

    def test_beta_1_1(self):
        """Test Beta(1,1) - uniform distribution"""
        norm = normalizer(1, 1)
        # B(1,1) = Gamma(1) * Gamma(1) / Gamma(2) = 1 * 1 / 1 = 1
        assert norm == pytest.approx(1.0)

    def test_beta_2_2(self):
        """Test Beta(2,2)"""
        norm = normalizer(2, 2)
        # B(2,2) = Gamma(2) * Gamma(2) / Gamma(4) = 1 * 1 / 6 = 1/6
        assert norm == pytest.approx(1/6, abs=0.001)

    def test_beta_5_1(self):
        """Test Beta(5,1)"""
        norm = normalizer(5, 1)
        # B(5,1) = Gamma(5) * Gamma(1) / Gamma(6) = 24 * 1 / 120 = 1/5
        assert norm == pytest.approx(1/5, abs=0.001)

    def test_beta_1_5(self):
        """Test Beta(1,5)"""
        norm = normalizer(1, 5)
        # B(1,5) = Gamma(1) * Gamma(5) / Gamma(6) = 1 * 24 / 120 = 1/5
        assert norm == pytest.approx(1/5, abs=0.001)

    def test_symmetry(self):
        """Test B(a,b) = B(b,a)"""
        assert normalizer(3, 7) == pytest.approx(normalizer(7, 3))

    def test_beta_10_10(self):
        """Test Beta(10,10) with larger parameters"""
        norm = normalizer(10, 10)
        # Should be a small positive number
        assert norm > 0
        assert norm < 1


class TestBetaPDF:
    """Test beta probability density function"""

    def test_uniform_at_half(self):
        """Test Beta(1,1) at x=0.5 - uniform distribution"""
        pdf = beta_pdf(0.5, 1, 1)
        # Uniform on [0,1] has pdf = 1
        assert pdf == pytest.approx(1.0, abs=0.01)

    def test_uniform_at_endpoints(self):
        """Test Beta(1,1) at endpoints"""
        pdf_0 = beta_pdf(0.0, 1, 1)
        pdf_1 = beta_pdf(1.0, 1, 1)
        # At x^0 * (1-x)^0 = 1, should equal 1
        assert pdf_0 == pytest.approx(1.0, abs=0.01)
        assert pdf_1 == pytest.approx(1.0, abs=0.01)

    def test_outside_bounds_below(self):
        """Test outside [0,1] returns 0"""
        pdf = beta_pdf(-0.1, 2, 2)
        assert pdf == 0.0

    def test_outside_bounds_above(self):
        """Test outside [0,1] returns 0"""
        pdf = beta_pdf(1.1, 2, 2)
        assert pdf == 0.0

    def test_beta_2_2_at_half(self):
        """Test Beta(2,2) at x=0.5 - symmetric"""
        pdf = beta_pdf(0.5, 2, 2)
        # Beta(2,2) is symmetric, peaked at 0.5
        # pdf(0.5) = 0.5^1 * 0.5^1 / B(2,2) = 0.25 / (1/6) = 1.5
        assert pdf == pytest.approx(1.5, abs=0.1)

    def test_beta_2_5_skewed(self):
        """Test Beta(2,5) - skewed towards 0"""
        pdf_low = beta_pdf(0.2, 2, 5)
        pdf_high = beta_pdf(0.8, 2, 5)
        # Beta(2,5) is skewed towards 0, so pdf(0.2) > pdf(0.8)
        assert pdf_low > pdf_high

    def test_beta_5_2_skewed(self):
        """Test Beta(5,2) - skewed towards 1"""
        pdf_low = beta_pdf(0.2, 5, 2)
        pdf_high = beta_pdf(0.8, 5, 2)
        # Beta(5,2) is skewed towards 1, so pdf(0.8) > pdf(0.2)
        assert pdf_high > pdf_low

    def test_symmetry(self):
        """Test symmetry: Beta(a,b)(x) = Beta(b,a)(1-x)"""
        x = 0.3
        pdf1 = beta_pdf(x, 3, 7)
        pdf2 = beta_pdf(1-x, 7, 3)
        assert pdf1 == pytest.approx(pdf2, abs=0.001)

    def test_integration_approximation(self):
        """Test that integral approximates 1"""
        # Numerical integration using trapezoidal rule
        alpha, beta = 3, 5
        n_points = 1000
        dx = 1.0 / n_points
        integral = 0.0
        
        for i in range(n_points):
            x = (i + 0.5) * dx
            integral += beta_pdf(x, alpha, beta) * dx
        
        # Should integrate to approximately 1
        assert integral == pytest.approx(1.0, abs=0.01)

    def test_beta_half_half(self):
        """Test Beta(0.5, 0.5) - U-shaped distribution"""
        pdf_middle = beta_pdf(0.5, 0.5, 0.5)
        pdf_near_0 = beta_pdf(0.1, 0.5, 0.5)
        pdf_near_1 = beta_pdf(0.9, 0.5, 0.5)
        
        # Beta(0.5, 0.5) is U-shaped, higher at endpoints
        assert pdf_near_0 > pdf_middle
        assert pdf_near_1 > pdf_middle

    @pytest.mark.parametrize("alpha,beta_param,x,expected_nonzero", [
        (1, 1, 0.5, True),    # Uniform
        (2, 2, 0.5, True),    # Symmetric
        (1, 1, -0.1, False),  # Out of bounds
        (1, 1, 1.5, False),   # Out of bounds
        (5, 1, 0.9, True),    # Skewed right
        (1, 5, 0.1, True),    # Skewed left
    ])
    def test_parametrized_pdf(self, alpha, beta_param, x, expected_nonzero):
        """Test various parameter combinations"""
        pdf = beta_pdf(x, alpha, beta_param)
        if expected_nonzero:
            assert pdf > 0
        else:
            assert pdf == 0
