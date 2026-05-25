#pragma once
#include <functional>
#include <map>
#include <string>
#include <vector>

std::map<std::string, int> word_count_old(const std::vector<std::string>& documents);

std::vector<std::pair<std::string, int>> wc_mapper(const std::string& document);
std::vector<std::pair<std::string, int>> word_count(const std::vector<std::string>& documents);

template<typename K, typename V, typename R>
std::vector<R> map_reduce(
    const std::vector<std::string>& inputs,
    std::function<std::vector<std::pair<K, V>>(const std::string&)> mapper,
    std::function<std::vector<R>(const K&, const std::vector<V>&)> reducer) {

    std::map<K, std::vector<V>> collector;
    for (const auto& input : inputs) {
        auto pairs = mapper(input);
        for (auto& [k, v] : pairs)
            collector[k].push_back(v);
    }

    std::vector<R> result;
    for (auto& [k, vs] : collector) {
        auto reduced = reducer(k, vs);
        result.insert(result.end(), reduced.begin(), reduced.end());
    }
    return result;
}

std::vector<std::pair<std::string, int>> matrix_multiply_mapper_A(int m, int i, int j, double value);
std::vector<std::pair<std::string, int>> matrix_multiply_mapper_B(int m, int i, int j, double value);
