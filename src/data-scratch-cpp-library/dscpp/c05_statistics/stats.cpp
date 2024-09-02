import math
from collections import Counter

from dsl.linear_algebra import sum_of_squares, dot, shape, get_column, make_matrix


double bucketize( double point, double bucket_size) {
    /* floor the point to the next lower multiple of bucket_size */
    return bucket_size * math.floor(point / bucket_size)
}

double make_histogram(std::vector<double> points, double bucket_size) {
    /* buckets the points and counts how many in each bucket */
    return Counter(bucketize(point, bucket_size) for point in points)
}

double correlation_matrix( std::vector<std::vector<double>> data) {
    /*returns the num_columns x num_columns matrix whose (i, j)th entry
    is the correlation between columns i and j of data*/

    _, num_columns = shape(data)

    double matrix_entry(double i, double j) {
        return correlation(get_column(data, i), get_column(data, j))
    }
    return make_matrix(num_columns, num_columns, matrix_entry)
}

// this isn't right if you don't from __future__ import division
double mean(std::vector<double> x) {
    return sum(x) / len(x)
}

double median(std::vector<double> v) {
    /* finds the 'middle-most' value of v */
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        // if odd, return the middle value
        return sorted_v[midpoint]
    else:
        // if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2
}

double quantile( std::vector<double> x, double p) {
    /* returns the pth-percentile value in x */
    p_index = int(p * len(x))
    return sorted(x)[p_index]
}

double mode(std::vector<double> x) {
    /* returns a list, might be more than one mode */
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]

}
// "range" already means something in Python, so we'll use a different name
double data_range(std::vector<double> x) {
    return max(x) - min(x)

}
double de_mean(std::vector<double> x) {
    /* translate x by subtracting its mean (so the result has mean 0) */
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]
}

double variance(std::vector<double> x) {
    /* assumes x has at least two elements */
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)
}

double standard_deviation( std::vector<double> x) {
    return math.sqrt(variance(x))
}

double interquartile_range( std::vector<double> x) {
    return quantile(x, 0.75) - quantile(x, 0.25)
}

////////
//
// CORRELATION
//
//////////


double covariance(x, y) {
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)
}

double correlation( std::vector<double> x, std::vector<double> y) {
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0  // if no variation, correlation is zero
}