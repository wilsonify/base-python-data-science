#include "decision_trees.h"
#include <algorithm>
#include <map>
#include <stdexcept>

using LabeledData = std::vector<std::pair<std::unordered_map<std::string,std::string>, std::string>>;

double entropy(const std::vector<double>& class_probabilities) {
    double result = 0.0;
    for (double p : class_probabilities)
        if (p > 0.0) result += -p * std::log2(p);
    return result;
}

std::vector<double> get_class_probabilities(const std::vector<std::string>& labels) {
    std::map<std::string, int> counts;
    for (const auto& label : labels)
        ++counts[label];
    double total = static_cast<double>(labels.size());
    std::vector<double> probs;
    probs.reserve(counts.size());
    for (const auto& [label, count] : counts)
        probs.push_back(count / total);
    return probs;
}

double data_entropy(const LabeledData& labeled_data) {
    std::vector<std::string> labels;
    labels.reserve(labeled_data.size());
    for (const auto& [attrs, label] : labeled_data)
        labels.push_back(label);
    return entropy(get_class_probabilities(labels));
}

double partition_entropy(const std::vector<LabeledData>& subsets) {
    size_t total_count = 0;
    for (const auto& subset : subsets)
        total_count += subset.size();
    double result = 0.0;
    for (const auto& subset : subsets)
        result += data_entropy(subset) * static_cast<double>(subset.size()) / total_count;
    return result;
}

double partition_entropy_by(const LabeledData& inputs, const std::string& attribute) {
    std::map<std::string, LabeledData> groups;
    for (const auto& item : inputs) {
        auto it = item.first.find(attribute);
        std::string key = (it != item.first.end()) ? it->second : "";
        groups[key].push_back(item);
    }
    std::vector<LabeledData> subsets;
    subsets.reserve(groups.size());
    for (auto& [k, v] : groups)
        subsets.push_back(std::move(v));
    return partition_entropy(subsets);
}

std::shared_ptr<TreeNode> build_tree_id3(const LabeledData& inputs, std::vector<std::string> split_candidates) {
    if (split_candidates.empty() && !inputs.empty()) {
        // First call: collect all attribute keys
        for (const auto& [attrs, label] : inputs)
            for (const auto& [key, val] : attrs)
                split_candidates.push_back(key);
        std::sort(split_candidates.begin(), split_candidates.end());
        split_candidates.erase(std::unique(split_candidates.begin(), split_candidates.end()), split_candidates.end());
    }

    size_t num_trues  = 0;
    size_t num_falses = 0;
    for (const auto& [attrs, label] : inputs) {
        if (label == "True" || label == "true" || label == "1") ++num_trues;
        else ++num_falses;
    }

    if (num_trues == 0) {
        auto leaf = std::make_shared<TreeNode>();
        leaf->is_leaf = true;
        leaf->leaf_value = false;
        return leaf;
    }
    if (num_falses == 0) {
        auto leaf = std::make_shared<TreeNode>();
        leaf->is_leaf = true;
        leaf->leaf_value = true;
        return leaf;
    }
    if (split_candidates.empty()) {
        auto leaf = std::make_shared<TreeNode>();
        leaf->is_leaf = true;
        leaf->leaf_value = (num_trues >= num_falses);
        return leaf;
    }

    // Find best split attribute
    std::string best_attr = split_candidates[0];
    double best_entropy = partition_entropy_by(inputs, best_attr);
    for (const auto& attr : split_candidates) {
        double e = partition_entropy_by(inputs, attr);
        if (e < best_entropy) {
            best_entropy = e;
            best_attr = attr;
        }
    }

    // Partition by best attribute
    std::map<std::string, LabeledData> partitions;
    for (const auto& item : inputs) {
        auto it = item.first.find(best_attr);
        std::string key = (it != item.first.end()) ? it->second : "";
        partitions[key].push_back(item);
    }

    // Remove best_attr from candidates
    std::vector<std::string> new_candidates;
    for (const auto& attr : split_candidates)
        if (attr != best_attr) new_candidates.push_back(attr);

    auto node = std::make_shared<TreeNode>();
    node->is_leaf = false;
    node->split_attribute = best_attr;

    for (auto& [val, subset] : partitions)
        node->children[val] = build_tree_id3(subset, new_candidates);

    // Default child: majority label
    auto default_leaf = std::make_shared<TreeNode>();
    default_leaf->is_leaf = true;
    default_leaf->leaf_value = (num_trues > num_falses);
    node->default_child = default_leaf;

    return node;
}

bool classify(const std::shared_ptr<TreeNode>& tree, const std::unordered_map<std::string,std::string>& inputs) {
    if (tree->is_leaf)
        return tree->leaf_value;

    auto it = inputs.find(tree->split_attribute);
    if (it == inputs.end())
        return classify(tree->default_child, inputs);

    auto child_it = tree->children.find(it->second);
    if (child_it == tree->children.end())
        return classify(tree->default_child, inputs);

    return classify(child_it->second, inputs);
}
