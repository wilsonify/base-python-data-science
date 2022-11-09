"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.sqrt_newton = void 0;
function sqrt_newton(x) {
    console.log("Newton Method Square Root");
    const eps = 0.001;
    if (x == 0.0) {
        return 0.0;
    }
    var isGoodEnough = function (guess) {
        return Math.abs(guess * guess - x) / (x + eps) < 0.001;
    };
    var improve = function (guess) {
        return (guess + x / (guess + eps)) / 2;
    };
    var sqrIter = function (guess) {
        return (isGoodEnough(guess)) ? guess : sqrIter(improve(guess));
    };
    return sqrIter(1.0);
}
exports.sqrt_newton = sqrt_newton;
;
