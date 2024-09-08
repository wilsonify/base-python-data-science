#include <algorithm>
#include <cstdio>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <sstream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>


// Struct representing a user with an ID and a list of friends (pointers to other User objects).
struct User {
    int id;
    std::vector<User*> friends;
};

// Functions related to user analysis.

std::string tenure_bucket(double tenure);

std::string predict_paid_or_unpaid(double years_experience);

int number_of_friends(const User& user);

std::vector<int> friends_of_friend_ids_bad(const User& user);

bool not_the_same(const User& user, const User& other_user);

bool not_friends(const User& user, const User& other_user);

std::map<int, int> friends_of_friend_ids(const User& user);

std::vector<int> data_scientists_who_like(const std::string& target_interest, 
    const std::vector<std::pair<int, std::string>>& interests_list);

std::map<int, int> most_common_interests_with(int user_id,
    const std::unordered_map<int, std::vector<std::string>>& interests_by_user_id,
    const std::unordered_map<std::string, std::vector<int>>& user_ids_by_interest);

void read_most_common_words(const std::map<std::string, int>& words_and_counts);

void read_num_friends_by_id(const std::vector<User>& users_list);

std::map<std::string, int> create_words_and_counts(const std::vector<std::pair<int, std::string>>& interests_list);

std::map<std::string, double> create_average_salary_by_bucket(
    const std::vector<std::pair<double, double>>& salaries_and_tenures);

std::unordered_map<double, double> create_average_salary_by_tenure(
    const std::unordered_map<double, std::vector<double>>& salary_by_tenure);

std::unordered_map<double, std::vector<double>> create_salary_by_tenure(
    const std::vector<std::pair<double, double>>& salaries_and_tenures);

std::unordered_map<int, std::vector<std::string>> create_interests_by_user(
    const std::vector<std::pair<int, std::string>>& interests_list);

std::unordered_map<std::string, std::vector<int>> create_users_by_interest(
    const std::vector<std::pair<int, std::string>>& interests_list);

void read_avg_connections(const std::vector<User>& users_list);

void read_user_connections(const std::vector<User>& users_list, int uid = 3);

void populate_friendships(const std::vector<std::pair<int, int>>& friendships, std::vector<User>& users_list);
