export function erf(x: number) {
    if (typeof (Math as any).erf === 'function') {
        return (Math as any).erf(x);
    }

    const a1 = 0.254829592;
    const a2 = -0.284496736;
    const a3 = 1.421413741;
    const a4 = -1.453152027;
    const a5 = 1.061405429;
    const p = 0.3275911;
    let sign = 1;
    if (x < 0) {
        sign = -1;
    }
    x = Math.abs(x);
    const t = 1 / (1 + p * x);
    const y = 1 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * Math.exp(-x * x);
    return sign * y;
}

export function uniform_pdf(x: number, a = 0, b = 1) {
    return a <= x && x < b ? 1 / (b - a) : 0;
}

export function uniform_cdf(x: number, a = 0, b = 1) {
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

export function normal_pdf(x: number, mu = 0, sigma = 1) {
    const sqrt_two_pi = Math.sqrt(2 * Math.PI);
    return Math.exp(-Math.pow(x - mu, 2) / 2 / Math.pow(sigma, 2)) / (sqrt_two_pi * sigma);
}

export function normal_cdf(x: number, mu = 0, sigma = 1) {
    if (sigma <= 0) {
        throw new Error('Standard deviation must be positive');
    }
    return (1 + erf((x - mu) / Math.sqrt(2) / sigma)) / 2;
}

export function inverse_normal_cdf(p: number, mu = 0, sigma = 1, tolerance = 1e-5) {
    if (p < 0 || p > 1) {
        throw new Error('Probability must be between 0 and 1');
    }
    if (sigma <= 0) {
        throw new Error('Standard deviation must be positive');
    }

    let hi_z: number, low_z: number, mid_z: number, mid_p: number;

    low_z = -10;
    hi_z = 10;
    mid_z = (low_z + hi_z) / 2;

    while (hi_z - low_z > tolerance) {
        mid_z = (low_z + hi_z) / 2;
        mid_p = normal_cdf(mid_z, mu, sigma);

        if (mid_p < p) {
            low_z = mid_z;
        } else if (mid_p > p) {
            hi_z = mid_z;
        } else {
            break;
        }
    }

    return mid_z;
}



export function random_choice(choices: Array<string>) {
    if (choices.length === 0) {
        throw new Error('Choices cannot be empty');
    }
    const index = Math.floor(Math.random() * choices.length);
    return choices[index];
}

export function random_kid() {
    return random_choice(["boy", "girl"]);
}

export function random_normal() {
    //"""returns a random draw from a standard normal distribution"""
    return inverse_normal_cdf(Math.random())
}


export function bernoulli_trial(p: number) {
    if (p < 0 || p > 1) {
        throw new Error('Probability must be between 0 and 1');
    }
    return Math.random() < p ? 1 : 0;
}

export function binomial(n: number, p: number) {
    if (n < 0 || p < 0 || p > 1) {
        throw new Error('Invalid parameters for binomial');
    }
    let result = 0;
    for (let i = 0; i < n; i += 1) {
        result += bernoulli_trial(p);
    }
    return result;
}

function choose(n: number, k: number): number {
    if (k < 0 || k > n) {
        return 0;
    }
    if (k === 0 || k === n) {
        return 1;
    }
    let numerator = 1;
    let denominator = 1;
    for (let i = 1; i <= k; i += 1) {
        numerator *= n - (k - i);
        denominator *= i;
    }
    return numerator / denominator;
}

export function binomial_distribution(n: number, p: number): number[] {
    if (n < 0 || p < 0 || p > 1) {
        throw new Error('Invalid parameters for binomial distribution');
    }
    const pmf: number[] = [];
    for (let k = 0; k <= n; k += 1) {
        pmf.push(choose(n, k) * Math.pow(p, k) * Math.pow(1 - p, n - k));
    }
    return pmf;
}

export function normal_probability_below(x: number, mu = 0, sigma = 1) {
    return normal_cdf(x, mu, sigma);
}

export function normal_probability_above(x: number, mu = 0, sigma = 1) {
    return 1 - normal_probability_below(x, mu, sigma);
}

export function normal_probability_between(lower: number, upper: number, mu = 0, sigma = 1) {
    return normal_probability_below(upper, mu, sigma) - normal_probability_below(lower, mu, sigma);
}

export function normal_upper_bound(prob: number, mu = 0, sigma = 1) {
    return inverse_normal_cdf(prob, mu, sigma);
}

export function normal_lower_bound(prob: number, mu = 0, sigma = 1) {
    return inverse_normal_cdf(1 - prob, mu, sigma);
}

export function normal_two_sided_bounds(prob: number, mu = 0, sigma = 1): [number, number] {
    const tailProbability = (1 - prob) / 2;
    return [
        normal_lower_bound(1 - tailProbability, mu, sigma),
        normal_upper_bound(1 - tailProbability, mu, sigma),
    ];
}
