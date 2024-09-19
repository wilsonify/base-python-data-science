from dsl.c02_crash_course.e0212_truth import get_first_char, get_safe_value, all_truthy, any_truthy


def test_get_first_char():
    assert get_first_char("hello") == "h"
    assert get_first_char("") == ""
    assert get_first_char(None) == ""


def test_get_safe_value():
    assert get_safe_value(5) == 5
    assert get_safe_value(None) == 0
    assert get_safe_value(0) == 0


def test_all_truthy():
    assert all_truthy([True, 1, "non-empty"]) == True
    assert all_truthy([True, 1, 0]) == False
    assert all_truthy([]) == True


def test_any_truthy():
    assert any_truthy([True, 1, "non-empty"]) == True
    assert any_truthy([False, 0, ""]) == False
    assert any_truthy([False, 0, "non-empty"]) == True
