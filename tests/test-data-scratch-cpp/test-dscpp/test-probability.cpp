#include <gtest/gtest.h>
#include "data-scratch-cpp-library.h"

TEST(smokeTest, BasicAssertion) {
    EXPECT_EQ(7 * 6, 42);
}

TEST(test_random_normal, test_random_normal01)
{
    double result;
    result = random_normal()
    EXPECT_GT(0, result);
    EXPECT_LT(1, result);
}
TEST(test_bernoulli_trial, test_bernoulli_trial01)
{
    double result;
    result = bernoulli_trial(0.5)
    EXPECT_GE(0, result);
    EXPECT_LE(1, result);
}


TEST(test_binomial, test_binomial01)
{
    //(1, 120, pytest.approx(120, abs=0.01))
    double result;
    result = binomial(1,120)
    result = round(result, 0)
    EXPECT_EQ(120, result);
}
TEST(test_binomial, test_binomial02)
{
    //(1, 1, pytest.approx(1, abs=0.01))
    double result;
    result = binomial(1,1)
    result = round(result, 0)
    EXPECT_EQ(1, result);
}
TEST(test_binomial, test_binomial03)
{
    //(0.2, 100, pytest.approx(20, abs=10))
    double result;
    result = binomial(0.2,100)
    result = round(result, 0)
    EXPECT_EQ(20, result);
}
TEST(test_binomial, test_binomial03)
{
    //(0, 120, pytest.approx(0, abs=0.01))
    double result;
    result = binomial(0, 120)
    result = round(result, 0)
    EXPECT_EQ(0, result);
}

TEST(test_inverse_normal_cdf, test_inverse_normal_cdf01)
{
    //(0.01, 100, 5, pytest.approx(88.36, abs=0.01))
    double result;
    result = inverse_normal_cdf(0.01, 100, 5)
    result = round(result, 2)
    EXPECT_EQ(88.36, result);
}
TEST(test_inverse_normal_cdf, test_inverse_normal_cdf01)
{
    //(0.10, 100, 5, pytest.approx(93.59, abs=0.01)),
    double result;
    result = inverse_normal_cdf(.10, 100, 5, pytest)
    result = round(result, 2)
    EXPECT_EQ(93.59, result);
}TEST(test_inverse_normal_cdf, test_inverse_normal_cdf01)
{
    //(0.5, 100, 5, pytest.approx(100, abs=0.01)),
    double result;
    result = inverse_normal_cdf(0.5, 100, 5)
    result = round(result, 2)
    EXPECT_EQ(100, result);
}
TEST(test_inverse_normal_cdf, test_inverse_normal_cdf01)
{
    //(0.95, 100, 5, pytest.approx(108, abs=1))
    double result;
    result = inverse_normal_cdf(0.95, 100)
    result = round(result, 2)
    EXPECT_EQ(108, result);
}

TEST(test_normal_cdf, test_normal_cdf01)
{
//(0.1, 100, 5, pytest.approx(0, abs=0.01))
    double result;
    result = test_normal_cdf(0.1, 100, 5)
    result = round(result, 2)
    EXPECT_EQ(0, result);
}
TEST(test_normal_cdf, test_normal_cdf02)
{
// (95, 100, 5, pytest.approx(0.16, abs=0.01)),
    double result;
    result = test_normal_cdf(95, 100, 5)
    result = round(result, 2)
    EXPECT_EQ(0.16, result);
}
TEST(test_normal_cdf, test_normal_cdf03)
{
// (100, 100, 5, pytest.approx(0.5, abs=0.01)),
    double result;
    result = test_normal_cdf(100, 100, 5)
    result = round(result, 2)
    EXPECT_EQ(0.5, result);
}
TEST(test_normal_cdf, test_normal_cdf04)
{
// (105, 100, 5, pytest.approx(0.84, abs=1))
    double result;
    result = test_normal_cdf(105, 100, 5)
    result = round(result, 2)
    EXPECT_EQ(0.84, result);
}
TEST(test_normal_pdf, test_normal_pdf01)
{
    // (0.1, 100, 5, pytest.approx(0, abs=0.01))
    double result;
    result = test_normal_cdf(0.1, 100, 5)
    result = round(result, 2)
    EXPECT_EQ(0.0, result);
}
TEST(test_normal_pdf, test_normal_pdf02)
{
// (95, 100, 5, pytest.approx(0.05, abs=0.01))
    double result;
    result = test_normal_cdf(95, 100, 5)
    result = round(result, 2)
    EXPECT_EQ(0.05, result);
}
TEST(test_normal_pdf, test_normal_pdf02)
{
// (100, 100, 5, pytest.approx(0.08, abs=0.01))
    double result;
    result = test_normal_cdf(100, 100, 5)
    result = round(result, 2)
    EXPECT_EQ(0.08, result);
}
TEST(test_normal_pdf, test_normal_pdf02)
{
// (105, 100, 5, pytest.approx(0.84, abs=1))
    double result;
    result = test_normal_cdf(105, 100, 5)
    result = round(result, 2)
    EXPECT_EQ(0.84, result);
}

TEST(test_uniform_cdf, test_uniform_cdf01)
{
    // (0.1, pytest.approx(0.1, abs=0.01)),
    double result;
    result = uniform_cdf(0.1)
    result = round(result, 2)
    EXPECT_EQ(0.1, result);
}
TEST(test_uniform_cdf, test_uniform_cdf02)
{
    // (0.5, pytest.approx(0.5, abs=0.01)),
    double result;
    result = uniform_cdf(0.5)
    result = round(result, 2)
    EXPECT_EQ(0.5, result);
}

TEST(test_uniform_cdf, test_uniform_cdf03)
{
    // (0.9, pytest.approx(0.9, abs=0.01)),
    double result;
    result = uniform_cdf(0.9)
    result = round(result, 2)
    EXPECT_EQ(0.9, result);
}
TEST(test_uniform_cdf, test_uniform_cdf04)
{
    // (2, pytest.approx(1, abs=0.1))
    double result;
    result = uniform_cdf(2)
    result = round(result, 2)
    EXPECT_EQ(1.0, result);
}

TEST(test_uniform_pdf, test_uniform_pdf01)
{
    // (-0.1, pytest.approx(0, abs=0.01)),
    double result;
    result = uniform_pdf(-0.1)
    result = round(result, 2)
    EXPECT_EQ(0.0, result);
}

TEST(test_uniform_pdf, test_uniform_pdf02)
{
    // (0.5, pytest.approx(1, abs=0.01)),
    double result;
    result = uniform_pdf(0.5)
    result = round(result, 2)
    EXPECT_EQ(1.0, result);
}

TEST(test_uniform_pdf, test_uniform_pdf03)
{
    // (0.9, pytest.approx(1, abs=0.01)),
    double result;
    result = uniform_pdf(0.9)
    result = round(result, 2)
    EXPECT_EQ(1.0, result);
}

TEST(test_uniform_pdf, test_uniform_pdf04)
{
    // (2, pytest.approx(0, abs=0.1))
    double result;
    result = uniform_pdf(2.0)
    result = round(result, 2)
    EXPECT_EQ(0.0, result);
}
