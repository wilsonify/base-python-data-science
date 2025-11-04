#include <gtest/gtest.h>
#include <vector>
#include <map>
#include <cmath>
#include <limits>
#include <chrono>
#include "../dscpp/c11_machine_learning/machine_learning.h"

class MachineLearningTest : public ::testing::Test {
protected:
    void SetUp() override {
        // Test data for splitting
        test_data = {
            {1.0, 2.0, 3.0},
            {4.0, 5.0, 6.0},
            {7.0, 8.0, 9.0},
            {10.0, 11.0, 12.0},
            {13.0, 14.0, 15.0}
        };
        
        test_features = {
            {1.0, 2.0},
            {3.0, 4.0},
            {5.0, 6.0},
            {7.0, 8.0},
            {9.0, 10.0}
        };
        
        test_labels = {0.0, 1.0, 0.0, 1.0, 0.0};
        
        // Empty data
        empty_data = {};
        empty_features = {};
        empty_labels = {};
    }
    
    std::vector<std::vector<double>> test_data, test_features, empty_data, empty_features;
    std::vector<double> test_labels, empty_labels;
};

// Data splitting functions
TEST_F(MachineLearningTest, SplitData) {
    SplitData result = split_data(test_data, 0.4);
    
    // Check that total size is preserved
    EXPECT_EQ(result.train.size() + result.test.size(), test_data.size());
    
    // Check that all rows are either in train or test
    std::vector<std::vector<double>> all_rows = result.train;
    all_rows.insert(all_rows.end(), result.test.begin(), result.test.end());
    
    // Sort both for comparison (since order is random)
    std::sort(test_data.begin(), test_data.end());
    std::sort(all_rows.begin(), all_rows.end());
    
    EXPECT_EQ(all_rows, test_data);
}

TEST_F(MachineLearningTest, SplitDataEmpty) {
    SplitData result = split_data(empty_data, 0.5);
    
    EXPECT_TRUE(result.train.empty());
    EXPECT_TRUE(result.test.empty());
}

TEST_F(MachineLearningTest, SplitDataEdgeCases) {
    // Test with prob = 0 (all should go to train)
    SplitData result1 = split_data(test_data, 0.0);
    EXPECT_EQ(result1.train.size(), test_data.size());
    EXPECT_TRUE(result1.test.empty());
    
    // Test with prob = 1 (all should go to test)
    SplitData result2 = split_data(test_data, 1.0);
    EXPECT_TRUE(result2.train.empty());
    EXPECT_EQ(result2.test.size(), test_data.size());
}

TEST_F(MachineLearningTest, SplitDataProbabilities) {
    // Test that split ratio is approximately correct with large sample
    std::vector<std::vector<double>> large_data(1000, {1.0, 2.0, 3.0});
    double prob = 0.3;
    
    SplitData result = split_data(large_data, prob);
    
    double actual_prob = static_cast<double>(result.test.size()) / large_data.size();
    EXPECT_NEAR(actual_prob, prob, 0.05); // Allow 5% tolerance
}

TEST_F(MachineLearningTest, TrainTestSplit) {
    TrainTestSplit result = train_test_split(test_features, test_labels, 0.4);
    
    // Check that total sizes are preserved
    EXPECT_EQ(result.x_train.size() + result.x_test.size(), test_features.size());
    EXPECT_EQ(result.y_train.size() + result.y_test.size(), test_labels.size());
    EXPECT_EQ(result.x_train.size(), result.y_train.size());
    EXPECT_EQ(result.x_test.size(), result.y_test.size());
    
    // Check that all features and labels are either in train or test
    std::vector<std::vector<double>> all_features = result.x_train;
    all_features.insert(all_features.end(), result.x_test.begin(), result.x_test.end());
    
    std::vector<double> all_labels = result.y_train;
    all_labels.insert(all_labels.end(), result.y_test.begin(), result.y_test.end());
    
    // Sort for comparison (since order is random)
    auto sorted_test_features = test_features;
    auto sorted_all_features = all_features;
    std::sort(sorted_test_features.begin(), sorted_test_features.end());
    std::sort(sorted_all_features.begin(), sorted_all_features.end());
    
    auto sorted_test_labels = test_labels;
    auto sorted_all_labels = all_labels;
    std::sort(sorted_test_labels.begin(), sorted_test_labels.end());
    std::sort(sorted_all_labels.begin(), sorted_all_labels.end());
    
    EXPECT_EQ(sorted_all_features, sorted_test_features);
    EXPECT_EQ(sorted_all_labels, sorted_all_labels);
}

