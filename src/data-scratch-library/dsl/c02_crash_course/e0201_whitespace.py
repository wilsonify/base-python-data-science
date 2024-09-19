def loop_sums():
    """
    This function returns a list of sums calculated from the nested loops.
    """
    result = []
    for i in [1, 2, 3, 4, 5]:
        result.append(i)
        for j in [1, 2, 3, 4, 5]:
            result.append(i + j)
        result.append(i)
    return result


def perform_long_computation():
    """
    Performs a long-winded computation and returns the result.
    """
    return sum(range(1, 21))


def get_list_of_lists():
    """
    Returns a list of lists.
    """
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def add_two_and_three():
    """
    Returns the result of 2 + 3.
    """
    return 2 + 3


def print_numbers():
    """
    This function returns the numbers 1 to 5 as a list.
    """
    return [i for i in [1, 2, 3, 4, 5]]


if __name__ == "__main__":
    loop_sums()
    long_winded_computation = perform_long_computation()
    assert long_winded_computation == (
            1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 +
            11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20
    )

    list_of_lists = get_list_of_lists()
    assert list_of_lists == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    easier_to_read_list_of_lists = [[1, 2, 3],
                                    [4, 5, 6],
                                    [7, 8, 9]]
    assert list_of_lists == easier_to_read_list_of_lists

    two_plus_three = add_two_and_three()
    assert two_plus_three == 2 + 3

    print_numbers()
