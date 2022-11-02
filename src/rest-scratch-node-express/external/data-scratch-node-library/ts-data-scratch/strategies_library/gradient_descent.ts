import { difference_quotient, estimate_gradient, in_random_order, minimize_stochastic, partial_difference_quotient } from "../gradient_descent";
import { dot } from "../linear_algebra";

interface Idifference_quotient {
    x: number;
    h: number;
}
const difference_quotient_strategy = (body: Idifference_quotient) => new Promise(
    async (resolve, reject) => {
        try {
            var x = body.x;
            var h = body.h;
            var result = difference_quotient((xi: number) => xi * xi, x, h);
            resolve(
                console.log(result)
            );
        } catch (e) {
            reject(
                console.error(`unable to resolve difference_quotient ${e}`)
            );
        }
    }
);

interface Ipartial_difference_quotient {
    v: any;
    i: any;
    h: any;
}
const partial_difference_quotient_strategy = (body: Ipartial_difference_quotient) => new Promise(
    async (resolve, reject) => {
        try {
            var v = body.v
            var i = body.i
            var h = body.h
            var output = partial_difference_quotient((xi: number) => xi * xi, v, i, h)
            resolve(
                console.log(output)
            );
        } catch (e) {
            reject(
                console.error(`unable to resolve difference_quotient ${e}`)
            );
        }
    })

interface Iestimate_gradient { v: any; h: any; }
const estimate_gradient_strategy = (body: Iestimate_gradient) => new Promise(
    async (resolve, reject) => {
        try {
            var v = body.v
            var h = body.h
            var output = estimate_gradient((xi: number[]) => dot(xi, xi), v, h)
            resolve(
                console.log(output)
            );
        } catch (e) {
            reject(
                console.error(`unable to resolve difference_quotient ${e}`)
            );
        }
    })

interface Iin_random_order { data: any; }
const in_random_order_strategy = (body: Iin_random_order) => new Promise(
    async (resolve, reject) => {
        try {
            var data = body.data
            var output = []
            for (var i = 0; i < data.length; i += 1) {
                output.push(in_random_order(data))
            }
            resolve(
                console.log(output)
            );
        } catch (e) {
            reject(
                console.error(`unable to resolve difference_quotient ${e}`)
            );
        }
    }
)
interface Imaximize_batch { x: any; }
const maximize_batch_strategy = (body: Imaximize_batch) => new Promise(
    async (resolve, reject) => {
        try {
            var x = body.x
            var target_fn = partial(directional_variance, x)
            var gradient_fn = partial(directional_variance_gradient, x)
            var theta_0 = [1 for _ in x[0]]
            var tolerance = 0.000001
            var result = gradient_descent.maximize_batch()
            resolve(
                console.log(result)
            );
        } catch (e) {
            reject(
                console.error(`unable to resolve difference_quotient ${e}`)
            );
        }
    })

interface Imaximize_stochastic { x: any; y: any; }
const maximize_stochastic_strategy = (body: Imaximize_stochastic) => new Promise(
    async (resolve, reject) => {
        try {
            var x = body.x
            var y = body.y
            var target_fn = negate(multiple_regression.squared_error),
            var gradient_fn = negate_all(multiple_regression.squared_error_gradient),
            var x = x,
            var y = y,
            var theta_0 = [random.random() for _ in x[0]],
            var alpha_0 = 0.01
            var result = gradient_descent.maximize_stochastic()
            resolve(
                console.log(result)
            );
        } catch (e) {
            reject(
                console.error(`unable to resolve difference_quotient ${e}`)
            );
        }
    })

interface Iminimize_batch { x: any; }
const minimize_batch_strategy = (body: Iminimize_batch) => new Promise(
    async (resolve, reject) => {
        try {
            var x = body.x
            var target_fn = partial(directional_variance, x)
            var gradient_fn = partial(directional_variance_gradient, x)
            var theta_0 = [1 for _ in x[0]]
            var tolerance = 0.000001theta_0 = [1 for _ in x[0]]
            var tolerance = 0.000001
            var result = minimize_batch()
            resolve(
                console.log(result)
            );
        } catch (e) {
            reject(
                console.error(`unable to resolve difference_quotient ${e}`)
            );
        }
    })
interface Iminimize_stochastic { x: any; y: any; }
const minimize_stochastic_strategy = (body: Iminimize_stochastic) => new Promise(
    async (resolve, reject) => {
        try {
            var x = body.x
            var y = body.y
            var target_fn = negate(multiple_regression.squared_error),
            var gradient_fn = negate_all(multiple_regression.squared_error_gradient),
            var x = x,
            var y = y,
            var theta_0 = [random.random() for _ in x[0]],
            var alpha_0 = 0.01
            var result = minimize_stochastic()
            resolve(
                console.log(result)
            );
        } catch (e) {
            reject(
                console.error(`unable to resolve difference_quotient ${e}`)
            );
        }
    })