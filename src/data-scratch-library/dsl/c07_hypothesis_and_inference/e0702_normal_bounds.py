######
#
#  normal bounds
#
######
from dsl.c06_probability.e0603_normal import inverse_normal_cdf
from dsl.c07_hypothesis_and_inference.e0701_coin_flip import normal_approximation_to_binomial


def normal_upper_bound(probability, mu=0.0, sigma=1.0):
    """returns the z for which P(Z <= z) = probability"""
    return inverse_normal_cdf(probability, mu, sigma)


def normal_lower_bound(probability, mu=0.0, sigma=1.0):
    """returns the z for which P(Z >= z) = probability"""
    return inverse_normal_cdf(1 - probability, mu, sigma)


def normal_two_sided_bounds(probability, mu=0.0, sigma=1.0):
    """returns the symmetric (about the mean) bounds
    that contain the specified probability"""
    tail_probability = (1 - probability) / 2

    # upper bound should have tail_probability above it
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)

    # lower bound should have tail_probability below it
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound


if __name__ == "__main__":
    mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
    lower_bound, upper_bound = normal_two_sided_bounds(0.95, mu_0, sigma_0)  # (469, 531)
