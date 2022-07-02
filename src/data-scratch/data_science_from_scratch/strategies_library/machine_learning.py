import os

import pytest

from data_science_from_scratch.library import machine_learning

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def accuracy(tp, fp, fn, tn, expected):
    result = machine_learning.accuracy(tp, fp, fn, tn)
    assert result == expected


def f1_score(tp, fp, fn, tn, expected):
    result = machine_learning.f1_score(tp, fp, fn, tn)
    assert result == expected


def precision(tp, fp, fn, tn, expected):
    result = machine_learning.precision(tp, fp, fn, tn)
    assert result == expected


def recall(tp, fp, fn, tn, expected):
    result = machine_learning.recall(tp, fp, fn, tn)
    assert result == expected


def split_data(random_matrix):
    result = machine_learning.split_data(random_matrix, 0.5)
    assert len(result[0]) == pytest.approx(50, abs=10)
    assert len(result[1]) == pytest.approx(50, abs=10)


def train_split(random_matrix):
    x_train, x_test, y_train, y_test = machine_learning.train_split(random_matrix, random_matrix, 0.5)
    assert len(x_train) == pytest.approx(50, abs=10)
    assert len(x_test) == pytest.approx(50, abs=10)
    assert len(y_train) == pytest.approx(50, abs=10)
    assert len(y_test) == pytest.approx(50, abs=10)
