import pytest

from dsl.c02_crash_course.e0220_annotations import (
    add,
    add_with_types,
    dot_product_list,
    dot_product_vector,
    Vector,
    ugly_function,
    total,
    twice,
    comma_repeater

)


# Test function for add with dynamic typing
def test_add_dynamic():
    """Tests the add function with different types."""
    assert add(10, 5) == 15, "Expected 10 + 5 = 15"
    assert add([1, 2], [3]) == [1, 2, 3], "Expected list concatenation"
    assert add("hi ", "there") == "hi there", "Expected string concatenation"
    with pytest.raises(TypeError):
        add(10, "five")



# Test function for add_with_types
def test_add_with_types():
    """Tests the add function with type annotations."""
    assert add_with_types(10, 5) == 15, "Expected 10 + 5 = 15"
    assert add_with_types("hi", "there") == "hithere"


# Test function for dot product calculations
def test_dot_product():
    """Tests the dot product functions."""
    assert dot_product_list([1, 2], [3, 4]) == 11, "Expected dot product 11"

    vec1 = Vector([1.0, 2.0])
    vec2 = Vector([3.0, 4.0])
    assert dot_product_vector(vec1, vec2) == 11.0, "Expected dot product 11.0"


# Test function for ugly_function
def test_ugly_function():
    """Tests the ugly_function with various types."""
    assert ugly_function(10, "hello") == 15, "Expected 10 + len('hello') = 15"
    assert ugly_function(10, 5) == 15, "Expected 10 + 5 = 15"
    assert ugly_function(10, 2.5) == 12, "Expected 10 + int(2.5) = 12"
    assert ugly_function(10, True) == 11, "Expected 10 + int(True) = 11"


# Test function for total
def test_total():
    """Tests the total function for summing a list of numbers."""
    assert total([1.0, 2.0, 3.0]) == 6.0, "Expected sum of 6.0"
    assert total([]) == 0.0, "Expected sum of an empty list to be 0.0"


# Test function for twice and comma_repeater
def test_twice():
    """Tests the twice function with comma_repeater."""
    assert twice(comma_repeater, "type hints") == "type hints, type hints", "Expected 'type hints, type hints'"
