"""
k-Nearest Neighbors classification algorithm.
"""

import random
from collections import Counter
from typing import List, Tuple, Any

from dsl.c04_linear_algebra.e0401_vectors import distance
from dsl.c05_statistics.e0501_central_tendancy import mean

LabeledPoint = Tuple[List[float], str]


def raw_majority_vote(labels: List[str]) -> str:
    """Return the most common label (ties broken arbitrarily)."""
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    return winner


def majority_vote(labels: List[str]) -> str:
    """Return the most common label, removing the farthest on ties.

    Assumes *labels* are ordered from nearest to farthest.
    """
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len(
        [count for count in vote_counts.values() if count == winner_count]
    )
    if num_winners == 1:
        return winner
    return majority_vote(labels[:-1])


def knn_classify(
    k: int, labeled_points: List[LabeledPoint], new_point: List[float]
) -> str:
    """Classify *new_point* by majority vote of its *k* nearest neighbours."""
    by_distance = sorted(
        labeled_points,
        key=lambda point_label: distance(point_label[0], new_point),
    )
    k_nearest_labels = [label for _, label in by_distance[:k]]
    return majority_vote(k_nearest_labels)


# ── Curse of dimensionality helpers ──────────────────────────────────


def random_point(dim: int) -> List[float]:
    """Return a random point in *dim* dimensions."""
    return [random.random() for _ in range(dim)]


def random_distances(dim: int, num_pairs: int) -> List[float]:
    """Return distances between *num_pairs* random point pairs in *dim*-d."""
    return [
        distance(random_point(dim), random_point(dim))
        for _ in range(num_pairs)
    ]
