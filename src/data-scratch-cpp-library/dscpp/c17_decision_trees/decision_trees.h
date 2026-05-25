#pragma once
#include <cmath>
#include <map>
#include <memory>
#include <string>
#include <unordered_map>
#include <variant>
#include <vector>

double entropy(const std::vector<double>& class_probabilities);
std::vector<double> get_class_probabilities(const std::vector<std::string>& labels);
double data_entropy(const std::vector<std::pair<std::unordered_map<std::string,std::string>, std::string>>& labeled_data);
double partition_entropy(const std::vector<std::vector<std::pair<std::unordered_map<std::string,std::string>, std::string>>>& subsets);
double partition_entropy_by(
    const std::vector<std::pair<std::unordered_map<std::string,std::string>, std::string>>& inputs,
    const std::string& attribute);

struct TreeNode {
    bool is_leaf = false;
    bool leaf_value = false;
    std::string split_attribute;
    std::unordered_map<std::string, std::shared_ptr<TreeNode>> children;
    std::shared_ptr<TreeNode> default_child;
};

std::shared_ptr<TreeNode> build_tree_id3(
    const std::vector<std::pair<std::unordered_map<std::string,std::string>, std::string>>& inputs,
    std::vector<std::string> split_candidates = {});

bool classify(const std::shared_ptr<TreeNode>& tree, const std::unordered_map<std::string,std::string>& inputs);
