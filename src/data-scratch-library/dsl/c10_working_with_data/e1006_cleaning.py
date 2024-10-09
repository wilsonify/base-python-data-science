import csv
import re
from typing import Optional, List

from dateutil.parser import parse

from dsl.c10_working_with_data.e1004_named_tuples import StockPrice


def parse_row(row: List[str]) -> StockPrice:
    """Parses a row of data into a StockPrice object.

    Args:
        row (List[str]): A list containing the stock symbol, date, and closing price.

    Returns:
        StockPrice: A StockPrice object containing the parsed data.
    """
    symbol, date, closing_price = row
    return StockPrice(symbol=symbol, date=parse(date).date(), closing_price=float(closing_price))


def try_parse_row(row: List[str]) -> Optional[StockPrice]:
    """Tries to parse a row of data into a StockPrice object, returning None for invalid rows.

    Args:
        row (List[str]): A list containing the stock symbol, date, and closing price.

    Returns:
        Optional[StockPrice]: A StockPrice object if successful, None otherwise.
    """
    try:
        symbol, date_, closing_price_ = row
    except ValueError:
        return None
    # Stock symbol should be all capital letters
    if not re.match(r"^[A-Z]+$", symbol):
        return None
    try:
        date = parse(date_).date()
    except ValueError:
        return None
    try:
        closing_price = float(closing_price_)
    except ValueError:
        return None
    return StockPrice(symbol, date, closing_price)


def process_csv(filename: str) -> List[StockPrice]:
    """Processes a CSV file and returns a list of StockPrice objects.

    Args:
        filename (str): The path to the CSV file.

    Returns:
        List[StockPrice]: A list of valid StockPrice objects parsed from the CSV.
    """
    data: List[StockPrice] = []
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            maybe_stock = try_parse_row(row)
            if maybe_stock is None:
                print(f"Skipping invalid row: {row}")
            else:
                data.append(maybe_stock)
    return data


if __name__ == "__main__":
    stock_data = process_csv("comma_delimited_stock_prices.csv")
    # You can print or process the stock_data further as needed
