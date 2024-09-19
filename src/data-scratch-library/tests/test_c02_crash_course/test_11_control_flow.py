from dsl.c02_crash_course.e0211_control_flow import conditional_message, get_parity, count_to_ten, \
    loop_with_continue_and_break


def test_conditional_message():
    assert conditional_message(0) == "when all else fails use else (if you want to)"


def test_get_parity():
    assert get_parity(0) == "even"
    assert get_parity(1) == "odd"
    assert get_parity(2) == "even"


def test_count_to_ten():
    expected_output = [f"{x} is less than 10" for x in range(10)]
    assert count_to_ten() == expected_output


def test_loop_with_continue_and_break():
    assert loop_with_continue_and_break() == [0, 1, 2, 4]
