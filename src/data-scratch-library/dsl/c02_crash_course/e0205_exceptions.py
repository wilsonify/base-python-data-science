def divide_by_zero():
    """
    Attempts to divide 0 by 0, raises a ZeroDivisionError, and catches it.
    Returns an error message instead of crashing.
    """
    try:
        result = 0 / 0
    except ZeroDivisionError:
        return "cannot divide by zero"
    return result
