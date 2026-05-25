#pragma once

#include "../c04_linear_algebra/linear_algebra.h"
#include "../c05_statistics/stats.h"
#include <compare>
#include <vector>
#include <string>
#include <map>

// Type definitions
template<typename T>
struct LabeledPoint {
    std::vector<double> point;
    T label;

    LabeledPoint() = default;

    // Three-way comparison operator synthesizes ==, <, <=, >, >= automatically
    auto operator<=>(const LabeledPoint& other) const = default;
};

template<typename T>
using VoteCounter = std::map<T, int>;

template<typename T>
struct KnnResult {
    T prediction;
    std::vector<double> distances;
    std::vector<LabeledPoint<T>> neighbors;
};

struct OptimalKResult {
    int optimalK;
    std::vector<double> accuracies;
};

// Voting functions
template<typename T>
VoteCounter<T> countVotes(const std::vector<T>& labels);

template<typename T>
T rawMajorityVote(const std::vector<T>& labels);

template<typename T>
T majorityVote(const std::vector<T>& labels);

// K-Nearest Neighbors classification
template<typename T>
T knnClassify(int k, const std::vector<LabeledPoint<T>>& labeledPoints, 
              const std::vector<double>& newPoint);

template<typename T>
KnnResult<T> knnClassifyWithDistance(int k, 
                                     const std::vector<LabeledPoint<T>>& labeledPoints, 
                                     const std::vector<double>& newPoint);

template<typename T>
T weightedKnnClassify(int k, const std::vector<LabeledPoint<T>>& labeledPoints, 
                      const std::vector<double>& newPoint);

// Cross-validation and optimization
template<typename T>
double knnCrossValidate(int k, const std::vector<LabeledPoint<T>>& labeledPoints, 
                        int folds = 5);

template<typename T>
OptimalKResult findOptimalK(const std::vector<LabeledPoint<T>>& labeledPoints, 
                           int maxK = 20, int folds = 5);

// Example data and functions
extern const std::vector<LabeledPoint<std::string>> cities;
std::string predictLanguageForCity(double longitude, double latitude);

