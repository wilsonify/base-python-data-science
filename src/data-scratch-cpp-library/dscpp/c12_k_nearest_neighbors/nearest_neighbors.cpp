// K-Nearest Neighbors Implementation - C++ Data Science Library
// Port from TypeScript implementation

#include "nearest_neighbors.h"
#include <algorithm>
#include <random>
#include <ranges>
#include <stdexcept>

// Random number generator
static std::random_device rd;
static std::mt19937 gen(rd());

// Template implementations

// Voting functions
template<typename T>
VoteCounter<T> countVotes(const std::vector<T>& labels) {
    VoteCounter<T> votes;
    
    for (const T& label : labels) {
        votes[label]++;
    }
    
    return votes;
}

template<typename T>
T rawMajorityVote(const std::vector<T>& labels) {
    if (labels.empty()) {
        throw std::invalid_argument("Cannot vote on empty labels");
    }
    
    const VoteCounter<T> votes = countVotes(labels);
    T winner = labels[0];
    int maxCount = 0;
    
    for (const auto& pair : votes) {
        if (pair.second > maxCount) {
            maxCount = pair.second;
            winner = pair.first;
        }
    }
    
    return winner;
}

template<typename T>
T majorityVote(const std::vector<T>& labels) {
    // assumes that labels are ordered from nearest to farthest
    if (labels.empty()) {
        throw std::invalid_argument("Cannot vote on empty labels");
    }
    
    const VoteCounter<T> voteCounts = countVotes(labels);
    
    // Find the label(s) with the highest vote count
    int maxCount = 0;
    for (const auto& pair : voteCounts) {
        if (pair.second > maxCount) {
            maxCount = pair.second;
        }
    }
    
    // Count how many labels have the max count
    std::vector<T> winners;
    for (const auto& pair : voteCounts) {
        if (pair.second == maxCount) {
            winners.push_back(pair.first);
        }
    }
    
    if (winners.size() == 1) {
        return winners[0]; // unique winner
    } else {
        // try again without the farthest (recursive tie-breaking)
        std::vector<T> reducedLabels(labels.begin(), labels.end() - 1);
        return majorityVote(reducedLabels);
    }
}

// K-Nearest Neighbors classification
template<typename T>
T knnClassify(int k, const std::vector<LabeledPoint<T>>& labeledPoints, 
              const std::vector<double>& newPoint) {
    if (k <= 0) {
        throw std::invalid_argument("k must be positive");
    }
    if (labeledPoints.empty()) {
        throw std::invalid_argument("No labeled points provided");
    }
    if (k > static_cast<int>(labeledPoints.size())) {
        k = static_cast<int>(labeledPoints.size());
    }
    
    // Create a copy and sort by distance
    std::vector<LabeledPoint<T>> sortedPoints = labeledPoints;
    std::ranges::sort(sortedPoints, 
              [&newPoint](const LabeledPoint<T>& a, const LabeledPoint<T>& b) {
                  return distance(a.point, newPoint) < distance(b.point, newPoint);
              });
    
    // Get the labels for the k closest
    std::vector<T> kNearestLabels;
    for (int i = 0; i < k; ++i) {
        kNearestLabels.push_back(sortedPoints[i].label);
    }
    
    // And let them vote
    return majorityVote(kNearestLabels);
}

template<typename T>
KnnResult<T> knnClassifyWithDistance(int k, 
                                     const std::vector<LabeledPoint<T>>& labeledPoints, 
                                     const std::vector<double>& newPoint) {
    if (k <= 0) {
        throw std::invalid_argument("k must be positive");
    }
    if (labeledPoints.empty()) {
        throw std::invalid_argument("No labeled points provided");
    }
    if (k > static_cast<int>(labeledPoints.size())) {
        k = static_cast<int>(labeledPoints.size());
    }
    
    // Create a copy and sort by distance
    std::vector<LabeledPoint<T>> sortedPoints = labeledPoints;
    std::ranges::sort(sortedPoints, 
              [&newPoint](const LabeledPoint<T>& a, const LabeledPoint<T>& b) {
                  return distance(a.point, newPoint) < distance(b.point, newPoint);
              });
    
    // Get the k closest neighbors
    std::vector<LabeledPoint<T>> kNearestNeighbors(sortedPoints.begin(), 
                                                   sortedPoints.begin() + k);
    
    std::vector<double> distances;
    std::vector<T> kNearestLabels;
    for (const auto& neighbor : kNearestNeighbors) {
        distances.push_back(distance(neighbor.point, newPoint));
        kNearestLabels.push_back(neighbor.label);
    }
    
    KnnResult<T> result;
    result.prediction = majorityVote(kNearestLabels);
    result.distances = distances;
    result.neighbors = kNearestNeighbors;
    
    return result;
}

