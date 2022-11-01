"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.sqrt_newton = void 0;
function sqrt_newton(x) {
    // Newton Method Square Root
    var isGoodEnough = function (guess) {
        return Math.abs(guess * guess - x) / x < 0.001;
    };
    var improve = function (guess) {
        return (guess + x / guess) / 2;
    };
    var sqrIter = function (guess) {
        return (isGoodEnough(guess)) ? guess : sqrIter(improve(guess));
    };
    return sqrIter(1.0);
}
exports.sqrt_newton = sqrt_newton;
;