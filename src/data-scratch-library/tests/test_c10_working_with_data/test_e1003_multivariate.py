# Test function
from dsl.c10_working_with_data.e1003_multivariate import correlation_matrix


def test_correlation_matrix():
    """
    Test the correlation_matrix function with known input and expected output.
    """
    # Define some test data
    data = [
        [1, 2, 3],
        [2, 4, 6],
        [1, 0, -1]
    ]

    # Compute the correlation matrix
    corr_matrix = correlation_matrix(data)

    # Define the expected correlation matrix based on the data
    expected_corr_matrix = [
        [1.0, 1.0, -1.0],
        [1.0, 1.0, -1.0],
        [-1.0, -1.0, 1.0]
    ]

    # Check each value in the computed matrix
    for i in range(len(expected_corr_matrix)):
        for j in range(len(expected_corr_matrix[i])):
            assert abs(corr_matrix[i][j] - expected_corr_matrix[i][j]) < 1e-9, \
                f"Mismatch at ({i}, {j}): {corr_matrix[i][j]} != {expected_corr_matrix[i][j]}"

