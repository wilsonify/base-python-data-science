#include "introduction.h"



std::string tenure_bucket(double tenure) {
    if (tenure < 2.0) {
        return "less than two";
    } else if (tenure < 5.0) {
        return "between two and five";
    } else {
        return "more than five";
    }
}

std::string predict_paid_or_unpaid(double years_experience) {
    if (years_experience < 3.0) {
        return "paid";
    } else if (years_experience < 8.5) {
        return "unpaid";
    } else {
        return "paid";
    }
}

int number_of_friends(const User& user) {
    return user.friends.size();
}

std::vector<int> friends_of_friend_ids_bad(const User& user) {
    std::vector<int> result;
    for (const auto& friend_ptr : user.friends) {
        for (const auto& foaf : friend_ptr->friends) {
            result.push_back(foaf->id);
        }
    }
    return result;
}

bool not_the_same(const User& user, const User& other_user) {
    return user.id != other_user.id;
}

bool not_friends(const User& user, const User& other_user) {
    return std::all_of(user.friends.begin(), user.friends.end(),
        [&other_user](const User* friend_ptr) {
            return not_the_same(*friend_ptr, other_user);
        });
}

std::map<int, int> friends_of_friend_ids(const User& user) {
    std::map<int, int> counter;
    for (const auto& friend_ptr : user.friends) {
        for (const auto& foaf : friend_ptr->friends) {
            if (not_the_same(user, *foaf) && not_friends(user, *foaf)) {
                counter[foaf->id]++;
            }
        }
    }
    return counter;
}

std::vector<int> data_scientists_who_like(const std::string& target_interest,
    const std::vector<std::pair<int, std::string>>& interests_list) {
    std::vector<int> result;
    for (const auto& [user_id, interest] : interests_list) {
        if (interest == target_interest) {
            result.push_back(user_id);
        }
    }
    return result;
}

std::map<int, int> most_common_interests_with(int user_id,
    const std::unordered_map<int, std::vector<std::string>>& interests_by_user_id,
    const std::unordered_map<std::string, std::vector<int>>& user_ids_by_interest) {
    std::map<int, int> counter;
    for (const auto& interest : interests_by_user_id.at(user_id)) {
        for (const auto& interested_user_id : user_ids_by_interest.at(interest)) {
            if (interested_user_id != user_id) {
                counter[interested_user_id]++;
            }
        }
    }
    return counter;
}

void read_most_common_words(const std::map<std::string, int>& words_and_counts) {
    std::cout << "MOST COMMON WORDS" << std::endl;
    for (const auto& [word, count] : words_and_counts) {
        if (count > 1) {
            std::cout << "word " << word << ", count " << count << std::endl;
        }
    }
}

void read_num_friends_by_id(const std::vector<User>& users_list) {
    std::vector<std::pair<int, int>> num_friends_by_id;
    for (const auto& user : users_list) {
        num_friends_by_id.emplace_back(user.id, number_of_friends(user));
    }

    std::sort(num_friends_by_id.begin(), num_friends_by_id.end(),
        [](const std::pair<int, int>& a, const std::pair<int, int>& b) {
            return b.second < a.second;
        });

    std::cout << "users sorted by number of friends:" << std::endl;
    for (const auto& [user_id, num_friends] : num_friends_by_id) {
        std::cout << "user_id: " << user_id << ", friends: " << num_friends << std::endl;
    }
}

std::map<std::string, int> create_words_and_counts(const std::vector<std::pair<int, std::string>>& interests_list) {
    std::map<std::string, int> words_and_counts;
    for (const auto& [user_id, interest] : interests_list) {
        std::istringstream iss(interest);
        std::string word;
        while (iss >> word) {
            std::transform(word.begin(), word.end(), word.begin(), ::tolower);
            words_and_counts[word]++;
        }
    }
    return words_and_counts;
}

std::map<std::string, double> create_average_salary_by_bucket(
    const std::vector<std::pair<double, double>>& salaries_and_tenures) {
    std::unordered_map<std::string, std::vector<double>> salary_by_tenure_bucket;
    for (const auto& [salary, tenure] : salaries_and_tenures) {
        std::string bucket = tenure_bucket(tenure);
        salary_by_tenure_bucket[bucket].push_back(salary);
    }

    std::map<std::string, double> average_salary_by_bucket;
    for (const auto& [bucket, salaries] : salary_by_tenure_bucket) {
        double sum_salaries = std::accumulate(salaries.begin(), salaries.end(), 0.0);
        average_salary_by_bucket[bucket] = sum_salaries / salaries.size();
    }
    return average_salary_by_bucket;
}

std::unordered_map<double, double> create_average_salary_by_tenure(
    const std::unordered_map<double, std::vector<double>>& salary_by_tenure) {
    std::unordered_map<double, double> average_salary_by_tenure;
    for (const auto& [tenure, salaries] : salary_by_tenure) {
        double sum_salaries = std::accumulate(salaries.begin(), salaries.end(), 0.0);
        average_salary_by_tenure[tenure] = sum_salaries / salaries.size();
    }
    return average_salary_by_tenure;
}

std::unordered_map<double, std::vector<double>> create_salary_by_tenure(
    const std::vector<std::pair<double, double>>& salaries_and_tenures) {
    std::unordered_map<double, std::vector<double>> salary_by_tenure;
    for (const auto& [salary, tenure] : salaries_and_tenures) {
        salary_by_tenure[tenure].push_back(salary);
    }
    return salary_by_tenure;
}

std::unordered_map<int, std::vector<std::string>> create_interests_by_user(
    const std::vector<std::pair<int, std::string>>& interests_list) {
    std::unordered_map<int, std::vector<std::string>> interests_by_user_id;
    for (const auto& [user_id, interest] : interests_list) {
        interests_by_user_id[user_id].push_back(interest);
    }
    return interests_by_user_id;
}

std::unordered_map<std::string, std::vector<int>> create_users_by_interest(
    const std::vector<std::pair<int, std::string>>& interests_list) {
    std::unordered_map<std::string, std::vector<int>> user_ids_by_interest;
    for (const auto& [user_id, interest] : interests_list) {
        user_ids_by_interest[interest].push_back(user_id);
    }
    return user_ids_by_interest;
}

void read_avg_connections(const std::vector<User>& users_list) {
    int num_users = users_list.size();
    int total_connections = std::accumulate(users_list.begin(), users_list.end(), 0,
        [](int sum, const User& user) { return sum + number_of_friends(user); });

    double avg_connections = static_cast<double>(total_connections) / num_users;
    std::cout << "avg_connections = " << avg_connections << std::endl;
    std::cout << "total connections " << total_connections << std::endl;
    std::cout << "number of users " << num_users << std::endl;
    std::cout << "average connections " << avg_connections << std::endl;
}

void read_user_connections(const std::vector<User>& users_list, int uid) {
    auto friends_of_friend_ids_uid = friends_of_friend_ids(users_list[uid]);
    std::cout << "friends_of_friend_ids_" << uid << " = ";
    for (const auto& [id, count] : friends_of_friend_ids_uid) {
        std::cout << id << ":" << count << " ";
    }
    std::cout << std::endl;
}

void populate_friendships(const std::vector<std::pair<int, int>>& friendships, std::vector<User>& users_list) {
    for (auto& user : users_list) {
        user.friends.clear();
    }
    for (const auto& [i, j] : friendships) {
        users_list[i].friends.push_back(&users_list[j]);
        users_list[j].friends.push_back(&users_list[i]);
    }
}
