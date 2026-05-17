"""
Machine learning utilities: data splitting and classification metrics.
"""

import random
from typing import List, Tuple, TypeVar, Any

X = TypeVar("X")


def split_data(data: List[X], prob: float) -> Tuple[List[X], List[X]]:
    """Split *data* into two lists with fractions [prob, 1 - prob]."""
    results: Tuple[List[X], List[X]] = ([], [])
    for row in data:
        results[0 if random.random() < prob else 1].append(row)
    return results


def train_test_split(
    x: List[Any], y: List[Any], test_pct: float
) -> Tuple[List[Any], List[Any], List[Any], List[Any]]:
    """Split paired *x* / *y* data into train and test sets."""
    data = list(zip(x, y))
    train, test = split_data(data, 1 - test_pct)
    x_train, y_train = list(zip(*train))
    x_test, y_test = list(zip(*test))
    return x_train, x_test, y_train, y_test


# ── Classification metrics ───────────────────────────────────────────


def accuracy(tp: int, fp: int, fn: int, tn: int) -> float:
    """Proportion of correct predictions."""
    return (tp + tn) / (tp + fp + fn + tn)


def precision(tp: int, fp: int, fn: int, tn: int) -> float:
    """Proportion of positive predictions that are correct."""
    return tp / (tp + fp)


def recall(tp: int, fp: int, fn: int, tn: int) -> float:
    """Proportion of actual positives correctly identified."""
    return tp / (tp + fn)


def f1_score(tp: int, fp: int, fn: int, tn: int) -> float:
    """Harmonic mean of precision and recall."""
    p = precision(tp, fp, fn, tn)
    r = recall(tp, fp, fn, tn)
    return 2 * p * r / (p + r)
