from functools import reduce

from dsl.c02_crash_course.manipulation import (
    picker, pluck
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


def combine_pct_changes(pct_change1, pct_change2):
    """
    to combine percent changes, we add 1 to each, multiply them, and subtract 1)
    for instance, if we combine +10% and -20%, the overall change is
    (1 + 10%) * (1 - 20%) - 1 = 1.1 * .8 - 1 = -12%
    """
    return (1 + pct_change1) * (1 + pct_change2) - 1


def overall_change(changes):
    return reduce(combine_pct_changes, pluck("change", changes))
