#include <cmath>

double entropy(probabilities);
double get_class_probabilities(labels);
double data_entropy(labeled_data);
double partition_entropy(subsets);
double group_by(items, key_fn);
double partition_by(inputs, attribute);
double partition_entropy_by(inputs, attribute);
double classify(tree, inputs);
double build_tree_id3(inputs, split_candidates=None);
double forest_classify(trees, inputs);
