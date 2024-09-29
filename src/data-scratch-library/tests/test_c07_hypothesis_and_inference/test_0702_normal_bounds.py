import math

import pytest

from dsl.c07_hypothesis_and_inference.e0701_coin_flip import normal_approximation_to_binomial
from dsl.c07_hypothesis_and_inference.e0702_normal_bounds import (
    normal_upper_bound,
    normal_lower_bound,
    normal_two_sided_bounds,
)


def test_normal_upper_bound():
    """Test that normal_upper_bound returns the correct z-value for a given probability."""
    # For a standard normal distribution (mu=0, sigma=1)
    # P(Z <= z) = 0.95 corresponds to z = ~1.645
    assert math.isclose(normal_upper_bound(0.95), 1.645, rel_tol=1e-3)

    # P(Z <= z) = 0.975 corresponds to z = ~1.96
    assert math.isclose(normal_upper_bound(0.975), 1.96, rel_tol=1e-3)


def test_normal_lower_bound():
    """Test that normal_lower_bound returns the correct z-value for a given probability."""
    # For a standard normal distribution (mu=0, sigma=1)
    # P(Z >= z) = 0.05 corresponds to z = ~1.645 (lower bound)
    assert math.isclose(normal_lower_bound(0.95), -1.645, rel_tol=1e-3)

    # P(Z >= z) = 0.025 corresponds to z = ~1.96
    assert math.isclose(normal_lower_bound(0.975), -1.96, rel_tol=1e-3)


def test_normal_two_sided_bounds():
    """Test that normal_two_sided_bounds returns the correct two-sided symmetric bounds."""
    # For 95% probability, the bounds should be around (-1.96, 1.96) for standard normal
    lower_bound, upper_bound = normal_two_sided_bounds(0.95)
    assert math.isclose(lower_bound, -1.96, rel_tol=1e-3)
    assert math.isclose(upper_bound, 1.96, rel_tol=1e-3)

    # For 99% probability, the bounds should be around (-2.58, 2.58)
    lower_bound, upper_bound = normal_two_sided_bounds(0.99)

    assert math.isclose(lower_bound, -2.58, rel_tol=0.1)
    assert math.isclose(upper_bound, 2.58, rel_tol=0.1)


def test_normal_two_sided_bounds_binomial():
    """Test normal_two_sided_bounds for a binomial approximation case."""
    # Approximation to binomial for n=1000, p=0.5
    mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
    lower_bound, upper_bound = normal_two_sided_bounds(0.95, mu_0, sigma_0)

    # We expect the bounds to be around 469 and 531 for a binomial approximation
    assert math.isclose(lower_bound, 469, rel_tol=1e-2)
    assert math.isclose(upper_bound, 531, rel_tol=1e-2)


if __name__ == "__main__":
    pytest.main()
