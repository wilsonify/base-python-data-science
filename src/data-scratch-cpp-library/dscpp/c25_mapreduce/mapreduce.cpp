#include "mapreduce.h"
#include <algorithm>
#include <cctype>
#include <sstream>

// Simple tokenizer: split on non-alpha chars, lowercase
static std::vector<std::string> tokenize_doc(const std::string& doc) {
    std::vector<std::string> tokens;
    std::string current;
    for (char c : doc) {
        if (std::isalpha(static_cast<unsigned char>(c))) {
            current += static_cast<char>(std::tolower(static_cast<unsigned char>(c)));
        } else {
            if (!current.empty()) {
                tokens.push_back(current);
                current.clear();
            }
        }
    }
    if (!current.empty())
        tokens.push_back(current);
    return tokens;
}

std::map<std::string, int> word_count_old(const std::vector<std::string>& documents) {
    std::map<std::string, int> counts;
    for (const auto& doc : documents)
        for (const auto& word : tokenize_doc(doc))
            ++counts[word];
    return counts;
}

std::vector<std::pair<std::string, int>> wc_mapper(const std::string& document) {
    std::vector<std::pair<std::string, int>> result;
    for (const auto& word : tokenize_doc(document))
        result.push_back({word, 1});
    return result;
}

std::vector<std::pair<std::string, int>> word_count(const std::vector<std::string>& documents) {
    std::map<std::string, int> collector;
    for (const auto& doc : documents)
        for (const auto& [word, count] : wc_mapper(doc))
            collector[word] += count;

    std::vector<std::pair<std::string, int>> result(collector.begin(), collector.end());
    return result;
}

std::vector<std::pair<std::string, int>> matrix_multiply_mapper_A(int m, int i, int j, double value) {
    // A[i][j] contributes to C[i][col] for each col in [0, m)
    // Key encodes (i, col), value encodes (j, value) -- simplified to string key
    std::vector<std::pair<std::string, int>> result;
    for (int col = 0; col < m; ++col) {
        std::string key = std::to_string(i) + "," + std::to_string(col);
        result.push_back({key, static_cast<int>(value * 1000)});
    }
    return result;
}

std::vector<std::pair<std::string, int>> matrix_multiply_mapper_B(int m, int i, int j, double value) {
    // B[i][j] contributes to C[row][j] for each row in [0, m)
    std::vector<std::pair<std::string, int>> result;
    for (int row = 0; row < m; ++row) {
        std::string key = std::to_string(row) + "," + std::to_string(j);
        result.push_back({key, static_cast<int>(value * 1000)});
    }
    return result;
}
