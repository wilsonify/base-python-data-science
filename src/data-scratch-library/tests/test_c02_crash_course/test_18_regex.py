import re

from dsl.c02_crash_course.e0218_regex import zip_lists, unzip_pairs, add


def test_regex1():
    # Function to test regex match and search operations
    assert not re.match("a", "cat")  # 'cat' doesn't start with 'a'
    assert re.search("a", "cat")  # 'cat' has an 'a' in it
    assert not re.search("c", "dog")  # 'dog' doesn't have a 'c' in it
    assert len(re.split("[ab]", "carbs")) == 3  # Split on a or b to ['c', 'r', 's']
    assert re.sub("[0-9]", "-", "R2D2") == "R-D-"  # Replace digits with dashes


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


def test_add():
    """Tests the add function."""
    assert add(1, 2) == 3, "Expected 3"

    try:
        add([1, 2])
    except TypeError:
        print("add expects two inputs")

    result = add(*[1, 2])
    assert result == 3, f"Expected 3, got {result}"
