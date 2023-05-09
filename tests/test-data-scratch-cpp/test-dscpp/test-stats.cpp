#include <gtest/gtest.h>
#include "data-scratch-cpp-library.h"

TEST(smokeTest, BasicAssertion) {
    EXPECT_EQ(7 * 6, 42);
}

TEST(test_bucketize, test_bucketize01)
{
    //(25.4958, 5, 25),
    double result;
    result = bucketize(25.4958, 5);
    EXPECT_EQ(25, result);
}
TEST(test_bucketize, test_bucketize02)
{
    //(250.303, 5, 250)
    double result;
    result = bucketize(250.303, 5);
    EXPECT_EQ(250, result);
}

TEST(test_bucketize, test_bucketize03)
{
    //(25.9, 25, 25),
    double result;
    result = bucketize(25.9, 25);
    EXPECT_EQ(25, result);
}

TEST(test_correlation, test_correlation01)
{
    // ([1, 2], [2, 1], pytest.approx(-1, abs=0.01)),
    double result;
    result = correlation({1, 2}, {2, 1});
    EXPECT_EQ(-1.0, result);
}

TEST(test_correlation, test_correlation02)
{
    // ([1, 2], [1, 2], pytest.approx(1, abs=0.01)),
    double result;
    result = correlation({1,2},{1,2});
    EXPECT_EQ(1.0, result);
}

TEST(test_correlation, test_correlation03)
{
    // ([1, 2, 3, 4, 5], [1, 1.5, 2, 2.5], pytest.approx(0.6, abs=0.1)),
    double result;
    result = correlation({1, 2, 3, 4, 5},{1, 1.5, 2, 2.5});
    EXPECT_EQ(0.6, result);
}

TEST(test_correlation, test_correlation04)
{
    // ([1, 0, 0, 1], [1, 2, 3, 4], pytest.approx(0, abs=0.01))
    double result;
    result = correlation({1,0,0,1},{1,2,3,4});
    EXPECT_EQ(0.0, result);
}

TEST(test_covariance, test_covariance01)
{
// ([1, 2], [2, 1], pytest.approx(-0.5, abs=0.01)),

    double result;
    result = covariance({1,2},{2,1});
    EXPECT_EQ(-0.5, result);
}

TEST(test_covariance, test_covariance02)
{
// ([1, 2], [1, 2], pytest.approx(0.5, abs=0.01)),

    double result;
    result = covariance({1,2},{1,2});
    EXPECT_EQ(0.5, result);
}

TEST(test_covariance, test_covariance03)
{
    // ([1, 2, 3, 4, 5], [1, 1.5, 2, 2.5], pytest.approx(0.6, abs=0.1))
    double result;
    result = covariance({1, 2, 3, 4, 5},{1, 1.5, 2, 2.5});
    EXPECT_EQ(0.6, result);
}

TEST(test_covariance, test_covariance04)
{
    // ([1, 0, 0, 1], [1, 2, 3, 4], pytest.approx(0, abs=0.01))
    double result;
    result = covariance({1,0,0,1},{1,2,3,4})
    EXPECT_EQ(0.0, result);
}

TEST(test_data_range, test_data_range01)
{
    // ([1, 2], pytest.approx(1, abs=0.01))
    double result;
    result = data_range({1,2});
    EXPECT_EQ(1.0, result);
}

TEST(test_data_range, test_data_range02)
{
    // ([1, 2, 10], pytest.approx(9, abs=0.01))
    double result;
    result = data_range({1, 2, 10});
    EXPECT_EQ(9.0, result);
}

TEST(test_data_range, test_data_range03)
{
    // ([1, 2, 3, 4, 5], pytest.approx(4, abs=0.1))
    double result;
    result = data_range({1, 2, 3, 4, 5});
    EXPECT_EQ(4.0, result);
}

TEST(test_data_range, test_data_range04)
{
    // ([1, 0, 0, 1], pytest.approx(1, abs=0.01))
    double result;
    result = data_range({1, 0, 0, 1});
    EXPECT_EQ(1.0, result);
}


TEST(test_de_mean, test_de_mean01)
{
    // ([1, 2], [-0.5, 0.5])
    double result;
    result = de_mean({1, 2});
    EXPECT_EQ({-0.5, 0.5}, result);
}

