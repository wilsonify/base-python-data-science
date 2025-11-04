#include <gtest/gtest.h>
#include <vector>
#include <cmath>
#include <limits>
#include <chrono>
#include "../dscpp/c04_linear_algebra/linear_algebra.h"

class LinearAlgebraTest : public ::testing::Test {
protected:
    void SetUp() override {
        // Test vectors
        v1 = {1.0, 2.0, 3.0};
        v2 = {4.0, 5.0, 6.0};
        v3 = {1.0, 1.0, 1.0};
        v4 = {-1.0, -1.0, -1.0};
        
        // Test matrices
        matrix1 = {{1.0, 2.0}, {3.0, 4.0}};
        matrix2 = {{5.0, 6.0}, {7.0, 8.0}};
        matrix3 = {{1.0, 2.0, 3.0}};
        
        // Empty vectors/matrices for edge cases
        empty_vector = {};
        empty_matrix = {};
    }
    
    std::vector<double> v1, v2, v3, v4, empty_vector;
    std::vector<std::vector<double>> matrix1, matrix2, matrix3, empty_matrix;
};

// Scalar operations
TEST_F(LinearAlgebraTest, ScalarAdd) {
    EXPECT_DOUBLE_EQ(scalar_add(2.0, 3.0), 5.0);
    EXPECT_DOUBLE_EQ(scalar_add(-1.0, 1.0), 0.0);
    EXPECT_DOUBLE_EQ(scalar_add(0.0, 0.0), 0.0);
}

// Vector operations
TEST_F(LinearAlgebraTest, VectorAdd) {
    auto result = vector_add(v1, v2);
    std::vector<double> expected = {5.0, 7.0, 9.0};
    EXPECT_EQ(result, expected);
    
    // Test with negative numbers
    auto result2 = vector_add(v3, v4);
    std::vector<double> expected2 = {0.0, 0.0, 0.0};
    EXPECT_EQ(result2, expected2);
}

TEST_F(LinearAlgebraTest, VectorAddThrowsOnDifferentSizes) {
    std::vector<double> short_vec = {1.0, 2.0};
    EXPECT_THROW(vector_add(v1, short_vec), std::invalid_argument);
}

TEST_F(LinearAlgebraTest, VectorSubtract) {
    auto result = vector_subtract(v2, v1);
    std::vector<double> expected = {3.0, 3.0, 3.0};
    EXPECT_EQ(result, expected);
    
    // Test with negative numbers
    auto result2 = vector_subtract(v3, v4);
    std::vector<double> expected2 = {2.0, 2.0, 2.0};
    EXPECT_EQ(result2, expected2);
}

TEST_F(LinearAlgebraTest, VectorSubtractThrowsOnDifferentSizes) {
    std::vector<double> short_vec = {1.0, 2.0};
    EXPECT_THROW(vector_subtract(v1, short_vec), std::invalid_argument);
}

TEST_F(LinearAlgebraTest, VectorSum) {
    std::vector<std::vector<double>> vectors = {v1, v2, v3};
    auto result = vector_sum(vectors);
    std::vector<double> expected = {6.0, 8.0, 10.0};
    EXPECT_EQ(result, expected);
}

TEST_F(LinearAlgebraTest, VectorSumEmpty) {
    auto result = vector_sum(empty_matrix);
    EXPECT_TRUE(result.empty());
}

TEST_F(LinearAlgebraTest, VectorSumSingle) {
    std::vector<std::vector<double>> vectors = {v1};
    auto result = vector_sum(vectors);
    EXPECT_EQ(result, v1);
}

TEST_F(LinearAlgebraTest, ScalarMultiply) {
    auto result = scalar_multiply(2.0, v1);
    std::vector<double> expected = {2.0, 4.0, 6.0};
    EXPECT_EQ(result, expected);
    
    // Test with zero
    auto result2 = scalar_multiply(0.0, v1);
    std::vector<double> expected2 = {0.0, 0.0, 0.0};
    EXPECT_EQ(result2, expected2);
}

