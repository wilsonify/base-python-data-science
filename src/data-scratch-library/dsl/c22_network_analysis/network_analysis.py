"""
Graph/network algorithms: BFS shortest paths, betweenness centrality,
closeness centrality, eigenvector centrality, and PageRank.
"""

import logging
from collections import deque
from functools import partial
from typing import Any, Callable, Dict, List, Optional, Tuple

from dsl.c04_linear_algebra.e0401_vectors import (
    distance,
    dot,
    magnitude,
    scalar_multiply,
)
from dsl.c04_linear_algebra.e0402_matrices import (
    get_column,
    get_row,
    make_matrix,
    shape,
)


# -- Friend graph construction --------------------------------------------------

def populate_friends(
    users: List[Dict[str, Any]], friendships: List[Tuple[int, int]]
) -> List[Dict[str, Any]]:
    """Add a ``friends`` list to each user dict."""
    for user in users:
        user["friends"] = []
    for i, j in friendships:
        users[i]["friends"].append(users[j])
        users[j]["friends"].append(users[i])
    return users


# -- Shortest paths (BFS) -------------------------------------------------------

def shortest_paths_from(from_user: Dict[str, Any]) -> Dict[int, List[List[int]]]:
    """Return all shortest paths from *from_user* to every reachable user."""
    shortest: Dict[int, List[List[int]]] = {from_user["id"]: [[]]}
    frontier = deque(
        (from_user, friend) for friend in from_user["friends"]
    )

    while frontier:
        prev, cur = frontier.popleft()
        uid = cur["id"]
        paths_to_prev = shortest[prev["id"]]
        old_paths = shortest.get(uid, [])
        new_paths = [p + [uid] for p in paths_to_prev]
        min_len = len(old_paths[0]) if old_paths else float("inf")
        new_paths = [p for p in new_paths if len(p) <= min_len and p not in old_paths]
        shortest[uid] = old_paths + new_paths
        for friend in cur["friends"]:
            if friend["id"] not in shortest:
                frontier.append((cur, friend))

    return shortest


def farness(user: Dict[str, Any]) -> int:
    """Sum of shortest-path lengths from *user* to every other user."""
    return sum(len(paths[0]) for paths in user["shortest_paths"].values())


