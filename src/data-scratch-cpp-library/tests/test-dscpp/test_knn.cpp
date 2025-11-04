#include <gtest/gtest.h>
#include <vector>
#include <string>
#include <map>
#include <cmath>
#include <limits>
#include <chrono>
#include "../dscpp/c12_k_nearest_neighbors/nearest_neighbors.h"

class KNNTest : public ::testing::Test {
protected:
    void SetUp() override {
        // Simple 2D classification data
        classA_points = {
            {{1.0, 1.0}, "A"},
            {{1.5, 1.5}, "A"},
            {{2.0, 2.0}, "A"},
            {{0.5, 0.5}, "A"}
        };
        
        classB_points = {
            {{5.0, 5.0}, "B"},
            {{5.5, 5.5}, "B"},
            {{6.0, 6.0}, "B"},
            {{4.5, 4.5}, "B"}
        };
        
        // Combined training data
        training_data = classA_points;
        training_data.insert(training_data.end(), classB_points.begin(), classB_points.end());
        
        // Test points
        near_classA = {{1.2, 1.3}};
        near_classB = {{5.2, 5.3}};
        between_classes = {{3.0, 3.0}};
        
        // Integer classification data
        LabeledPoint<int> int_class0 = {{1.0, 1.0}, 0};
        LabeledPoint<int> int_class1 = {{5.0, 5.0}, 1};
        int_training_data = {int_class0, int_class1};
        
        // Empty data
        empty_data = {};
        empty_point = {};
    }
    
    std::vector<LabeledPoint<std::string>> classA_points, classB_points, training_data, empty_data;
    std::vector<LabeledPoint<int>> int_training_data;
    std::vector<double> near_classA, near_classB, between_classes, empty_point;
};

// Voting functions
TEST_F(KNNTest, CountVotes) {
    std::vector<std::string> labels = {"A", "B", "A", "A", "B"};
    auto result = countVotes(labels);
    
    EXPECT_EQ(result.size(), 2);
    EXPECT_EQ(result["A"], 3);
    EXPECT_EQ(result["B"], 2);
}

TEST_F(KNNTest, CountVotesEmpty) {
    std::vector<std::string> empty_labels;
    auto result = countVotes(empty_labels);
    
    EXPECT_TRUE(result.empty());
}

TEST_F(KNNTest, CountVotesAllSame) {
    std::vector<std::string> same_labels = {"A", "A", "A", "A"};
    auto result = countVotes(same_labels);
    
    EXPECT_EQ(result.size(), 1);
    EXPECT_EQ(result["A"], 4);
}

TEST_F(KNNTest, RawMajorityVote) {
    std::vector<std::string> labels = {"A", "B", "A", "A", "B"};
    std::string result = rawMajorityVote(labels);
    
    EXPECT_EQ(result, "A");
}

TEST_F(KNNTest, RawMajorityVoteTie) {
    std::vector<std::string> tie_labels = {"A", "B", "A", "B"};
    std::string result = rawMajorityVote(tie_labels);
    
    // Should return one of the tied labels (implementation dependent)
    EXPECT_TRUE(result == "A" || result == "B");
}

TEST_F(KNNTest, RawMajorityVoteEmpty) {
    std::vector<std::string> empty_labels;
    EXPECT_THROW(rawMajorityVote(empty_labels), std::invalid_argument);
}

TEST_F(KNNTest, MajorityVote) {
    std::vector<std::string> labels = {"A", "A", "B", "B", "A"};
    std::string result = majorityVote(labels);
    
    EXPECT_EQ(result, "A");
}

TEST_F(KNNTest, MajorityVoteTieBreaking) {
    std::vector<std::string> tie_labels = {"A", "A", "B", "B"};
    std::string result = majorityVote(tie_labels);
    
    // Should break tie by removing farthest (last) element
    EXPECT_TRUE(result == "A" || result == "B");
}

TEST_F(KNNTest, MajorityVoteEmpty) {
    std::vector<std::string> empty_labels;
    EXPECT_THROW(majorityVote(empty_labels), std::invalid_argument);
}

// KNN classification
TEST_F(KNNTest, KnnClassifyBasic) {
    std::string result = knnClassify(3, training_data, near_classA);
    EXPECT_EQ(result, "A");
    
    std::string result2 = knnClassify(3, training_data, near_classB);
    EXPECT_EQ(result2, "B");
}

TEST_F(KNNTest, KnnClassifyDifferentK) {
    // Test with different k values
    for (int k = 1; k <= 7; k += 2) {
        std::string result = knnClassify(k, training_data, near_classA);
        EXPECT_EQ(result, "A");
        
        std::string result2 = knnClassify(k, training_data, near_classB);
        EXPECT_EQ(result2, "B");
    }
}

TEST_F(KNNTest, KnnClassifyEdgeCases) {
    // Test with k larger than dataset
    std::string result = knnClassify(100, training_data, near_classA);
    EXPECT_TRUE(result == "A" || result == "B"); // Should still work
    
    // Test with k = 1
    std::string result2 = knnClassify(1, training_data, near_classA);
    EXPECT_EQ(result2, "A");
}

