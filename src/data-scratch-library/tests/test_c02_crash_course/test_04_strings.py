from dsl.c02_crash_course.e0204_strings import (
    create_single_quoted_string,
    create_double_quoted_string,
    get_tab_string_length,
    get_raw_tab_string_length,
    create_multiline_string,
    combine_names_with_fstring,
    combine_names_with_addition,
    combine_names_with_format
)


def test_create_single_quoted_string():
    assert create_single_quoted_string() == 'data science'


def test_create_double_quoted_string():
    assert create_double_quoted_string() == "data science"


def test_get_tab_string_length():
    assert get_tab_string_length() == 1  # Tab is a single character


def test_get_raw_tab_string_length():
    assert get_raw_tab_string_length() == 2  # Raw string has two characters ('\' and 't')


def test_create_multiline_string():
    expected = """This is the first line.
and this is the second line
and this is the third line"""
    assert create_multiline_string() == expected


def test_combine_names_with_fstring():
    assert combine_names_with_fstring("Joel", "Grus") == "Joel Grus"


def test_combine_names_with_addition():
    assert combine_names_with_addition("Joel", "Grus") == "Joel Grus"


def test_combine_names_with_format():
    assert combine_names_with_format("Joel", "Grus") == "Joel Grus"
