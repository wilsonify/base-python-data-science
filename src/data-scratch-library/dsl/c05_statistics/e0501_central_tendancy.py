from collections import Counter
from typing import List


def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)


def median(v: List[float]) -> float:
    """finds the 'middle-most' value of v"""
    n = len(v)
    assert n > 0, "Cannot compute median of an empty list"
    if n % 2 == 1:
        # if odd, return the middle value
        sorted_v = sorted(v)
        midpoint = n // 2
        return sorted_v[midpoint]
    else:
        # if even, return the average of two middle values
        sorted_v = sorted(v)
        midpoint = n // 2
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2.0


def quantile(x, p):
    """returns the pth-percentile value in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]


def mode(x):
    """returns a list, might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]
