import re

from dsl.c02_crash_course.e0218_regex import (
    re_count_ab,
    re_has_a_c,
    re_has_an_a,
    re_starts_with_a,
    re_digits_to_dashes
)


def test_re_starts_with_a():
    # 'cat' doesn't start with 'a'
    assert not re_starts_with_a("cat")
    assert not re.match("a", "cat")


def test_re_has_an_a():
    # 'cat' has an 'a' in it
    assert re_has_an_a("cat")
    assert re.search("a", "cat")


def test_re_has_a_c():
    # 'dog' doesn't have a 'c' in it
    assert not re_has_a_c("dog")
    assert not re.search("c", "dog")


def test_re_count_ab():
    # Split on a or b to ['c', 'r', 's']
    assert re_count_ab("carbs") == 3
    assert len(re.split("[ab]", "carbs")) == 3


def test_re_digits_to_dashes():
    # Replace digits with dashes
    assert re_digits_to_dashes("R2D2")
    assert re.sub("[0-9]", "-", "R2D2") == "R-D-"
