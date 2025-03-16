import csv
import re
from datetime import datetime
from typing import Optional, List

from dsl.c10_working_with_data.e1004_named_tuples import StockPrice


def parse_row(row: List[str]) -> StockPrice:
    """Parses a row of data into a StockPrice object.

    Args:
        row (List[str]): A list containing the stock symbol, date, and closing price.

    Returns:
        StockPrice: A StockPrice object containing the parsed data.
    """
    symbol, date_str, closing_price_str = row

    # Ensure the stock symbol is all capital letters
    if not re.fullmatch(r"^[A-Z]+$", symbol):
        raise ValueError(f"Invalid stock symbol: {symbol}")

    # Try parsing the date with multiple possible formats
    date_formats = ["%Y-%m-%d", "%m/%d/%Y", "%d-%m-%Y"]  # Extend as needed
    date = None
    for fmt in date_formats:
        try:
            date = datetime.strptime(date_str, fmt).date()
            break
        except ValueError:
            continue

    if date is None:
        raise ValueError(f"Invalid date format: {date_str}")

    # Convert closing price to float
    try:
        closing_price = float(closing_price_str)
    except ValueError:
        raise ValueError(f"Invalid closing price: {closing_price_str}")

    return StockPrice(symbol, date, closing_price)


def try_parse_row(row: List[str]) -> Optional[StockPrice]:
    """Tries to parse a row of data into a StockPrice object, returning None for invalid rows.

    Args:
        row (List[str]): A list containing the stock symbol, date, and closing price.

    Returns:
        Optional[StockPrice]: A StockPrice object if successful, None otherwise.
    """
    try:
        symbol, date_str, closing_price_str = row
    except ValueError:
        return None

    # Ensure the stock symbol is all capital letters
    if not re.fullmatch(r"^[A-Z]+$", symbol):
        return None

    # Try parsing the date with multiple possible formats
    date_formats = ["%Y-%m-%d", "%m/%d/%Y", "%d-%m-%Y"]  # Add more formats if needed
    date = None
    for fmt in date_formats:
        try:
            date = datetime.strptime(date_str, fmt).date()
            break  # Stop trying once a valid format is found
        except ValueError:
            continue

    if date is None:
        return None

    # Convert closing price to float
    try:
        closing_price = float(closing_price_str)
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
