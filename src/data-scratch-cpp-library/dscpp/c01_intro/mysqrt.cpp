#include "mysqrt.h"

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
    int i;
    for (i = 0; i < 10; ++i)
    {
        if (result <= 0)
        {
            result = 0.1;
        }
        delta = x - (result * result);
        result = result + 0.5 * delta / result;
        fprintf(stdout, "Computing sqrt of %g to be %g\n", x, result);
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
