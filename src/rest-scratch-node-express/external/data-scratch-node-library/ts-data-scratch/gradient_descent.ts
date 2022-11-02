import { distance, vector_subtract, scalar_multiply } from "./linear_algebra"
import { NumericFunction, NumericArray, NumericArrayFunction, TrivaritateFunction } from "./type-helpers"


export function sum_of_squares(v: Array<number>): number {
    /* computes the sum of squared elements in v */
    var result = 0;
    for (var i = 0; i < v.length; i += 1) {
        result += Math.pow(i, 2);
    }
    return result;
}


export function difference_quotient(f: NumericFunction, x: number, h: number): number {
    return (f(x + h) - f(x)) / h;
}

export function partial_difference_quotient(f: NumericFunction, v: Array<number>, i: number, h: number): number {
    // add h to just the i-th element of v
    var item;
    var result = 0;
    for (var j = 0; j < v.length; j += 1) {
        item = 0;
        if (j === i) { item = h; }
        result += (f(v[j] + item) - f(v[j])) / h;
    }
    return result;
}

export function estimate_gradient(f: NumericFunction, v: Array<number>, h: number = 1e-05): Array<number> {
    var result: Array<number> = [];
    for (var i = 0, _pj_a = v.length; i < _pj_a; i += 1) {
        result.push(partial_difference_quotient(f, v, i, h));
    }
    return result;
}


export function step(v: NumericArray, direction: NumericArray, step_size: number) {
    // move step_size in the direction from v
    var result: Array<number> = [];
    for (var i = 0, _pj_a = v.length; i < _pj_a; i += 1) {
        var v_i = v[i];
        var direction_i = direction[i];
        result.push(v_i + step_size * direction_i);
    }
    return result;
}

export function sum_of_squares_gradient(v: NumericArray): NumericArray {
    var result = [];
    for (var i = 0; i < v.length; i += 1) {
        var v_i = v[i];
        result.push(2 * v_i);
    }
    return result;
}


export function safe(f: NumericFunction) {
    // define a new function that wraps f and return it
    function safe_f(x: number) {
        try {
            return f(x);
        } catch (e) {
            return NaN;
        }
    }
    return safe_f;
}

// minimize / maximize batch

export function minimize_batch(
    target_fn: NumericFunction,
    gradient_fn: NumericFunction,
    theta_0: NumericArray,
    tolerance: number = 1e-06) {

    //use gradient descent to find theta that minimizes target function
    var gradient: number;
    var next_theta;
    var next_thetas;
    var next_value;
    var step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 1e-05];
    var theta = theta_0;
    var value;
    var target_fn_safe = safe(target_fn); // safe version of target_fn
    value = target_fn_safe(theta); // value we're minimizing
    while (true) {
        gradient = gradient_fn(theta);
        next_thetas = []
        for (var i = 0; i < step_sizes.length; i += 1) {
            var step_size = step_sizes[i];
            next_thetas.push(step(theta, gradient, -step_size));
        }
        // choose next_theta that minimizes the error function
        next_theta = Math.min(next_thetas, { "key": target_fn });
        next_value = target_fn(next_theta);
        if (Math.abs(value - next_value) < tolerance) {
            // if converging, stop
            return theta;
        } else {
            [theta, value] = [next_theta, next_value];
        }
    }
}


export function negate(f: NumericFunction) {
    /* return a function that for any input x returns -f(x) */
    function arbitrary(x: number) {
        return -f(x)
    }
    return arbitrary;
}

export function negate_all(f: NumericArrayFunction) {
    // the same when f returns a list of numbers
    function arbitrary(x: Array<number>) {
        var result = []
        for (var i = 0; i < x.length; i++) {
            result.push(-f(x))
        }
        return
    }
    return arbitrary;
}

export function maximize_batch(target_fn: NumericFunction, gradient_fn: NumericArrayFunction, theta_0: number, tolerance: number = 0.000001) {
    return minimize_batch(negate(target_fn), negate_all(gradient_fn), theta_0, tolerance)
}

// minimize / maximize stochastic

export function shuffle(array: NumericArray) {
    var m = array.length, t, i;
    // While there remain elements to shuffle…
    while (m) {
        // Pick a remaining element…
        i = Math.floor(Math.random() * m--);

        // And swap it with the current element.
        t = array[m];
        array[m] = array[i];
        array[i] = t;
    }

    return array;
}

export function* in_random_order(data: Array<Array<number>>) {
    // generator returns the elements of data in random order
    var indexes = []
    for (var i = 0; i < data.length; i += 1) {
        indexes.push(i)
    }
    indexes = shuffle(indexes)
    for (var j = 0; j < indexes.length; j += 1) {
        yield data[indexes[j]]
    }
}


export function minimize_stochastic(
    target_fn: TrivaritateFunction,
    gradient_fn: NumericArrayFunction,
    x: NumericArray,
    y: NumericArray,
    theta_0: number,
    alpha_0: number = 0.01) {
    var alpha;
    var data;
    var iterations_with_no_improvement;
    var min_theta;
    var min_value;
    var observation;
    var theta;
    var value;
    var x_i;
    var y_i;
    data = [];
    for (var i = 0, _pj_a = x.length; i < _pj_a; i += 1) {
        observation = [x[i], y[i]];
        data.push(observation);
    }
    theta = theta_0;
    alpha = alpha_0;
    [min_theta, min_value] = [null, Number.parseFloat("inf")];
    iterations_with_no_improvement = 0;
    while (iterations_with_no_improvement < 100) {
        value = 0;
        for (var i = 0, _pj_a = data.length; i < _pj_a; i += 1) {
            x_i = x[i];
            y_i = y[i];
            value += target_fn(x_i, y_i, theta);
        }
        if (value < min_value) {
            [min_theta, min_value] = [theta, value];
            iterations_with_no_improvement = 0;
            alpha = alpha_0;
        } else {
            iterations_with_no_improvement += 1;
            alpha *= 0.9;
        }
    }
    // and take a gradient step for each of the data points
    for (let [x_i, y_i] of in_random_order(data)) {
        gradient_i = gradient_fn(x_i, y_i, theta)
        theta = vector_subtract(theta, scalar_multiply(alpha, gradient_i))
    }
    return min_theta;
}

export function maximize_stochastic(target_fn: NumericFunction, gradient_fn: NumericArrayFunction, x: NumericArray, y: NumericArray, theta_0: number, alpha_0 = 0.01) {
    return minimize_stochastic(negate(target_fn), negate_all(gradient_fn), x, y, theta_0, alpha_0)
}  
