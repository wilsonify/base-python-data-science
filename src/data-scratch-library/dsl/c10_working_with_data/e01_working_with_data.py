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
from dsl.c10_working_with_data.e1007_manipulation import day_over_day_changes
from dsl.c10_working_with_data.e1008_rescaling import scale, rescale


def square_root(x, tolerance=1e-10):
    """Computes the square root of a number using Newton's method."""
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number.")

    guess = x
    while abs(guess * guess - x) > tolerance:
        guess = (guess + x / guess) / 2
    return guess


def de_mean_matrix(matrix):
    """Subtracts the mean of each column from the respective column values."""
    num_rows, num_cols = len(matrix), len(matrix[0])
    means = [sum(row[j] for row in matrix) / num_rows for j in range(num_cols)]
    return [[row[j] - means[j] for j in range(num_cols)] for row in matrix]


def magnitude(vector):
    """Returns the magnitude (length) of a vector."""
    return square_root(sum(x ** 2 for x in vector))


def direction(vector):
    """Returns a unit vector in the same direction as the input vector."""
    mag = magnitude(vector)
    return [x / mag for x in vector] if mag != 0 else vector


def dot(v, w):
    """Computes the dot product of two vectors."""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def project(v, w):
    """Projects vector v onto vector w."""
    coefficient = dot(v, w) / dot(w, w)
    return [coefficient * w_i for w_i in w]


def argmax(lst):
    """Returns the index of the maximum value in a list."""
    if not lst:
        raise ValueError("Cannot compute argmax of an empty list.")

    max_index = 0
    max_value = lst[0]
    for i, value in enumerate(lst):
        if value > max_value:
            max_value = value
            max_index = i
    return max_index


def covariance_matrix(matrix):
    """Computes the covariance matrix of a dataset."""
    num_rows, num_cols = len(matrix), len(matrix[0])
    means = [sum(row[j] for row in matrix) / num_rows for j in range(num_cols)]

    cov_matrix = [[0] * num_cols for _ in range(num_cols)]
    for i in range(num_cols):
        for j in range(num_cols):
            cov_matrix[i][j] = sum(
                (row[i] - means[i]) * (row[j] - means[j]) for row in matrix
            ) / (num_rows - 1)
    return cov_matrix


def eig(matrix, max_iterations=1000, tolerance=1e-10):
    """Computes the eigenvalues and eigenvectors of a symmetric matrix using the power iteration method."""
    num_cols = len(matrix)
    eigenvectors = [[1 if i == j else 0 for j in range(num_cols)] for i in range(num_cols)]
    eigenvalues = [0] * num_cols

    for col in range(num_cols):
        v = [1] * num_cols
        lambda_ = max(matrix)
        for _ in range(max_iterations):
            w = [sum(matrix[i][j] * v[j] for j in range(num_cols)) for i in range(num_cols)]
            lambda_ = max(abs(x) for x in w)
            if lambda_ == 0:
                break
            v = [x / lambda_ for x in w]
            if max(abs(w[i] - lambda_ * v[i]) for i in range(num_cols)) < tolerance:
                break
        eigenvalues[col] = lambda_
        eigenvectors[col] = v

    return eigenvalues, eigenvectors


def principal_component_analysis(matrix, num_components):
    """Finds the first `num_components` principal components of the matrix."""
    components = []
    for _ in range(num_components):
        column_vectors = list(zip(*matrix))
        mean_vector = [sum(col) / len(col) for col in column_vectors]
        demeaned = [[row[i] - mean_vector[i] for i in range(len(row))] for row in matrix]
        demeaned_covariance = covariance_matrix(demeaned)
        eigenvalues, eigenvectors = eig(demeaned_covariance)
        principal_component = eigenvectors[:, argmax(eigenvalues)]
        components.append(principal_component)

        # Remove the component from the matrix
        matrix = [[row[i] - project(row, principal_component)[i] for i in range(len(row))] for row in matrix]
    return components


def transform_vector(vector, components):
    """Transforms a vector into the principal component space."""
    return [dot(vector, component) for component in components]


