#include <gtest/gtest.h>
#include <vector>
#include <map>
#include <cmath>
#include <limits>
#include <chrono>
#include "../dscpp/c05_statistics/stats.h"

class StatisticsTest : public ::testing::Test {
protected:
    void SetUp() override {
        // Test data sets
        simple_data = {1.0, 2.0, 3.0, 4.0, 5.0};
        even_data = {2.0, 4.0, 6.0, 8.0};
        odd_data = {1.0, 3.0, 5.0, 7.0, 9.0};
        duplicate_data = {1.0, 2.0, 2.0, 3.0, 3.0, 3.0};
        negative_data = {-1.0, -2.0, -3.0, -4.0, -5.0};
        mixed_data = {-2.0, -1.0, 0.0, 1.0, 2.0};
        
        // Test matrices
        correlation_matrix_data = {
            {1.0, 2.0, 3.0},
            {2.0, 4.0, 6.0},
            {3.0, 6.0, 9.0}
        };
        
        // Empty data
        empty_data = {};
        empty_matrix = {};
    }
    
    std::vector<double> simple_data, even_data, odd_data, duplicate_data, 
                        negative_data, mixed_data, empty_data;
    std::vector<std::vector<double>> correlation_matrix_data, empty_matrix;
};

// Basic statistics functions
TEST_F(StatisticsTest, Bucketize) {
    EXPECT_DOUBLE_EQ(bucketize(1.5, 1.0), 1.0);
    EXPECT_DOUBLE_EQ(bucketize(2.9, 1.0), 2.0);
    EXPECT_DOUBLE_EQ(bucketize(3.0, 1.0), 3.0);
    EXPECT_DOUBLE_EQ(bucketize(-1.5, 1.0), -2.0);
    EXPECT_DOUBLE_EQ(bucketize(0.5, 0.5), 0.0);
}

TEST_F(StatisticsTest, Counter) {
    auto result = Counter(simple_data);
    EXPECT_EQ(result.size(), 5);
    EXPECT_EQ(result["1.0"], 1);
    EXPECT_EQ(result["2.0"], 1);
    EXPECT_EQ(result["3.0"], 1);
    EXPECT_EQ(result["4.0"], 1);
    EXPECT_EQ(result["5.0"], 1);
    
    // Test with duplicates
    auto result2 = Counter(duplicate_data);
    EXPECT_EQ(result2.size(), 3);
    EXPECT_EQ(result2["1.0"], 1);
    EXPECT_EQ(result2["2.0"], 2);
    EXPECT_EQ(result2["3.0"], 3);
}

TEST_F(StatisticsTest, MakeHistogram) {
    auto result = make_histogram(simple_data, 2.0);
    EXPECT_EQ(result.size(), 3);
    EXPECT_EQ(result["0.0"], 1);  // 1.0 -> 0.0
    EXPECT_EQ(result["2.0"], 2);  // 2.0, 3.0 -> 2.0
    EXPECT_EQ(result["4.0"], 2);  // 4.0, 5.0 -> 4.0
}

// Central tendency
TEST_F(StatisticsTest, Summation) {
    double result = summation(simple_data);
    EXPECT_DOUBLE_EQ(result, 15.0);
    
    double result2 = summation(negative_data);
    EXPECT_DOUBLE_EQ(result2, -15.0);
    
    double result3 = summation(empty_data);
    EXPECT_DOUBLE_EQ(result3, 0.0);
}

TEST_F(StatisticsTest, Mean) {
    double result = mean(simple_data);
    EXPECT_DOUBLE_EQ(result, 3.0);
    
    double result2 = mean(negative_data);
    EXPECT_DOUBLE_EQ(result2, -3.0);
    
    double result3 = mean(mixed_data);
    EXPECT_DOUBLE_EQ(result3, 0.0);
}

TEST_F(StatisticsTest, MeanEmpty) {
    double result = mean(empty_data);
    EXPECT_TRUE(std::isnan(result));
}

TEST_F(StatisticsTest, MedianOdd) {
    double result = median(odd_data);
    EXPECT_DOUBLE_EQ(result, 5.0);
}

TEST_F(StatisticsTest, MedianEven) {
    double result = median(even_data);
    EXPECT_DOUBLE_EQ(result, 5.0);  // (4 + 6) / 2 = 5
}

TEST_F(StatisticsTest, MedianEmpty) {
    double result = median(empty_data);
    EXPECT_TRUE(std::isnan(result));
}

TEST_F(StatisticsTest, MedianNegative) {
    double result = median(negative_data);
    EXPECT_DOUBLE_EQ(result, -3.0);
}

