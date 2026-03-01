"""
Recommender systems: popularity, user-based, and item-based collaborative filtering.

All matrices are built lazily (on first call) rather than at module-import time.
"""

import math
from collections import Counter, defaultdict
from typing import List, Tuple

from dsl.c04_linear_algebra.e0401_vectors import dot
from .data import users_interests


def cosine_similarity(v: List[float], w: List[float]) -> float:
    """Cosine similarity between two vectors."""
    return dot(v, w) / math.sqrt(dot(v, v) * dot(w, w))


# -- Popularity-based -----------------------------------------------------------

def _popular_interests() -> List[Tuple[str, int]]:
    """Return interest counts sorted by popularity."""
    return Counter(
        interest
        for user_interests in users_interests
        for interest in user_interests
    ).most_common()


def most_popular_new_interests(
    user_interests: List[str], max_results: int = 5
) -> List[Tuple[str, int]]:
    """Suggest popular interests the user doesn't already have."""
    return [
        (interest, freq)
        for interest, freq in _popular_interests()
        if interest not in user_interests
    ][:max_results]


# -- User-based collaborative filtering ----------------------------------------

def _unique_interests() -> List[str]:
    return sorted({i for ui in users_interests for i in ui})


def make_user_interest_vector(user_interests: List[str]) -> List[int]:
    """Binary vector: 1 if user has the interest, 0 otherwise."""
    uniq = _unique_interests()
    return [1 if interest in user_interests else 0 for interest in uniq]


def _user_interest_matrix() -> List[List[int]]:
    return [make_user_interest_vector(ui) for ui in users_interests]


def _user_similarities() -> List[List[float]]:
    matrix = _user_interest_matrix()
    return [
        [cosine_similarity(a, b) for b in matrix]
        for a in matrix
    ]


def most_similar_users_to(user_id: int) -> List[Tuple[int, float]]:
    """Return other users sorted by descending similarity."""
    sims = _user_similarities()
    pairs = [
        (other_id, sim)
        for other_id, sim in enumerate(sims[user_id])
        if user_id != other_id and sim > 0
    ]
    return sorted(pairs, key=lambda p: p[1], reverse=True)


def user_based_suggestions(
    user_id: int, include_current_interests: bool = False
) -> List[Tuple[str, float]]:
    """Suggest interests weighted by similar users."""
    suggestions: defaultdict[str, float] = defaultdict(float)
    for other_id, similarity in most_similar_users_to(user_id):
        for interest in users_interests[other_id]:
            suggestions[interest] += similarity
    ranked = sorted(suggestions.items(), key=lambda p: p[1], reverse=True)
    if include_current_interests:
        return ranked
    return [(s, w) for s, w in ranked if s not in users_interests[user_id]]


# -- Item-based collaborative filtering ----------------------------------------

def _interest_user_matrix() -> List[List[int]]:
    uim = _user_interest_matrix()
    uniq = _unique_interests()
    return [
        [uim[u][j] for u in range(len(uim))]
        for j in range(len(uniq))
    ]


def _interest_similarities() -> List[List[float]]:
    ium = _interest_user_matrix()
    return [
        [cosine_similarity(a, b) for b in ium]
        for a in ium
    ]


def most_similar_interests_to(interest_id: int) -> List[Tuple[str, float]]:
    """Return interests sorted by descending similarity to *interest_id*."""
    uniq = _unique_interests()
    sims = _interest_similarities()[interest_id]
    pairs = [
        (uniq[other_id], sim)
        for other_id, sim in enumerate(sims)
        if interest_id != other_id and sim > 0
    ]
    return sorted(pairs, key=lambda p: p[1], reverse=True)


def item_based_suggestions(
    user_id: int, include_current_interests: bool = False
) -> List[Tuple[str, float]]:
    """Suggest interests based on item–item similarity."""
    suggestions: defaultdict[str, float] = defaultdict(float)
    uiv = _user_interest_matrix()[user_id]
    for interest_id, is_interested in enumerate(uiv):
        if is_interested:
            for interest, sim in most_similar_interests_to(interest_id):
                suggestions[interest] += sim
    ranked = sorted(suggestions.items(), key=lambda p: p[1], reverse=True)
    if include_current_interests:
        return ranked
    return [(s, w) for s, w in ranked if s not in users_interests[user_id]]