def parse_date(date_str: str):
    """Attempts to parse a date string into a datetime object."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None


def parse_dict(row_dict, parsers):
    """Parses a dictionary with specific data parsers."""
    return {
        key: parsers[key](value) if key in parsers and value else value
        for key, value in row_dict.items()
    }


def parse_rows_with(reader, parsers):
    """Parses rows with specific parsers, handling errors gracefully."""
    for row in reader:
        try:
            yield [parsers[i](field) if parsers[i] else field for i, field in enumerate(row)]
        except ValueError:
            yield [None if parsers[i] else field for i, field in enumerate(row)]


def read_stocks_txt(path_to_stocks):
    """Reads tab-delimited stock price data."""
    _data = []
    parsers = {"date": parse_date, "closing_price": float}
    with open(path_to_stocks, "r", encoding="utf8", newline="") as f:
        reader_dict = csv.DictReader(f, delimiter="\t")
        _data = [parse_dict(row_dict, parsers) for row_dict in reader_dict]
    return _data


def read_comma_delimited_stock_prices(path_to_csv_data):
    """Reads CSV stock price data and applies parsers."""
    _data = []
    parsers = [parse_date, None, float]
    with open(path_to_csv_data, "r", encoding="utf8", newline="") as f:
        reader_csv = csv.reader(f)
        for line in parse_rows_with(reader_csv, parsers):
            _data.append(line)
            if any(x is None for x in line):
                logging.info("Invalid line: %r", line)

    return _data


def group_by_symbol(_data, column_name="symbol"):
    """Groups stock data by symbol."""
    logging.info("Grouping rows by symbol")
    by_symbol = defaultdict(list)
    for row_data in _data:
        by_symbol[row_data[column_name]].append(row_data)
    return by_symbol


def group_by(key_fn, rows, value_transform):
    """Groups rows by a given key function and applies a transformation."""
    grouped = defaultdict(list)
    for row in rows:
        grouped[key_fn(row)].append(value_transform(row))
    return grouped


def picker(field_name):
    """Returns a function that picks a specific field from a dictionary."""
    return lambda row: row[field_name]


def overall_change(changes):
    """Computes the overall change for a set of stock changes."""
    return sum(change["change"] for change in changes)


def main1(path_to_csv_data):
    """Main function for reading CSV stock data."""
    logging.info("Safe parsing of stock data")
    _data = read_comma_delimited_stock_prices(path_to_csv_data)


def main2(path_to_stocks):
    """Main function for analyzing stock data."""
    xs = [random_normal() for _ in range(1000)]
    ys1 = [x + random_normal() / 2 for x in xs]
    ys2 = [-x + random_normal() / 2 for x in xs]

    logging.info("Correlation(xs, ys1) = %f", correlation(xs, ys1))
    logging.info("Correlation(xs, ys2) = %f", correlation(xs, ys2))

    logging.info("Analyzing stocks...")
    _data = read_stocks_txt(path_to_stocks)

    max_aapl_price = max(
        row["closing_price"] for row in _data if row["symbol"] == "AAPL"
    )
    logging.info("Max AAPL price: %f", max_aapl_price)

    by_symbol = group_by_symbol(_data)

    max_price_by_symbol = {
        symbol: max(row["closing_price"] for row in rows)
        for symbol, rows in by_symbol.items()
    }
    logging.info("Max price by symbol: %s", max_price_by_symbol)

    changes_by_symbol = group_by(picker("symbol"), _data, day_over_day_changes)

    all_changes = [change for changes in changes_by_symbol.values() for change in changes]

    max_all_changes = max(all_changes, key=picker("change"))
    min_all_changes = min(all_changes, key=picker("change"))

    logging.info("Max change: %s", max_all_changes)
    logging.info("Min change: %s", min_all_changes)

    overall_change_by_month = group_by(
        lambda row: row["date"].month, all_changes, overall_change
    )
    logging.info("Overall change by month: %s", overall_change_by_month)


def main3():
    """Main function for rescaling data."""
    logging.info("Rescaling data...")

    _data = [[1, 20, 2], [1, 30, 3], [1, 40, 4]]
    scale_data = scale(_data)
    rescale_data = rescale(_data)

    logging.info("Original data: %s", _data)
    logging.info("Scaled data: %s", scale_data)
    logging.info("Rescaled data: %s", rescale_data)


def main4():
    """Main function for PCA analysis."""
    logging.info("Performing PCA...")

    data_path = abspath(f"{dirname(__file__)}/../../../../data/x_matrix.json")

    with open(data_path, "r") as f:
        x_matrix_list = json.load(f)

    x_matrix_demeaned = de_mean_matrix(x_matrix_list)
    components_p = principal_component_analysis(x_matrix_demeaned, 2)
    transform_demeaned = transform_vector(x_matrix_demeaned[0], components_p)

    logging.info("Principal components: %s", components_p)
    logging.info("First point: %s", x_matrix_demeaned[0])
    logging.info("First point transformed: %s", transform_demeaned)


if __name__ == "__main__":
    dictConfig(dict(
        version=1,
        formatters={"simple": {"format": "%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"}},
        handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
        root={"handlers": ["console"], "level": logging.DEBUG},
    ))

    current_dir = abspath(dirname(__file__))
    data_dir = os.path.join(current_dir, "../../../../data")

    main1(path_to_csv_data=os.path.join(data_dir, "comma_delimited_stock_prices.csv"))
    main2(path_to_stocks=os.path.join(data_dir, "stocks.txt"))
    main3()
    main4()
