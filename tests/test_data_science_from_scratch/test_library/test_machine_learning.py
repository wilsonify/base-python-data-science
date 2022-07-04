import logging
import os
from inspect import getmembers, isfunction

import pytest

from data_science_from_scratch.library import machine_learning

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def test_smoke():
    logging.info("is anything on fire")
    for member in getmembers(machine_learning):
        if isfunction(member[1]):
            print(member[0])



@pytest.mark.parametrize(
    ("tp", "fp", "fn", "tn", "expected"), (
            (100, 120, 200, 303, pytest.approx(0.55, abs=0.01)),
            (100, 1, 200, 303, pytest.approx(0.66, abs=0.01)),
            (0, 120, 200, 303, pytest.approx(0.48, abs=0.01))
    ))
def test_accuracy(tp, fp, fn, tn, expected):
    result = machine_learning.accuracy(tp, fp, fn, tn)
    assert result == expected


@pytest.mark.parametrize(
    ("tp", "fp", "fn", "tn", "expected"), (
            (100, 120, 200, 303, pytest.approx(0.38, abs=0.01)),
            (100, 1, 200, 303, pytest.approx(0.49, abs=0.01)),
            (1, 120, 200, 303, pytest.approx(0.01, abs=0.01))
    ))
def test_f1_score(tp, fp, fn, tn, expected):
    result = machine_learning.f1_score(tp, fp, fn, tn)
    assert result == expected


@pytest.mark.parametrize(
    ("tp", "fp", "fn", "tn", "expected"), (
            (100, 120, 200, 303, pytest.approx(0.45, abs=0.01)),
            (100, 1, 200, 303, pytest.approx(0.99, abs=0.01)),
            (1, 120, 200, 303, pytest.approx(0.01, abs=0.01))
    ))
def test_precision(tp, fp, fn, tn, expected):
    result = machine_learning.precision(tp, fp, fn, tn)
    assert result == expected


@pytest.mark.parametrize(
    ("tp", "fp", "fn", "tn", "expected"), (
            (100, 120, 200, 303, pytest.approx(0.33, abs=0.01)),
            (100, 1, 200, 303, pytest.approx(0.33, abs=0.01)),
            (1, 120, 200, 303, pytest.approx(0.01, abs=0.01))
    ))
def test_recall(tp, fp, fn, tn, expected):
    result = machine_learning.recall(tp, fp, fn, tn)
    assert result == expected


def test_split_data(random_matrix):
    result = machine_learning.split_data(random_matrix, 0.5)
    assert len(result[0]) == pytest.approx(50, abs=10)
    assert len(result[1]) == pytest.approx(50, abs=10)


def test_train_test_split(random_matrix):
    print(random_matrix)
    x_train, x_test, y_train, y_test = machine_learning.train_test_split(random_matrix, random_matrix, 0.5)
    assert len(x_train) == pytest.approx(50, abs=10)
    assert len(x_test) == pytest.approx(50, abs=10)
    assert len(y_train) == pytest.approx(50, abs=10)
    assert len(y_test) == pytest.approx(50, abs=10)
