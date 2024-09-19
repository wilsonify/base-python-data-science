from dsl.c02_crash_course.e0207_tuples import create_tuple, try_modify_tuple, sum_and_product, swap_variables


def test_create_tuple():
    assert create_tuple(1, 2) == (1, 2)


def test_try_modify_tuple():
    tpl = (1, 2, 3)
    assert try_modify_tuple(tpl, 1, 10) == "cannot modify a tuple"


def test_sum_and_product():
    assert sum_and_product(2, 3) == (5, 6)
    assert sum_and_product(5, 10) == (15, 50)


def test_swap_variables():
    x, y = swap_variables(1, 2)
    assert x == 2
    assert y == 1
