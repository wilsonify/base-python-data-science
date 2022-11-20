"""
A decision tree uses a tree structure to represent a number of possible decision paths and an outcome for each path.

"""

import logging
import math
from collections import Counter, defaultdict
from functools import partial
from logging.config import dictConfig

from dsl import config


def entropy(class_probabilities):
    """given a list of class probabilities, compute the entropy"""
    return sum(-p * math.log(p, 2) for p in class_probabilities if p)


def get_class_probabilities(labels):
    total_count = len(labels)
    return [count / total_count for count in Counter(labels).values()]


def data_entropy(labeled_data):
    labels = [label for _, label in labeled_data]
    probabilities = get_class_probabilities(labels)
    return entropy(probabilities)


def partition_entropy(subsets):
    """find the entropy from this partition of data into subsets"""
    total_count = sum(len(subset) for subset in subsets)

    return sum(data_entropy(subset) * len(subset) / total_count for subset in subsets)


def group_by(items, key_fn):
    """returns a defaultdict(list), where each input item
    is in the list whose key is key_fn(item)"""
    groups = defaultdict(list)
    for item in items:
        key = key_fn(item)
        groups[key].append(item)
    return groups


def partition_by(inputs, attribute):
    """returns a dict of inputs partitioned by the attribute
    each input is a pair (attribute_dict, label)"""
    return group_by(inputs, lambda x: x[0][attribute])


def partition_entropy_by(inputs, attribute):
    """computes the entropy corresponding to the given partition"""
    partitions = partition_by(inputs, attribute)
    return partition_entropy(partitions.values())


def classify(tree, inputs):
    """classify the input using the given decision tree"""

    # if this is a leaf node, return its value
    if tree in [True, False]:
        return tree

    # otherwise find the correct subtree
    attribute, subtree_dict = tree

    subtree_key = inputs.get(attribute)  # None if input is missing attribute

    if subtree_key not in subtree_dict:  # if no subtree for key,
        subtree_key = None  # we'll use the None subtree

    subtree = subtree_dict[subtree_key]  # choose the appropriate subtree
    return classify(subtree, inputs)  # and use it to classify the input


def build_tree_id3(inputs, split_candidates=None):
    # if this is our first pass,
    # all keys of the first input are split candidates
    if split_candidates is None:
        split_candidates = inputs[0][0].keys()

    # count Trues and Falses in the inputs
    num_inputs = len(inputs)
    num_trues = len([label for item, label in inputs if label])
    num_falses = num_inputs - num_trues

    if num_trues == 0:  # if only Falses are left
        return False  # return a "False" leaf

    if num_falses == 0:  # if only Trues are left
        return True  # return a "True" leaf

    if not split_candidates:  # if no split candidates left
        return num_trues >= num_falses  # return the majority leaf

    # otherwise, split on the best attribute
    best_attribute = min(split_candidates, key=partial(partition_entropy_by, inputs))

    partitions = partition_by(inputs, best_attribute)
    new_candidates = [a for a in split_candidates if a != best_attribute]

    # recursively build the subtrees
    subtrees = {
        attribute: build_tree_id3(subset, new_candidates)
        for attribute, subset in partitions.items()
    }

    subtrees[None] = num_trues > num_falses  # default case

    return best_attribute, subtrees


def forest_classify(trees, inputs):
    votes = [classify(tree, inputs) for tree in trees]
    vote_counts = Counter(votes)
    return vote_counts.most_common(1)[0][0]


def main():
    inputs_list = [
        ({"level": "Senior", "lang": "Java", "tweets": "no", "phd": "no"}, False),
        ({"level": "Senior", "lang": "Java", "tweets": "no", "phd": "yes"}, False),
        ({"level": "Mid", "lang": "Python", "tweets": "no", "phd": "no"}, True),
        ({"level": "Junior", "lang": "Python", "tweets": "no", "phd": "no"}, True),
        ({"level": "Junior", "lang": "R", "tweets": "yes", "phd": "no"}, True),
        ({"level": "Junior", "lang": "R", "tweets": "yes", "phd": "yes"}, False),
        ({"level": "Mid", "lang": "R", "tweets": "yes", "phd": "yes"}, True),
        ({"level": "Senior", "lang": "Python", "tweets": "no", "phd": "no"}, False),
        ({"level": "Senior", "lang": "R", "tweets": "yes", "phd": "no"}, True),
        ({"level": "Junior", "lang": "Python", "tweets": "yes", "phd": "no"}, True),
        ({"level": "Senior", "lang": "Python", "tweets": "yes", "phd": "yes"}, True),
        ({"level": "Mid", "lang": "Python", "tweets": "no", "phd": "yes"}, True),
        ({"level": "Mid", "lang": "Java", "tweets": "yes", "phd": "no"}, True),
        ({"level": "Junior", "lang": "Python", "tweets": "no", "phd": "yes"}, False),
    ]

    for _key in ["level", "lang", "tweets", "phd"]:
        logging.info("%r", "key = {}".format(_key))
        partition_entropy_key = partition_entropy_by(inputs_list, _key)
        logging.info("%r", "partition_entropy = {}".format(partition_entropy_key))

    senior_inputs = [
        (in_put, label) for in_put, label in inputs_list if in_put["level"] == "Senior"
    ]

    for _key in ["lang", "tweets", "phd"]:
        logging.info("%r", "_key = {}".format(_key))
        partition_entropy2 = partition_entropy_by(senior_inputs, _key)
        logging.info("%r", "partition_entropy = {}".format(partition_entropy2))

    logging.info("building the tree")
    _tree = build_tree_id3(inputs_list)
    logging.info("%r", "tree = {}".format(_tree))

    logging.info(
        "%r",
        "Junior / Java / tweets / no phd {}".format(
            classify(
                _tree, {"level": "Junior", "lang": "Java", "tweets": "yes", "phd": "no"}
            ),
        ),
    )

    logging.info(
        "%r",
        "Junior / Java / tweets / phd {}".format(
            classify(
                _tree,
                {"level": "Junior", "lang": "Java", "tweets": "yes", "phd": "yes"},
            ),
        ),
    )

    logging.info("%r", "Intern {}".format(classify(_tree, {"level": "Intern"})))
    logging.info("%r", "Senior {}".format(classify(_tree, {"level": "Senior"})))


if __name__ == "__main__":
    dictConfig(config.LOGGING_CONFIG_DICT)
    main()