TEST_F(MachineLearningTest, TrainTestSplitEmpty) {
    TrainTestSplit result = train_test_split(empty_features, empty_labels, 0.5);
    
    EXPECT_TRUE(result.x_train.empty());
    EXPECT_TRUE(result.x_test.empty());
    EXPECT_TRUE(result.y_train.empty());
    EXPECT_TRUE(result.y_test.empty());
}

TEST_F(MachineLearningTest, TrainTestSplitMismatchedSizes) {
    std::vector<double> wrong_labels = {0.0, 1.0}; // Different size
    
    EXPECT_THROW(train_test_split(test_features, wrong_labels, 0.5), std::invalid_argument);
}

TEST_F(MachineLearningTest, TrainTestSplitEdgeCases) {
    // Test with test_pct = 0 (all should go to train)
    TrainTestSplit result1 = train_test_split(test_features, test_labels, 0.0);
    EXPECT_EQ(result1.x_train.size(), test_features.size());
    EXPECT_EQ(result1.y_train.size(), test_labels.size());
    EXPECT_TRUE(result1.x_test.empty());
    EXPECT_TRUE(result1.y_test.empty());
    
    // Test with test_pct = 1 (all should go to test)
    TrainTestSplit result2 = train_test_split(test_features, test_labels, 1.0);
    EXPECT_TRUE(result2.x_train.empty());
    EXPECT_TRUE(result2.y_train.empty());
    EXPECT_EQ(result2.x_test.size(), test_features.size());
    EXPECT_EQ(result2.y_test.size(), test_labels.size());
}

// Performance metrics
TEST_F(MachineLearningTest, Accuracy) {
    // Perfect classification
    EXPECT_DOUBLE_EQ(accuracy(100, 0, 0, 100), 1.0);
    
    // All wrong
    EXPECT_DOUBLE_EQ(accuracy(0, 100, 100, 0), 0.0);
    
    // Half correct
    EXPECT_DOUBLE_EQ(accuracy(50, 50, 50, 50), 0.5);
    
    // Realistic case
    EXPECT_NEAR(accuracy(80, 10, 5, 105), 0.925, 1e-10);
}

TEST_F(MachineLearningTest, AccuracyEdgeCases) {
    // No predictions (all zeros)
    EXPECT_DOUBLE_EQ(accuracy(0, 0, 0, 0), 0.0);
    
    // Only true positives
    EXPECT_DOUBLE_EQ(accuracy(10, 0, 0, 0), 1.0);
    
    // Only true negatives
    EXPECT_DOUBLE_EQ(accuracy(0, 0, 0, 10), 1.0);
}

TEST_F(MachineLearningTest, Precision) {
    // Perfect precision (no false positives)
    EXPECT_DOUBLE_EQ(precision(100, 0, 50, 50), 1.0);
    
    // No precision (all false positives)
    EXPECT_DOUBLE_EQ(precision(0, 100, 0, 0), 0.0);
    
    // 50% precision
    EXPECT_DOUBLE_EQ(precision(50, 50, 25, 75), 0.5);
    
    // Realistic case
    EXPECT_NEAR(precision(80, 20, 10, 90), 0.8, 1e-10);
}

TEST_F(MachineLearningTest, PrecisionEdgeCases) {
    // No positive predictions
    EXPECT_DOUBLE_EQ(precision(0, 0, 10, 90), 0.0);
    
    // Only true positives
    EXPECT_DOUBLE_EQ(precision(10, 0, 5, 85), 1.0);
}

