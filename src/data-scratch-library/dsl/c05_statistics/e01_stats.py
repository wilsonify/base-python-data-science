"""
describe how many friends your members have
"""
import logging
from logging.config import dictConfig
from os.path import abspath, dirname

from dsl.c05_statistics.c01_userdata import UserData
from dsl.c05_statistics.e0503_correlation import covariance, correlation
from dsl.c05_statistics.e0502_dispersion import data_range, variance, standard_deviation, interquartile_range
from dsl.c05_statistics.e0501_central_tendancy import mean, median, quantile, mode



def main():
    user_data = UserData.from_json(abspath(f"{dirname(__file__)}/../../../../data/user_minutes_and_friends.json"))
    num_points = len(user_data.num_friends)  # 204

    largest_value = max(user_data.num_friends)  # 100
    smallest_value = min(user_data.num_friends)  # 1

    sorted_values = sorted(user_data.num_friends)
    smallest_sorted_value = sorted_values[0]  # 1
    second_smallest_value = sorted_values[1]  # 1
    second_largest_value = sorted_values[-2]  # 49

    logging.info("%r", f"num_points = {num_points}")
    logging.info("%r", f"largest_value = {largest_value}")
    logging.info("%r", f"smallest_value = {smallest_value}")
    logging.info("%r", f"smallest_sorted_value = {smallest_sorted_value}")
    logging.info("%r", f"second_smallest_value = {second_smallest_value}")
    logging.info("%r", f"second_largest_value = {second_largest_value}")
    logging.info("%r", f"mean(num_friends) = {mean(user_data.num_friends)}")
    logging.info("%r", f"median(num_friends) = {median(user_data.num_friends)}")
    logging.info("%r", f"quantile(num_friends, 0.10) = {quantile(user_data.num_friends, 0.10)}")
    logging.info("%r", f"quantile(num_friends, 0.25) = {quantile(user_data.num_friends, 0.25)}")
    logging.info("%r", f"quantile(num_friends, 0.75) = {quantile(user_data.num_friends, 0.75)}")
    logging.info("%r", f"quantile(num_friends, 0.90) = {quantile(user_data.num_friends, 0.90)}")
    logging.info("%r", f"mode(num_friends) = {mode(user_data.num_friends)}")
    logging.info("%r", f"data_range(num_friends) = {data_range(user_data.num_friends)}")
    logging.info("%r", f"variance(num_friends) = {variance(user_data.num_friends)}")
    logging.info("%r", f"standard_deviation(num_friends) = {standard_deviation(user_data.num_friends)}")
    logging.info("%r", f"interquartile_range(num_friends) = {interquartile_range(user_data.num_friends)}")
    logging.info("%r",
                 f"covariance(num_friends, daily_minutes) = {covariance(user_data.num_friends, user_data.daily_minutes)}")
    logging.info("%r",
                 f"correlation(num_friends, daily_minutes) = {correlation(user_data.num_friends, user_data.daily_minutes)}")
    outlier = user_data.num_friends.index(100)  # index of outlier

    num_friends_good = [x for i, x in enumerate(user_data.num_friends) if i != outlier]

    daily_minutes_good = [x for i, x in enumerate(user_data.daily_minutes) if i != outlier]
    correlation_friends_minutes = correlation(num_friends_good, daily_minutes_good)
    logging.info("%r", f"correlation(num_friends_good, daily_minutes_good) {correlation_friends_minutes}")


if __name__ == "__main__":
    dictConfig(dict(
        version=1,
        formatters={"simple": {"format": """%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"""}},
        handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
        root={"handlers": ["console"], "level": logging.DEBUG},
    ))

    main()
