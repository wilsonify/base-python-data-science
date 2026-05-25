#include "strength.h"
#include <ranges>

double strength(double actual, double expected)
{
    double result;
    double eps = 0.001;
    result = actual / (expected + eps);
    return result;
}

std::vector<double> strength_vector(std::vector<double> actual, std::vector<double> expected)
{
    std::vector<double> result;
    result.resize(expected.size());
    std::ranges::transform(
        expected, actual,
        result.begin(),
        strength
        );
    return result;
}
