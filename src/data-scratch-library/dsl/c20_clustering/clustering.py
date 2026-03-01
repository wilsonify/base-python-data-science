"""
K-means and hierarchical (agglomerative) clustering.
"""

import random
from typing import Any, Callable, List, Tuple, Union

from dsl.c04_linear_algebra.e0401_vectors import (
    distance,
    squared_distance,
    vector_mean,
)

# Type alias for a hierarchical cluster (recursive).
Cluster = Union[Tuple[Any, ...], Tuple[int, List["Cluster"]]]


class KMeans:
    """K-means clustering."""

    def __init__(self, k: int) -> None:
        self.k = k
        self.means: List[List[float]] = []

    def classify(self, point: List[float]) -> int:
        """Return the index of the nearest cluster centre."""
        return min(range(self.k), key=lambda i: squared_distance(point, self.means[i]))

    def train(self, inputs: List[List[float]]) -> None:
        """Run Lloyd's algorithm until convergence."""
        self.means = random.sample(inputs, self.k)
        assignments = None
        while True:
            new_assignments = [self.classify(x) for x in inputs]
            if assignments == new_assignments:
                return
            assignments = new_assignments
            for i in range(self.k):
                cluster_points = [p for p, a in zip(inputs, assignments) if a == i]
                if cluster_points:
                    self.means[i] = vector_mean(cluster_points)


def squared_clustering_errors(inputs: List[List[float]], k: int) -> float:
    """Total squared error from k-means clustering."""
    clusterer = KMeans(k)
    clusterer.train(inputs)
    assignments = [clusterer.classify(x) for x in inputs]
    return sum(
        squared_distance(x, clusterer.means[a])
        for x, a in zip(inputs, assignments)
    )


# -- Hierarchical clustering ---------------------------------------------------

def is_leaf(cluster: Cluster) -> bool:
    """A cluster is a leaf if it has length 1."""
    return len(cluster) == 1


def get_children(cluster: Cluster) -> List[Cluster]:
    """Return the two children of a merged cluster."""
    if is_leaf(cluster):
        raise TypeError("a leaf cluster has no children")
    return cluster[1]


def get_values(cluster: Cluster) -> list:
    """Return all leaf values below *cluster*."""
    if is_leaf(cluster):
        return list(cluster)
    return [v for child in get_children(cluster) for v in get_values(child)]


def cluster_distance(
    c1: Cluster, c2: Cluster, distance_agg: Callable = min
) -> float:
    """Aggregate distance between all pairs of leaf values."""
    return distance_agg(
        distance(v1, v2) for v1 in get_values(c1) for v2 in get_values(c2)
    )


def get_merge_order(cluster: Cluster) -> float:
    """Return the merge order of a cluster (inf for leaves)."""
    if is_leaf(cluster):
        return float("inf")
    return cluster[0]


def bottom_up_cluster(
    inputs: List[List[float]], distance_agg: Callable = min
) -> Cluster:
    """Agglomerative clustering (bottom-up, single/complete linkage)."""
    clusters: List[Cluster] = [(inp,) for inp in inputs]
    while len(clusters) > 1:
        c1, c2 = min(
            (
                (ci, cj)
                for i, ci in enumerate(clusters)
                for cj in clusters[:i]
            ),
            key=lambda pair: cluster_distance(pair[0], pair[1], distance_agg),
        )
        clusters = [c for c in clusters if c != c1 and c != c2]
        merged: Cluster = (len(clusters), [c1, c2])
        clusters.append(merged)
    return clusters[0]


def generate_clusters(base_cluster: Cluster, num_clusters: int) -> List[Cluster]:
    """Unmerge *base_cluster* until we have *num_clusters* clusters."""
    clusters = [base_cluster]
    while len(clusters) < num_clusters:
        next_c = min(clusters, key=get_merge_order)
        clusters = [c for c in clusters if c != next_c]
        clusters.extend(get_children(next_c))
    return clusters
