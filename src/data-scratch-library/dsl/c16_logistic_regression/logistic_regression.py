import logging
import math
from functools import reduce, partial

from dsl.c04_linear_algebra.e0401_vectors import dot, vector_add
from dsl.c08_gradient_descent.e0804_minibatch_gd import maximize_batch
from dsl.c08_gradient_descent.e0805_stochastic_gd import maximize_stochastic


def logistic(x):
    # avoid overflow, log(1e308) is around 709
    if x > 709:
        return 1.0
    elif x < -709:
        return 0.0
    result = 1.0 / (1 + math.exp(-x))
    return result


def logistic_prime(x):
    return logistic(x) * (1 - logistic(x))


def logistic_log_likelihood_i(x_i, y_i, beta):
    if y_i == 1:
        return math.log(logistic(dot(x_i, beta)))
    else:
        return math.log(1 - logistic(dot(x_i, beta)))


def logistic_log_likelihood(x, y, beta):
    return sum(logistic_log_likelihood_i(x_i, y_i, beta) for x_i, y_i in zip(x, y))


def logistic_log_partial_ij(x_i, y_i, beta, j):
    """here i is the index of the data point,
    j the index of the derivative"""

    return (y_i - logistic(dot(x_i, beta))) * x_i[j]


def logistic_log_gradient_i(x_i, y_i, beta):
    """the gradient of the log likelihood
    corresponding to the i-th data point"""

    return [logistic_log_partial_ij(x_i, y_i, beta, j) for j, _ in enumerate(beta)]


def logistic_log_gradient(x, y, beta):
    return reduce(
        vector_add, [logistic_log_gradient_i(x_i, y_i, beta) for x_i, y_i in zip(x, y)]
    )


def score_logistic(beta_hat, x_test, y_test):
    true_positives = 0
    false_positives = 0
    true_negatives = 0
    false_negatives = 0
    for _x_i, _y_i in zip(x_test, y_test):
        predict = logistic(dot(beta_hat, _x_i))

        if _y_i == 1 and predict >= 0.5:  # TP: paid and we predict paid
            true_positives += 1
        elif _y_i == 1:  # FN: paid and we predict unpaid
            false_negatives += 1
        elif predict >= 0.5:  # FP: unpaid and we predict paid
            false_positives += 1
        else:  # TN: unpaid and we predict unpaid
            true_negatives += 1
    precision = true_positives / (true_positives + false_positives)
    recall = true_positives / (true_positives + false_negatives)
    return precision, recall


def logistic_fit(x, y):
    """
    maximize log likelihood using gradient descent, from a random starting point
    """
    logging.info("logistic regression")
    fn = partial(logistic_log_likelihood, x, y)
    gradient_fn = partial(logistic_log_gradient, x, y)
    beta_0 = [1, 1, 1]
    beta_1 = maximize_batch(fn, gradient_fn, beta_0)
    beta_hat = maximize_stochastic(logistic_log_likelihood_i, logistic_log_gradient_i, x, y, beta_1)
    logging.info("%r", "beta stochastic {}".format(beta_hat))
    return beta_hat
