import logging
import random


#
# data splitting
#


def split_data(data, prob):
    """split data into fractions [prob, 1 - prob]"""
    results = [], []
    for row in data:
        results[0 if random.random() < prob else 1].append(row)
    return results


def train_test_split(x, y, test_pct):
    data = list(zip(x, y))  # pair corresponding values
    train, test = split_data(data, 1 - test_pct)  # split the dataset of pairs
    x_train, y_train = list(zip(*train))  # magical un-zip trick
    x_test, y_test = list(zip(*test))
    return x_train, x_test, y_train, y_test


#
# correctness
#


def accuracy(tp, fp, fn, tn):
    correct = tp + tn
    total = tp + fp + fn + tn
    return correct / total


def precision(tp, fp, fn, tn):
    logging.debug("%s", "tp = {}".format(tp))
    logging.debug("%s", "fp = {}".format(fp))
    logging.debug("%s", "fn = {}".format(fn))
    logging.debug("%s", "tn = {}".format(tn))
    return tp / (tp + fp)


def recall(tp, fp, fn, tn):
    logging.debug("%s", "tp = {}".format(tp))
    logging.debug("%s", "fp = {}".format(fp))
    logging.debug("%s", "fn = {}".format(fn))
    logging.debug("%s", "tn = {}".format(tn))
    return tp / (tp + fn)


def f1_score(tp, fp, fn, tn):
    p = precision(tp, fp, fn, tn)
    r = recall(tp, fp, fn, tn)

    return 2 * p * r / (p + r)
