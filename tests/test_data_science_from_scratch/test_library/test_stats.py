import logging
import os

import pytest

from data_science_from_scratch.library import stats

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def test_smoke():
    logging.info("is anything on fire")


@pytest.mark.parametrize(
    ("v1", "v2", "expected"), (
            ([1, 2], [2, 1], pytest.approx(-1, abs=0.01)),
            ([1, 2], [1, 2], pytest.approx(1, abs=0.01)),
            ([1, 2, 3, 4, 5], [1, 1.5, 2, 2.5], pytest.approx(0.6, abs=0.1)),
            ([1, 0, 0, 1], [1, 2, 3, 4], pytest.approx(0, abs=0.01))
    ))
def test_correlation(v1, v2, expected):
    result = stats.correlation(v1, v2)
    assert result == expected


@pytest.mark.parametrize(
    ("v1", "v2", "expected"), (
            ([1, 2], [2, 1], pytest.approx(-0.5, abs=0.01)),
            ([1, 2], [1, 2], pytest.approx(0.5, abs=0.01)),
            ([1, 2, 3, 4, 5], [1, 1.5, 2, 2.5], pytest.approx(0.6, abs=0.1)),
            ([1, 0, 0, 1], [1, 2, 3, 4], pytest.approx(0, abs=0.01))
    ))
def test_covariance(v1, v2, expected):
    result = stats.covariance(v1, v2)
    assert result == expected


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


def test_main():
    stats.main()


def test_make_friend_counts_histogram():
    stats.make_friend_counts_histogram()


def test_mean():
    stats.mean()


def test_median():
    stats.median()


def test_mode():
    stats.mode()


def test_num_friends():
    stats.num_friends()


def test_num_points():
    stats.num_points()


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
