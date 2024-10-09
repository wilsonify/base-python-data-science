import datetime
from dataclasses import dataclass


@dataclass
class StockPrice2:
    symbol: str
    date: datetime.date
    closing_price: float

    def is_high_tech(self) -> bool:
        """Returns True if the stock symbol is a high-tech company."""
        return self.symbol in ['MSFT', 'GOOG', 'FB', 'AMZN', 'AAPL']


def create_stock_price(symbol: str, date: datetime.date, closing_price: float) -> StockPrice2:
    """Creates a StockPrice2 dataclass object."""
    return StockPrice2(symbol, date, closing_price)



