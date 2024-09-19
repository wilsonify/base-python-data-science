from dsl.c02_crash_course.e0213_sort import sort_list, sort_by_key


def test_sort_list():
    assert sort_list([4, 1, 2, 3]) == [1, 2, 3, 4]
    assert sort_list([4, 1, 2, 3], reverse=True) == [4, 3, 2, 1]


def test_sort_by_key():
    items = {'apple': 5, 'banana': 2, 'cherry': 10}
    assert sort_by_key(items.items(), key_func=lambda item: item[1]) == [('banana', 2), ('apple', 5), ('cherry', 10)]
    assert sort_by_key(items.items(), key_func=lambda item: item[1], reverse=True) == [('cherry', 10), ('apple', 5),
                                                                                       ('banana', 2)]
