#include "linear_algebra.h"

double sum_of_squares(v);
double difference_quotient(f, x, h);
double partial_difference_quotient(f, v, i, h);
double estimate_gradient(f, v, h=0.00001);
double step(v, direction, step_size);
double sum_of_squares_gradient(v);
double safe(f);
double minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001);
double negate(f);
double negate_all(f);
double maximize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001);
double in_random_order(data);
double minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01);
double maximize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01);