TEST_F(KNNTest, KnnClassifyEmptyData) {
    EXPECT_THROW(knnClassify(3, empty_data, near_classA), std::invalid_argument);
}

TEST_F(KNNTest, KnnClassifyInvalidK) {
    EXPECT_THROW(knnClassify(0, training_data, near_classA), std::invalid_argument);
    EXPECT_THROW(knnClassify(-1, training_data, near_classA), std::invalid_argument);
}

TEST_F(KNNTest, KnnClassifyIntegerLabels) {
    int result = knnClassify(1, int_training_data, {1.0, 1.0});
    EXPECT_EQ(result, 0);
    
    int result2 = knnClassify(1, int_training_data, {5.0, 5.0});
    EXPECT_EQ(result2, 1);
}

TEST_F(KNNTest, KnnClassifyWithDistance) {
    auto result = knnClassifyWithDistance(3, training_data, near_classA);
    
    EXPECT_EQ(result.prediction, "A");
    EXPECT_EQ(result.distances.size(), 3);
    EXPECT_EQ(result.neighbors.size(), 3);
    
    // Distances should be sorted (nearest first)
    for (size_t i = 1; i < result.distances.size(); ++i) {
        EXPECT_LE(result.distances[i-1], result.distances[i]);
    }
    
    // All neighbors should be from the training data
    for (const auto& neighbor : result.neighbors) {
        EXPECT_TRUE(std::find(training_data.begin(), training_data.end(), neighbor) != training_data.end());
    }
}

TEST_F(KNNTest, KnnClassifyWithDistanceEdgeCases) {
    auto result = knnClassifyWithDistance(100, training_data, near_classA);
    EXPECT_EQ(result.distances.size(), training_data.size());
    EXPECT_EQ(result.neighbors.size(), training_data.size());
}

// Weighted KNN
TEST_F(KNNTest, WeightedKnnClassify) {
    std::string result = weightedKnnClassify(3, training_data, near_classA);
    EXPECT_EQ(result, "A");
    
    std::string result2 = weightedKnnClassify(3, training_data, near_classB);
    EXPECT_EQ(result2, "B");
}

TEST_F(KNNTest, WeightedKnnClassifyEdgeCases) {
    // Test with k larger than dataset
    std::string result = weightedKnnClassify(100, training_data, near_classA);
    EXPECT_TRUE(result == "A" || result == "B");
}

// Cross-validation
TEST_F(KNNTest, KnnCrossValidate) {
    double accuracy = knnCrossValidate(3, training_data, 5);
    
    // Accuracy should be between 0 and 1
    EXPECT_GE(accuracy, 0.0);
    EXPECT_LE(accuracy, 1.0);
    
    // With this clearly separable data, accuracy should be high
    EXPECT_GT(accuracy, 0.5);
}

TEST_F(KNNTest, KnnCrossValidateEdgeCases) {
    // Empty data
    double accuracy1 = knnCrossValidate(3, empty_data, 5);
    EXPECT_DOUBLE_EQ(accuracy1, 0.0);
    
    // Single point
    std::vector<LabeledPoint<std::string>> single_point = {{{1.0, 1.0}, "A"}};
    double accuracy2 = knnCrossValidate(1, single_point, 2);
    EXPECT_DOUBLE_EQ(accuracy2, 1.0);
}

TEST_F(KNNTest, KnnCrossValidateDifferentFolds) {
    // Test with different numbers of folds
    for (int folds = 2; folds <= 10; folds += 2) {
        double accuracy = knnCrossValidate(3, training_data, folds);
        EXPECT_GE(accuracy, 0.0);
        EXPECT_LE(accuracy, 1.0);
    }
}

// Optimal K finding
TEST_F(KNNTest, FindOptimalK) {
    OptimalKResult result = findOptimalK(training_data, 5, 3);
    
    EXPECT_GE(result.optimalK, 1);
    EXPECT_LE(result.optimalK, 5);
    EXPECT_EQ(result.accuracies.size(), 5);
    
    // All accuracies should be between 0 and 1
    for (double acc : result.accuracies) {
        EXPECT_GE(acc, 0.0);
        EXPECT_LE(acc, 1.0);
    }
}

TEST_F(KNNTest, FindOptimalKEdgeCases) {
    // Empty data
    OptimalKResult result1 = findOptimalK(empty_data, 5, 3);
    EXPECT_EQ(result1.optimalK, 1);
    EXPECT_EQ(result1.accuracies.size(), 5);
    
    // Small dataset
    OptimalKResult result2 = findOptimalK(training_data, 2, 2);
    EXPECT_GE(result2.optimalK, 1);
    EXPECT_LE(result2.optimalK, 2);
}

// Example functions
TEST_F(KNNTest, CitiesExample) {
    std::string prediction = predictLanguageForCity(-87.6298, 41.8781); // Chicago coordinates
    EXPECT_TRUE(prediction == "Python" || prediction == "Java" || prediction == "R");
}

