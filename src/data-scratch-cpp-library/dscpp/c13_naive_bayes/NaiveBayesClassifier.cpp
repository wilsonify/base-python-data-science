#include "NaiveBayesClassifier.h"
#include <algorithm>   // for std::count_if
#include <ranges>
#include <unordered_map>
#include <vector>
#include <string>
#include <string_view>
#include <tuple>
#include <cmath>       // for std::log and std::exp
#include <sstream>     // for std::stringstream
#include <cctype>      // for std::tolower

struct TransparentStringHash {
    using is_transparent = void;
    std::size_t operator()(std::string_view sv) const noexcept {
        return std::hash<std::string_view>{}(sv);
    }
};

// Tokenize into lowercase words
std::vector<std::string> tokenize(const std::string& message) {
    std::vector<std::string> tokens;
    std::string token;
    std::stringstream ss(message);

    while (ss >> token) {
        for (char& c : token) {
            c = std::tolower(c);
        }
        tokens.push_back(token);
    }

    return tokens;
}

// Count words in a training set, distinguishing between spam and non-spam
std::unordered_map<std::string, std::pair<int, int>, TransparentStringHash, std::equal_to<>> count_words(const std::vector<std::pair<std::string, bool>>& training_set) {
    std::unordered_map<std::string, std::pair<int, int>, TransparentStringHash, std::equal_to<>> counts;

    for (const auto& [message, is_spam] : training_set) {
        auto words = tokenize(message);

        for (const auto& word : words) {
            if (is_spam) {
                counts[word].first++;  // Increment spam count
            } else {
                counts[word].second++; // Increment non-spam count
            }
        }
    }

    return counts;
}

// Calculate the probabilities of each word being in a spam or non-spam message
std::vector<std::tuple<std::string, double, double>> word_probabilities(
    const std::unordered_map<std::string, std::pair<int, int>, TransparentStringHash, std::equal_to<>>& counts,
    int total_spams,
    int total_non_spams,
    double k = 0.5)
{
    std::vector<std::tuple<std::string, double, double>> probabilities;

    for (const auto& [word, counts_pair] : counts) {
        auto [spam_count, non_spam_count] = counts_pair;

        double p_word_given_spam = (spam_count + k) / (total_spams + 2 * k);
        double p_word_given_non_spam = (non_spam_count + k) / (total_non_spams + 2 * k);

        probabilities.emplace_back(word, p_word_given_spam, p_word_given_non_spam);
    }

    return probabilities;
}

// Calculate the probability that a message is spam
double get_spam_probability(
    const std::vector<std::tuple<std::string, double, double>>& word_probs,
    const std::string& message)
{
    auto message_words = tokenize(message);

    double log_prob_if_spam = 0.0;
    double log_prob_if_not_spam = 0.0;

    for (const auto& [word, prob_if_spam, prob_if_not_spam] : word_probs) {
        bool word_in_message = std::ranges::find(message_words, word) != message_words.end();

        if (word_in_message) {
            log_prob_if_spam += std::log(prob_if_spam);
            log_prob_if_not_spam += std::log(prob_if_not_spam);
        } else {
            log_prob_if_spam += std::log(1.0 - prob_if_spam);
            log_prob_if_not_spam += std::log(1.0 - prob_if_not_spam);
        }
    }

    double prob_if_spam = std::exp(log_prob_if_spam);
    double prob_if_not_spam = std::exp(log_prob_if_not_spam);

    return prob_if_spam / (prob_if_spam + prob_if_not_spam);
}

// NaiveBayesClassifier class implementation
NaiveBayesClassifier::NaiveBayesClassifier(double k) : k(k) {}

void NaiveBayesClassifier::train(const std::vector<std::pair<std::string, bool>>& training_set) {
    int num_spams = std::count_if(training_set.begin(), training_set.end(),
                                  [](const std::pair<std::string, bool>& item) { return item.second; });
    int num_non_spams = training_set.size() - num_spams;

    auto word_counts = count_words(training_set);
    word_probs = word_probabilities(word_counts, num_spams, num_non_spams, k);
}

double NaiveBayesClassifier::classify(const std::string& message) {
    return get_spam_probability(word_probs, message);
}
