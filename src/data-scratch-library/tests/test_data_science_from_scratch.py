import logging
from os.path import abspath, dirname

import pytest

from dsl.c01_intro import e01_introduction
from dsl.c07_hypothesis_and_inference import e01_hypothesis_and_inference
from dsl.c10_working_with_data import e01_working_with_data
from dsl.c12_k_nearest_neighbors import e01_nearest_neighbors
from dsl.c13_naive_bayes import e01_naive_bayes
from dsl.c14_simple_linear_regression import e01_simple_linear_regression
from dsl.c15_multiple_regression import e01_multiple_regression
from dsl.c16_logistic_regression import e01_logistic_regression
from dsl.c17_decision_trees import e01_decision_trees
from dsl.c18_neural_networks import e01_neural_networks
from dsl.c22_network_analysis import e01_network_analysis
from dsl.c23_recommender_systems import e01_recommender_systems
from dsl.c24_databases import e01_databases
from dsl.c25_mapreduce import e01_mapreduce

current_dir = abspath(dirname(__file__))

data_dir = abspath(f"{current_dir}/../../../data")


def test_smoke():
    logging.info("is anything on fire")


def test_databases():
    e01_databases.main()


def test_decision_trees():
    e01_decision_trees.main()


def test_hypothesis_and_inference():
    e01_hypothesis_and_inference.main()


def test_introduction():
    e01_introduction.main()


def test_logistic_regression():
    e01_logistic_regression.main()


def test_mapreduce():
    e01_mapreduce.main()


@pytest.mark.skip(reason="takes ~2min")
def test_multiple_regression():
    e01_multiple_regression.main()


def test_naive_bayes():
    e01_naive_bayes.main(f"{data_dir}/spam/*")


def test_nearest_neighbors():
    e01_nearest_neighbors.main()


def test_network_analysis():
    e01_network_analysis.main()


def test_neural_networks():
    e01_neural_networks.main()


def test_recommender_systems():
    e01_recommender_systems.main()


def test_simple_linear_regression():
    e01_simple_linear_regression.main()


def test_working_with_data():
    e01_working_with_data.main1(path_to_csv_data=f"{data_dir}/comma_delimited_stock_prices.csv")
    e01_working_with_data.main2(path_to_stocks=f"{data_dir}/stocks.txt")
    e01_working_with_data.main3()
    e01_working_with_data.main4()
