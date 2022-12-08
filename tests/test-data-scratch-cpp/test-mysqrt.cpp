#include <gtest/gtest.h>
#include "data-scratch-cpp-library.h"

TEST(mysqrtTests, returns5With25PassedIn)
{
    double result;
    result = mysqrt(25.0);
    EXPECT_EQ(5.0, result);
}

TEST(mysqrtTests, returns0WithNegativePassedIn)
{
    double result;
    result = mysqrt(-25.0);
    EXPECT_EQ(0.0, result);
}

TEST(mysqrtTests, returns10With100PassedIn)
{
    double result;
    result = mysqrt(100.0);
    EXPECT_EQ(10.0, result);
}

TEST(mysqrtTests, returns212With44944PassedIn)
{
    double result;
    result = mysqrt(44944.0);
    EXPECT_EQ(212.02703422038516, result);
}