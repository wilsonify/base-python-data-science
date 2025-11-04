#include <gtest/gtest.h>
#include <vector>
#include <string>
#include <cmath>
#include <limits>
#include <chrono>
#include "../dscpp/c06_probability/probability.h"

class ProbabilityTest : public ::testing::Test {
protected:
    void SetUp() override {
        // Test strings for random choice
        test_choices = {"apple", "banana", "cherry", "date"};
        
        // Test data for statistical validation
        large_sample_size = 10000;
        tolerance = 0.05; // 5% tolerance for statistical tests
    }
    
    std::vector<std::string> test_choices;
    int large_sample_size;
    double tolerance;
};

// Error function and normal distribution
TEST_F(ProbabilityTest, ErfBasicValues) {
    // erf(0) = 0
    EXPECT_NEAR(erf(0.0), 0.0, 1e-10);
    
    // erf(infinity) = 1
    EXPECT_NEAR(erf(10.0), 1.0, 1e-10);
    
    // erf(-infinity) = -1
    EXPECT_NEAR(erf(-10.0), -1.0, 1e-10);
    
    // erf(1) ≈ 0.84270079
    EXPECT_NEAR(erf(1.0), 0.84270079, 1e-8);
    
    // erf(-1) ≈ -0.84270079
    EXPECT_NEAR(erf(-1.0), -0.84270079, 1e-8);
}

TEST_F(ProbabilityTest, ErfSymmetry) {
    // erf(-x) = -erf(x)
    for (double x = 0.1; x <= 2.0; x += 0.1) {
        EXPECT_NEAR(erf(-x), -erf(x), 1e-10);
    }
}

TEST_F(ProbabilityTest, UniformPDF) {
    // Standard uniform [0,1]
    EXPECT_DOUBLE_EQ(uniform_pdf(0.5, 0.0, 1.0), 1.0);
    EXPECT_DOUBLE_EQ(uniform_pdf(0.0, 0.0, 1.0), 1.0);
    EXPECT_DOUBLE_EQ(uniform_pdf(0.999, 0.0, 1.0), 1.0);
    
    // Outside range
    EXPECT_DOUBLE_EQ(uniform_pdf(-0.1, 0.0, 1.0), 0.0);
    EXPECT_DOUBLE_EQ(uniform_pdf(1.0, 0.0, 1.0), 0.0);
    EXPECT_DOUBLE_EQ(uniform_pdf(1.1, 0.0, 1.0), 0.0);
    
    // Custom range [2,4]
    EXPECT_DOUBLE_EQ(uniform_pdf(3.0, 2.0, 4.0), 0.5);  // 1/(4-2) = 0.5
    EXPECT_DOUBLE_EQ(uniform_pdf(2.0, 2.0, 4.0), 0.5);
    EXPECT_DOUBLE_EQ(uniform_pdf(1.9, 2.0, 4.0), 0.0);
    EXPECT_DOUBLE_EQ(uniform_pdf(4.0, 2.0, 4.0), 0.0);
}

TEST_F(ProbabilityTest, UniformCDF) {
    // Standard uniform [0,1]
    EXPECT_DOUBLE_EQ(uniform_cdf(-0.1, 0.0, 1.0), 0.0);
    EXPECT_DOUBLE_EQ(uniform_cdf(0.0, 0.0, 1.0), 0.0);
    EXPECT_DOUBLE_EQ(uniform_cdf(0.5, 0.0, 1.0), 0.5);
    EXPECT_DOUBLE_EQ(uniform_cdf(0.75, 0.0, 1.0), 0.75);
    EXPECT_DOUBLE_EQ(uniform_cdf(1.0, 0.0, 1.0), 1.0);
    EXPECT_DOUBLE_EQ(uniform_cdf(1.1, 0.0, 1.0), 1.0);
    
    // Custom range [2,4]
    EXPECT_DOUBLE_EQ(uniform_cdf(1.0, 2.0, 4.0), 0.0);
    EXPECT_DOUBLE_EQ(uniform_cdf(2.0, 2.0, 4.0), 0.0);
    EXPECT_DOUBLE_EQ(uniform_cdf(3.0, 2.0, 4.0), 0.5);
    EXPECT_DOUBLE_EQ(uniform_cdf(4.0, 2.0, 4.0), 1.0);
    EXPECT_DOUBLE_EQ(uniform_cdf(5.0, 2.0, 4.0), 1.0);
}