TEST(test_de_mean, test_de_mean02)
{
    // ([1, 2, 12], [-4.0, -3.0, 7.0])
    double result;
    result = de_mean({1, 2, 12});
    EXPECT_EQ({-4.0, -3.0, 7.0}, result);
}

TEST(test_de_mean, test_de_mean03)
{
    // ([1, 2, 3, 4, 5], [-2.0, -1.0, 0.0, 1.0, 2.0])
    double result;
    result = de_mean({1, 2, 3, 4, 5});
    EXPECT_EQ({-2.0, -1.0, 0.0, 1.0, 2.0}, result);
}

TEST(test_de_mean, test_de_mean04)
{
    // ([1, 0, 0, 1], [0.5, -0.5, -0.5, 0.5])
    std::vector<double> result;
    result = de_mean({1, 0, 0, 1});
    EXPECT_EQ({0.5, -0.5, -0.5, 0.5}, result);
}

TEST(test_interquartile_range, test_interquartile_range01)
{
    // ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5),

    double result;
    result = interquartile_range({1, 2, 3, 4, 5, 6, 7, 8, 9, 10});
    EXPECT_EQ(5.0, result);
}
TEST(test_interquartile_range, test_interquartile_range02)
{
    // ([1, 2, 3, 4, 5, 100, 123], 98)
    double result;
    result = interquartile_range({1, 2, 3, 4, 5, 100, 123});
    EXPECT_EQ(98, result);
}
TEST(test_interquartile_range, test_interquartile_range03)
{
    // ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 3)
    double result;
    result = interquartile_range({1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7});
    EXPECT_EQ(3, result);
}
TEST(test_interquartile_range, test_interquartile_range04)
{
    // ([1, 0, 0, 1], pytest.approx(1, abs=0.01))
    double result;
    result = interquartile_range({1, 0, 0, 1});
    EXPECT_EQ(1.0, result);
}
TEST(test_mean, test_mean01)
{
    // ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5)
    double result;
    result = mean({1, 2, 3, 4, 5, 6, 7, 8, 9, 10});
    EXPECT_EQ(5.5, result);
}
TEST(test_mean, test_mean02)
{
    // ([1, 2, 3, 4, 5, 100, 123], 34)
    double result;
    result = mean({1, 2, 3, 4, 5, 100, 123});
    EXPECT_EQ(34, result);
}

TEST(test_mean, test_mean03)
{
    // ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], pytest.approx(5.27, abs=0.01))
    double result;
    result = mean({1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7});
    EXPECT_EQ(5.27, result);
}
TEST(test_mean, test_mean04)
{
    // ([1, 0, 0, 1], pytest.approx(0.5, abs=0.01))
    double result;
    result = mean({1, 0, 0, 1});
    EXPECT_EQ(0.5, result);
}

TEST(test_median, test_median01)
{
    // ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5),

    double result;
    result = median({1, 2, 3, 4, 5, 6, 7, 8, 9, 10});
    EXPECT_EQ(5.5, result);
}

TEST(test_median, test_median02)
{
    // ([1, 2, 3, 4, 5, 100, 123], 4),
    double result;
    result = median({1, 2, 3, 4, 5, 100, 123});
    EXPECT_EQ(4.0, result);
}

TEST(test_median, test_median03)
{
    // ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 4),
    double result;
    result = median({1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7});
    EXPECT_EQ(4.0, result);
}

TEST(test_median, test_median04)
{
    // ([1, 0, 0, 1], 0.5)
    double result;
    result = median({1, 0, 0, 1});
    EXPECT_EQ(0.5, result);
}

TEST(test_mode, test_mode01)
{
    // ([1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10], [5]),
    std::vector<double> result;
    result = mode({1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10});
    EXPECT_EQ({3}, result);
}

TEST(test_mode, test_mode02)
{
    // ([1, 2, 3, 4, 5, 100, 123, 98, 98], [98]),
    std::vector<double> result;
    result = mode({1, 2, 3, 4, 5, 100, 123, 98, 98});
    EXPECT_EQ({98}, result);
}

TEST(test_mode, test_mode03)
{
    // ([1, 4, 6, 5, 4, 3, 3, 15, 4, 3, 6, 7, 3], [3]),
    std::vector<double> result;
    result = mode({1, 4, 6, 5, 4, 3, 3, 15, 4, 3, 6, 7, 3});
    EXPECT_EQ({3.0}, result);
}

