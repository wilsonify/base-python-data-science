import logging
import os

import pytest
from data_science_from_scratch import (
    databases,
    decision_trees,
    hypothesis_and_inference,
    introduction,
    logistic_regression,
    mapreduce,
    multiple_regression,
    naive_bayes,
    nearest_neighbors,
    network_analysis,
    neural_networks,
    recommender_systems,
    simple_linear_regression,
    working_with_data,
)

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def test_smoke():
    logging.info("is anything on fire")


def test_databases():
    databases.main()


def test_decision_trees():
    decision_trees.main()


def test_hypothesis_and_inference():
    hypothesis_and_inference.main()


def test_introduction():
    introduction.main()


def test_logistic_regression():
    logistic_regression.main()


def test_mapreduce():
    mapreduce.main()


@pytest.mark.skip(reason="long running test")
def test_multiple_regression():
    multiple_regression.main()


def test_naive_bayes():
    path = os.path.join(parent_dir, "data", "spam", "*")
    naive_bayes.train_and_test_model(path)


def test_nearest_neighbors():
    nearest_neighbors.main()


def test_network_analysis():
    network_analysis.main()


def test_neural_networks():
    neural_networks.main()


def test_recommender_systems():
    recommender_systems.main()


def test_simple_linear_regression():
    simple_linear_regression.main()


def test_working_with_data():
    working_with_data.main(
        path_to_csv_data=os.path.join(
            parent_dir, "data", "comma_delimited_stock_prices.csv"),
        path_to_stocks=os.path.join(parent_dir, "data", "stocks.txt")
    )
