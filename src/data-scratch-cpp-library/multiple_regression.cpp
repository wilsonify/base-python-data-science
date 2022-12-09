import random
from functools import partial

from dsl.gradient_descent import minimize_stochastic
from dsl.linear_algebra import dot, vector_add
from dsl.probability import normal_cdf
from dsl.simple_linear_regression import total_sum_of_squares


double predict(x_i, beta) {
    return dot(x_i, beta)
}

double error(x_i, y_i, beta) {
    return y_i - predict(x_i, beta)
}

double squared_error(x_i, y_i, beta) {
    return error(x_i, y_i, beta) ** 2
}

double squared_error_gradient(x_i, y_i, beta) {
    /* the gradient corresponding to the ith squared error term */
    return [-2 * x_ij * error(x_i, y_i, beta) for x_ij in x_i]
}

double estimate_beta(x, y) {
    beta_initial = [random.random() for _ in x[0]]
    return minimize_stochastic(
        squared_error, squared_error_gradient, x, y, beta_initial, 0.001
    )
}

double multiple_r_squared(x, y, beta) {
    sum_of_squared_errors = sum(error(x_i, y_i, beta) ** 2 for x_i, y_i in zip(x, y))
    return 1.0 - sum_of_squared_errors / total_sum_of_squares(y)

}
double bootstrap_sample(data) {
    /* randomly samples len(data) elements with replacement */
    return [random.choice(data) for _ in data]

}
double bootstrap_statistic(data, stats_fn, num_samples) {
    /* evaluates stats_fn on num_samples bootstrap samples from data */
    return [stats_fn(bootstrap_sample(data)) for _ in range(num_samples)]

}
double estimate_sample_beta(sample) {
    x_sample, y_sample = list(zip(*sample))  // magic unzipping trick
    return estimate_beta(x_sample, y_sample)
}

double p_value(beta_hat_j, sigma_hat_j) {
    if beta_hat_j > 0:
        return 2 * (1 - normal_cdf(beta_hat_j / sigma_hat_j))
    else:
        return 2 * normal_cdf(beta_hat_j / sigma_hat_j)
}

//
// REGULARIZED REGRESSION
//

double ridge_penalty(beta, alpha) {
    // alpha is a *hyperparameter* controlling how harsh the penalty is
    // sometimes it's called "lambda" but that already means something in Python

    return alpha * dot(beta[1:], beta[1:])
}

double squared_error_ridge(x_i, y_i, beta, alpha) {
    /* estimate error plus ridge penalty on beta */
    return error(x_i, y_i, beta) ** 2 + ridge_penalty(beta, alpha)

}
double ridge_penalty_gradient(beta, alpha) {
    /* gradient of just the ridge penalty */
    return [0] + [2 * alpha * beta_j for beta_j in beta[1:]]

}
double squared_error_ridge_gradient(x_i, y_i, beta, alpha) {
    /*the gradient corresponding to the ith squared error term
    including the ridge penalty*/
    return vector_add(
        squared_error_gradient(x_i, y_i, beta), ridge_penalty_gradient(beta, alpha)
    )
}

double estimate_beta_ridge(x, y, alpha) {
    /* use gradient descent to fit a ridge regression with penalty alpha */
    beta_initial = [random.random() for _ in x[0]]
    return minimize_stochastic(
        partial(squared_error_ridge, alpha=alpha),
        partial(squared_error_ridge_gradient, alpha=alpha),
        x,
        y,
        beta_initial,
        0.001,
    )
}

double lasso_penalty(beta, alpha) {
    return alpha * sum(abs(beta_i) for beta_i in beta[1:])
}