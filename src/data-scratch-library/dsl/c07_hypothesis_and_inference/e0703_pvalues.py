import random

from dsl.c07_hypothesis_and_inference.e0701_coin_flip import normal_probability_above, normal_probability_below, \
    normal_approximation_to_binomial, normal_probability_between
from dsl.c07_hypothesis_and_inference.e0702_normal_bounds import normal_two_sided_bounds, normal_upper_bound


def two_sided_p_value(x, mu=0.0, sigma=1.0):
    if x >= mu:
        # if x is greater than the mean, the tail is above x
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # if x is less than the mean, the tail is below x
        return 2 * normal_probability_below(x, mu, sigma)


def count_extreme_values():
    extreme_value_count = 0
    for _ in range(100000):
        num_heads = sum(
            1 if random.random() < 0.5 else 0 for _ in range(1000)  # count # of heads
        )  # in 1000 flips
        if num_heads >= 530 or num_heads <= 470:  # and count how often
            extreme_value_count += 1  # the # is 'extreme'

    return extreme_value_count / 100000


if __name__ == "__main__":
    mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
    lower_bound, upper_bound = normal_two_sided_bounds(0.95, mu_0, sigma_0)  # (469, 531)
    upper_p_value = normal_probability_above(524.5, mu_0, sigma_0)  # 0.061
    lower_p_value = normal_probability_below(526.5, mu_0, sigma_0)  # 0.047

    # 95% bounds based on assumption p is 0.5
    lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)
    # actual mu and sigma based on p = 0.55
    mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)
    # a type 2 error means we fail to reject the null hypothesis,
    # which will happen when X is still in our original interval
    type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
    power = 1 - type_2_probability
    # 0.887

    hi = normal_upper_bound(0.95, mu_0, sigma_0)
    # is 526 (< 531, since we need more probability in the upper tail)
    type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
    power = 1 - type_2_probability
    # 0.936