TEST_F(ProbabilityTest, NormalPDF) {
    // Standard normal N(0,1)
    EXPECT_NEAR(normal_pdf(0.0, 0.0, 1.0), 0.39894228, 1e-8);  // 1/sqrt(2π)
    EXPECT_NEAR(normal_pdf(1.0, 0.0, 1.0), 0.24197072, 1e-8);
    EXPECT_NEAR(normal_pdf(-1.0, 0.0, 1.0), 0.24197072, 1e-8);
    
    // Custom normal N(2,3)
    EXPECT_NEAR(normal_pdf(2.0, 2.0, 3.0), 0.13298076, 1e-8);  // 1/(3*sqrt(2π))
    EXPECT_NEAR(normal_pdf(5.0, 2.0, 3.0), 0.10648267, 1e-8);
    
    // Symmetry
    EXPECT_NEAR(normal_pdf(1.0, 0.0, 1.0), normal_pdf(-1.0, 0.0, 1.0), 1e-10);
}

TEST_F(ProbabilityTest, NormalCDF) {
    // Standard normal N(0,1)
    EXPECT_NEAR(normal_cdf(0.0, 0.0, 1.0), 0.5, 1e-10);
    EXPECT_NEAR(normal_cdf(1.0, 0.0, 1.0), 0.84134475, 1e-8);
    EXPECT_NEAR(normal_cdf(-1.0, 0.0, 1.0), 0.15865525, 1e-8);
    EXPECT_NEAR(normal_cdf(1.96, 0.0, 1.0), 0.9750021, 1e-6);
    
    // Custom normal N(2,3)
    EXPECT_NEAR(normal_cdf(2.0, 2.0, 3.0), 0.5, 1e-10);
    EXPECT_NEAR(normal_cdf(5.0, 2.0, 3.0), 0.84134475, 1e-8);
    
    // Symmetry
    double cdf_pos = normal_cdf(1.0, 0.0, 1.0);
    double cdf_neg = normal_cdf(-1.0, 0.0, 1.0);
    EXPECT_NEAR(cdf_pos + cdf_neg, 1.0, 1e-10);
}

TEST_F(ProbabilityTest, InverseNormalCDF) {
    // Standard normal N(0,1)
    EXPECT_NEAR(inverse_normal_cdf(0.5, 0.0, 1.0), 0.0, 1e-6);
    EXPECT_NEAR(inverse_normal_cdf(0.84134475, 0.0, 1.0), 1.0, 1e-4);
    EXPECT_NEAR(inverse_normal_cdf(0.15865525, 0.0, 1.0), -1.0, 1e-4);
    EXPECT_NEAR(inverse_normal_cdf(0.975, 0.0, 1.0), 1.96, 1e-3);
    
    // Custom normal N(2,3)
    EXPECT_NEAR(inverse_normal_cdf(0.5, 2.0, 3.0), 2.0, 1e-6);
    EXPECT_NEAR(inverse_normal_cdf(0.84134475, 2.0, 3.0), 5.0, 1e-4);
    
    // Roundtrip property: CDF(inverse_CDF(p)) ≈ p
    for (double p = 0.1; p <= 0.9; p += 0.1) {
        double x = inverse_normal_cdf(p, 0.0, 1.0);
        double p_roundtrip = normal_cdf(x, 0.0, 1.0);
        EXPECT_NEAR(p_roundtrip, p, 1e-4);
    }
}

