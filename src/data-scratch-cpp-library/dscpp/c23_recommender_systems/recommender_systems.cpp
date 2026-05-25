#include "recommender_systems.h"
#include <algorithm>
#include <map>
#include <set>

double cosine_similarity(const std::vector<double>& v, const std::vector<double>& w) {
    double denom = std::sqrt(dot(v, v) * dot(w, w));
    if (denom == 0.0) return 0.0;
    return dot(v, w) / denom;
}

std::vector<std::pair<std::string, int>> most_popular_new_interests(
    const std::vector<std::string>& user_interests,
    const std::vector<std::pair<std::string, int>>& popular_interests,
    int max_results) {

    std::set<std::string> current(user_interests.begin(), user_interests.end());
    std::vector<std::pair<std::string, int>> result;
    for (const auto& [interest, freq] : popular_interests) {
        if (current.find(interest) == current.end()) {
            result.push_back({interest, freq});
            if (static_cast<int>(result.size()) >= max_results) break;
        }
    }
    return result;
}

std::vector<int> make_user_interest_vector(
    const std::vector<std::string>& user_interests,
    const std::vector<std::string>& unique_interests) {

    std::set<std::string> current(user_interests.begin(), user_interests.end());
    std::vector<int> result;
    result.reserve(unique_interests.size());
    for (const auto& interest : unique_interests)
        result.push_back(current.count(interest) ? 1 : 0);
    return result;
}

std::vector<std::vector<double>> compute_user_similarities(
    const std::vector<std::vector<int>>& user_interest_matrix) {

    size_t n = user_interest_matrix.size();
    std::vector<std::vector<double>> sims(n, std::vector<double>(n, 0.0));

    for (size_t i = 0; i < n; ++i) {
        std::vector<double> vi(user_interest_matrix[i].begin(), user_interest_matrix[i].end());
        for (size_t j = 0; j < n; ++j) {
            std::vector<double> vj(user_interest_matrix[j].begin(), user_interest_matrix[j].end());
            sims[i][j] = cosine_similarity(vi, vj);
        }
    }
    return sims;
}

std::vector<std::pair<int, double>> most_similar_users_to(
    int user_id,
    const std::vector<std::vector<double>>& user_similarities) {

    std::vector<std::pair<int, double>> pairs;
    const auto& row = user_similarities[user_id];
    for (size_t i = 0; i < row.size(); ++i) {
        if (static_cast<int>(i) != user_id && row[i] > 0.0)
            pairs.push_back({static_cast<int>(i), row[i]});
    }
    std::sort(pairs.begin(), pairs.end(),
              [](const auto& a, const auto& b) { return a.second > b.second; });
    return pairs;
}

std::vector<std::pair<std::string, double>> user_based_suggestions(
    int user_id,
    const std::vector<std::vector<double>>& user_similarities,
    const std::vector<std::vector<std::string>>& users_interests,
    bool include_current_interests) {

    std::map<std::string, double> suggestions;
    for (const auto& [other_user_id, similarity] : most_similar_users_to(user_id, user_similarities)) {
        for (const auto& interest : users_interests[other_user_id])
            suggestions[interest] += similarity;
    }

    std::vector<std::pair<std::string, double>> result(suggestions.begin(), suggestions.end());
    std::sort(result.begin(), result.end(),
              [](const auto& a, const auto& b) { return a.second > b.second; });

    if (include_current_interests)
        return result;

    const auto& current = users_interests[user_id];
    std::set<std::string> current_set(current.begin(), current.end());
    std::vector<std::pair<std::string, double>> filtered;
    for (const auto& [interest, score] : result)
        if (!current_set.count(interest))
            filtered.push_back({interest, score});
    return filtered;
}

std::vector<std::vector<double>> compute_interest_similarities(
    const std::vector<std::vector<int>>& user_interest_matrix,
    int num_interests) {

    // Transpose to interest_user_matrix
    size_t num_users = user_interest_matrix.size();
    std::vector<std::vector<int>> interest_user_matrix(num_interests, std::vector<int>(num_users, 0));
    for (size_t u = 0; u < num_users; ++u)
        for (int i = 0; i < num_interests; ++i)
            interest_user_matrix[i][u] = user_interest_matrix[u][i];

    std::vector<std::vector<double>> sims(num_interests, std::vector<double>(num_interests, 0.0));
    for (int i = 0; i < num_interests; ++i) {
        std::vector<double> vi(interest_user_matrix[i].begin(), interest_user_matrix[i].end());
        for (int j = 0; j < num_interests; ++j) {
            std::vector<double> vj(interest_user_matrix[j].begin(), interest_user_matrix[j].end());
            sims[i][j] = cosine_similarity(vi, vj);
        }
    }
    return sims;
}

std::vector<std::pair<std::string, double>> most_similar_interests_to(
    int interest_id,
    const std::vector<std::vector<double>>& interest_similarities,
    const std::vector<std::string>& unique_interests) {

    const auto& row = interest_similarities[interest_id];
    std::vector<std::pair<std::string, double>> pairs;
    for (size_t i = 0; i < row.size(); ++i) {
        if (static_cast<int>(i) != interest_id && row[i] > 0.0)
            pairs.push_back({unique_interests[i], row[i]});
    }
    std::sort(pairs.begin(), pairs.end(),
              [](const auto& a, const auto& b) { return a.second > b.second; });
    return pairs;
}

std::vector<std::pair<std::string, double>> item_based_suggestions(
    int user_id,
    const std::vector<std::vector<int>>& user_interest_matrix,
    const std::vector<std::vector<double>>& interest_similarities,
    const std::vector<std::string>& unique_interests,
    const std::vector<std::vector<std::string>>& users_interests,
    bool include_current_interests) {

    std::map<std::string, double> suggestions;
    const auto& user_vec = user_interest_matrix[user_id];
    for (size_t i = 0; i < user_vec.size(); ++i) {
        if (user_vec[i] == 1) {
            for (const auto& [interest, sim] : most_similar_interests_to(
                    static_cast<int>(i), interest_similarities, unique_interests))
                suggestions[interest] += sim;
        }
    }

    std::vector<std::pair<std::string, double>> result(suggestions.begin(), suggestions.end());
    std::sort(result.begin(), result.end(),
              [](const auto& a, const auto& b) { return a.second > b.second; });

    if (include_current_interests)
        return result;

    const auto& current = users_interests[user_id];
    std::set<std::string> current_set(current.begin(), current.end());
    std::vector<std::pair<std::string, double>> filtered;
    for (const auto& [interest, score] : result)
        if (!current_set.count(interest))
            filtered.push_back({interest, score});
    return filtered;
}
