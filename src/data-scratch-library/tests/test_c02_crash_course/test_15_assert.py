from dsl.c02_crash_course.e0215_assert import smallest_item, smallest_item_guarded


def test_smoke():
    assert 1 + 1 == 2
    assert 1 + 1 == 2, "1 + 1 should equal 2 but didn't"


def test_smallest_item():
    assert smallest_item([10, 20, 5, 40]) == 5
    assert smallest_item([1, 0, -1, 2]) == -1


def test_smallest_item_guarded():
    assert smallest_item_guarded([10, 20, 5, 40]) == 5
    assert smallest_item_guarded([1, 0, -1, 2]) == -1
