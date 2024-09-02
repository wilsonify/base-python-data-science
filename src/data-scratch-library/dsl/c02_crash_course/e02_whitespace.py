if __name__ == "__main__":
    for i in [1, 2, 3, 4, 5]:
        print(i)
        for j in [1, 2, 3, 4, 5]:
            print(j)
            print(i + j)
        print(i)
    print("done looping")

    long_winded_computation = (
            1 + 2 + 3 + 4 + 5 +
            6 + 7 + 8 + 9 + 10 +
            11 + 12 + 13 + 14 + 15 +
            16 + 17 + 18 + 19 + 20
    )

    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    easier_to_read_list_of_lists = [[1, 2, 3],
                                    [4, 5, 6],
                                    [7, 8, 9]]

    two_plus_three = 2 + 3

    for i in [1, 2, 3, 4, 5]:
        # whitespace here could cause IndentationError: expected an indented block
        print(i)