TEST_F(LinearAlgebraTest, VectorMean) {
    std::vector<std::vector<double>> vectors = {v1, v2, v3};
    auto result = vector_mean(vectors);
    std::vector<double> expected = {2.0, 8.0/3.0, 10.0/3.0};
    
    ASSERT_EQ(result.size(), expected.size());
    for (size_t i = 0; i < result.size(); ++i) {
        EXPECT_NEAR(result[i], expected[i], 1e-10);
    }
}

// Vector math operations
TEST_F(LinearAlgebraTest, Dot) {
    double result = dot(v1, v2);
    EXPECT_DOUBLE_EQ(result, 32.0);  // 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32
    
    // Test with negative numbers
    double result2 = dot(v3, v4);
    EXPECT_DOUBLE_EQ(result2, -3.0);  // 1*(-1) + 1*(-1) + 1*(-1) = -3
}

TEST_F(LinearAlgebraTest, DotThrowsOnDifferentSizes) {
    std::vector<double> short_vec = {1.0, 2.0};
    EXPECT_THROW(dot(v1, short_vec), std::invalid_argument);
}

TEST_F(LinearAlgebraTest, SumOfSquares) {
    double result = sum_of_squares(v1);
    EXPECT_DOUBLE_EQ(result, 14.0);  // 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14
}

TEST_F(LinearAlgebraTest, Magnitude) {
    double result = magnitude(v1);
    EXPECT_NEAR(result, std::sqrt(14.0), 1e-10);
    
    // Test with unit vector
    std::vector<double> unit_vec = {1.0, 0.0, 0.0};
    double result2 = magnitude(unit_vec);
    EXPECT_DOUBLE_EQ(result2, 1.0);
}

TEST_F(LinearAlgebraTest, SquaredDistance) {
    double result = squared_distance(v1, v2);
    EXPECT_DOUBLE_EQ(result, 27.0);  // (4-1)^2 + (5-2)^2 + (6-3)^2 = 9 + 9 + 9 = 27
}

TEST_F(LinearAlgebraTest, Distance) {
    double result = distance(v1, v2);
    EXPECT_NEAR(result, std::sqrt(27.0), 1e-10);
    
    // Test distance from origin
    std::vector<double> origin = {0.0, 0.0, 0.0};
    double result2 = distance(origin, v1);
    EXPECT_NEAR(result2, std::sqrt(14.0), 1e-10);
}

// Matrix operations
TEST_F(LinearAlgebraTest, Shape) {
    auto result = shape(matrix1);
    EXPECT_EQ(result.first, 2);
    EXPECT_EQ(result.second, 2);
    
    auto result2 = shape(matrix3);
    EXPECT_EQ(result2.first, 1);
    EXPECT_EQ(result2.second, 3);
    
    auto result3 = shape(empty_matrix);
    EXPECT_EQ(result3.first, 0);
    EXPECT_EQ(result3.second, 0);
}

TEST_F(LinearAlgebraTest, GetRow) {
    auto result = get_row(matrix1, 0);
    std::vector<double> expected = {1.0, 2.0};
    EXPECT_EQ(result, expected);
    
    auto result2 = get_row(matrix1, 1);
    std::vector<double> expected2 = {3.0, 4.0};
    EXPECT_EQ(result2, expected2);
}

TEST_F(LinearAlgebraTest, GetRowThrowsOnInvalidIndex) {
    EXPECT_THROW(get_row(matrix1, -1), std::out_of_range);
    EXPECT_THROW(get_row(matrix1, 2), std::out_of_range);
}

TEST_F(LinearAlgebraTest, GetColumn) {
    auto result = get_column(matrix1, 0);
    std::vector<double> expected = {1.0, 3.0};
    EXPECT_EQ(result, expected);
    
    auto result2 = get_column(matrix1, 1);
    std::vector<double> expected2 = {2.0, 4.0};
    EXPECT_EQ(result2, expected2);
}

TEST_F(LinearAlgebraTest, GetColumnThrowsOnInvalidIndex) {
    EXPECT_THROW(get_column(matrix1, -1), std::out_of_range);
    EXPECT_THROW(get_column(matrix1, 2), std::out_of_range);
}

TEST_F(LinearAlgebraTest, GetColumnThrowsOnEmptyMatrix) {
    EXPECT_THROW(get_column(empty_matrix, 0), std::invalid_argument);
}

