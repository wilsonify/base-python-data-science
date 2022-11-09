from data_science_from_scratch.library.manipulation import (
    picker
)


def percent_price_change(yesterday, today):
    return today["closing_price"] / yesterday["closing_price"] - 1


def day_over_day_changes(grouped_rows):
    # sort the rows by date
    ordered = sorted(grouped_rows, key=picker("date"))
    # zip with an offset to get pairs of consecutive days
    return [
        {
            "symbol": today["symbol"],
            "date": today["date"],
            "change": percent_price_change(yesterday, today),
        }
        for yesterday, today in zip(ordered, ordered[1:])
    ]