// Random functions
TEST_F(ProbabilityTest, RandomChoice) {
    // Test that random_choice returns valid results
    std::string result = random_choice(test_choices);
    EXPECT_TRUE(std::find(test_choices.begin(), test_choices.end(), result) != test_choices.end());
    
    // Test with single choice
    std::vector<std::string> single_choice = {"only"};
    std::string result2 = random_choice(single_choice);
    EXPECT_EQ(result2, "only");
    
    // Test with empty vector
    std::vector<std::string> empty_choice;
    std::string result3 = random_choice(empty_choice);
    EXPECT_TRUE(result3.empty());
}

TEST_F(ProbabilityTest, RandomKid) {
    std::string result = random_kid();
    EXPECT_TRUE(result == "boy" || result == "girl");
}

TEST_F(ProbabilityTest, RandomNormal) {
    // Test that random_normal returns finite values
    double result = random_normal();
    EXPECT_TRUE(std::isfinite(result));
    
    // Test statistical properties with large sample
    double sum = 0.0;
    double sum_squares = 0.0;
    int sample_size = 1000;
    
    for (int i = 0; i < sample_size; ++i) {
        double sample = random_normal();
        sum += sample;
        sum_squares += sample * sample;
        EXPECT_TRUE(std::isfinite(sample));
    }
    
    double mean = sum / sample_size;
    double variance = (sum_squares - sum * sum / sample_size) / (sample_size - 1);
    
    // For standard normal, mean should be near 0, variance near 1
    EXPECT_NEAR(mean, 0.0, 0.1);  // Allow 0.1 tolerance for mean
    EXPECT_NEAR(variance, 1.0, 0.2);  // Allow 0.2 tolerance for variance
}

// Probability distributions
TEST_F(ProbabilityTest, BernoulliTrial) {
    // Test edge cases
    EXPECT_EQ(bernoulli_trial(0.0), 0);
    EXPECT_EQ(bernoulli_trial(1.0), 1);
    
    // Test that result is always 0 or 1
    for (double p = 0.1; p <= 0.9; p += 0.1) {
        int result = bernoulli_trial(p);
        EXPECT_TRUE(result == 0 || result == 1);
    }
    
    // Test statistical properties with large sample
    double sum = 0.0;
    double p = 0.3;
    int sample_size = 10000;
    
    for (int i = 0; i < sample_size; ++i) {
        sum += bernoulli_trial(p);
    }
    
    double empirical_p = sum / sample_size;
    EXPECT_NEAR(empirical_p, p, tolerance);
}

TEST_F(ProbabilityTest, Binomial) {
    // Test edge cases
    EXPECT_EQ(binomial(0.0, 10), 0);
    EXPECT_EQ(binomial(1.0, 10), 10);
    EXPECT_EQ(binomial(0.5, 0), 0);
    
    // Test that result is in valid range
    for (double p = 0.1; p <= 0.9; p += 0.1) {
        for (int n = 1; n <= 10; ++n) {
            int result = binomial(p, n);
            EXPECT_GE(result, 0);
            EXPECT_LE(result, n);
        }
    }
    
    // Test statistical properties with large sample
    double sum = 0.0;
    double p = 0.3;
    int n = 20;
    int sample_size = 1000;
    
    for (int i = 0; i < sample_size; ++i) {
        sum += binomial(p, n);
    }
    
    double empirical_mean = sum / sample_size;
    double theoretical_mean = n * p;
    EXPECT_NEAR(empirical_mean, theoretical_mean, theoretical_mean * tolerance);
}

// Edge cases and special values
TEST_F(ProbabilityTest, HandlesZeroVariance) {
    // Normal distribution with zero variance
    EXPECT_NEAR(normal_pdf(5.0, 5.0, 0.0), std::numeric_limits<double>::infinity(), 1e-10);
    EXPECT_NEAR(normal_cdf(4.0, 5.0, 0.0), 0.0, 1e-10);
    EXPECT_NEAR(normal_cdf(5.0, 5.0, 0.0), 0.5, 1e-10);
    EXPECT_NEAR(normal_cdf(6.0, 5.0, 0.0), 1.0, 1e-10);
}

