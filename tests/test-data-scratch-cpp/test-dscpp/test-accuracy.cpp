#include <gtest/gtest.h>
#include "data-scratch-cpp-library.h"

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