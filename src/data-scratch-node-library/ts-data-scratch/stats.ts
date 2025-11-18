import { sum_of_squares, dot, shape, get_column, make_matrix } from "./linear_algebra"
import { NumericFunction, BivaritateFunction,  NumericArray, NumericArrayFunction } from "./type-helpers"


export function bucketize(point: number, bucket_size: number): number {
    // floor the point to the next lower multiple of bucket_size
    return bucket_size * Math.floor(point / bucket_size);
}


export function Counter(array: Array<number>) {
    let count = new Map<string, number>();
    for (const v of array) {
        const val = v.toString();
        const prev = count.get(val) || 0;
        count.set(val, prev + 1);
    }
    return count;
}

export function make_histogram(points: Array<number>, bucket_size: number) {
    // buckets the points and counts how many in each bucket
    const counting: number[] = [];
    for (const point of points) {
        counting.push(bucketize(point, bucket_size));
    }
    const result = Counter(counting);

    return result;
}


export function correlation_matrix(data: Array<Array<number>>) {
    //returns the num_columns x num_columns matrix whose (i, j)th entry is the correlation between columns i and j of data
    const [, num_columns] = shape(data);

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
    let hi: number, lo: number, midpoint: number;
    const n = v.length;
    const sorted_v = v.slice().sort((a, b) => a - b);
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
    const p_index = Math.floor(p * x.length)
    return x.slice().sort((a, b) => a - b)[p_index]
}


export function mode(x: Array<number>): Array<number> {
    // returns a list, might be more than one mode
    const counts = Counter(x)
    const max_count = Math.max(...counts.values())
    const result: number[] = [];
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
    const x_bar = mean(x);
    const result: number[] = [];
    for (const x_i of x) {
        result.push(x_i - x_bar);
    }
    return result
}


export function variance(x: Array<number>) {
    const n = x.length
    if (n < 2) {
        return Number.NaN
    }
    const deviations = de_mean(x)
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
    const n = x.length
    if (n < 2) {
        return Number.NaN
    }
    return dot(de_mean(x), de_mean(y)) / (n - 1)
}

export function correlation(x: Array<number>, y: Array<number>) {
    const n = x.length
    if (n < 2) {
        return Number.NaN
    }
    const n2 = y.length
    if (n2 < 2) {
        return Number.NaN
    }
    const eps = 0.0001
    const stdev_x = standard_deviation(x)
    const stdev_y = standard_deviation(y)
    const divisor = (stdev_x * stdev_y) + eps
    return covariance(x, y) / divisor
}