TEST_F(ProbabilityTest, HandlesNegativeParameters) {
    // Standard deviation should be positive
    EXPECT_DOUBLE_EQ(normal_pdf(0.0, 0.0, -1.0), normal_pdf(0.0, 0.0, 1.0));
    EXPECT_DOUBLE_EQ(normal_cdf(0.0, 0.0, -1.0), normal_cdf(0.0, 0.0, 1.0));
    
    // Uniform distribution should handle negative ranges
    EXPECT_DOUBLE_EQ(uniform_pdf(-1.5, -2.0, -1.0), 1.0);
    EXPECT_DOUBLE_EQ(uniform_cdf(-1.5, -2.0, -1.0), 0.5);
}

// Mathematical properties
TEST_F(ProbabilityTest, PDFIntegrationProperties) {
    // For uniform distribution, PDF should integrate to 1 over its range
    double a = 0.0, b = 4.0;
    double pdf_value = uniform_pdf(2.0, a, b);
    EXPECT_DOUBLE_EQ(pdf_value * (b - a), 1.0);
    
    // For normal distribution, PDF should be positive everywhere
    EXPECT_GT(normal_pdf(0.0, 0.0, 1.0), 0.0);
    EXPECT_GT(normal_pdf(10.0, 0.0, 1.0), 0.0);
    EXPECT_GT(normal_pdf(-10.0, 0.0, 1.0), 0.0);
}

TEST_F(ProbabilityTest, CDFProperties) {
    // CDF should be monotonic increasing
    for (double x = -3.0; x <= 3.0; x += 0.1) {
        double cdf1 = normal_cdf(x, 0.0, 1.0);
        double cdf2 = normal_cdf(x + 0.1, 0.0, 1.0);
        EXPECT_LE(cdf1, cdf2);
    }
    
    // CDF should approach 0 as x -> -infinity and 1 as x -> infinity
    EXPECT_LT(normal_cdf(-5.0, 0.0, 1.0), 0.001);
    EXPECT_GT(normal_cdf(5.0, 0.0, 1.0), 0.999);
}

TEST_F(ProbabilityTest, InverseCDFProperties) {
    // Inverse CDF should be monotonic increasing
    for (double p = 0.1; p <= 0.8; p += 0.1) {
        double inv1 = inverse_normal_cdf(p, 0.0, 1.0);
        double inv2 = inverse_normal_cdf(p + 0.1, 0.0, 1.0);
        EXPECT_LE(inv1, inv2);
    }
    
    // Inverse CDF should handle edge cases
    EXPECT_LT(inverse_normal_cdf(0.001, 0.0, 1.0), -3.0);
    EXPECT_GT(inverse_normal_cdf(0.999, 0.0, 1.0), 3.0);
}

// Performance tests
TEST_F(ProbabilityTest, PerformanceSanity) {
    // Test that functions can handle large numbers of calls efficiently
    int iterations = 10000;
    
    auto start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < iterations; ++i) {
        double x = static_cast<double>(i) / 1000.0;
        normal_cdf(x, 0.0, 1.0);
    }
    auto end = std::chrono::high_resolution_clock::now();
    
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    EXPECT_LT(duration.count(), 1000); // Should complete in less than 1 second
}

// Consistency tests
TEST_F(ProbabilityTest, ConsistencyBetweenPDFAndCDF) {
    // For very small intervals, CDF difference should approximate PDF
    double x = 0.0;
    double h = 1e-6;
    double cdf_diff = normal_cdf(x + h, 0.0, 1.0) - normal_cdf(x, 0.0, 1.0);
    double pdf_val = normal_pdf(x, 0.0, 1.0);
    
    EXPECT_NEAR(cdf_diff / h, pdf_val, 1e-3);
}
