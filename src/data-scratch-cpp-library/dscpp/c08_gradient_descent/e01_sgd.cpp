#include <iostream>
#include <random>
#include <vector>
#include "gradient_descent.h"
#include "../c04_linear_algebra/linear_algebra.h"

int main() {
    std::mt19937 rng(42);
    std::uniform_int_distribution<int> dist(-10, 10);

    std::vector<double> v = {
        static_cast<double>(dist(rng)),
        static_cast<double>(dist(rng)),
        static_cast<double>(dist(rng))
    };

    double tolerance = 0.0000001;
    int max_iter = 1000;

    std::cout << "using the gradient\n";
    for (int i = 0; i < max_iter; ++i) {
        auto gradient = sum_of_squares_gradient(v);
        auto next_v = grad_step(v, gradient, -0.01);
        if (distance(next_v, v) < tolerance)
            break;
        v = next_v;
    }

    std::cout << "minimum v:";
    for (double vi : v) std::cout << " " << vi;
    std::cout << "\n";
    std::cout << "minimum value: " << sum_of_squares(v) << "\n";

    std::cout << "using minimize_batch\n";
    rng.seed(42);
    v = {
        static_cast<double>(dist(rng)),
        static_cast<double>(dist(rng)),
        static_cast<double>(dist(rng))
    };

    v = minimize_batch(
        [](const std::vector<double>& x) { return sum_of_squares(x); },
        sum_of_squares_gradient,
        v
    );

    std::cout << "minimum v =";
    for (double vi : v) std::cout << " " << vi;
    std::cout << "\n";
    std::cout << "minimum value = " << sum_of_squares(v) << "\n";

    return 0;
}
