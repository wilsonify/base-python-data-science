double accuracy(double tp, double fp, double fn, double tn)
{
    double result;
    double eps = 0.01;
    result = (tp + tn) / (tp + fp + fn + tn + eps);
    return result;
}
