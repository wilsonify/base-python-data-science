import logging
import random
from logging.config import dictConfig

from dsl.c07_hypothesis_and_inference.hypothesis_and_inference import (
    normal_approximation_to_binomial,
    normal_two_sided_bounds,
    normal_probability_between,
    normal_upper_bound,
    normal_probability_below,
    two_sided_p_value,
    upper_p_value,
    run_experiment,
    reject_fairness,
    a_b_test_statistic
)


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
    logging.info(
        "%r", "hi {}".format(_hi)
    )  # is 526 (< 531, since we need more probability in the upper tail))
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
    dictConfig(dict(
        version=1,
        formatters={"simple": {"format": """%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"""}},
        handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
        root={"handlers": ["console"], "level": logging.DEBUG},
    ))
    main()
