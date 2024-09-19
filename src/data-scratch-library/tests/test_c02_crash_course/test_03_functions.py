from dsl.c02_crash_course.e0203_functions import double, apply_to_one, another_double, my_print, full_name


def test_double():
    assert double(2) == 4
    assert double(-3) == -6
    assert double(0) == 0


def test_apply_to_one():
    assert apply_to_one(double) == 2  # Calls double(1)
    assert apply_to_one(lambda x: x + 4) == 5  # Calls lambda(1)


def test_another_double():
    assert another_double(2) == 4
    assert another_double(-3) == -6
    assert another_double(0) == 0


def test_my_print():
    assert my_print("hello") == "hello"
    assert my_print() == "my default message"  # Test the default message


def test_full_name():
    assert full_name("Joel", "Grus") == "Joel Grus"
    assert full_name("Joel") == "Joel Something"  # Uses default last name
    assert full_name(last="Grus") == "What's-his-name Grus"  # Uses default first name
