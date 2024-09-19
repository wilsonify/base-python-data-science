import pytest

from dsl.c02_crash_course.e0206_lists import (
    list_length, list_sum, get_nth_element, slice_list,
    list_contains, list_extend, list_append, unpack_list
)


def test_list_length():
    assert list_length([1, 2, 3]) == 3


def test_list_sum():
    assert list_sum([1, 2, 3]) == 6


def test_get_nth_element():
    lst = [0, 1, 2, 3, 4, 5]
    assert get_nth_element(lst, 0) == 0
    assert get_nth_element(lst, -1) == 5


def test_slice_list():
    lst = [0, 1, 2, 3, 4, 5]
    assert slice_list(lst, 0, 3) == [0, 1, 2]
    assert slice_list(lst, 3, None) == [3, 4, 5]
    assert slice_list(lst, -3, None) == [3, 4, 5]
    assert slice_list(lst, None, None, 2) == [0, 2, 4]


def test_list_contains():
    assert list_contains([1, 2, 3], 2)
    assert not list_contains([1, 2, 3], 0)


def test_list_extend():
    lst = [1, 2, 3]
    assert list_extend(lst, [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_list_append():
    lst = [1, 2, 3]
    assert list_append(lst, 0) == [1, 2, 3, 0]


def test_unpack_list():
    x, y = unpack_list([1, 2])
    assert x == 1
    assert y == 2

    with pytest.raises(ValueError):
        unpack_list([1, 2, 3])
