import { NumericFunction, BivaritateFunction,  NumericArray, NumericArrayFunction } from "./type-helpers"

function erf(x: number) {
    var a1 = 0.254829592;
    var a2 = -0.284496736;
    var a3 = 1.421413741;
    var a4 = -1.453152027;
    var a5 = 1.061405429;
    var p = 0.3275911;
    var sign = 1;
    if (x < 0) { sign = -1; }
    x = Math.abs(x);
    var t = 1.0 / (1.0 + p * x);
    var y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * Math.exp(-x * x);
    return sign * y;
}

function uniform_pdf(x: number, a = 0, b = 1) {
    return a <= x && x < b ? 1 / (b - a) : 0;
}

function uniform_cdf(x: number, a = 0, b = 1) {
    /* returns the probability that a uniform random variable is less than x */
    if (x < a) {
        return 0;
    }

    if (a < x && x < b) {
        return (x - a) / (b - a);
    }

    if (b <= x) {
        return 1;
    }
}

function normal_pdf(x: number, mu = 0, sigma = 1) {
    var sqrt_two_pi;
    sqrt_two_pi = Math.sqrt(2 * Math.PI);
    return Math.exp(-Math.pow(x - mu, 2) / 2 / Math.pow(sigma, 2)) / (sqrt_two_pi * sigma);
}

function normal_cdf(x: number, mu = 0.0, sigma = 1.0) {
    return (1.0 + erf((x - mu) / Math.sqrt(2.0) / sigma)) / 2.0;
}

function inverse_normal_cdf(p: number, mu = 0, sigma = 1, tolerance = 1e-05) {
    /* find approximate inverse using binary search */
    var hi_p, hi_z, low_p, low_z, mid_p, mid_z;

    [low_z, low_p] = [-10.0, 0];
    [hi_z, hi_p] = [10.0, 1];
    mid_z = (low_z + hi_z) / 2;

    while (hi_z - low_z > tolerance) {
        mid_z = (low_z + hi_z) / 2;
        mid_p = normal_cdf(mid_z);

        if (mid_p < p) {
            [low_z, low_p] = [mid_z, mid_p];
        } else {
            if (mid_p > p) {
                [hi_z, hi_p] = [mid_z, mid_p];
            } else {
                break;
            }
        }
    }

    return mid_z;
}



function random_choice(choices: Array<string>) {
    var index = Math.floor(Math.random() * choices.length);
    return choices[index];
}

function random_kid() {
    return random_choice(["boy", "girl"])
}

function random_normal() {
    //"""returns a random draw from a standard normal distribution"""
    return inverse_normal_cdf(Math.random())
}


function bernoulli_trial(p: number) {
    var result = 0;
    if (Math.random() < p) {
        result = 1;
    }
    return result
}

function binomial(p: number, n: number) {
    var result = 0;
    for (var i = 0; i < n; i += 1) {
        result += bernoulli_trial(p)
    }
    return result
}