def populate_shortest_paths(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Compute and attach ``shortest_paths`` to each user."""
    for user in users:
        user["shortest_paths"] = shortest_paths_from(user)
    return users


# -- Betweenness centrality -----------------------------------------------------

def populate_betweeness(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Compute and attach ``betweenness_centrality`` to each user."""
    initialize_centrality(users)
    for source in users:
        process_shortest_paths(source, users)
    return users


def initialize_centrality(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Reset betweenness centrality values to 0.0."""
    for user in users:
        user["betweenness_centrality"] = 0.0
    return users


def update_centrality(
    path: List[int],
    contribution: float,
    source_id: int,
    target_id: int,
    users: List[Dict[str, Any]],
) -> None:
    """Apply path contribution to intermediate nodes only."""
    for uid in path:
        if uid not in (source_id, target_id):
            users[uid]["betweenness_centrality"] += contribution


def process_shortest_paths(
    source: Dict[str, Any], users: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """Update betweenness using one source user's shortest paths."""
    source_id = source["id"]
    for target_id, paths in source["shortest_paths"].items():
        if source_id < target_id:
            contribution = 1 / len(paths)
            for path in paths:
                update_centrality(path, contribution, source_id, target_id, users)
    return users


def populate_betweeness_v1(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Compatibility wrapper using helper-based implementation."""
    initialize_centrality(users)
    for source in users:
        process_shortest_paths(source, users)
    return users


# -- Closeness centrality -------------------------------------------------------

def populate_closeness(
    users: List[Dict[str, Any]], eps: float = 0.001
) -> List[Dict[str, Any]]:
    """Compute and attach ``closeness_centrality`` to each user."""
    for user in users:
        user["closeness_centrality"] = 1 / (farness(user) + eps)
    return users


def get_betweeness(users: List[Dict[str, Any]]) -> List[Tuple[int, float]]:
    """Return and log per-user betweenness centrality."""
    values = [(u["id"], u["betweenness_centrality"]) for u in users]
    for uid, value in values:
        logging.info("user %d betweenness %.4f", uid, value)
    return values


def get_closeness(users: List[Dict[str, Any]]) -> List[Tuple[int, float]]:
    """Return and log per-user closeness centrality."""
    values = [(u["id"], u["closeness_centrality"]) for u in users]
    for uid, value in values:
        logging.info("user %d closeness %.4f", uid, value)
    return values


# -- Adjacency matrix & eigenvector centrality -----------------------------------

def construct_adjacency(
    users: List[Dict[str, Any]], friendships: List[Tuple[int, int]]
) -> List[List[int]]:
    """Build an adjacency matrix from *friendships*."""
    n = len(users)

    def entry(i: int, j: int) -> int:
        return 1 if (i, j) in friendships or (j, i) in friendships else 0

    return make_matrix(n, n, entry)


def matrix_product_entry(
    a: List[List[float]], b: List[List[float]], i: int, j: int
) -> float:
    """Dot product of row *i* of *a* with column *j* of *b*."""
    return dot(get_row(a, i), get_column(b, j))


def matrix_multiply(
    a: List[List[float]], b: List[List[float]]
) -> List[List[float]]:
    """Multiply matrices *a* and *b*."""
    n1, k1 = shape(a)
    n2, k2 = shape(b)
    if k1 != n2:
        raise ArithmeticError("incompatible shapes!")
    return make_matrix(n1, k2, partial(matrix_product_entry, a, b))


def vector_as_matrix(v: List[float]) -> List[List[float]]:
    """Convert a vector to an n×1 matrix."""
    return [[vi] for vi in v]


def vector_from_matrix(m: List[List[float]]) -> List[float]:
    """Convert an n×1 matrix to a vector."""
    return [row[0] for row in m]


def matrix_operate(a: List[List[float]], v: List[float]) -> List[float]:
    """Return the matrix–vector product *a* · *v*."""
    return vector_from_matrix(matrix_multiply(a, vector_as_matrix(v)))


def find_eigenvector(
    a: List[List[float]], tolerance: float = 1e-5
) -> Tuple[List[float], float]:
    """Power-iteration method for the dominant eigenvector."""
    guess = [1.0 for _ in a]
    while True:
        result = matrix_operate(a, guess)
        length = magnitude(result)
        next_guess = scalar_multiply(1 / length, result)
        if distance(guess, next_guess) < tolerance:
            return next_guess, length
        guess = next_guess


def compute_eigenvectors(adjacency_matrix: List[List[int]]) -> List[float]:
    """Return eigenvector centralities from the adjacency matrix."""
    centralities, _ = find_eigenvector(adjacency_matrix)
    return centralities


def get_eigenvector_centrality(
    centralities: List[float],
) -> List[Tuple[int, float]]:
    """Return and log eigenvector centrality values."""
    values = list(enumerate(centralities))
    for uid, value in values:
        logging.info("user %d eigenvector %.4f", uid, value)
    return values


# -- Endorsements & PageRank ----------------------------------------------------

def populate_endorsments(
    users: List[Dict[str, Any]], endorsements: List[Tuple[int, int]]
) -> List[Dict[str, Any]]:
    """Add ``endorses`` and ``endorsed_by`` lists to each user."""
    for user in users:
        user["endorses"] = []
        user["endorsed_by"] = []
    for source_id, target_id in endorsements:
        users[source_id]["endorses"].append(users[target_id])
        users[target_id]["endorsed_by"].append(users[source_id])
    return users


def populate_endorsements(
    users: List[Dict[str, Any]],
) -> List[Tuple[int, int]]:
    """Return a list of (user_id, num_endorsements) pairs."""
    return [(u["id"], len(u["endorsed_by"])) for u in users]


def page_rank(
    users: List[Dict[str, Any]],
    damping: float = 0.85,
    num_iters: int = 100,
) -> Dict[int, float]:
    """Compute PageRank over the endorsement graph."""
    n = len(users)
    pr: Dict[int, float] = {u["id"]: 1 / n for u in users}
    base = (1 - damping) / n
    for _ in range(num_iters):
        next_pr: Dict[int, float] = {u["id"]: base for u in users}
        for user in users:
            share = pr[user["id"]] * damping
            for endorsee in user["endorses"]:
                next_pr[endorsee["id"]] += share / len(user["endorses"])
        pr = next_pr
    return pr


def get_page_ranks(page_ranks: Dict[int, float]) -> List[Tuple[int, float]]:
    """Return and log PageRank values sorted by user id."""
    values = sorted(page_ranks.items(), key=lambda pair: pair[0])
    for uid, value in values:
        logging.info("user %d pagerank %.4f", uid, value)
    return values
