#include <gtest/gtest.h>
#include "data-scratch-cpp-library.h"

TEST(smokeTest, BasicAssertion) {
    EXPECT_EQ(7 * 6, 42);
}

TEST(accuracyTests, accuracyTest01)
{
    double result;
    result = accuracy(1.0, 1.0, 1.0, 1.0);
    EXPECT_EQ(0.49875311720698257, result);
}

TEST(accuracyTests, accuracyTest02)
{
    double result;
    result = accuracy(10.0, 10.0, 10.0, 10.0);
    EXPECT_EQ(0.49987503124218946, result);
}

TEST(accuracyTests, accuracyTest03)
{
    double result;
    result = accuracy(10.0, 100.0, 1000.0, 10000.0);
    EXPECT_EQ(0.90098928803844458, result);
}

TEST(accuracyTests, accuracyTest04)
{
    double result;
    result = accuracy(0.0, 0.0, 0.0, 0.0);
    EXPECT_EQ(0.0, result);
}

TEST(accuracyTests, accuracyTest05)
{
    // (100, 120, 200, 303, pytest.approx(0.55, abs=0.01)),
    double result;
    result = accuracy(100, 120, 200, 303);
    result = round(result,2)
    EXPECT_EQ(0.55, result);
}
TEST(accuracyTests, accuracyTest06)
{
    // (100, 1, 200, 303, pytest.approx(0.66, abs=0.01)),
    double result;
    result = accuracy(100, 1, 200, 303);
    result = round(result,2)
    EXPECT_EQ(0.66, result);
}
TEST(accuracyTests, accuracyTest04)
{
    // (0, 120, 200, 303, pytest.approx(0.48, abs=0.01))
    double result;
    result = accuracy(0, 120, 200, 303);
    result = round(result, 2)
    EXPECT_EQ(0.48, result);
}

TEST(f1Tests, f1Test01)
{
    //(100, 120, 200, 303, pytest.approx(0.38, abs=0.01)),
    double result;
    result = f1_score(100, 120, 200, 303);
    result = round(result, 2)
    EXPECT_EQ(0.38, result);
}
TEST(f1Tests, f1Test02)
{
    //(100, 1, 200, 303, pytest.approx(0.49, abs=0.01)),
    double result;
    result = f1_score(100, 1, 200, 303);
    result = round(result, 2)
    EXPECT_EQ(0.49, result);
}
TEST(f1Tests, f1Test03)
{
    //(1, 120, 200, 303, pytest.approx(0.01, abs=0.01))
    double result;
    result = f1_score(1, 120, 200, 303);
    result = round(result, 2)
    EXPECT_EQ(0.01, result);
}

TEST(precisionTests, precisionTest01)
{
    //(100, 120, 200, 303, pytest.approx(0.45, abs=0.01))
    double result;
    result = f1_score(100, 120, 200, 303);
    result = round(result, 2)
    EXPECT_EQ(0.45, result);
}
TEST(precisionTests, precisionTest02)
{
    //(100, 1, 200, 303, pytest.approx(0.99, abs=0.01)),
    double result;
    result = f1_score(100, 1, 200, 303);
    result = round(result, 2)
    EXPECT_EQ(0.99, result);
}
TEST(precisionTests, precisionTest03)
{
    //(1, 120, 200, 303, pytest.approx(0.01, abs=0.01))
    double result;
    result = f1_score(1, 120, 200, 303);
    result = round(result, 2)
    EXPECT_EQ(0.01, result);
}
TEST(recallTests, recallTest01)
{
    //(100, 120, 200, 303, pytest.approx(0.33, abs=0.01)),
    double result;
    result = f1_score(100, 120, 200, 303);
    result = round(result, 2)
    EXPECT_EQ(0.33, result);
}
TEST(recallTests, recallTest02)
{
    //(100, 1, 200, 303, pytest.approx(0.33, abs=0.01))
    double result;
    result = f1_score(100, 1, 200, 303);
    result = round(result, 2)
    EXPECT_EQ(0.33, result);
}
TEST(recallTests, recallTest03)
{
    //(1, 120, 200, 303, pytest.approx(0.01, abs=0.01))
    double result;
    result = f1_score(1, 120, 200, 303);
    result = round(result, 2)
    EXPECT_EQ(0.01, result);
}