import datetime

from dsl.c10_working_with_data.e1005_dataclass import create_stock_price


def test_stock_price_creation():
    """Tests the creation and attributes of StockPrice2."""
    price = create_stock_price('MSFT', datetime.date(2018, 12, 14), 106.03)

    # Test attribute access
    assert price.symbol == 'MSFT'
    assert price.closing_price == 106.03
    assert price.is_high_tech() == True

    # Test non-tech stock
    non_tech_price = create_stock_price('XOM', datetime.date(2018, 12, 14), 82.35)
    assert non_tech_price.is_high_tech() == False

    print("test_stock_price_creation passed!")


def test_stock_split():
    """Tests the behavior of mutating the closing price (e.g., for a stock split)."""
    price = create_stock_price('MSFT', datetime.date(2018, 12, 14), 106.03)

    # Apply stock split
    price.closing_price /= 2
    assert price.closing_price == 53.015  # More accurate floating-point result

    print("test_stock_split passed!")


def test_new_field_addition():
    """Tests adding new fields to the StockPrice2 object dynamically."""
    price = create_stock_price('MSFT', datetime.date(2018, 12, 14), 106.03)

    # Add new field dynamically (which can lead to typos/errors)
    price.cosing_price = 75  # Typo, but it's allowed in a mutable class
    assert hasattr(price, 'cosing_price')  # Ensure the field was added
    assert price.cosing_price == 75

