import { difference_quotient, estimate_gradient, in_random_order, partial_difference_quotient } from "../gradient_descent";
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