template<typename T>
T weightedKnnClassify(int k, const std::vector<LabeledPoint<T>>& labeledPoints, 
                      const std::vector<double>& newPoint) {
    if (k <= 0) {
        throw std::invalid_argument("k must be positive");
    }
    if (labeledPoints.empty()) {
        throw std::invalid_argument("No labeled points provided");
    }
    if (k > static_cast<int>(labeledPoints.size())) {
        k = static_cast<int>(labeledPoints.size());
    }
    
    // Create a copy and sort by distance
    std::vector<LabeledPoint<T>> sortedPoints = labeledPoints;
    std::ranges::sort(sortedPoints, 
              [&newPoint](const LabeledPoint<T>& a, const LabeledPoint<T>& b) {
                  return distance(a.point, newPoint) < distance(b.point, newPoint);
              });
    
    // Get the k closest neighbors
    std::vector<LabeledPoint<T>> kNearestNeighbors(sortedPoints.begin(), 
                                                   sortedPoints.begin() + k);
    
    // Calculate weighted votes (inverse distance weighting)
    VoteCounter<T> weightedVotes;
    
    for (const auto& neighbor : kNearestNeighbors) {
        double dist = distance(neighbor.point, newPoint);
        // Avoid division by zero
        double weight = (dist == 0) ? 1.0 : 1.0 / (dist + 1e-10);
        weightedVotes[neighbor.label] += weight;
    }
    
    // Find the label with the highest total weight
    T winner = kNearestNeighbors[0].label;
    double maxWeight = 0;
    
    for (const auto& pair : weightedVotes) {
        if (pair.second > maxWeight) {
            maxWeight = pair.second;
            winner = pair.first;
        }
    }
    
    return winner;
}

template<typename T>
double knnCrossValidate(int k, const std::vector<LabeledPoint<T>>& labeledPoints, 
                        int folds) {
    if (labeledPoints.empty()) {
        return 0.0;
    }
    if (folds <= 1) {
        folds = 2;
    }
    if (folds > static_cast<int>(labeledPoints.size())) {
        folds = static_cast<int>(labeledPoints.size());
    }
    
    // Shuffle the data
    std::vector<LabeledPoint<T>> shuffled = labeledPoints;
    std::ranges::shuffle(shuffled, gen);
    
    int foldSize = static_cast<int>(shuffled.size()) / folds;
    int correctPredictions = 0;
    
    for (int i = 0; i < folds; i++) {
        // Create train/test split for this fold
        int testStart = i * foldSize;
        int testEnd = (i + 1) * foldSize;
        if (i == folds - 1) {
            testEnd = static_cast<int>(shuffled.size()); // Include remaining items
        }
        
        std::vector<LabeledPoint<T>> testSet(shuffled.begin() + testStart, 
                                            shuffled.begin() + testEnd);
        std::vector<LabeledPoint<T>> trainSet;
        
        // Add all other folds to train set
        trainSet.insert(trainSet.end(), shuffled.begin(), shuffled.begin() + testStart);
        trainSet.insert(trainSet.end(), shuffled.begin() + testEnd, shuffled.end());
        
        // Test on this fold
        for (const auto& testPoint : testSet) {
            T prediction = knnClassify(k, trainSet, testPoint.point);
            if (prediction == testPoint.label) {
                correctPredictions++;
            }
        }
    }
    
    return static_cast<double>(correctPredictions) / static_cast<double>(shuffled.size());
}

template<typename T>
OptimalKResult findOptimalK(const std::vector<LabeledPoint<T>>& labeledPoints, 
                           int maxK, int folds) {
    if (maxK <= 0) {
        maxK = 1;
    }
    if (maxK > static_cast<int>(labeledPoints.size())) {
        maxK = static_cast<int>(labeledPoints.size());
    }
    
    std::vector<double> accuracies;
    
    for (int k = 1; k <= maxK; k++) {
        double accuracy = knnCrossValidate(k, labeledPoints, folds);
        accuracies.push_back(accuracy);
    }
    
    // Find k with highest accuracy
    int optimalK = 1;
    double maxAccuracy = accuracies[0];
    
    for (size_t i = 1; i < accuracies.size(); i++) {
        if (accuracies[i] > maxAccuracy) {
            maxAccuracy = accuracies[i];
            optimalK = static_cast<int>(i) + 1; // k = i + 1 because we start from k=1
        }
    }
    
    OptimalKResult result;
    result.optimalK = optimalK;
    result.accuracies = accuracies;
    
    return result;
}