TEST(test_mode, test_mode04)
{
    // ([1, 0, 0, 1], [1, 0])
    std::vector<double> result;
    result = mode({1, 0, 0, 1});
    EXPECT_EQ({1,0}, result);
}

TEST(test_quantile, test_quantile01)
{
    // (0.99, [1, 0, 0, 1], 1)
    double result;
    result = quantile(0.99,{1, 0, 0, 1});
    EXPECT_EQ(1.0, result);
}

TEST(test_quantile, test_quantile02)
{
    // (0.1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2),
    double result;
    result = quantile(0.1, {1, 2, 3, 4, 5, 6, 7, 8, 9, 10});
    EXPECT_EQ(2.0, result);
}

TEST(test_quantile, test_quantile03)
{
    // (0.5, [1, 2, 3, 4, 5, 100, 123], 4),
    double result;
    result = quantile(0.5, {1, 2, 3, 4, 5, 100, 123});
    EXPECT_EQ(4.0, result);
}

TEST(test_quantile, test_quantile04)
{
    // (0.75, [1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 6),
    double result;
    result = quantile(0.75, {1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7});
    EXPECT_EQ(6.0, result);
}

TEST(test_standard_deviation, test_standard_deviation01)
{
    // ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], pytest.approx(3.03, abs=0.01)),
    double result;
    result = standard_deviation({1, 2, 3, 4, 5, 6, 7, 8, 9, 10});
    EXPECT_EQ(3.03, result);
}

TEST(test_standard_deviation, test_standard_deviation02)
{
    // ([1, 2, 3, 4, 5, 100, 123], pytest.approx(53.37, abs=0.01)),
    double result;
    result = standard_deviation({1, 2, 3, 4, 5, 100, 123});
    EXPECT_EQ(53.37, result);
}

TEST(test_standard_deviation, test_standard_deviation03)
{
    // ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], pytest.approx(3.64, abs=0.01)),
    double result;
    result = standard_deviation({1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7});
    EXPECT_EQ(3.64, result);
}

TEST(test_standard_deviation, test_standard_deviation04)
{
    // ([1, 0, 0, 1], pytest.approx(0.577, abs=0.01))
    double result;
    result = standard_deviation({1, 0, 0, 1});
    EXPECT_EQ(0.577, result);
}

TEST(test_sum_of_squares, test_sum_of_squares01)
{
    // ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 385),

    double result;
    result = sum_of_squares({1, 2, 3, 4, 5, 6, 7, 8, 9, 10});
    EXPECT_EQ(385, result);
}
TEST(test_sum_of_squares, test_sum_of_squares02)
{
    // ([1, 2, 3, 4, 5, 100, 123], 25184),

    double result;
    result = sum_of_squares({1, 2, 3, 4, 5, 100, 123});
    EXPECT_EQ(25184.0, result);
}
TEST(test_sum_of_squares, test_sum_of_squares03)
{
    // ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 438),
    double result;
    result = sum_of_squares({1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7});
    EXPECT_EQ(438, result);
}
TEST(test_sum_of_squares, test_sum_of_squares04)
{
    // ([1, 0, 0, 1], 2)
    double result;
    result = sum_of_squares({1, 0, 0, 1});
    EXPECT_EQ(2.0, result);
}


TEST(test_variance, test_variance01)
{
    // ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], pytest.approx(9.17, abs=0.01))
    double result;
    result = variance({1, 2, 3, 4, 5, 6, 7, 8, 9, 10});
    EXPECT_EQ(0, result);
}

TEST(test_variance, test_variance02)
{
    // ([1, 2, 3, 4, 5, 100, 123], pytest.approx(2848.67, abs=0.01))

    double result;
    result = variance({1, 2, 3, 4, 5, 100, 123});
    result = round(result,2);
    EXPECT_EQ(2848.67, result);
}

TEST(test_variance, test_variance03)
{
    // ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], pytest.approx(13.218, abs=0.01))

    double result;
    result = variance({1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7});
    result = round(result, 2);
    EXPECT_EQ(13.22, result);
}

TEST(test_variance, test_variance04)
{
    // ([1, 0, 0, 1], pytest.approx(0.33, abs=0.01))
    double result;
    result = variance({1,0,0,1});
    result = round(result,2);
    EXPECT_EQ(0.33, result);
}
