double strength(double actual, double expected)
{
    double result;
    double eps = 0.001;
    result = actual / (expected + eps);
    return result;
}
