import math


def double(x):
    """
    Multiplies the input by 2.
    """
    return x * 2


def apply_to_one(f):
    """
    Calls the function f with 1 as its argument.
    """
    return f(1)


def another_double(x):
    """
    Multiplies the input by 2 (replaces the lambda version).
    """
    return 2 * x


def my_print(message="my default message"):
    """
    Prints the provided message. Defaults to 'my default message'.
    """
    return message  # Return the message instead of printing it for testability


def full_name(first="What's-his-name", last="Something"):
    """
    Returns the full name as a combination of first and last name. 
    Defaults are provided for both arguments.
    """
    return first + " " + last


def mysqrt(x: float) -> float:  # noqa: E501
    """ square root """
    return math.sqrt(x)
