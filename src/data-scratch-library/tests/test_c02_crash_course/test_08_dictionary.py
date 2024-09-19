from dsl.c02_crash_course.e0208_dictionary import (
    create_grades, get_grade, update_grades, check_student_in_grades,
    count_words, create_default_dict_list, create_default_dict_dict, create_default_dict_pair
)


def test_create_grades():
    grades = create_grades()
    assert grades == {"Joel": 80, "Tim": 95}


def test_get_grade():
    grades = create_grades()
    assert get_grade(grades, "Joel") == 80
    assert get_grade(grades, "Kate") == 0
    assert get_grade(grades, "Kate", 100) == 100


def test_update_grades():
    grades = create_grades()
    updated_grades = update_grades(grades, "Kate", 100)
    assert updated_grades == {"Joel": 80, "Tim": 95, "Kate": 100}


def test_check_student_in_grades():
    grades = create_grades()
    assert check_student_in_grades(grades, "Joel") is True
    assert check_student_in_grades(grades, "Kate") is False


def test_count_words():
    document = ["data", "science", "data", "awesome"]
    word_counts = count_words(document)
    assert word_counts == {"data": 2, "science": 1, "awesome": 1}


def test_create_default_dict_list():
    dd_list = create_default_dict_list()
    assert dd_list[2] == [1]


def test_create_default_dict_dict():
    dd_dict = create_default_dict_dict()
    assert dd_dict["Joel"]["City"] == "Seattle"


def test_create_default_dict_pair():
    dd_pair = create_default_dict_pair()
    assert dd_pair[2] == [0, 1]
