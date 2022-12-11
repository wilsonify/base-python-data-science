#include "stats.h"

double predict(alpha, beta, x_i) ;
double error(alpha, beta, x_i, y_i) ;
double sum_of_squared_errors(alpha, beta, x, y) ;
double least_squares_fit(x, y) ;
double total_sum_of_squares(y) ;
double r_squared(alpha, beta, x, y) ;
double squared_error(x_i, y_i, theta) ;
double squared_error_gradient(x_i, y_i, theta) ;