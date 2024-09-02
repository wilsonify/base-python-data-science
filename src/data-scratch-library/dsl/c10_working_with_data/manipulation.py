from collections import defaultdict
from functools import partial

from dsl.c04_linear_algebra.linear_algebra import shape, get_column, make_matrix, magnitude, dot, vector_sum, \
    scalar_multiply, vector_subtract
from dsl.c05_statistics.stats import mean, standard_deviation
from dsl.c08_gradient_descent.gradient_descent import maximize_batch, maximize_stochastic


def parse_row(input_row, parsers):
    return [
        try_or_none(parser)(value) if parser is not None else value
        for value, parser in zip(input_row, parsers)
    ]


def parse_rows_with(reader, parsers):
    """wrap a reader to apply the parsers to each of its rows"""
    for row in reader:
        yield parse_row(row, parsers)


def try_or_none(arbitrary_function):
    """wraps f to return None if f raises an exception
    assumes f takes only one input"""

    def f_or_none(x):
        try:
            return arbitrary_function(x)
        except (ValueError, IndexError, KeyError, OSError):
            return None

    return f_or_none


def try_parse_field(field_name, value, parser_dict):
    """try to parse value using the appropriate function from parser_dict"""
    parser = parser_dict.get(field_name)  # None if no such entry
    if parser is not None:
        return try_or_none(parser)(value)
    else:
        return value


def parse_dict(input_dict, parser_dict):
    return {
        field_name: try_parse_field(field_name, value, parser_dict)
        for field_name, value in input_dict.items()
    }


def picker(field_name):
    """returns a function that picks a field out of a dict"""
    return lambda row: row[field_name]


def pluck(field_name, rows):
    """turn a list of dicts into the list of field_name values"""
    return map(picker(field_name), rows)


def group_by(grouper, rows, value_transform=None):
    # key is output of grouper, value is list of rows
    grouped = defaultdict(list)
    for row in rows:
        grouped[grouper(row)].append(row)
    if value_transform is None:
        return grouped
    else:
        return {key: value_transform(rows) for key, rows in grouped.items()}


def scale(data_matrix):
    num_rows, num_cols = shape(data_matrix)
    means = [mean(get_column(data_matrix, j)) for j in range(num_cols)]
    stdevs = [standard_deviation(get_column(data_matrix, j)) for j in range(num_cols)]
    return means, stdevs


def rescale(data_matrix):
    """rescales the input data so that each column
    has mean 0 and standard deviation 1
    ignores columns with no deviation"""
    means, stdevs = scale(data_matrix)

    def rescaled(i, j):
        if stdevs[j] > 0:
            return (data_matrix[i][j] - means[j]) / stdevs[j]
        else:
            return data_matrix[i][j]

    num_rows, num_cols = shape(data_matrix)
    return make_matrix(num_rows, num_cols, rescaled)


def de_mean_matrix(a_matrix):
    """returns the result of subtracting from every value in A the mean
    value of its column. the resulting matrix has mean 0 in every column"""
    nr, nc = shape(a_matrix)
    column_means, _ = scale(a_matrix)
    return make_matrix(nr, nc, lambda i, j: a_matrix[i][j] - column_means[j])


def direction(w):
    mag = magnitude(w)
    return [w_i / mag for w_i in w]


def directional_variance_i(x_i, w):
    """the variance of the row x_i in the direction w"""
    return dot(x_i, direction(w)) ** 2


def directional_variance(x_matrix, w):
    """the variance of the data in the direction w"""
    return sum(directional_variance_i(x_i, w) for x_i in x_matrix)


def directional_variance_gradient_i(x_i, w):
    """the contribution of row x_i to the gradient of
    the direction-w variance"""
    projection_length = dot(x_i, direction(w))
    return [2 * projection_length * x_ij for x_ij in x_i]


def directional_variance_gradient(x_matrix, w):
    return vector_sum(directional_variance_gradient_i(x_i, w) for x_i in x_matrix)


def first_principal_component(x_matrix):
    guess = [1 for _ in x_matrix[0]]
    unscaled_maximizer = maximize_batch(
        partial(directional_variance, x_matrix),  # is now a function of w
        partial(directional_variance_gradient, x_matrix),  # is now a function of w
        guess,
    )
    return direction(unscaled_maximizer)


def first_principal_component_sgd(matrix_x):
    guess = [1 for _ in matrix_x[0]]
    unscaled_maximizer = maximize_stochastic(
        lambda x, _, w: directional_variance_i(x, w),
        lambda x, _, w: directional_variance_gradient_i(x, w),
        matrix_x,
        [None for _ in matrix_x],
        guess,
    )
    return direction(unscaled_maximizer)


def project(v, w):
    """return the projection of v onto w"""
    coefficient = dot(v, w)
    return scalar_multiply(coefficient, w)


def remove_projection_from_vector(v, w):
    """projects v onto w and subtracts the result from v"""
    return vector_subtract(v, project(v, w))


def remove_projection(x_matrix, w):
    """for each row of X
    projects the row onto w, and subtracts the result from the row"""
    return [remove_projection_from_vector(x_i, w) for x_i in x_matrix]


def principal_component_analysis(x_vector, num_components):
    components = []
    for _ in range(num_components):
        component = first_principal_component(x_vector)
        components.append(component)
        x_vector = remove_projection(x_vector, component)

    return components


def transform_vector(v, components):
    return [dot(v, w) for w in components]


def transform(x_vector, components):
    return [transform_vector(x_i, components) for x_i in x_vector]
