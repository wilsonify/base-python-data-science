import { sum_of_squares } from "../linear_algebra";
import { bucketize, correlation, correlation_matrix, covariance, data_range, de_mean, interquartile_range, mean, median, mode, quantile, standard_deviation, variance } from "../stats"

interface Ibucketize {
    point: any;
    bucket_size: any;
}

const bucketize_strategy = (body: Ibucketize) => new Promise(
    async (resolve, reject) => {
        try {
            var point = body.point
            var bucket_size = body.bucket_size
            var result = bucketize(point, bucket_size)
            resolve(console.log(result))
        } catch (e) {
            reject(
                console.log(`unable to resolve bucketize ${e}`)
            );
        }
    }
)

const correlation_matrix_strategy = (body: { data: any; }) => new Promise(
    async (resolve, reject) => {
        try {
            var data = body.data
            var result = correlation_matrix(data)
            resolve(console.log(result))
        } catch (e) {
            reject(
                console.log(`unable to resolve correlation_matrix ${e}`)
            );
        }
    }
)

const correlation_strategy = (body: { x: any; y: any; }) => new Promise(
    async (resolve, reject) => {
        try {
            var x = body.x
            var y = body.y
            var result = correlation(x, y)
            resolve(console.log(result))
        } catch (e) {
            reject(
                console.log(`unable to resolve correlation ${e}`)
            );
        }
    }
)

const covariance_strategy = (body: { x: any; y: any; }) => new Promise(
    async (resolve, reject) => {
        try {
            var x = body.x
            var y = body.y
            var result = covariance(x, y)
            resolve(console.log(result))
        } catch (e) {
            reject(
                console.log(`unable to resolve covariance ${e}`)
            );
        }
    }
)

const data_range_strategy = (body: { x: any; }) => new Promise(
    async (resolve, reject) => {
        try {
            var x = body.x
            var result = data_range(x)
            resolve(console.log(result))
        } catch (e) {
            reject(
                console.log(`unable to resolve data_range ${e}`)
            );
        }
    }
)

const de_mean_strategy = (body: { x: any; }) => new Promise(
    async (resolve, reject) => {
        try {
            var x = body.x
            var result = de_mean(x)
            resolve(console.log(result))
        } catch (e) {
            reject(
                console.log(`unable to resolve de_mean ${e}`)
            );
        }
    }
)

const interquartile_range_strategy = (body: { x: any; }) => new Promise(
    async (resolve, reject) => {
        try {
            var x = body.x
            var result = interquartile_range(x)
            resolve(console.log(result))
        } catch (e) {
            reject(
                console.log(`unable to resolve interquartile_range ${e}`)
            );
        }
    }
)

const mean_strategy = (body: { x: any; }) => new Promise(
    async (resolve, reject) => {
        try {
            var x = body.x
            var result = mean(x)
            resolve(console.log(result))
        } catch (e) {
            reject(
                console.log(`unable to resolve mean ${e}`)
            );
        }
    }
)

const median_strategy = (body: { x: any; }) => new Promise(
    async (resolve, reject) => {
        try {
            var x = body.x
            var result = median(x)
            resolve(console.log(result))

        } catch (e) {
            reject(
                console.log(`unable to resolve median ${e}`)
            );
        }
    }
)

const mode_strategy = (body: { x: any; }) => new Promise(
    async (resolve, reject) => {
        try {
            var x = body.x
            var result = mode(x)
            resolve(console.log(result))
        } catch (e) {
            reject(
                console.log(`unable to resolve mode ${e}`)
            );
        }
    }
)

const quantile_strategy = (body: { x: any; p: any; }) => new Promise(
    async (resolve, reject) => {
        try {
            var x = body.x
            var p = body.p
            var result = quantile(x, p)
            resolve(console.log(result))

        } catch (e) {
            reject(
                console.log(`unable to resolve quantile ${e}`)
            );
        }
    }
)

const standard_deviation_strategy = (body: { x: any; }) => new Promise(
    async (resolve, reject) => {
        try {
            var x = body.x
            var result = standard_deviation(x)
            resolve(console.log(result))
        } catch (e) {
            reject(
                console.log(`unable to resolve standard_deviation ${e}`)
            );
        }
    }
)

const sum_of_squares_strategy = (body: { x: any; }) => new Promise(
    async (resolve, reject) => {
        try {
            var x = body.x
            var result = sum_of_squares(x)
            resolve(console.log(result))
        } catch (e) {
            reject(
                console.log(`unable to resolve sum_of_squares ${e}`)
            );
        }
    }
)

const variance_strategy = (body: { x: any; }) => new Promise(
    async (resolve, reject) => {
        try {
            var x = body.x
            var result = variance(x)
            resolve(console.log(result))
        } catch (e) {
            reject(
                console.log(`unable to resolve variance ${e}`)
            );
        }
    }
)
