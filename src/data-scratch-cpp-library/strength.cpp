#include <algorithm>

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
    std::vector<double> input;
    result.resize(expected.size());
    std::transform(
        expected.begin(), expected.end(), // interate over these
        actual.begin(), // access corresponding from here
        result.begin(), // save results here
        strength
        );
    return result;
}
