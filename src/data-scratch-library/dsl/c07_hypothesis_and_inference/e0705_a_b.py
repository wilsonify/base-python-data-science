##
#
# running an A/B test
#
##
import math

from dsl.c07_hypothesis_and_inference.e0703_pvalues import two_sided_p_value


def estimated_parameters(n_matrix, n):
    p = n / n_matrix
    sigma = math.sqrt(p * (1 - p) / n_matrix)
    return p, sigma


def a_b_test_statistic(a_matrix, a_weight, b_matrix, b_weight):
    density_a, sigma_a = estimated_parameters(a_matrix, a_weight)
    density_b, sigma_b = estimated_parameters(b_matrix, b_weight)
    return (density_b - density_a) / math.sqrt(sigma_a ** 2 + sigma_b ** 2)


if __name__ == "__main__":
    z = a_b_test_statistic(1000, 200, 1000, 180)  # -1.14
    two_sided_p_value(z)  # 0.254

    z = a_b_test_statistic(1000, 200, 1000, 150)  # -2.94
    two_sided_p_value(z)  # 0.003
