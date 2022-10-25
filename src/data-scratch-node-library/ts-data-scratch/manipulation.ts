
import { maximize_batch, maximize_stochastic } from "./gradient_descent";

import { shape, get_column, make_matrix, magnitude, dot, vector_sum, scalar_multiply, vector_subtract } from "./linear_algebra";

import { mean, standard_deviation } from "./stats";

import { NumericFunction, ParserFunction, BivaritateFunction,  NumericArray, NumericArrayFunction } from "./type-helpers"

var defaultDict = new Proxy({}, { get: (target:string, name:string) => name in target ? target[name] : 0 })

function  parse_row(input_row:Array<number>, parsers:Array<ParserFunction>) {
    var result = [];
    for (var i = 0;i<input_row.length;i+=1) {
        var value = input_row[i];
        var parser = parsers[i];
        var safe_parser = try_or_none(parser);
        var parsed = safe_parser(value);
        result.push(parsed);
    }
    return result
}

function  parse_rows_with(reader:Array<Array<number>>, parsers:Array<ParserFunction>) {
    // wrap a reader to apply the parsers to each of its rows    
    for (var i = 0; i<reader.length; i+=1) {
        var row = reader[i]
        yield parse_row(row, parsers)
    }
}

function try_or_none(arbitrary_function:ParserFunction) {
    // wraps f to return None if f raises an exception assumes f takes only one input
    function  f_or_none(x:string) {
        try {
            return arbitrary_function(x) 
        } catch (e) {
            return NaN
    }}

    return f_or_none
}

function try_parse_field(field_name:string, value:string, parser_dict:Map<string,ParserFunction>) {
    // try to parse value using the appropriate function from parser_dict
    var parser = parser_dict.get(field_name)  // None if no such entry
    if (parser == null) {
        console.log(`${field_name} parser is null or undefined`);
        return NaN
    }
    if (parser === null) {
        console.log(`${field_name} parser is identical to null`);
        return NaN
    }
    if (typeof parser === 'undefined') {
        console.log(`${field_name} parser is identical to undefined`);
        return NaN
    }
    var safe_parser=try_or_none(parser)
    return safe_parser(value)
}

function  parse_dict(input_dict, parser_dict) {
    return {
        field_name: try_parse_field(field_name, value, parser_dict)
        for field_name, value in input_dict.items()
    }
}

function  picker(field_name) {
    //returns a function that picks a field out of a dict
    return lambda row: row[field_name]
}

function  pluck(field_name, rows) {
    //turn a list of dicts into the list of field_name values
    return map(picker(field_name), rows)
}

function  group_by(grouper, rows, value_transform=None) {
    # key is output of grouper, value is list of rows
    grouped = defaultdict(list)
    for row in rows:
        grouped[grouper(row)].append(row)
    if value_transform is None:
        return grouped
    else:
        return {key: value_transform(rows) for key, rows in grouped.items()}
}

function  scale(data_matrix) {
    num_rows, num_cols = shape(data_matrix)
    means = [mean(get_column(data_matrix, j)) for j in range(num_cols)]
    stdevs = [standard_deviation(get_column(data_matrix, j)) for j in range(num_cols)]
    return means, stdevs
}

function  rescale(data_matrix) {
    /*
    rescales the input data so that each column has mean 0 and standard deviation 1 
    ignores columns with no deviation
    */
    means, stdevs = scale(data_matrix)

    function  rescaled(i, j) {
        if stdevs[j] > 0:
            return (data_matrix[i][j] - means[j]) / stdevs[j]
        else:
            return data_matrix[i][j]
    }

    num_rows, num_cols = shape(data_matrix)
    return make_matrix(num_rows, num_cols, rescaled)
}

function  de_mean_matrix(a_matrix) {
    /*
    returns the result of subtracting from every value in A the mean
    value of its column. the resulting matrix has mean 0 in every column
    */
    nr, nc = shape(a_matrix)
    column_means, _ = scale(a_matrix)
    return make_matrix(nr, nc, lambda i, j: a_matrix[i][j] - column_means[j])
}

function  direction(w) {
    mag = magnitude(w)
    return [w_i / mag for w_i in w]
}

function  directional_variance_i(x_i, w) {
    //the variance of the row x_i in the direction w
    return dot(x_i, direction(w)) ** 2
}

function  directional_variance(x_matrix, w) {
    //the variance of the data in the direction w
    return sum(directional_variance_i(x_i, w) for x_i in x_matrix)
}

function  directional_variance_gradient_i(x_i, w) {
    /*
    the contribution of row x_i to the gradient of
    the direction-w variance
    */
    projection_length = dot(x_i, direction(w))
    return [2 * projection_length * x_ij for x_ij in x_i]
}

function  directional_variance_gradient(x_matrix, w) {
    return vector_sum(directional_variance_gradient_i(x_i, w) for x_i in x_matrix)
}

function  first_principal_component(x_matrix) {
    guess = [1 for _ in x_matrix[0]]
    unscaled_maximizer = maximize_batch(
        partial(directional_variance, x_matrix),  # is now a function of w
        partial(directional_variance_gradient, x_matrix),  # is now a function of w
        guess,
    )
    return direction(unscaled_maximizer)
    }

function  first_principal_component_sgd(matrix_x) {
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

function  project(v, w) {
    //return the projection of v onto w
    coefficient = dot(v, w)
    return scalar_multiply(coefficient, w)
}

function  remove_projection_from_vector(v, w) {
    //projects v onto w and subtracts the result from v
    return vector_subtract(v, project(v, w))
}

function  remove_projection(x_matrix, w) {
    /*
    for each row of X
    projects the row onto w, and subtracts the result from the row
    */
    return [remove_projection_from_vector(x_i, w) for x_i in x_matrix]
}

function  principal_component_analysis(x_vector, num_components) {
    components = []
    for _ in range(num_components):
        component = first_principal_component(x_vector)
        components.append(component)
        x_vector = remove_projection(x_vector, component)

    return components
}

function  transform_vector(v, components) {
    return [dot(v, w) for w in components]
}

function  transform(x_vector, components) {
    return [transform_vector(x_i, components) for x_i in x_vector]
}