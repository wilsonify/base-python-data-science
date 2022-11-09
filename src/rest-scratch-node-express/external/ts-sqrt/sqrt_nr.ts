export function sqrt_newton(x: number): number {
    console.log("Newton Method Square Root")
    const eps = 0.001
    if (x == 0.0) {
        return 0.0
    }
    var isGoodEnough = function (guess: number) {
        return Math.abs(guess * guess - x) / (x + eps) < 0.001;
    };

    var improve = function (guess: number): number {
        return (guess + x / (guess + eps)) / 2;
    };

    var sqrIter = function (guess: number): number {
        return (isGoodEnough(guess)) ? guess : sqrIter(improve(guess))
    };

    return sqrIter(1.0);
};
