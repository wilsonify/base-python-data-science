from typing import List, Union, Callable


def add(a, b):
    # Function to add two values (dynamically typed)
    return a + b


def add_with_types(a: int, b: int) -> int:
    # Function to add two integers with type annotations
    return a + b


def dot_product_list(x, y):
    """Calculates dot product of two lists (dynamically typed)."""
    return sum(x_i * y_i for x_i, y_i in zip(x, y))


class Vector(List[float]):
    # Class to represent a Vector (typed)
    pass


def dot_product_vector(x: Vector, y: Vector) -> float:
    """
    Calculates the dot product of two vectors (typed with type annotations).
    """
    return sum(x_i * y_i for x_i, y_i in zip(x, y))


def ugly_function(value: int, operation: Union[str, int, float, bool]) -> int:
    """
    Performs a dummy operation with Union of different types.
    """
    if isinstance(operation, str):
        return value + len(operation)
    elif isinstance(operation, int):
        return value + operation
    elif isinstance(operation, float):
        return value + int(operation)
    elif isinstance(operation, bool):
        return value + int(operation)
    else:
        raise ValueError("Unsupported operation type")


# Function that sums a list of numbers
def total(xs: List[float]) -> float:
    """Calculates the sum of a list of floats."""
    return sum(xs)


# Function that repeats a string n times and joins them with commas
def comma_repeater(s: str, n: int) -> str:
    """Repeats a string n times, joined with commas."""
    return ', '.join([s] * n)


# Function that uses a Callable to repeat a string
def twice(repeater: Callable[[str, int], str], s: str) -> str:
    """Repeats a string twice using the provided repeater function."""
    return repeater(s, 2)
