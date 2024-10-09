import csv
import json
import logging
import os
from collections import defaultdict
from datetime import datetime
from logging.config import dictConfig
from os.path import abspath, dirname

from dsl.c05_statistics.e0503_correlation import correlation
from dsl.c06_probability.e0603_normal import random_normal
from dsl.c10_working_with_data.manipulation import (
    parse_rows_with,
    parse_dict,
    group_by,
    picker,
    scale,
    rescale,
    de_mean_matrix,
    principal_component_analysis,
    transform_vector,
)
from dsl.c10_working_with_data.working_with_data import day_over_day_changes, overall_change


def parse_date(date_str: str):
    # Simplified version of date parsing
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return None


def read_stocks_txt(path_to_stocks):
    _data = []
    parsers = {"date": parse_date, "closing_price": float}
    with open(path_to_stocks, "r", encoding="utf8", newline="") as f:
        reader_dict = csv.DictReader(f, delimiter="\t")
        _data = [parse_dict(row_dict, parsers) for row_dict in reader_dict]
    return _data


def read_comma_delimited_stock_prices(path_to_csv_data):
    _data = []
    parsers = [parse_date, None, float]
    with open(path_to_csv_data, "r", encoding="utf8", newline="") as f:
        reader_csv = csv.reader(f)
        for line in parse_rows_with(reader_csv, parsers):
            _data.append(line)
            if any(x is None for x in line):
                logging.info("%r", f"line = {line}")

    return _data


def group_by_symbol(_data, column_name="symbol"):
    logging.info("group rows by symbol")
    by_symbol = defaultdict(list)
    for row_data in _data:
        by_symbol[row_data[column_name]].append(row_data)
    return by_symbol


def main1(path_to_csv_data):
    logging.info("safe parsing")
    _data = read_comma_delimited_stock_prices(path_to_csv_data)


def main2(path_to_stocks):
    xs = [random_normal() for _ in range(1000)]
    ys1 = [x + random_normal() / 2 for x in xs]
    ys2 = [-x + random_normal() / 2 for x in xs]
    logging.info("%r", f"correlation(xs, ys1) {correlation(xs, ys1)}")
    logging.info("%r", f"correlation(xs, ys2) {correlation(xs, ys2)}")
    logging.info("stocks")
    _data = read_stocks_txt(path_to_stocks)
    max_aapl_price = max(row_aapl["closing_price"] for row_aapl in _data if row_aapl["symbol"] == "AAPL")
    logging.info("%r", f"max aapl price {max_aapl_price}")

    by_symbol = group_by_symbol(_data)

    # use a dict comprehension to find the max for each symbol
    max_price_by_symbol = {
        symbol: max(row_of_group["closing_price"] for row_of_group in grouped_rows)
        for symbol, grouped_rows in by_symbol.items()
    }
    logging.info("%r", "max price by symbol {}".format(max_price_by_symbol))

    # key is symbol, value is list of "change" dicts
    changes_by_symbol = group_by(picker("symbol"), _data, day_over_day_changes)

    # collect all "change" dicts into one big list
    all_changes = [
        change for changes in changes_by_symbol.values() for change in changes
    ]

    max_all_changes = max(all_changes, key=picker("change"))
    min_all_changes = min(all_changes, key=picker("change"))
    logging.info("%r", f"max change {max_all_changes}")
    logging.info("%r", f"min change {min_all_changes}")

    overall_change_by_month = group_by(
        lambda row_r: row_r["date"].month,
        all_changes,
        overall_change
    )
    logging.info("%r", f"overall change by month {overall_change_by_month}")


def main3():
    logging.info("rescaling")

    _data = [[1, 20, 2], [1, 30, 3], [1, 40, 4]]
    scale_data = scale(_data)
    rescale_data = rescale(_data)
    logging.info("%r", f"original: {_data}")
    logging.info("%r", f"scale: {scale_data}")
    logging.info("%r", f"rescaled: {rescale_data}")


def main4():
    logging.info("PCA")
    x_matrix_list = json.load(open(abspath(f"{dirname(__file__)}/../../../../data/x_matrix.json"), "r"))
    x_matrix_demeaned = de_mean_matrix(x_matrix_list)
    components_p = principal_component_analysis(x_matrix_demeaned, 2)
    transform_demeaned = transform_vector(x_matrix_demeaned[0], components_p)
    logging.info("%r", "principal components {}".format(components_p))
    logging.info("%r", "first point {}".format(x_matrix_demeaned[0]))
    logging.info("%r", f"first point transformed {transform_demeaned}")


if __name__ == "__main__":
    dictConfig(dict(
        version=1,
        formatters={"simple": {"format": """%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"""}},
        handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
        root={"handlers": ["console"], "level": logging.DEBUG},
    ))
    current_dir = abspath(os.path.dirname(__file__))
    data_dir = abspath(f"{current_dir}/../../../../data")

    main1(path_to_csv_data=f"{data_dir}/comma_delimited_stock_prices.csv")
    main2(path_to_stocks=f"{data_dir}/stocks.txt")
    main3()
    main4()