TEST_F(StatisticsTest, Quantile) {
    double result = quantile(simple_data, 0.0);
    EXPECT_DOUBLE_EQ(result, 1.0);
    
    double result2 = quantile(simple_data, 0.5);
    EXPECT_DOUBLE_EQ(result2, 3.0);
    
    double result3 = quantile(simple_data, 1.0);
    EXPECT_DOUBLE_EQ(result3, 5.0);
}

TEST_F(StatisticsTest, QuantileEmpty) {
    double result = quantile(empty_data, 0.5);
    EXPECT_TRUE(std::isnan(result));
}

TEST_F(StatisticsTest, Mode) {
    auto result = mode(duplicate_data);
    ASSERT_EQ(result.size(), 1);
    EXPECT_DOUBLE_EQ(result[0], 3.0);
    
    // Test with no duplicates
    auto result2 = mode(simple_data);
    ASSERT_EQ(result2.size(), 5);
    // All values should be present since they all appear once
}

TEST_F(StatisticsTest, ModeEmpty) {
    auto result = mode(empty_data);
    EXPECT_TRUE(result.empty());
}

TEST_F(StatisticsTest, DataRange) {
    double result = data_range(simple_data);
    EXPECT_DOUBLE_EQ(result, 4.0);  // 5 - 1 = 4
    
    double result2 = data_range(mixed_data);
    EXPECT_DOUBLE_EQ(result2, 4.0);  // 2 - (-2) = 4
}

TEST_F(StatisticsTest, DataRangeEmpty) {
    double result = data_range(empty_data);
    EXPECT_TRUE(std::isnan(result));
}

// Dispersion measures
TEST_F(StatisticsTest, DeMean) {
    auto result = de_mean(simple_data);
    std::vector<double> expected = {-2.0, -1.0, 0.0, 1.0, 2.0};
    ASSERT_EQ(result.size(), expected.size());
    for (size_t i = 0; i < result.size(); ++i) {
        EXPECT_DOUBLE_EQ(result[i], expected[i]);
    }
}

TEST_F(StatisticsTest, Variance) {
    double result = variance(simple_data);
    EXPECT_NEAR(result, 2.5, 1e-10);  // Sample variance: sum((x-mean)^2)/(n-1)
    
    double result2 = variance(mixed_data);
    EXPECT_NEAR(result2, 2.5, 1e-10);
}

TEST_F(StatisticsTest, VarianceEmpty) {
    double result = variance(empty_data);
    EXPECT_TRUE(std::isnan(result));
}

TEST_F(StatisticsTest, VarianceSingle) {
    std::vector<double> single_data = {5.0};
    double result = variance(single_data);
    EXPECT_TRUE(std::isnan(result));
}

TEST_F(StatisticsTest, StandardDeviation) {
    double result = standard_deviation(simple_data);
    EXPECT_NEAR(result, std::sqrt(2.5), 1e-10);
    
    double result2 = standard_deviation(mixed_data);
    EXPECT_NEAR(result2, std::sqrt(2.5), 1e-10);
}

TEST_F(StatisticsTest, StandardDeviationEmpty) {
    double result = standard_deviation(empty_data);
    EXPECT_TRUE(std::isnan(result));
}

TEST_F(StatisticsTest, InterquartileRange) {
    double result = interquartile_range(simple_data);
    EXPECT_DOUBLE_EQ(result, 2.0);  // Q3(4) - Q1(2) = 2
    
    double result2 = interquartile_range(odd_data);
    EXPECT_DOUBLE_EQ(result2, 4.0);  // Q3(7) - Q1(3) = 4
}

// Correlation and covariance
TEST_F(StatisticsTest, Covariance) {
    std::vector<double> x = {1.0, 2.0, 3.0, 4.0, 5.0};
    std::vector<double> y = {2.0, 4.0, 6.0, 8.0, 10.0};
    double result = covariance(x, y);
    EXPECT_NEAR(result, 5.0, 1e-10);  // Perfect positive correlation
}

TEST_F(StatisticsTest, CovarianceEmpty) {
    std::vector<double> x = {};
    std::vector<double> y = {};
    double result = covariance(x, y);
    EXPECT_TRUE(std::isnan(result));
}

TEST_F(StatisticsTest, CovarianceDifferentSizes) {
    std::vector<double> x = {1.0, 2.0, 3.0};
    std::vector<double> y = {1.0, 2.0};
    double result = covariance(x, y);
    EXPECT_TRUE(std::isnan(result));
}

TEST_F(StatisticsTest, Correlation) {
    std::vector<double> x = {1.0, 2.0, 3.0, 4.0, 5.0};
    std::vector<double> y = {2.0, 4.0, 6.0, 8.0, 10.0};
    double result = correlation(x, y);
    EXPECT_NEAR(result, 1.0, 1e-10);  // Perfect positive correlation
}

