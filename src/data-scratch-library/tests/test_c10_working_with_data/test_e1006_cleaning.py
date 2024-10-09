from datetime import date

from dsl.c10_working_with_data.e1006_cleaning import (
    parse_row,
    try_parse_row
)


def test_parse_row():
    """Test the parse_row function."""
    row = ["MSFT", "2018-12-14", "106.03"]
    stock = parse_row(row)

    assert stock.symbol == "MSFT"
    assert stock.date == date(2018, 12, 14)
    assert stock.closing_price == 106.03


def test_try_parse_row_valid():
    """Test the try_parse_row function with valid data."""
    row = ["MSFT", "2018-12-14", "106.03"]
    stock = try_parse_row(row)

    assert stock is not None
    assert stock.symbol == "MSFT"
    assert stock.date == date(2018, 12, 14)
    assert stock.closing_price == 106.03


def test_try_parse_row_invalid_symbol():
    """Test the try_parse_row function with an invalid stock symbol."""
    row = ["MSFT0", "2018-12-14", "106.03"]
    assert try_parse_row(row) is None


def test_try_parse_row_invalid_date():
    """Test the try_parse_row function with an invalid date."""
    row = ["MSFT", "2018-12--14", "106.03"]
    assert try_parse_row(row) is None


def test_try_parse_row_invalid_closing_price():
    """Test the try_parse_row function with an invalid closing price."""
    row = ["MSFT", "2018-12-14", "x"]
    assert try_parse_row(row) is None


def test_try_parse_row_no_data():
    """Test the try_parse_row function with no data."""
    row = []
    assert try_parse_row(row) is None
