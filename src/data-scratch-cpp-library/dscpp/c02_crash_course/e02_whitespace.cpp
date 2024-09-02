#include <iostream>
#include <vector>
#include <numeric>

int main() {
    // Loop over integers from 1 to 5
    for (int i : {1, 2, 3, 4, 5}) {
        std::cout << i << std::endl;
        // Nested loop
        for (int j : {1, 2, 3, 4, 5}) {
            std::cout << j << std::endl;
            std::cout << (i + j) << std::endl;
        }
        std::cout << i << std::endl;
    }
    std::cout << "done looping" << std::endl;

    // Long-winded computation
    int long_winded_computation = (
        1 + 2 + 3 + 4 + 5 +
        6 + 7 + 8 + 9 + 10 +
        11 + 12 + 13 + 14 + 15 +
        16 + 17 + 18 + 19 + 20
    );

    // Printing the result of long_winded_computation
    std::cout << "Result of long_winded_computation: " << long_winded_computation << std::endl;

    // List of lists
    std::vector<std::vector<int>> list_of_lists = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    std::vector<std::vector<int>> easier_to_read_list_of_lists = {{1, 2, 3},
                                                                  {4, 5, 6},
                                                                  {7, 8, 9}};

    // Basic arithmetic
    int two_plus_three = 2 + 3;

    // Printing the result of two_plus_three
    std::cout << "Result of 2 + 3: " << two_plus_three << std::endl;

    // Another loop over integers from 1 to 5
    for (int i : {1, 2, 3, 4, 5}) {
        // No indentation errors in C++, but the whitespace is retained for readability
        std::cout << i << std::endl;
    }

    return 0;
}
