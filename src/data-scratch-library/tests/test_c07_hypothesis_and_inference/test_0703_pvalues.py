import math
from random import seed

from dsl.c07_hypothesis_and_inference.e0701_coin_flip import normal_probability_between, normal_probability_above
from dsl.c07_hypothesis_and_inference.e0702_normal_bounds import normal_upper_bound
from dsl.c07_hypothesis_and_inference.e0703_pvalues import (
    two_sided_p_value,
    count_extreme_values,
    normal_probability_above,
    normal_probability_below,
    normal_approximation_to_binomial,
    normal_two_sided_bounds,
)


def test_two_sided_p_value():
    """Test that two_sided_p_value returns correct p-values for given x."""
    assert math.isclose(two_sided_p_value(0), 1.0, rel_tol=1e-3)
    assert math.isclose(two_sided_p_value(2), 0.0455, rel_tol=1e-3)
    assert math.isclose(two_sided_p_value(-2), 0.0455, rel_tol=1e-3)


def test_count_extreme_values():
    """Test that count_extreme_values returns a value close to expected."""
    seed(0)
    extreme_value_frequency = count_extreme_values(num_trials=10000)
    assert math.isclose(extreme_value_frequency, 0.06171, abs_tol=0.02)


def test_normal_probability_bounds():
    """Test the normal_two_sided_bounds, normal_approximation_to_binomial, and tail probabilities."""
    seed(0)
    n, p = 1000, 0.5
    mu_0, sigma_0 = normal_approximation_to_binomial(n, p)

    lower_bound, upper_bound = normal_two_sided_bounds(0.95, mu_0, sigma_0)
    assert math.isclose(lower_bound, 469, rel_tol=1e-1)
    assert math.isclose(upper_bound, 531, rel_tol=1e-1)

    result = normal_probability_above(524.5, mu_0, sigma_0)
    assert math.isclose(result, 0.061, rel_tol=1e-2)

    result = normal_probability_below(526.5, mu_0, sigma_0)
    assert math.isclose(result, 0.95, abs_tol=0.01)


def test_type_2_error_and_power():
    """Test the calculation of type 2 error probability and power."""
    n, p = 1000, 0.5
    mu_0, sigma_0 = normal_approximation_to_binomial(n, p)

    lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)

    mu_1, sigma_1 = normal_approximation_to_binomial(n, 0.55)

    type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)

    power = 1 - type_2_probability

    assert math.isclose(power, 0.887, rel_tol=1e-2)

    hi_one_sided = normal_upper_bound(0.95, mu_0, sigma_0)
    type_2_probability_one_sided = normal_probability_below(hi_one_sided, mu_1, sigma_1)
    power_one_sided = 1 - type_2_probability_one_sided

    assert math.isclose(power_one_sided, 0.936, rel_tol=1e-2)
