from typing import List
from dsl.c04_linear_algebra.e0401_vectors import Vector
from dsl.c04_linear_algebra.e0402_matrices import Matrix, make_matrix
from dsl.c05_statistics.e0503_correlation import correlation


def correlation_matrix(data: List[Vector]) -> Matrix:
    """
    Returns a len(data) x len(data) matrix whose (i, j)-th entry
    is the correlation between data[i] and data[j].

    Args:
        data (List[Vector]): A list of vectors, where each vector represents
                             a dimension in the dataset.

    Returns:
        Matrix: A square matrix of correlation coefficients.
    """
    def correlation_ij(i: int, j: int) -> float:
        return correlation(data[i], data[j])

    return make_matrix(len(data), len(data), correlation_ij)