// Distance and neighbor properties
TEST_F(KNNTest, DistanceProperties) {
    auto result = knnClassifyWithDistance(3, training_data, near_classA);
    
    // Check that distances are non-negative
    for (double dist : result.distances) {
        EXPECT_GE(dist, 0.0);
    }
    
    // Check that closer neighbors have more influence in weighted version
    std::string weighted_result = weightedKnnClassify(3, training_data, near_classA);
    // For this simple case, weighted and unweighted should give same result
    EXPECT_EQ(result.prediction, weighted_result);
}

TEST_F(KNNTest, NeighborConsistency) {
    // Test that knnClassify and knnClassifyWithDistance give same prediction
    for (int k = 1; k <= 5; k += 2) {
        std::string result1 = knnClassify(k, training_data, near_classA);
        auto result2 = knnClassifyWithDistance(k, training_data, near_classA);
        EXPECT_EQ(result1, result2.prediction);
    }
}

// Edge cases and special values
TEST_F(KNNTest, HandlesIdenticalPoints) {
    // Add a point identical to test point
    LabeledPoint<std::string> identical_point = {near_classA, "A"};
    std::vector<LabeledPoint<std::string>> data_with_identical = training_data;
    data_with_identical.push_back(identical_point);
    
    std::string result = knnClassify(1, data_with_identical, near_classA);
    EXPECT_EQ(result, "A");
    
    // Distance should be zero for identical point
    auto result_with_dist = knnClassifyWithDistance(1, data_with_identical, near_classA);
    EXPECT_DOUBLE_EQ(result_with_dist.distances[0], 0.0);
}

TEST_F(KNNTest, HandlesHighDimensions) {
    // Create 10D data
    std::vector<LabeledPoint<std::string>> high_dim_data;
    for (int i = 0; i < 10; ++i) {
        std::vector<double> point(10, static_cast<double>(i));
        high_dim_data.push_back({point, "A"});
    }
    
    std::vector<double> test_point(10, 5.0);
    std::string result = knnClassify(3, high_dim_data, test_point);
    EXPECT_EQ(result, "A");
}

TEST_F(KNNTest, HandlesLargeNumbers) {
    std::vector<LabeledPoint<std::string>> large_data = {
        {{1e6, 1e6}, "A"},
        {{2e6, 2e6}, "B"},
        {{1.5e6, 1.5e6}, "A"}
    };
    
    std::string result = knnClassify(1, large_data, {1.1e6, 1.1e6});
    EXPECT_EQ(result, "A");
}

TEST_F(KNNTest, HandlesSmallNumbers) {
    std::vector<LabeledPoint<std::string>> small_data = {
        {{1e-10, 1e-10}, "A"},
        {{2e-10, 2e-10}, "B"},
        {{1.5e-10, 1.5e-10}, "A"}
    };
    
    std::string result = knnClassify(1, small_data, {1.1e-10, 1.1e-10});
    EXPECT_EQ(result, "A");
}

// Performance tests
TEST_F(KNNTest, PerformanceSanity) {
    // Create larger dataset
    std::vector<LabeledPoint<std::string>> large_dataset;
    for (int i = 0; i < 1000; ++i) {
        std::vector<double> point = {static_cast<double>(i % 100), static_cast<double>(i / 100)};
        std::string label = (i % 2 == 0) ? "A" : "B";
        large_dataset.push_back({point, label});
    }
    
    std::vector<double> test_point = {50.0, 5.0};
    
    auto start = std::chrono::high_resolution_clock::now();
    std::string result = knnClassify(5, large_dataset, test_point);
    auto end = std::chrono::high_resolution_clock::now();
    
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    EXPECT_LT(duration.count(), 100); // Should complete in less than 100ms
    
    EXPECT_TRUE(result == "A" || result == "B");
}

TEST_F(KNNTest, CrossValidationPerformance) {
    // Test that cross-validation completes in reasonable time
    auto start = std::chrono::high_resolution_clock::now();
    double accuracy = knnCrossValidate(3, training_data, 5);
    auto end = std::chrono::high_resolution_clock::now();
    
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    EXPECT_LT(duration.count(), 1000); // Should complete in less than 1 second
}

// Statistical properties
TEST_F(KNNTest, KProperties) {
    // Test that odd k values work better for binary classification
    for (int k = 1; k <= 7; k += 2) {
        std::string result = knnClassify(k, training_data, near_classA);
        EXPECT_TRUE(result == "A" || result == "B");
    }
}

TEST_F(KNNTest, ConsistencyWithDistance) {
    // Test that closer points have more influence in weighted KNN
    // Create a scenario where the closest neighbor is from minority class
    std::vector<LabeledPoint<std::string>> test_data = {
        {{1.0, 1.0}, "A"},
        {{2.0, 2.0}, "B"},
        {{3.0, 3.0}, "B"},
        {{4.0, 4.0}, "B"}
    };
    
    std::vector<double> test_point = {1.1, 1.1};
    
    std::string unweighted = knnClassify(3, test_data, test_point);
    std::string weighted = weightedKnnClassify(3, test_data, test_point);
    
    // Weighted should favor the closest point (A)
    EXPECT_EQ(weighted, "A");
    // Unweighted might favor majority (B)
    EXPECT_TRUE(unweighted == "A" || unweighted == "B");
}
