import logging
import math
import random
from logging.config import dictConfig

from data_science_from_scratch import config
from data_science_from_scratch.library.probability import normal_cdf, inverse_normal_cdf


def normal_approximation_to_binomial(n, p):
    """finds mu and sigma corresponding to a Binomial(n, p)"""
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma


#####
#
# probabilities a normal lies in an interval
#
######

# the normal cdf _is_ the probability the variable is below a threshold
normal_probability_below = normal_cdf


# it's above the threshold if it's not below the threshold
def normal_probability_above(lo, mu=0.0, sigma=1.0):
    return 1 - normal_cdf(lo, mu, sigma)


# it's between if it's less than hi, but not less than lo
def normal_probability_between(lo, hi, mu=0.0, sigma=1.0):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)


# it's outside if it's not between
def normal_probability_outside(lo, hi, mu=0.0, sigma=1.0):
    return 1 - normal_probability_between(lo, hi, mu, sigma)


######
#
#  normal bounds
#
######


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


upper_p_value = normal_probability_above
lower_p_value = normal_probability_below


##
#
# P-hacking
#
##


def run_experiment():
    """flip a fair coin 1000 times, True = heads, False = tails"""
    return [random.random() < 0.5 for _ in range(1000)]


def reject_fairness(experiment):
    """using the 5% significance levels"""
    num_heads = len([flip for flip in experiment if flip])
    return num_heads < 469 or num_heads > 531


##
#
# running an A/B test
#
##


def estimated_parameters(n_matrix, n):
    p = n / n_matrix
    sigma = math.sqrt(p * (1 - p) / n_matrix)
    return p, sigma


def a_b_test_statistic(a_matrix, a_weight, b_matrix, b_weight):
    density_a, sigma_a = estimated_parameters(a_matrix, a_weight)
    density_b, sigma_b = estimated_parameters(b_matrix, b_weight)
    return (density_b - density_a) / math.sqrt(sigma_a ** 2 + sigma_b ** 2)


##
#
# Bayesian Inference
#
##


def normalizer(alpha, beta):
    """a normalizing constant so that the total probability is 1"""
    return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)


def beta_pdf(x, alpha, beta):
    if x < 0 or x > 1:  # no weight outside of [0, 1]
        return 0
    return x ** (alpha - 1) * (1 - x) ** (beta - 1) / normalizer(alpha, beta)


def main():
    mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
    logging.info("%r", "mu_0 {}".format(mu_0))
    logging.info("%r", "sigma_0 {}".format(sigma_0))
    logging.info(
        "%r",
        "normal_two_sided_bounds(0.95, mu_0, sigma_0) {}".format(
            normal_two_sided_bounds(0.95, mu_0, sigma_0),
        ),
    )
    logging.info("power of a test")

    logging.info("95% bounds based on assumption p is 0.5")

    _lo, _hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)
    logging.info("%r", "lo {}".format(_lo))
    logging.info("%r", "hi {}".format(_hi))

    logging.info("actual mu and sigma based on p = 0.55")
    mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)
    logging.info("%r", "mu_1 {}".format(mu_1))
    logging.info("%r", "sigma_1 {}".format(sigma_1))

    # a type 2 error means we fail to reject the null hypothesis
    # which will happen when X is still in our original interval
    type_2_probability = normal_probability_between(_lo, _hi, mu_1, sigma_1)
    power = 1 - type_2_probability  # 0.887

    logging.info("%r", "type 2 probability {}".format(type_2_probability))
    logging.info("%r", "power {}".format(power))

    logging.info("one-sided test")
    _hi = normal_upper_bound(0.95, mu_0, sigma_0)
    logging.info("%r", "hi {}".format(_hi))  # is 526 (< 531, since we need more probability in the upper tail))
    type_2_probability = normal_probability_below(_hi, mu_1, sigma_1)
    power = 1 - type_2_probability  # = 0.936
    logging.info("%r", "type 2 probability {}".format(type_2_probability))
    logging.info("%r", "power {}".format(power))

    logging.info(
        "%r",
        "two_sided_p_value(529.5, mu_0, sigma_0) {}".format(
            two_sided_p_value(529.5, mu_0, sigma_0),
        ),
    )

    logging.info(
        "%r",
        "two_sided_p_value(531.5, mu_0, sigma_0) {}".format(
            two_sided_p_value(531.5, mu_0, sigma_0),
        ),
    )

    logging.info(
        "%r",
        "upper_p_value(525, mu_0, sigma_0) {}".format(
            upper_p_value(525, mu_0, sigma_0)
        ),
    )
    logging.info(
        "%r",
        "upper_p_value(527, mu_0, sigma_0) {}".format(
            upper_p_value(527, mu_0, sigma_0)
        ),
    )

    logging.info("P-hacking")

    random.seed(0)
    n_experiments = 1000
    experiments = [run_experiment() for _ in range(n_experiments)]
    num_rejections = len(
        [experiment for experiment in experiments if reject_fairness(experiment)]
    )

    logging.info("%r", "rejections: {} out of {}".format(num_rejections, n_experiments))

    logging.info("A/B testing")
    z = a_b_test_statistic(1000, 200, 1000, 180)
    logging.info("%r", "a_b_test_statistic(1000, 200, 1000, 180) {}".format(z))
    logging.info("%r", "p-value {}".format(two_sided_p_value(z)))

    z = a_b_test_statistic(1000, 200, 1000, 150)
    logging.info("%r", "a_b_test_statistic(1000, 200, 1000, 150) {}".format(z))
    logging.info("%r", "p-value {}".format(two_sided_p_value(z)))


if __name__ == "__main__":
    dictConfig(config.LOGGING_CONFIG_DICT)
    main()
