#include "mysqrt.h"
#include <iostream>

double mysqrt(double x)
{
    // a hack square root calculation using simple operations
    if (x <= 0)
    {
        return 0;
    }

    double result;
    double delta;
    result = x;

    // do ten iterations
    for (int i = 0; i < 10; ++i)
    {
        if (result <= 0)
        {
            result = 0.1;
        }
        delta = x - (result * result);
        result = result + 0.5 * delta / result;
        std::cout << "Computing sqrt of " << x << " to be " << result << "\n";
    }
    return result;
}

std::vector<double> mysqrt_vector(std::vector<double> x)
{
    std::vector<double> result;
    result.resize(x.size());
    std::transform(
        x.begin(), x.end(), // iterate from start to end
        result.begin(), // save results here
        mysqrt // transformation
        );
    return result;
}
