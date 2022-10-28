export function sqrt_newton(x: number): number {
    // Newton Method Square Root
    var isGoodEnough = function (guess: number) {
        return Math.abs(guess * guess - x) / x < 0.001;
    };

    var improve = function (guess: number): number {
        return (guess + x / guess) / 2;
    };

    var sqrIter = function (guess: number): number {
        return (isGoodEnough(guess)) ? guess : sqrIter(improve(guess))
    };

    return sqrIter(1.0);
};
