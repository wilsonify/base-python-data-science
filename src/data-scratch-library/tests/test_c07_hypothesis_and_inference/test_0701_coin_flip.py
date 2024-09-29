import math

from dsl.c07_hypothesis_and_inference.e0701_coin_flip import (
    normal_approximation_to_binomial,
    normal_probability_below,
    normal_probability_above,
    normal_probability_between,
    normal_probability_outside,
)


def test_normal_approximation_to_binomial():
    """Test that the normal approximation to binomial gives correct mu and sigma."""
    mu, sigma = normal_approximation_to_binomial(1000, 0.5)
    assert mu == 500
    assert math.isclose(sigma, 15.81, rel_tol=1e-2)


def test_normal_probability_below():
    """Test the normal_probability_below function."""
    # For a standard normal distribution (mu=0, sigma=1), 50% of values are below 0
    assert math.isclose(normal_probability_below(0), 0.5, rel_tol=1e-5)
    # Approx 84.13% of values are below 1 for standard normal distribution
    assert math.isclose(normal_probability_below(1), 0.8413, rel_tol=1e-4)


def test_normal_probability_above():
    """Test the normal_probability_above function."""
    # For a standard normal distribution, 50% of values are above 0
    assert math.isclose(normal_probability_above(0), 0.5, rel_tol=1e-5)
    # Approx 15.87% of values are above 1 for standard normal distribution
    assert math.isclose(normal_probability_above(1), 0.1587, rel_tol=0.01)


def test_normal_probability_between():
    """Test the normal_probability_between function."""
    # In a standard normal distribution, about 68% of values are between -1 and 1
    assert math.isclose(normal_probability_between(-1, 1), 0.6827, rel_tol=1e-4)
    # About 95% of values are between -2 and 2 in a standard normal distribution
    assert math.isclose(normal_probability_between(-2, 2), 0.9545, rel_tol=1e-4)


def test_normal_probability_outside():
    """Test the normal_probability_outside function."""
    # Outside -1 and 1 in a standard normal distribution is about 32% of the values
    assert math.isclose(normal_probability_outside(-1, 1), 0.3173, rel_tol=1e-4)
    # Outside -2 and 2 is about 5% of the values
    assert math.isclose(normal_probability_outside(-2, 2), 0.0455, rel_tol=1e-4)
