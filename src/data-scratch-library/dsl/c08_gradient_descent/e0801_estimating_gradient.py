import operator
from typing import Callable

from dsl.c04_linear_algebra import Vector


def difference_quotient(f: Callable[[float], float | list[float]], x: float, h: float) -> float | list[float]:
    """
    f is a function of one variable,
    its derivative at a point x measures how f(x)
    changes when we make a very small change to x.
    The derivative is defined as the limit of the difference quotient as h goes to zero
    """
    try:
        return (f(x + h) - f(x)) / h
    except TypeError:
        diff = map(operator.sub, f(x + h), f(x))
        return [_ / h for _ in diff]


def partial_difference_quotient(
        f: Callable[[Vector], float],
        v: Vector,
        i: int,
        h: float) -> float:
    """
    Returns the i-th partial difference quotient of f at v
    """

    # add h to just the i-th element of v
    w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)]

    try:
        return (f(w) - f(v)) / h
    except TypeError:
        diff = map(operator.sub, f(w), f(v))
        return [_ / h for _ in diff]


def estimate_gradient(
        f: Callable[[Vector], float],
        v: Vector,
        h: float = 0.0001):
    return [partial_difference_quotient(f, v, i, h) for i, _ in enumerate(v)]