TEST_F(LinearAlgebraTest, MakeMatrix) {
    auto matrix_entry = [](int i, int j) { return i * 10 + j; };
    auto result = make_matrix(2, 3, matrix_entry);
    
    std::vector<std::vector<double>> expected = {
        {0.0, 1.0, 2.0},
        {10.0, 11.0, 12.0}
    };
    EXPECT_EQ(result, expected);
}

TEST_F(LinearAlgebraTest, IsDiagonal) {
    EXPECT_DOUBLE_EQ(is_diagonal(0, 0), 1.0);
    EXPECT_DOUBLE_EQ(is_diagonal(1, 1), 1.0);
    EXPECT_DOUBLE_EQ(is_diagonal(0, 1), 0.0);
    EXPECT_DOUBLE_EQ(is_diagonal(1, 0), 0.0);
}

TEST_F(LinearAlgebraTest, IdentityMatrix) {
    // The identity matrix should be 5x5 with 1s on diagonal
    auto result = identity_matrix;
    EXPECT_EQ(result.size(), 5);
    EXPECT_EQ(result[0].size(), 5);
    
    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < 5; ++j) {
            if (i == j) {
                EXPECT_DOUBLE_EQ(result[i][j], 1.0);
            } else {
                EXPECT_DOUBLE_EQ(result[i][j], 0.0);
            }
        }
    }
}

TEST_F(LinearAlgebraTest, MatrixAdd) {
    auto result = matrix_add(matrix1, matrix2);
    std::vector<std::vector<double>> expected = {
        {6.0, 8.0},
        {10.0, 12.0}
    };
    EXPECT_EQ(result, expected);
}

TEST_F(LinearAlgebraTest, MatrixAddThrowsOnDifferentShapes) {
    std::vector<std::vector<double>> different_matrix = {{1.0, 2.0, 3.0}};
    EXPECT_THROW(matrix_add(matrix1, different_matrix), std::invalid_argument);
}

// Edge cases and special values
TEST_F(LinearAlgebraTest, HandlesLargeNumbers) {
    std::vector<double> large_vec = {1e6, 1e6};
    auto result = vector_add(large_vec, large_vec);
    std::vector<double> expected = {2e6, 2e6};
    EXPECT_EQ(result, expected);
}

TEST_F(LinearAlgebraTest, HandlesSmallNumbers) {
    std::vector<double> small_vec = {1e-10, 1e-10};
    auto result = vector_add(small_vec, small_vec);
    std::vector<double> expected = {2e-10, 2e-10};
    EXPECT_EQ(result, expected);
}

TEST_F(LinearAlgebraTest, HandlesNegativeNumbers) {
    std::vector<double> neg_vec = {-1.0, -2.0, -3.0};
    auto result = scalar_multiply(-1.0, neg_vec);
    std::vector<double> expected = {1.0, 2.0, 3.0};
    EXPECT_EQ(result, expected);
}

TEST_F(LinearAlgebraTest, HandlesZeroVector) {
    std::vector<double> zero_vec = {0.0, 0.0, 0.0};
    EXPECT_DOUBLE_EQ(magnitude(zero_vec), 0.0);
    EXPECT_DOUBLE_EQ(sum_of_squares(zero_vec), 0.0);
    
    auto result = vector_add(v1, zero_vec);
    EXPECT_EQ(result, v1);
}

// Performance tests (basic sanity checks)
TEST_F(LinearAlgebraTest, PerformanceSanity) {
    // Create larger vectors for basic performance testing
    std::vector<double> large_vec1(1000, 1.0);
    std::vector<double> large_vec2(1000, 2.0);
    
    // These should complete quickly
    auto start = std::chrono::high_resolution_clock::now();
    auto result = vector_add(large_vec1, large_vec2);
    auto end = std::chrono::high_resolution_clock::now();
    
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    EXPECT_LT(duration.count(), 100); // Should complete in less than 100ms
    
    EXPECT_EQ(result.size(), 1000);
    EXPECT_DOUBLE_EQ(result[0], 3.0);
    EXPECT_DOUBLE_EQ(result[999], 3.0);
}
