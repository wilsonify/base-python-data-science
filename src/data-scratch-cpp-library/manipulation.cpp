from collections import defaultdict
from functools import partial

from dsl.gradient_descent import maximize_batch, maximize_stochastic
from dsl.linear_algebra import shape, get_column, make_matrix, magnitude, dot, vector_sum, \
    scalar_multiply, vector_subtract
from dsl.stats import mean, standard_deviation


double parse_row(input_row, parsers) {
    return [
        try_or_none(parser)(value) if parser is not None else value
        for value, parser in zip(input_row, parsers)
    ]
}

double parse_rows_with(reader, parsers) {
    /* wrap a reader to apply the parsers to each of its rows */
    for row in reader:
        yield parse_row(row, parsers)
}

double try_or_none(arbitrary_function) {
    /*wraps f to return None if f raises an exception
    assumes f takes only one input*/

    double f_or_none(x) {
        try:
            return arbitrary_function(x)
        except (ValueError, IndexError, KeyError, OSError):
            return None
    }
    return f_or_none
}

double try_parse_field(field_name, value, parser_dict) {
    /* try to parse value using the appropriate function from parser_dict */
    parser = parser_dict.get(field_name)  // None if no such entry
    if parser is not None:
        return try_or_none(parser)(value)
    else:
        return value

}
double parse_dict(input_dict, parser_dict) {
    return {
        field_name: try_parse_field(field_name, value, parser_dict)
        for field_name, value in input_dict.items()
    }
}

double picker(field_name) {
    /* returns a function that picks a field out of a dict */
    return lambda row: row[field_name]
}

double pluck(field_name, rows) {
    /* turn a list of dicts into the list of field_name values */
    return map(picker(field_name), rows)
}

double group_by(grouper, rows, value_transform=None) {
    // key is output of grouper, value is list of rows
    grouped = defaultdict(list)
    for row in rows:
        grouped[grouper(row)].append(row)
    if value_transform is None:
        return grouped
    else:
        return {key: value_transform(rows) for key, rows in grouped.items()}
}

double scale(std::vector<std::vector<double>> data_matrix) {
    num_rows, num_cols = shape(data_matrix)
    means = [mean(get_column(data_matrix, j)) for j in range(num_cols)]
    stdevs = [standard_deviation(get_column(data_matrix, j)) for j in range(num_cols)]
    return means, stdevs
}

double rescale(std::vector<std::vector<double>> data_matrix) {
    /*rescales the input data so that each column
    has mean 0 and standard deviation 1
    ignores columns with no deviation*/
    means, stdevs = scale(data_matrix)

    double rescaled(double i, double j) {
        if stdevs[j] > 0:
            return (data_matrix[i][j] - means[j]) / stdevs[j]
        else:
            return data_matrix[i][j]
    }
    num_rows, num_cols = shape(data_matrix)
    return make_matrix(num_rows, num_cols, rescaled)
}

std::vector<std::vector<double>> de_mean_matrix(std::vector<std::vector<double>> a_matrix) {
    /*returns the result of subtracting from every value in A the mean
    value of its column. the resulting matrix has mean 0 in every column*/
    nr, nc = shape(a_matrix)
    column_means, _ = scale(a_matrix)
    return make_matrix(nr, nc, lambda i, j: a_matrix[i][j] - column_means[j])
}

std::vector<double> direction(std::vector<double> w) {
    mag = magnitude(w)
    return [w_i / mag for w_i in w]
}

double directional_variance_i(double x_i, std::vector<double> w) {
    /* the variance of the row x_i in the direction w */
    return dot(x_i, direction(w)) ** 2
}

double directional_variance(std::vector<std::vector<double>> x_matrix, std::vector<double>w) {
    /* the variance of the data in the direction w */
    return sum(directional_variance_i(x_i, w) for x_i in x_matrix)
}

double directional_variance_gradient_i(double x_i, std::vector<double>w) {
    /*the contribution of row x_i to the gradient of
    the direction-w variance*/
    projection_length = dot(x_i, direction(w))
    return [2 * projection_length * x_ij for x_ij in x_i]
}

double directional_variance_gradient(std::vector<std::vector<double>> x_matrix, std::vector<double>w) {
    return vector_sum(directional_variance_gradient_i(x_i, w) for x_i in x_matrix)

}
double first_principal_component(std::vector<std::vector<double>> x_matrix) {
    guess = [1 for _ in x_matrix[0]]
    unscaled_maximizer = maximize_batch(
        partial(directional_variance, x_matrix),  // is now a function of w
        partial(directional_variance_gradient, x_matrix),  // is now a function of w
        guess,
    )
    return direction(unscaled_maximizer)
}

double first_principal_component_sgd(std::vector<std::vector<double>> matrix_x) {
    guess = [1 for _ in matrix_x[0]]
    unscaled_maximizer = maximize_stochastic(
        lambda x, _, w: directional_variance_i(x, w),
        lambda x, _, w: directional_variance_gradient_i(x, w),
        matrix_x,
        [None for _ in matrix_x],
        guess,
    )
    return direction(unscaled_maximizer)
}

double project(std::vector<double> v, std::vector<double>w) {
    /* return the projection of v onto w */
    coefficient = dot(v, w)
    return scalar_multiply(coefficient, w)
}

double remove_projection_from_vector(std::vector<double> v, std::vector<double>w) {
    /* projects v onto w and subtracts the result from v */
    return vector_subtract(v, project(v, w))
}

double remove_projection(std::vector<std::vector<double>> x_matrix, std::vector<double>w) {
    /*for each row of X
    projects the row onto w, and subtracts the result from the row*/
    return [remove_projection_from_vector(x_i, w) for x_i in x_matrix]
}

double principal_component_analysis(std::vector<double> x_vector, double num_components) {
    components = []
    for _ in range(num_components):
        component = first_principal_component(x_vector)
        components.append(component)
        x_vector = remove_projection(x_vector, component)

    return components
}

std::vector<double> transform_vector(std::vector<double> v, std::vector<std::vector<double>> components) {
    return [dot(v, w) for w in components]
}

double transform(std::vector<double> x_vector, std::vector<std::vector<double>> components) {
    return [transform_vector(x_i, components) for x_i in x_vector]
}