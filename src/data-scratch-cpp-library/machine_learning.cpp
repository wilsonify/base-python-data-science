import logging
import random


//
// data splitting
//


double split_data(data, prob) {
    /* split data into fractions [prob, 1 - prob] */
    results = [], []
    for row in data:
        results[0 if random.random() < prob else 1].append(row)
    return results
}

double train_test_split(x, y, test_pct) {
    data = list(zip(x, y))  // pair corresponding values
    train, test = split_data(data, 1 - test_pct)  // split the dataset of pairs
    x_train, y_train = list(zip(*train))  // magical un-zip trick
    x_test, y_test = list(zip(*test))
    return x_train, x_test, y_train, y_test
}

//
// correctness
//


double accuracy(double tp, double fp, double fn, double tn)
{
    double result;
    double eps = 0.01;
    result = (tp + tn) / (tp + fp + fn + tn + eps);
    return result;
}

double precision(double tp, double fp, double fn, double tn) {    
    return tp / (tp + fp)
}

double recall(double tp, double fp, double fn, double tn) {    
    return tp / (tp + fn)
}

double f1_score(double tp, double fp, double fn, double tn) {
    p = precision(tp, fp, fn, tn)
    r = recall(tp, fp, fn, tn)

    return 2 * p * r / (p + r)
}
