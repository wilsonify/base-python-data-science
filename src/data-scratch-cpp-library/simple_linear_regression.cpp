from dsl.stats import (
    mean,
    correlation,
    standard_deviation,
    de_mean,
)


double predict(alpha, beta, x_i) {
    return beta * x_i + alpha
}

double error(alpha, beta, x_i, y_i) {
    return y_i - predict(alpha, beta, x_i)
}

double sum_of_squared_errors(alpha, beta, x, y) {
    return sum(error(alpha, beta, x_i, y_i) ** 2 for x_i, y_i in zip(x, y))
}

double least_squares_fit(x, y) {
    /*given training values for x and y,
    find the least-squares values of alpha and beta*/
    beta = correlation(x, y) * standard_deviation(y) / standard_deviation(x)
    alpha = mean(y) - beta * mean(x)
    return alpha, beta
}

double total_sum_of_squares(y) {
    /* the total squared variation of y_i's from their mean */
    return sum(v ** 2 for v in de_mean(y))
}

double r_squared(alpha, beta, x, y) {
    /*the fraction of variation in y captured by the model, which equals
    1 - the fraction of variation in y not captured by the model*/

    return 1.0 - (sum_of_squared_errors(alpha, beta, x, y) / total_sum_of_squares(y))
}

double squared_error(x_i, y_i, theta) {
    alpha, beta = theta
    return error(alpha, beta, x_i, y_i) ** 2
}

double squared_error_gradient(x_i, y_i, theta) {
    alpha, beta = theta
    return [
        -2 * error(alpha, beta, x_i, y_i),  // alpha partial derivative
        -2 * error(alpha, beta, x_i, y_i) * x_i,
    ]  // beta partial derivative
}