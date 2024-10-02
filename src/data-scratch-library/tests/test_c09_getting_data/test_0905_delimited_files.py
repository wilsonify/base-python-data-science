import csv
from os import remove

from dsl.c09_getting_data.e0905_delimited_files import write_bad_csv_file, write_comma_delimited_file, \
    read_colon_delimited_file, read_tab_delimited_file


def test_read_tab_delimited_file():
    # Create a sample tab-delimited file
    with open('test_tab_delimited_stock_prices.txt', 'w') as f:
        f.write("2023-09-01\tAAPL\t150.12\n2023-09-02\tMSFT\t299.30\n")

    rows = read_tab_delimited_file('test_tab_delimited_stock_prices.txt')
    assert rows == [
        ['2023-09-01', 'AAPL', '150.12'],
        ['2023-09-02', 'MSFT', '299.30']
    ]
    remove("test_tab_delimited_stock_prices.txt")


def test_read_colon_delimited_file():
    # Create a sample colon-delimited file
    with open('test_colon_delimited_stock_prices.txt', 'w') as f:
        f.write("date:symbol:closing_price\n2023-09-01:AAPL:150.12\n2023-09-02:MSFT:299.30\n")

    rows = read_colon_delimited_file('test_colon_delimited_stock_prices.txt')
    assert rows == [
        {"date": "2023-09-01", "symbol": "AAPL", "closing_price": "150.12"},
        {"date": "2023-09-02", "symbol": "MSFT", "closing_price": "299.30"}
    ]
    remove("test_colon_delimited_stock_prices.txt")


def test_write_comma_delimited_file():
    # Data to be written to CSV
    todays_prices = {'AAPL': 150.12, 'MSFT': 299.30, 'GOOGL': 2750.00}

    # Write to a test CSV file
    write_comma_delimited_file('test_comma_delimited_stock_prices.csv', todays_prices)

    # Read the file back and verify the contents
    with open('test_comma_delimited_stock_prices.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        rows = [row for row in csv_reader]
        assert rows == [
            ['AAPL', '150.12'],
            ['MSFT', '299.3'],
            ['GOOGL', '2750.0']
        ]
    remove("test_comma_delimited_stock_prices.csv")


def test_write_bad_csv_file():
    # Bad CSV data with commas in fields
    results = [
        ["test1", "success", "Monday"],
        ["test2", "success, kind of", "Tuesday"],
        ["test3", "failure, kind of", "Wednesday"],
        ["test4", "failure, utter", "Thursday"]
    ]

    # Write the bad CSV
    write_bad_csv_file('test_bad_csv.txt', results)

    # Read the file back and check for incorrect formatting
    with open('test_bad_csv.txt', 'r') as f:
        lines = f.readlines()
        assert lines == [
            "test1,success,Monday\n",
            "test2,success, kind of,Tuesday\n",
            "test3,failure, kind of,Wednesday\n",
            "test4,failure, utter,Thursday\n"
        ]
    remove("test_bad_csv.txt")
