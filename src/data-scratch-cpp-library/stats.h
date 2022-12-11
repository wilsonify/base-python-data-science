import math
from collections import Counter

from dsl.linear_algebra import sum_of_squares, dot, shape, get_column, make_matrix


double bucketize( double point, double bucket_size) ;

double make_histogram(std::vector<double> points, double bucket_size) ;

double correlation_matrix( std::vector<std::vector<double>> data) ;
    return make_matrix(num_columns, num_columns, matrix_entry)
}

// this isn't right if you don't from __future__ import division
double mean(std::vector<double> x) ;

double median(std::vector<double> v) ;

double quantile( std::vector<double> x, double p) ;

double mode(std::vector<double> x) ;
// "range" already means something in Python, so we'll use a different name
double data_range(std::vector<double> x) ;
double de_mean(std::vector<double> x) ;

double variance(std::vector<double> x) ;

double standard_deviation( std::vector<double> x) ;

double interquartile_range( std::vector<double> x) ;

////////
//
// CORRELATION
//
//////////


double covariance(x, y) ;

double correlation( std::vector<double> x, std::vector<double> y) ;