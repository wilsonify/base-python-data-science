from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from typing import List

from dsl.c10_working_with_data.e1004_named_tuples import StockPrice


@dataclass
class DailyChange:
    symbol: str
    date: date
    pct_change: float


def max_stock_price(data, symbol):
    """Find the maximum closing price for a given stock symbol."""
    return max(
        stock_price.closing_price
        for stock_price in data
        if stock_price.symbol == symbol
    )


def max_prices_by_symbol(data):
    """Return a dictionary of symbols with their maximum closing prices."""
    max_prices = defaultdict(lambda: float('-inf'))
    for sp in data:
        symbol, closing_price = sp.symbol, sp.closing_price
        if closing_price > max_prices[symbol]:
            max_prices[symbol] = closing_price
    return dict(max_prices)


def pct_change(yesterday: StockPrice, today):
    """Calculate percentage change between yesterday's and today's prices."""
    return today.closing_price / yesterday.closing_price - 1


def day_over_day_changes(prices):
    """Return a list of percentage changes for consecutive days."""
    return [
        DailyChange(
            symbol=today.symbol,
            date=today.date,
            pct_change=pct_change(yesterday, today)
        )
        for yesterday, today in zip(prices, prices[1:])
    ]


def group_prices_by_symbol(data):
    """Group stock prices by symbol."""
    prices = defaultdict(list)
    for sp in data:
        prices[sp.symbol].append(sp)
    return {symbol: sorted(symbol_prices) for symbol, symbol_prices in prices.items()}


def find_largest_and_smallest_changes(data):
    """Find the largest and smallest day-over-day percentage changes."""
    prices_by_symbol = group_prices_by_symbol(data)
    all_changes = [
        change
        for symbol_prices in prices_by_symbol.values()
        for change in day_over_day_changes(symbol_prices)
    ]
    max_change = max(all_changes, key=lambda change: change.pct_change)
    min_change = min(all_changes, key=lambda change: change.pct_change)
    return max_change, min_change


def average_daily_change_by_month(all_changes):
    """Return the average daily percentage change by month."""
    changes_by_month: List[DailyChange] = {month: [] for month in range(1, 13)}
    for change in all_changes:
        changes_by_month[change.date.month].append(change)
    avg_daily_change = {
        month: sum(change.pct_change for change in changes) / len(changes)
        for month, changes in changes_by_month.items()
    }
