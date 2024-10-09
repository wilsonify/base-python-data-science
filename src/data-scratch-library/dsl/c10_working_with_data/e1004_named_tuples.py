import datetime
from collections import namedtuple
from typing import NamedTuple, Dict

# Example 1: Using namedtuple
StockPrice0 = namedtuple('StockPrice', ['symbol', 'date', 'closing_price'])


def create_stock_price_namedtuple(symbol: str, date: datetime.date, closing_price: float) -> StockPrice0:
    """Creates a namedtuple StockPrice."""
    return StockPrice0(symbol, date, closing_price)


class StockPrice(NamedTuple):
    """Example 2: Using NamedTuple with methods"""
    symbol: str
    date: datetime.date
    closing_price: float

    def is_high_tech(self) -> bool:
        """Returns True if the stock symbol is a high-tech company."""
        return self.symbol in ['MSFT', 'GOOG', 'FB', 'AMZN', 'AAPL']


def create_stock_price(symbol: str, date: datetime.date, closing_price: float) -> StockPrice:
    """Creates a StockPrice object."""
    return StockPrice(symbol, date, closing_price)




# Example 3: Typing dictionaries with datetime as key and float as value
def create_price_dict() -> Dict[datetime.date, float]:
    """Creates a dictionary mapping dates to stock prices."""
    return {
        datetime.date(2023, 1, 1): 100.0,
        datetime.date(2023, 1, 2): 102.0,
    }