TEST_F(StatisticsTest, CorrelationNegative) {
    std::vector<double> x = {1.0, 2.0, 3.0, 4.0, 5.0};
    std::vector<double> y = {10.0, 8.0, 6.0, 4.0, 2.0};
    double result = correlation(x, y);
    EXPECT_NEAR(result, -1.0, 1e-10);  // Perfect negative correlation
}

TEST_F(StatisticsTest, CorrelationEmpty) {
    std::vector<double> x = {};
    std::vector<double> y = {};
    double result = correlation(x, y);
    EXPECT_TRUE(std::isnan(result));
}

TEST_F(StatisticsTest, CorrelationDifferentSizes) {
    std::vector<double> x = {1.0, 2.0, 3.0};
    std::vector<double> y = {1.0, 2.0};
    double result = correlation(x, y);
    EXPECT_TRUE(std::isnan(result));
}

TEST_F(StatisticsTest, CorrelationMatrix) {
    auto result = correlation_matrix(correlation_matrix_data);
    ASSERT_EQ(result.size(), 3);
    ASSERT_EQ(result[0].size(), 3);
    
    // Diagonal should be 1 (perfect correlation with itself)
    EXPECT_NEAR(result[0][0], 1.0, 1e-10);
    EXPECT_NEAR(result[1][1], 1.0, 1e-10);
    EXPECT_NEAR(result[2][2], 1.0, 1e-10);
    
    // Off-diagonal should be high (strong correlation)
    EXPECT_NEAR(result[0][1], 1.0, 1e-10);
    EXPECT_NEAR(result[0][2], 1.0, 1e-10);
    EXPECT_NEAR(result[1][2], 1.0, 1e-10);
}

// Edge cases and special values
TEST_F(StatisticsTest, HandlesLargeNumbers) {
    std::vector<double> large_data = {1e6, 2e6, 3e6};
    double result = mean(large_data);
    EXPECT_DOUBLE_EQ(result, 2e6);
}

TEST_F(StatisticsTest, HandlesSmallNumbers) {
    std::vector<double> small_data = {1e-10, 2e-10, 3e-10};
    double result = mean(small_data);
    EXPECT_DOUBLE_EQ(result, 2e-10);
}

TEST_F(StatisticsTest, HandlesInfinity) {
    std::vector<double> inf_data = {1.0, 2.0, std::numeric_limits<double>::infinity()};
    double result = mean(inf_data);
    EXPECT_TRUE(std::isinf(result));
}

TEST_F(StatisticsTest, HandlesIdenticalValues) {
    std::vector<double> identical_data = {5.0, 5.0, 5.0, 5.0, 5.0};
    double result = variance(identical_data);
    EXPECT_DOUBLE_EQ(result, 0.0);
    
    double result2 = standard_deviation(identical_data);
    EXPECT_DOUBLE_EQ(result2, 0.0);
    
    double result3 = data_range(identical_data);
    EXPECT_DOUBLE_EQ(result3, 0.0);
}

// Statistical properties validation
TEST_F(StatisticsTest, MeanVarianceRelationship) {
    // Test that variance is always non-negative
    auto result = de_mean(simple_data);
    double variance_calc = sum_of_squares(result) / (simple_data.size() - 1);
    EXPECT_GE(variance_calc, 0.0);
}

TEST_F(StatisticsTest, StandardDeviationIsSqrtOfVariance) {
    double var = variance(simple_data);
    double std_dev = standard_deviation(simple_data);
    EXPECT_NEAR(std_dev, std::sqrt(var), 1e-10);
}

TEST_F(StatisticsTest, QuantileProperties) {
    // Q0 should be min, Q1 should be <= median, Q3 should be >= median, Q4 should be max
    double q0 = quantile(simple_data, 0.0);
    double q1 = quantile(simple_data, 0.25);
    double q2 = quantile(simple_data, 0.5);
    double q3 = quantile(simple_data, 0.75);
    double q4 = quantile(simple_data, 1.0);
    
    EXPECT_LE(q0, q1);
    EXPECT_LE(q1, q2);
    EXPECT_LE(q2, q3);
    EXPECT_LE(q3, q4);
}

// Performance tests
TEST_F(StatisticsTest, PerformanceSanity) {
    // Create large dataset
    std::vector<double> large_data(10000);
    for (size_t i = 0; i < large_data.size(); ++i) {
        large_data[i] = static_cast<double>(i);
    }
    
    auto start = std::chrono::high_resolution_clock::now();
    double result = mean(large_data);
    auto end = std::chrono::high_resolution_clock::now();
    
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    EXPECT_LT(duration.count(), 100); // Should complete in less than 100ms
    
    EXPECT_NEAR(result, 4999.5, 1e-10);
}