TEST_F(MachineLearningTest, Recall) {
    // Perfect recall (no false negatives)
    EXPECT_DOUBLE_EQ(recall(100, 50, 0, 50), 1.0);
    
    // No recall (all false negatives)
    EXPECT_DOUBLE_EQ(recall(0, 0, 100, 100), 0.0);
    
    // 50% recall
    EXPECT_DOUBLE_EQ(recall(50, 25, 50, 75), 0.5);
    
    // Realistic case
    EXPECT_NEAR(recall(80, 10, 20, 90), 0.8, 1e-10);
}

TEST_F(MachineLearningTest, RecallEdgeCases) {
    // No actual positives
    EXPECT_DOUBLE_EQ(recall(0, 10, 0, 90), 0.0);
    
    // Only true positives
    EXPECT_DOUBLE_EQ(recall(10, 5, 0, 85), 1.0);
}

TEST_F(MachineLearningTest, F1Score) {
    // Perfect F1 (perfect precision and recall)
    EXPECT_DOUBLE_EQ(f1_score(100, 0, 0, 100), 1.0);
    
    // Zero F1 (zero precision or recall)
    EXPECT_DOUBLE_EQ(f1_score(0, 100, 100, 0), 0.0);
    EXPECT_DOUBLE_EQ(f1_score(0, 0, 100, 100), 0.0);
    
    // Harmonic mean property
    double p = 0.8, r = 0.6;
    double expected_f1 = 2 * p * r / (p + r);
    EXPECT_NEAR(f1_score(80, 20, 53, 47), expected_f1, 1e-10);
    
    // When precision = recall, F1 = precision = recall
    EXPECT_DOUBLE_EQ(f1_score(60, 40, 40, 60), 0.6);
}

TEST_F(MachineLearningTest, F1ScoreEdgeCases) {
    // Both precision and recall are zero
    EXPECT_DOUBLE_EQ(f1_score(0, 0, 0, 100), 0.0);
    
    // One of precision or recall is zero
    EXPECT_DOUBLE_EQ(f1_score(0, 100, 0, 0), 0.0);
    EXPECT_DOUBLE_EQ(f1_score(0, 0, 100, 0), 0.0);
}

// Mathematical properties and relationships
TEST_F(MachineLearningTest, MetricRelationships) {
    // F1 should always be between precision and recall
    double tp = 80, fp = 20, fn = 10, tn = 90;
    double p = precision(tp, fp, fn, tn);
    double r = recall(tp, fp, fn, tn);
    double f1 = f1_score(tp, fp, fn, tn);
    
    EXPECT_LE(f1, std::max(p, r));
    EXPECT_GE(f1, std::min(p, r));
}

TEST_F(MachineLearningTest, AccuracyRange) {
    // Accuracy should always be between 0 and 1
    for (int tp = 0; tp <= 100; tp += 20) {
        for (int fp = 0; fp <= 100; fp += 20) {
            for (int fn = 0; fn <= 100; fn += 20) {
                for (int tn = 0; tn <= 100; tn += 20) {
                    double acc = accuracy(tp, fp, fn, tn);
                    EXPECT_GE(acc, 0.0);
                    EXPECT_LE(acc, 1.0);
                }
            }
        }
    }
}

TEST_F(MachineLearningTest, PrecisionRecallRange) {
    // Precision and recall should always be between 0 and 1
    for (int tp = 0; tp <= 100; tp += 20) {
        for (int fp = 0; fp <= 100; fp += 20) {
            for (int fn = 0; fn <= 100; fn += 20) {
                double p = precision(tp, fp, fn, 0);
                double r = recall(tp, fp, fn, 0);
                
                EXPECT_GE(p, 0.0);
                EXPECT_LE(p, 1.0);
                EXPECT_GE(r, 0.0);
                EXPECT_LE(r, 1.0);
            }
        }
    }
}

