"""
Decision-tree construction (ID3) and random-forest classification.
"""

import math
from collections import Counter, defaultdict
from functools import partial
from typing import Any, Callable, Dict, List, Sequence, Tuple, TypeVar, Union

# A decision tree is either a leaf (True/False) or a (attribute, subtree_dict) pair.
DecisionTree = Union[bool, Tuple[str, Dict[Any, "DecisionTree"]]]

T = TypeVar("T")


def entropy(class_probabilities: Sequence[float]) -> float:
    """Compute Shannon entropy from a list of class probabilities."""
    return sum(-p * math.log(p, 2) for p in class_probabilities if p)


def get_class_probabilities(labels: List[Any]) -> List[float]:
    """Return the list of class probabilities for the given labels."""
    total = len(labels)
    return [count / total for count in Counter(labels).values()]


def data_entropy(labeled_data: List[Tuple[Any, Any]]) -> float:
    """Entropy of a labeled data set (list of (features, label) pairs)."""
    labels = [label for _, label in labeled_data]
    return entropy(get_class_probabilities(labels))


def partition_entropy(subsets: List[List[Tuple[Any, Any]]]) -> float:
    """Weighted entropy of a partition of labeled data into subsets."""
    total = sum(len(s) for s in subsets)
    return sum(data_entropy(s) * len(s) / total for s in subsets)


def group_by(items: List[T], key_fn: Callable[[T], Any]) -> Dict[Any, List[T]]:
    """Group *items* into a defaultdict(list) keyed by *key_fn*."""
    groups: Dict[Any, List[T]] = defaultdict(list)
    for item in items:
        groups[key_fn(item)].append(item)
    return groups


def partition_by(
    inputs: List[Tuple[Dict[str, Any], Any]], attribute: str
) -> Dict[Any, List[Tuple[Dict[str, Any], Any]]]:
    """Partition inputs by the value of *attribute*."""
    return group_by(inputs, lambda x: x[0][attribute])


def partition_entropy_by(
    inputs: List[Tuple[Dict[str, Any], Any]], attribute: str
) -> float:
    """Compute the partition entropy when splitting on *attribute*."""
    partitions = partition_by(inputs, attribute)
    return partition_entropy(list(partitions.values()))


def classify(tree: DecisionTree, inputs: Dict[str, Any]) -> bool:
    """Classify *inputs* using the given decision *tree*."""
    if tree in (True, False):
        return tree

    attribute, subtree_dict = tree
    subtree_key = inputs.get(attribute)
    if subtree_key not in subtree_dict:
        subtree_key = None
    return classify(subtree_dict[subtree_key], inputs)


def build_tree_id3(
    inputs: List[Tuple[Dict[str, Any], bool]],
    split_candidates: List[str] = None,
) -> DecisionTree:
    """Build a decision tree using the ID3 algorithm."""
    if split_candidates is None:
        split_candidates = list(inputs[0][0].keys())

    num_trues = sum(1 for _, label in inputs if label)
    num_falses = len(inputs) - num_trues

    if num_trues == 0:
        return False
    if num_falses == 0:
        return True
    if not split_candidates:
        return num_trues >= num_falses

    best = min(split_candidates, key=partial(partition_entropy_by, inputs))
    partitions = partition_by(inputs, best)
    new_candidates = [a for a in split_candidates if a != best]

    subtrees = {
        val: build_tree_id3(subset, new_candidates)
        for val, subset in partitions.items()
    }
    subtrees[None] = num_trues > num_falses
    return (best, subtrees)


def forest_classify(trees: List[DecisionTree], inputs: Dict[str, Any]) -> bool:
    """Classify by majority vote of several decision trees."""
    votes = [classify(tree, inputs) for tree in trees]
    return Counter(votes).most_common(1)[0][0]
