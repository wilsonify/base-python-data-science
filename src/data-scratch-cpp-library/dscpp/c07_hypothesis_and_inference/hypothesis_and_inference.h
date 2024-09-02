#include <cmath>
#include "probability.h"

double normal_approximation_to_binomial(n, p);
double normal_probability_above(lo, mu=0.0, sigma=1.0);
double normal_probability_between(lo, hi, mu=0.0, sigma=1.0);
double normal_probability_outside(lo, hi, mu=0.0, sigma=1.0);
double normal_upper_bound(probability, mu=0.0, sigma=1.0);
double normal_lower_bound(probability, mu=0.0, sigma=1.0);
double normal_two_sided_bounds(probability, mu=0.0, sigma=1.0);
double two_sided_p_value(x, mu=0.0, sigma=1.0);
double count_extreme_values();
double run_experiment();
double reject_fairness(experiment);
double estimated_parameters(std::vector<std::vector<double>> n_matrix, double n);
double a_b_test_statistic( std::vector<std::vector<double>> a_matrix,  double a_weight,  std::vector<std::vector<double>> b_matrix, double b_weight);
double normalizer(alpha, beta);
double beta_pdf(x, alpha, beta);