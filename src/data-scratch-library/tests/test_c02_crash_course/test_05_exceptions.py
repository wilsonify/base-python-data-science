from dsl.c02_crash_course.e0205_exceptions import divide_by_zero


def test_divide_by_zero():
    assert divide_by_zero() == "cannot divide by zero"
