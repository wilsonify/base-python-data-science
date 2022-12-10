import math
import random

from dsl.probability import normal_cdf, inverse_normal_cdf


double normal_approximation_to_binomial(n, p) {
    /* finds mu and sigma corresponding to a Binomial(n, p) */
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma
}

//////////
//
// probabilities a normal lies in an interval
//
////////////

// the normal cdf _is_ the probability the variable is below a threshold
normal_probability_below = normal_cdf


// it's above the threshold if it's not below the threshold
double normal_probability_above(lo, mu=0.0, sigma=1.0) {
    return 1 - normal_cdf(lo, mu, sigma)
}

// it's between if it's less than hi, but not less than lo
double normal_probability_between(lo, hi, mu=0.0, sigma=1.0) {
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)
}

// it's outside if it's not between
double normal_probability_outside(lo, hi, mu=0.0, sigma=1.0) {
    return 1 - normal_probability_between(lo, hi, mu, sigma)
}

////////////
//
//  normal bounds
//
////////////


double normal_upper_bound(probability, mu=0.0, sigma=1.0) {
    /* returns the z for which P(Z <= z) = probability */
    return inverse_normal_cdf(probability, mu, sigma)
}

double normal_lower_bound(probability, mu=0.0, sigma=1.0) {
    /* returns the z for which P(Z >= z) = probability */
    return inverse_normal_cdf(1 - probability, mu, sigma)
}

double normal_two_sided_bounds(probability, mu=0.0, sigma=1.0) {
    /*returns the symmetric (about the mean) bounds
    that contain the specified probability*/
    tail_probability = (1 - probability) / 2

    // upper bound should have tail_probability above it
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)

    // lower bound should have tail_probability below it
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound

}
double two_sided_p_value(x, mu=0.0, sigma=1.0) {
    if x >= mu:
        // if x is greater than the mean, the tail is above x
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        // if x is less than the mean, the tail is below x
        return 2 * normal_probability_below(x, mu, sigma)
}

double count_extreme_values() {
    extreme_value_count = 0
    for _ in range(100000):
        num_heads = sum(
            1 if random.random() < 0.5 else 0 for _ in range(1000)  // count // of heads
        )  // in 1000 flips
        if num_heads >= 530 or num_heads <= 470:  // and count how often
            extreme_value_count += 1  // the // is 'extreme'

    return extreme_value_count / 100000
}

upper_p_value = normal_probability_above
lower_p_value = normal_probability_below


////
//
// P-hacking
//
////


double run_experiment() {
    /* flip a fair coin 1000 times, True = heads, False = tails */
    return [random.random() < 0.5 for _ in range(1000)]
}

double reject_fairness(experiment) {
    /* using the 5% significance levels */
    num_heads = len([flip for flip in experiment if flip])
    return num_heads < 469 or num_heads > 531
}

////
//
// running an A/B test
//
////


double estimated_parameters(std::vector<std::vector<double>> n_matrix, double n) {
    p = n / n_matrix
    sigma = math.sqrt(p * (1 - p) / n_matrix)
    return p, sigma
}

double a_b_test_statistic(
     std::vector<std::vector<double>> a_matrix, 
     double a_weight, 
     std::vector<std::vector<double>> b_matrix,
      double b_weight) {
    density_a, sigma_a = estimated_parameters(a_matrix, a_weight)
    density_b, sigma_b = estimated_parameters(b_matrix, b_weight)
    return (density_b - density_a) / math.sqrt(sigma_a ** 2 + sigma_b ** 2)
}

////
//
// Bayesian Inference
//
////


double normalizer(alpha, beta) {
    /* a normalizing constant so that the total probability is 1 */
    return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)
}

double beta_pdf(x, alpha, beta) {
    if x < 0 or x > 1:  // no weight outside of [0, 1]
        return 0
    return x ** (alpha - 1) * (1 - x) ** (beta - 1) / normalizer(alpha, beta)
}