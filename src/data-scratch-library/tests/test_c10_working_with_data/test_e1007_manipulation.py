from dsl.c10_working_with_data.e1007_manipulation import average_daily_change_by_month, DailyChange, \
    find_largest_and_smallest_changes, StockPrice, day_over_day_changes, max_prices_by_symbol, max_stock_price


def test_max_stock_price():
    data = [StockPrice("AAPL", "2023-10-01", 150.0),
            StockPrice("AAPL", "2023-10-02", 155.0)]
    assert max_stock_price(data, 'AAPL') == 155.0

def test_max_prices_by_symbol():
    data = [StockPrice("AAPL", "2023-10-01", 150.0),
            StockPrice("AAPL", "2023-10-02", 155.0),
            StockPrice("MSFT", "2023-10-01", 300.0),
            StockPrice("MSFT", "2023-10-02", 305.0)]
    max_prices = max_prices_by_symbol(data)
    assert max_prices['AAPL'] == 155.0
    assert max_prices['MSFT'] == 305.0

def test_day_over_day_changes():
    prices = [StockPrice("AAPL", "2023-10-01", 150.0),
              StockPrice("AAPL", "2023-10-02", 155.0)]
    changes = day_over_day_changes(prices)
    assert len(changes) == 1
    assert changes[0].pct_change == (155.0 / 150.0 - 1)

def test_find_largest_and_smallest_changes():
    data = [StockPrice("AAPL", "2023-10-01", 150.0),
            StockPrice("AAPL", "2023-10-02", 155.0),
            StockPrice("AAPL", "2023-10-03", 140.0)]
    max_change, min_change = find_largest_and_smallest_changes(data)
    assert max_change.pct_change == (155.0 / 150.0 - 1)
    assert min_change.pct_change == (140.0 / 155.0 - 1)

def test_average_daily_change_by_month():
    changes = [
        DailyChange("AAPL", "2023-10-01", 0.05),
        DailyChange("AAPL", "2023-10-02", -0.03)
    ]
    averages = average_daily_change_by_month(changes)
    assert averages[10] == (0.05 - 0.03) / 2

