import {
    bernoulli_trial,
    binomial,
    inverse_normal_cdf,
    normal_cdf,
    normal_pdf,
    random_kid,
    uniform_cdf,
    uniform_pdf,    

} from "../probability";

interface Ibernoulli_trial {
    p: number;
}

const bernoulli_trial_strategy = (body: Ibernoulli_trial) => new Promise(
    async (resolve, reject) => {
        try {
            var p = body.p
            var result = bernoulli_trial(p)
            resolve(console.log(result))
        } catch (e) {
            reject(
                console.log(`unable to resolve bernoulli_trial ${e}`)
            );
        }
    }
)

interface Ibinomial {
    p: number;
    n: number;
}

const binomial_strategy = (body: Ibinomial) => new Promise(
    async (resolve, reject) => {
        try {
            var p = body.p
            var n = body.n
            var result = binomial(p, n)
            resolve(console.log(result))
        } catch (e) {
            reject(
                console.log(`unable to resolve binomial ${e}`)
            );
        }
    }
)
interface Iinverse_normal_cdf {
    p: number;
    mu: number;
    sigma: number;
}

const inverse_normal_cdf_strategy = (body: Iinverse_normal_cdf) => new Promise(
    async (resolve, reject) => {
        try {
            var p = body.p
            var mu = body.mu
            var sigma = body.sigma
            var result = inverse_normal_cdf(p, mu, sigma)
            resolve(console.log(result))
        } catch (e) {
            reject(
                console.log(`unable to resolve inverse_normal_cdf ${e}`)
            );
        }
    }
)
interface Inormal_cdf {
    x: number;
    mu: number;
    sigma: number;
}

const normal_cdf_strategy = (body: Inormal_cdf) => new Promise(
    async (resolve, reject) => {
        try {
            var x = body.x
            var mu = body.mu
            var sigma = body.sigma
            var result = normal_cdf(x, mu, sigma)
            resolve(console.log(result))
        } catch (e) {
            reject(
                console.log(`unable to resolve normal_cdf ${e}`)
            );
        }
    }
)
interface Inormal_pdf {
    x: number;
    mu: number;
    sigma: number;
}

const normal_pdf_strategy = (body: Inormal_pdf) => new Promise(
    async (resolve, reject) => {
        try {
            var x = body.x
            var mu = body.mu
            var sigma = body.sigma
            var result = normal_pdf(x, mu, sigma)
            resolve(console.log(result))
        } catch (e) {
            reject(
                console.log(`unable to resolve normal_pdf ${e}`)
            );
        }
    }
)

const random_kid_strategy = () => new Promise(
    async (resolve, reject) => {
        try {
            var result = random_kid()
            resolve(console.log(result))
        } catch (e) {
            reject(
                console.log(`unable to resolve random_kid ${e}`)
            );
        }
    }
)

interface Iuniform_cdf {
    x: number;
}

const uniform_cdf_strategy = (body: Iuniform_cdf) => new Promise(
    async (resolve, reject) => {
        try {
            var x = body.x
            var result = uniform_cdf(x)
            resolve(console.log(result))
        } catch (e) {
            reject(
                console.log(`unable to resolve uniform_cdf ${e}`)
            );
        }
    }
)

interface Iuniform_pdf {
    x: number;
}

const uniform_pdf_strategy = (body: Iuniform_pdf) => new Promise(
    async (resolve, reject) => {
        try {
            var x = body.x
            var result = uniform_pdf(x)
            resolve(console.log(result))
        } catch (e) {
            reject(
                console.log(`unable to resolve uniform_pdf ${e}`)
            );
        }
    }
)