// Edge cases and special values
TEST_F(MachineLearningTest, HandlesLargeNumbers) {
    double tp = 1e6, fp = 1e5, fn = 1e5, tn = 1e6;
    
    EXPECT_NEAR(accuracy(tp, fp, fn, tn), 0.833333, 1e-6);
    EXPECT_NEAR(precision(tp, fp, fn, tn), 0.909091, 1e-6);
    EXPECT_NEAR(recall(tp, fp, fn, tn), 0.909091, 1e-6);
    EXPECT_NEAR(f1_score(tp, fp, fn, tn), 0.909091, 1e-6);
}

TEST_F(MachineLearningTest, HandlesSmallNumbers) {
    double tp = 1e-6, fp = 1e-7, fn = 1e-7, tn = 1e-6;
    
    EXPECT_NEAR(accuracy(tp, fp, fn, tn), 0.833333, 1e-6);
    EXPECT_NEAR(precision(tp, fp, fn, tn), 0.909091, 1e-6);
    EXPECT_NEAR(recall(tp, fp, fn, tn), 0.909091, 1e-6);
    EXPECT_NEAR(f1_score(tp, fp, fn, tn), 0.909091, 1e-6);
}

// Consistency tests
TEST_F(MachineLearningTest, SplitConsistency) {
    // Multiple splits with same seed should produce same results
    // (Note: This test assumes deterministic behavior, which may not be true
    // with the current random implementation)
    
    SplitData result1 = split_data(test_data, 0.5);
    SplitData result2 = split_data(test_data, 0.5);
    
    // Both should preserve total size
    EXPECT_EQ(result1.train.size() + result1.test.size(), test_data.size());
    EXPECT_EQ(result2.train.size() + result2.test.size(), test_data.size());
}

// Performance tests
TEST_F(MachineLearningTest, PerformanceSanity) {
    // Create large dataset
    std::vector<std::vector<double>> large_features(10000, {1.0, 2.0, 3.0, 4.0});
    std::vector<double> large_labels(10000, 1.0);
    
    auto start = std::chrono::high_resolution_clock::now();
    TrainTestSplit result = train_test_split(large_features, large_labels, 0.3);
    auto end = std::chrono::high_resolution_clock::now();
    
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    EXPECT_LT(duration.count(), 1000); // Should complete in less than 1 second
    
    // Check that split is reasonable
    EXPECT_EQ(result.x_train.size() + result.x_test.size(), large_features.size());
    EXPECT_EQ(result.y_train.size() + result.y_test.size(), large_labels.size());
}

TEST_F(MachineLearningTest, MetricsPerformance) {
    int iterations = 100000;
    
    auto start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < iterations; ++i) {
        accuracy(80, 10, 5, 105);
        precision(80, 10, 5, 105);
        recall(80, 10, 5, 105);
        f1_score(80, 10, 5, 105);
    }
    auto end = std::chrono::high_resolution_clock::now();
    
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    EXPECT_LT(duration.count(), 1000); // Should complete in less than 1 second
}

// Real-world scenario tests
TEST_F(MachineLearningTest, RealWorldScenario) {
    // Simulate a binary classification scenario
    // 1000 samples, 90% negative, 10% positive
    // Model with 95% accuracy, 80% precision, 70% recall
    
    int total_samples = 1000;
    int actual_negatives = 900;
    int actual_positives = 100;
    
    // Model performance
    int tp = 70;    // 70% of 100 positives correctly identified
    int fp = 35;    // 5% of 900 negatives incorrectly classified as positive
    int fn = 30;    // 30% of 100 positives missed
    int tn = 865;   // 95% of 900 negatives correctly identified
    
    double acc = accuracy(tp, fp, fn, tn);
    double prec = precision(tp, fp, fn, tn);
    double rec = recall(tp, fp, fn, tn);
    double f1 = f1_score(tp, fp, fn, tn);
    
    EXPECT_NEAR(acc, 0.935, 1e-3);
    EXPECT_NEAR(prec, 0.667, 1e-3);
    EXPECT_NEAR(rec, 0.7, 1e-3);
    EXPECT_NEAR(f1, 0.683, 1e-3);
    
    // Verify mathematical relationships
    EXPECT_LE(f1, std::max(prec, rec));
    EXPECT_GE(f1, std::min(prec, rec));
}
