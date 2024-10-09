import datetime

from dsl.c10_working_with_data.e1004_named_tuples import create_stock_price, create_stock_price_namedtuple, \
    create_price_dict


def test_namedtuple_with_methods():
    """Tests the StockPrice NamedTuple class and its methods."""
    price = create_stock_price('MSFT', datetime.date(2018, 12, 14), 106.03)

    # Test attributes
    assert price.symbol == 'MSFT'
    assert price.closing_price == 106.03

    # Test method
    assert price.is_high_tech() == True

    # Test for a non-high-tech company
    non_tech_price = create_stock_price('XOM', datetime.date(2018, 12, 14), 82.35)
    assert non_tech_price.is_high_tech() == False

    print("test_namedtuple_with_methods passed!")


def test_namedtuple_stock_price():
    """Tests the namedtuple StockPrice behavior."""
    price = create_stock_price_namedtuple('MSFT', datetime.date(2018, 12, 14), 106.03)
    assert price.symbol == 'MSFT'
    assert price.closing_price == 106.03
    print("test_namedtuple_stock_price passed!")


def test_price_dict():
    """Tests the creation and type of a price dictionary."""
    prices = create_price_dict()

    assert isinstance(prices, dict)
    assert isinstance(list(prices.keys())[0], datetime.date)
    assert isinstance(list(prices.values())[0], float)

    print("test_price_dict passed!")
