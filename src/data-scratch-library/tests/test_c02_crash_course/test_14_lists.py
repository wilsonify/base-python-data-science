from dsl.c02_crash_course.e0214_lists import get_even_numbers, get_square_dict, get_increasing_pairs


def test_get_even_numbers():
    assert get_even_numbers(5) == [0, 2, 4]


def test_get_square_dict():
    assert get_square_dict(5) == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


def test_get_increasing_pairs():
    assert get_increasing_pairs(3) == [(0, 1), (0, 2), (1, 2)]
