import pytest

from dsl.c02_crash_course.e0219_functional import (
    add,
    doubler,
    doubler_correct,
    other_way_magic,
    unzip_pairs,
    zip_lists,
)


def test_zip_unzip():
    """Tests zipping and unzipping functionality."""
    list1 = ['a', 'b', 'c']
    list2 = [1, 2, 3]
    zipped = zip_lists(list1, list2)
    assert zipped == [('a', 1), ('b', 2), ('c', 3)], f"Expected [('a', 1), ('b', 2), ('c', 3)], got {zipped}"

    pairs = [('a', 1), ('b', 2), ('c', 3)]
    letters, numbers = unzip_pairs(pairs)
    assert letters == ('a', 'b', 'c'), f"Expected ('a', 'b', 'c'), got {letters}"
    assert numbers == (1, 2, 3), f"Expected (1, 2, 3), got {numbers}"


def test_add1():
    """Tests the add function."""
    assert add(1, 2) == 3, "Expected 3"


def test_add2():
    """ add expects two inputs """
    with pytest.raises(TypeError):
        add([1, 2])


def test_add3():
    """Tests the add function."""
    result = add(*[1, 2])
    assert result == 3, f"Expected 3, got {result}"


# Test function for doubler with single argument function
def test_doubler_single_arg():
    """Tests the doubler function with a function that takes a single argument."""

    def f1(x):
        return x + 1

    g = doubler(f1)
    assert g(3) == 8, "(3 + 1) * 2 should equal 8"
    assert g(-1) == 0, "(-1 + 1) * 2 should equal 0"


# Test function for argument unpacking
def test_other_way_magic():
    """Tests argument unpacking with *args and **kwargs."""
    x_y_list = [1, 2]
    z_dict = {"z": 3}
    result = other_way_magic(*x_y_list, **z_dict)
    assert result == 6, f"Expected 6, got {result}"


# Test function for doubler_correct
def test_doubler_correct():
    """Tests the doubler_correct function with a function that takes multiple arguments."""

    def f2(x, y):
        return x + y

    g = doubler_correct(f2)
    assert g(1, 2) == 6, "doubler should work now with multiple arguments"
