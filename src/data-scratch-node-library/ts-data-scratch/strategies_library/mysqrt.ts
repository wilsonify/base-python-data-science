import { sqrt_newton } from "../sqrt_nr";

/**
* Description of the endpoint
*
* sqrtInput SqrtInput  (optional)
* returns sqrt-output
* */
interface IsqrtInput {
    x: number;
}

const sqrt = (sqrtInput: IsqrtInput) => new Promise(
    async (resolve, reject) => {
        try {
            console.log("sqrt")
            console.log("sqrtInput = ", sqrtInput)
            var result = sqrt_newton(sqrtInput.x);
            console.log("result  = ", result)
            resolve(console.log({
                "result": result,
                "x": sqrtInput.x,
            }));
        } catch (e) {
            reject(
                console.error(`unable to resolve sqrt_newton ${e}`)
            );
        }
    },
);




