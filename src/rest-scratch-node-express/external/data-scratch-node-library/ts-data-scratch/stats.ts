import { sum_of_squares, dot, shape, get_column, make_matrix } from "./linear_algebra"
import { NumericFunction, BivaritateFunction,  NumericArray, NumericArrayFunction } from "./type-helpers"


export function bucketize(point: number, bucket_size: number): number {
    // floor the point to the next lower multiple of bucket_size
    return bucket_size * Math.floor(point / bucket_size);
}


export function Counter(array: Array<number>) {
    let count = new Map<string, number>();
    for (var i = 0; i < array.length; i += 1) {
        var val = array[i].toString()
        var prev = count.get(val) || 0;
        count.set(val, prev + 1)
    }
    return count;
}

export function make_histogram(points: Array<number>, bucket_size: number) {
    // buckets the points and counts how many in each bucket
    var counting = [];
    for (var point, _pj_c = 0, _pj_a = points, _pj_b = _pj_a.length; _pj_c < _pj_b; _pj_c += 1) {
        point = _pj_a[_pj_c];
        counting.push(bucketize(point, bucket_size));
    }
    var result = Counter(counting);

    return result;
}


export function correlation_matrix(data: Array<Array<number>>) {
    //returns the num_columns x num_columns matrix whose (i, j)th entry is the correlation between columns i and j of data
    var _, num_columns;
    [_, num_columns] = shape(data);

    function matrix_entry(i:number, j:number) {
        return correlation(get_column(data, i), get_column(data, j));
    }

    return make_matrix(num_columns, num_columns, matrix_entry);
}


export function summation(x: Array<number>): number {
    return x.reduce((a, b) => a + b, 0)
}

export function mean(x: Array<number>): number {
    return summation(x) / x.length;
}

export function median(v: Array<number>): number {
    //finds the 'middle-most' value of v by binary search
    var hi, lo, midpoint, n, sorted_v;
    n = v.length;
    sorted_v = v.sort();
    midpoint = Math.floor(n / 2);

    if (n % 2 === 1) {
        return sorted_v[midpoint];
    } else {
        lo = midpoint - 1;
        hi = midpoint;
        return (sorted_v[lo] + sorted_v[hi]) / 2;
    }
}


export function quantile(x: Array<number>, p: number): number {
    // returns the pth-percentile value in x
    var p_index = Math.floor(p * x.length)
    return x.sort()[p_index]
}


export function mode(x: Array<number>): Array<number> {
    // returns a list, might be more than one mode
    var counts = Counter(x)
    var max_count = Math.max(...counts.values())
    var result = [];
    for (let [key, value] of counts) {
        if (value === max_count) {
            result.push(Number(key));
        }
    }
    return result

}

export function data_range(x:Array<number>) {
    // "range" already means something in Python, so we'll use a different name
    return Math.max(...x) - Math.min(...x)
}


export function de_mean(x: Array<number>) {
    // translate x by subtracting its mean (so the result has mean 0)
    var x_bar = mean(x);
    var result = [];
    for (var i = 0; i < x.length; i += 1) {
        var x_i = x[i]
        result.push(x_i - x_bar)
    }
    return result
}


export function variance(x: Array<number>) {
    var n = x.length
    if (n < 2) {
        return NaN
    }
    var deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)
}


export function standard_deviation(x: Array<number>) {
    return Math.sqrt(variance(x))
}

export function interquartile_range(x: Array<number>) {
    return quantile(x, 0.75) - quantile(x, 0.25)
}

// CORRELATION

export function covariance(x: Array<number>, y: Array<number>) {
    var n = x.length
    if (n < 2) {
        return NaN
    }
    return dot(de_mean(x), de_mean(y)) / (n - 1)
}

export function correlation(x: Array<number>, y: Array<number>) {
    var n = x.length
    if (n < 2) {
        return NaN
    }
    var n2 = y.length
    if (n2 < 2) {
        return NaN
    }
    var eps = 0.0001
    var stdev_x = standard_deviation(x)
    var stdev_y = standard_deviation(y)
    var divisor = (stdev_x * stdev_y) + eps
    return covariance(x, y) / divisor
}

