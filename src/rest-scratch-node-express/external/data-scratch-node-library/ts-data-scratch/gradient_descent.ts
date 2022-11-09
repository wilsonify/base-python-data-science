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


