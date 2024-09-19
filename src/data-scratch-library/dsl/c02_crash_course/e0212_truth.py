def get_first_char(s):
    """Returns the first character of the string s, or an empty string if s is empty or None."""
    return s[0] if s else ""

def get_safe_value(x):
    """Returns x if x is not None, otherwise returns 0."""
    return x or 0

def all_truthy(iterable):
    """Returns True if all elements in iterable are truthy."""
    return all(iterable)

def any_truthy(iterable):
    """Returns True if any element in iterable is truthy."""
    return any(iterable)
