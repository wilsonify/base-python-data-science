from dsl.c02_crash_course.e0210_sets import (
    create_set_with_elements,
    add_elements_to_set,
    is_element_in_set,
    get_set_length,
    get_distinct_items,
    convert_set_to_list
)


def test_create_set_with_elements():
    elements = [1, 2, 3, 1]
    result_set = create_set_with_elements(elements)
    assert result_set == {1, 2, 3}


def test_add_elements_to_set():
    s = {1}
    elements = [2, 2, 3]
    result_set = add_elements_to_set(s, elements)
    assert result_set == {1, 2, 3}


def test_is_element_in_set():
    s = {1, 2, 3}
    assert is_element_in_set(s, 2) == True
    assert is_element_in_set(s, 4) == False


def test_get_set_length():
    s = {1, 2, 3}
    assert get_set_length(s) == 3


def test_get_distinct_items():
    elements = [1, 2, 3, 1, 2, 3]
    distinct_items = get_distinct_items(elements)
    assert distinct_items == {1, 2, 3}


def test_convert_set_to_list():
    s = {1, 2, 3}
    result_list = convert_set_to_list(s)
    assert sorted(result_list) == [1, 2, 3]  # Sets are unordered, so sort for comparison
