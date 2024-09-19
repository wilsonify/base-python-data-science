from dsl.c02_crash_course.e0201_whitespace import loop_sums, perform_long_computation, get_list_of_lists, \
    add_two_and_three, print_numbers


def test_loop_sums():
    loop_sums()


def test_long_winded_computation():
    long_winded_computation = perform_long_computation()
    assert long_winded_computation == (
            1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 +
            11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20
    )


def test_get_list_of_lists():
    list_of_lists = get_list_of_lists()
    assert list_of_lists == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    easier_to_read_list_of_lists = [[1, 2, 3],
                                    [4, 5, 6],
                                    [7, 8, 9]]
    assert list_of_lists == easier_to_read_list_of_lists


def test_add_two_and_three():
    two_plus_three = add_two_and_three()
    assert two_plus_three == 2 + 3


def test_print_numbers():
    print_numbers()
