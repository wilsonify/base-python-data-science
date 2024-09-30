def safe(f):
    """Define a new function that wraps f and returns it"""

    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except KeyboardInterrupt:
            raise  # Re-raise KeyboardInterrupt so it is not caught
        except (KeyError, ValueError, AttributeError, ZeroDivisionError):
            return float("inf")  # Return "infinity" for all other exceptions

    return safe_f


def negate(f):
    """
    return a function that for any input x returns -f(x)
    """
    return lambda *args, **kwargs: -f(*args, **kwargs)


def negate_all(f):
    """
    the same when f returns a list of numbers
    """
    return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]
