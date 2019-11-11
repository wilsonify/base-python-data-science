import logging
import os

from data_science_from_scratch.library import stats

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def test_smoke():
    logging.info("is anything on fire")


def test_correlation():
    stats.correlation()


def test_covariance():
    stats.covariance()


def test_daily_minutes():
    stats.daily_minutes()


def test_daily_minutes_good():
    stats.daily_minutes_good()


def test_data_range():
    stats.data_range()


def test_de_mean():
    stats.de_mean()


def test_dictConfig():
    stats.dictConfig()


def test_dot():
    stats.dot()


def test_interquartile_range():
    stats.interquartile_range()


def test_largest_value():
    stats.largest_value()


def test_logging():
    stats.logging()


def test_main():
    stats.main()


def test_make_friend_counts_histogram():
    stats.make_friend_counts_histogram()


def test_math():
    stats.math()


def test_mean():
    stats.mean()


def test_median():
    stats.median()


def test_mode():
    stats.mode()


def test_num_friends():
    stats.num_friends()


def test_num_friends_good():
    stats.num_friends_good()


def test_num_points():
    stats.num_points()


def test_outlier():
    stats.outlier()


def test_quantile():
    stats.quantile()


def test_second_largest_value():
    stats.second_largest_value()


def test_second_smallest_value():
    stats.second_smallest_value()


def test_smallest_sorted_value():
    stats.smallest_sorted_value()


def test_smallest_value():
    stats.smallest_value()


def test_sorted_values():
    stats.sorted_values()


def test_standard_deviation():
    stats.standard_deviation()


def test_sum_of_squares():
    stats.sum_of_squares()


def test_variance():
    stats.variance()
