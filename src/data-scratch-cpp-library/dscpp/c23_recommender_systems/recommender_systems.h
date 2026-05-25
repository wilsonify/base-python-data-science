#pragma once
#include <cmath>
#include <map>
#include <string>
#include <vector>
#include "../c04_linear_algebra/linear_algebra.h"

double cosine_similarity(const std::vector<double>& v, const std::vector<double>& w);

std::vector<std::pair<std::string, int>> most_popular_new_interests(
    const std::vector<std::string>& user_interests,
    const std::vector<std::pair<std::string, int>>& popular_interests,
    int max_results=5);

std::vector<int> make_user_interest_vector(
    const std::vector<std::string>& user_interests,
    const std::vector<std::string>& unique_interests);

std::vector<std::vector<double>> compute_user_similarities(
    const std::vector<std::vector<int>>& user_interest_matrix);

std::vector<std::pair<int, double>> most_similar_users_to(
    int user_id,
    const std::vector<std::vector<double>>& user_similarities);

std::vector<std::pair<std::string, double>> user_based_suggestions(
    int user_id,
    const std::vector<std::vector<double>>& user_similarities,
    const std::vector<std::vector<std::string>>& users_interests,
    bool include_current_interests=false);

std::vector<std::vector<double>> compute_interest_similarities(
    const std::vector<std::vector<int>>& user_interest_matrix,
    int num_interests);

std::vector<std::pair<std::string, double>> most_similar_interests_to(
    int interest_id,
    const std::vector<std::vector<double>>& interest_similarities,
    const std::vector<std::string>& unique_interests);

std::vector<std::pair<std::string, double>> item_based_suggestions(
    int user_id,
    const std::vector<std::vector<int>>& user_interest_matrix,
    const std::vector<std::vector<double>>& interest_similarities,
    const std::vector<std::string>& unique_interests,
    const std::vector<std::vector<std::string>>& users_interests,
    bool include_current_interests=false);
