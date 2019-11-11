import logging
import os

from data_science_from_scratch.library import machine_learning

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def test_smoke():
    logging.info("is anything on fire")


def test_accuracy():
    machine_learning.accuracy()


def test_config():
    machine_learning.config()


def test_dictConfig():
    machine_learning.dictConfig()


def test_f1_score():
    machine_learning.f1_score()


def test_logging():
    machine_learning.logging()


def test_precision():
    machine_learning.precision()


def test_random():
    machine_learning.random()


def test_recall():
    machine_learning.recall()


def test_split_data():
    machine_learning.split_data()


def test_train_test_split():
    machine_learning.train_test_split()
