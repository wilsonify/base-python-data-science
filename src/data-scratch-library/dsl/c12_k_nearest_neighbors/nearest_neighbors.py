"""
k-Nearest Neighbors classification algorithm.
"""

import logging
import random
from collections import Counter
from typing import List, Tuple, Any

from dsl.c04_linear_algebra.e0401_vectors import distance
from dsl.c05_statistics.e0501_central_tendancy import mean
from dsl.c12_k_nearest_neighbors.data import cities

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


def try_several_k(
    city_data: List[LabeledPoint], ks: Tuple[int, ...] = (1, 3, 5, 7)
) -> None:
    """Run leave-one-out evaluation for multiple values of *k*."""
    for k in ks:
        num_correct = sum(
            knn_classify(
                k,
                [c for c in city_data if c != (location, language)],
                location,
            )
            == language
            for location, language in city_data
        )
        logging.info("%d neighbors: %d correct / %d", k, num_correct, len(city_data))


def get_distances(
    min_dim: int = 1, max_dim: int = 100, step: int = 5, num_pairs: int = 10_000
) -> List[Tuple[int, float, float, float]]:
    """Compute and log distance summary stats across dimensions."""
    summaries: List[Tuple[int, float, float, float]] = []
    for dim in range(min_dim, max_dim + 1, step):
        distances = random_distances(dim, num_pairs)
        min_distance = min(distances)
        mean_distance = mean(distances)
        ratio = min_distance / mean_distance
        summaries.append((dim, min_distance, mean_distance, ratio))
        logging.info(
            "dim %3d | min %.4f | mean %.4f | ratio %.4f",
            dim,
            min_distance,
            mean_distance,
            ratio,
        )
    return summaries