// Example data and functions
const std::vector<LabeledPoint<std::string>> cities = {
    {{-86.75, 33.5666666666667}, "Python"},
    {{-88.25, 30.6833333333333}, "Python"},
    {{-112.016666666667, 33.4333333333333}, "Java"},
    {{-110.933333333333, 32.1166666666667}, "Java"},
    {{-92.2333333333333, 34.7333333333333}, "R"},
    {{-121.95, 37.7}, "R"},
    {{-118.15, 33.8166666666667}, "Python"},
    {{-118.233333333333, 34.05}, "Python"},
    {{-122.416666666667, 37.7833333333333}, "R"},
    {{-87.6833333333333, 41.8333333333333}, "Java"},
    {{-84.4333333333333, 33.65}, "Python"},
    {{-116.216666666667, 43.6166666666667}, "Java"},
    {{-95.9333333333333, 36.1166666666667}, "R"},
    {{-96.7833333333333, 32.7833333333333}, "Python"},
    {{-89.6333333333333, 41.85}, "Java"},
    {{-104.716666666667, 38.8166666666667}, "Python"},
    {{-94.6, 39.1166666666667}, "Java"},
    {{-96.7, 32.7833333333333}, "Python"},
    {{-122.35, 47.6166666666667}, "Python"},
    {{-95.35, 29.9666666666667}, "Java"}
};

std::string predictLanguageForCity(double longitude, double latitude) {
    return knnClassify(3, cities, {longitude, latitude});
}

// Explicit template instantiations for common types
template std::string rawMajorityVote(const std::vector<std::string>& labels);
template int rawMajorityVote(const std::vector<int>& labels);
template double rawMajorityVote(const std::vector<double>& labels);
template bool rawMajorityVote(const std::vector<bool>& labels);

template std::string majorityVote(const std::vector<std::string>& labels);
template int majorityVote(const std::vector<int>& labels);
template double majorityVote(const std::vector<double>& labels);
template bool majorityVote(const std::vector<bool>& labels);

template std::string knnClassify(int k, const std::vector<LabeledPoint<std::string>>& labeledPoints, const std::vector<double>& newPoint);
template int knnClassify(int k, const std::vector<LabeledPoint<int>>& labeledPoints, const std::vector<double>& newPoint);
template double knnClassify(int k, const std::vector<LabeledPoint<double>>& labeledPoints, const std::vector<double>& newPoint);
template bool knnClassify(int k, const std::vector<LabeledPoint<bool>>& labeledPoints, const std::vector<double>& newPoint);

template KnnResult<std::string> knnClassifyWithDistance(int k, const std::vector<LabeledPoint<std::string>>& labeledPoints, const std::vector<double>& newPoint);
template KnnResult<int> knnClassifyWithDistance(int k, const std::vector<LabeledPoint<int>>& labeledPoints, const std::vector<double>& newPoint);
template KnnResult<double> knnClassifyWithDistance(int k, const std::vector<LabeledPoint<double>>& labeledPoints, const std::vector<double>& newPoint);
template KnnResult<bool> knnClassifyWithDistance(int k, const std::vector<LabeledPoint<bool>>& labeledPoints, const std::vector<double>& newPoint);

template std::string weightedKnnClassify(int k, const std::vector<LabeledPoint<std::string>>& labeledPoints, const std::vector<double>& newPoint);
template int weightedKnnClassify(int k, const std::vector<LabeledPoint<int>>& labeledPoints, const std::vector<double>& newPoint);
template double weightedKnnClassify(int k, const std::vector<LabeledPoint<double>>& labeledPoints, const std::vector<double>& newPoint);
template bool weightedKnnClassify(int k, const std::vector<LabeledPoint<bool>>& labeledPoints, const std::vector<double>& newPoint);

template double knnCrossValidate(int k, const std::vector<LabeledPoint<std::string>>& labeledPoints, int folds);
template double knnCrossValidate(int k, const std::vector<LabeledPoint<int>>& labeledPoints, int folds);
template double knnCrossValidate(int k, const std::vector<LabeledPoint<double>>& labeledPoints, int folds);
template double knnCrossValidate(int k, const std::vector<LabeledPoint<bool>>& labeledPoints, int folds);

template OptimalKResult findOptimalK(const std::vector<LabeledPoint<std::string>>& labeledPoints, int maxK, int folds);
template OptimalKResult findOptimalK(const std::vector<LabeledPoint<int>>& labeledPoints, int maxK, int folds);
template OptimalKResult findOptimalK(const std::vector<LabeledPoint<double>>& labeledPoints, int maxK, int folds);
template OptimalKResult findOptimalK(const std::vector<LabeledPoint<bool>>& labeledPoints, int maxK, int folds);
