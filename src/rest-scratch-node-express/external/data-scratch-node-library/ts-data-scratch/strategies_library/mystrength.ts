import { getStrength } from "../signal-strength";

/*
//    actual = body["actual"]
//    expected = body["expected"]
//    strength = mystrength(actual, expected)
//    out_dict = dict(
//        actual=actual,
//        expected=expected,
//        strength=strength,
//    )
*/
interface IstrengthInput {
    actual: number;
    expected: number;
}

const strength = (strengthInput: IstrengthInput) => new Promise(
    async (resolve, reject) => {
        try {
            console.log("strength")
            console.log("strengthInput = ", strengthInput)
            var actual = strengthInput.actual;
            var expected = strengthInput.expected;
            var strength = getStrength(actual, expected);
            var payload = {
                "expected": expected,
                "actual": actual,
                "strength": strength
            };
            console.log("payload = ", payload)
            resolve(console.log(payload));
        } catch (e) {
            reject(
                console.log(`unable to resolve getStrength ${e}`)
            );
        }
    },
);
