def create_tuple(a, b):
    """Returns a tuple from two inputs."""
    return a, b

def try_modify_tuple(tpl, index, value):
    """Tries to modify a tuple, returns a message if not allowed."""
    try:
        tpl[index] = value
    except TypeError:
        return "cannot modify a tuple"

def sum_and_product(x, y):
    """Returns the sum and product of two numbers as a tuple."""
    return (x + y), (x * y)

def swap_variables(a, b):
    """Swaps two variables using tuple unpacking."""
    return b, a
