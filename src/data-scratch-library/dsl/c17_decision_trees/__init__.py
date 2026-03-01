"""
Chapter 17: Decision Trees

ID3-based decision-tree learning and random-forest classification.
"""

from .decision_trees import (
    entropy,
    get_class_probabilities,
    data_entropy,
    partition_entropy,
    group_by,
    partition_by,
    partition_entropy_by,
    classify,
    build_tree_id3,
    forest_classify,
)
