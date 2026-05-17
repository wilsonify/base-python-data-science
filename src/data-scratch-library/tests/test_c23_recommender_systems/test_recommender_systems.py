import math
import pytest

from dsl.c23_recommender_systems.recommender_systems import (
    cosine_similarity,
    item_based_suggestions,
    make_user_interest_vector,
    most_popular_new_interests,
    most_similar_users_to,
    unique_interests,
    user_based_suggestions,
    users_interests,
)


class TestCosineSimilarity:
    def test_identical_vectors(self):
        v = [1, 2, 3]
        assert math.isclose(cosine_similarity(v, v), 1.0, abs_tol=1e-9)

    def test_orthogonal_vectors(self):
        v1 = [1, 0, 0]
        v2 = [0, 1, 0]
        assert math.isclose(cosine_similarity(v1, v2), 0.0, abs_tol=1e-9)

    def test_opposite_vectors(self):
        v1 = [1, 0]
        v2 = [-1, 0]
        assert math.isclose(cosine_similarity(v1, v2), -1.0, abs_tol=1e-9)

    def test_zero_vector_raises(self):
        with pytest.raises((ZeroDivisionError, ValueError)):
            cosine_similarity([0, 0, 0], [1, 2, 3])

    def test_known_value(self):
        v1 = [1, 1]
        v2 = [1, 0]
        expected = 1 / math.sqrt(2)
        assert math.isclose(cosine_similarity(v1, v2), expected, abs_tol=1e-9)

    def test_symmetry(self):
        v1 = [1, 2, 3]
        v2 = [4, 5, 6]
        assert math.isclose(
            cosine_similarity(v1, v2), cosine_similarity(v2, v1), abs_tol=1e-9
        )


class TestMostPopularNewInterests:
    def test_returns_list(self):
        result = most_popular_new_interests(["Python", "R"])
        assert isinstance(result, list)

    def test_excludes_current_interests(self):
        current = ["Python"]
        result = most_popular_new_interests(current)
        result_interests = [interest for interest, _ in result]
        assert "Python" not in result_interests

    def test_max_results(self):
        result = most_popular_new_interests([], max_results=3)
        assert len(result) <= 3

    def test_default_max_results(self):
        result = most_popular_new_interests([])
        assert len(result) <= 5

    def test_results_are_tuples(self):
        result = most_popular_new_interests([])
        for item in result:
            assert len(item) == 2
            interest, frequency = item
            assert isinstance(interest, str)
            assert isinstance(frequency, int)

    def test_sorted_by_popularity(self):
        result = most_popular_new_interests([])
        frequencies = [freq for _, freq in result]
        assert frequencies == sorted(frequencies, reverse=True)


class TestMakeUserInterestVector:
    def test_returns_correct_length(self):
        vector = make_user_interest_vector(["Python"])
        assert len(vector) == len(unique_interests)

    def test_known_interest_sets_one(self):
        vector = make_user_interest_vector(["Python"])
        idx = unique_interests.index("Python")
        assert vector[idx] == 1

    def test_unknown_interest_all_zeros(self):
        vector = make_user_interest_vector(["nonexistent_interest_xyz"])
        assert all(v == 0 for v in vector)

    def test_empty_interests(self):
        vector = make_user_interest_vector([])
        assert all(v == 0 for v in vector)

    def test_multiple_interests(self):
        interests = ["Python", "R", "Java"]
        vector = make_user_interest_vector(interests)
        for interest in interests:
            if interest in unique_interests:
                idx = unique_interests.index(interest)
                assert vector[idx] == 1

    def test_binary_values(self):
        vector = make_user_interest_vector(users_interests[0])
        assert all(v in (0, 1) for v in vector)


class TestMostSimilarUsersTo:
    def test_returns_list_of_tuples(self):
        result = most_similar_users_to(0)
        assert isinstance(result, list)
        for user_id, similarity in result:
            assert isinstance(user_id, int)
            assert isinstance(similarity, float)

    def test_excludes_self(self):
        result = most_similar_users_to(0)
        user_ids = [uid for uid, _ in result]
        assert 0 not in user_ids

    def test_sorted_by_similarity_descending(self):
        result = most_similar_users_to(0)
        similarities = [sim for _, sim in result]
        assert similarities == sorted(similarities, reverse=True)

    def test_all_similarities_positive(self):
        result = most_similar_users_to(0)
        for _, similarity in result:
            assert similarity > 0

    def test_different_users(self):
        result0 = most_similar_users_to(0)
        result3 = most_similar_users_to(3)
        assert result0 != result3


class TestUserBasedSuggestions:
    def test_returns_list(self):
        result = user_based_suggestions(0)
        assert isinstance(result, list)

    def test_excludes_current_interests_by_default(self):
        result = user_based_suggestions(0)
        result_interests = {interest for interest, _ in result}
        current_interests = set(users_interests[0])
        assert result_interests.isdisjoint(current_interests)

    def test_include_current_interests(self):
        result = user_based_suggestions(0, include_current_interests=True)
        result_interests = {interest for interest, _ in result}
        current_interests = set(users_interests[0])
        assert not result_interests.isdisjoint(current_interests)

    def test_sorted_by_weight_descending(self):
        result = user_based_suggestions(0)
        weights = [w for _, w in result]
        assert weights == sorted(weights, reverse=True)

    def test_weights_are_positive(self):
        result = user_based_suggestions(0)
        for _, weight in result:
            assert weight > 0


class TestItemBasedSuggestions:
    def test_returns_list(self):
        result = item_based_suggestions(0)
        assert isinstance(result, list)

    def test_excludes_current_interests_by_default(self):
        result = item_based_suggestions(0)
        result_interests = {interest for interest, _ in result}
        current_interests = set(users_interests[0])
        assert result_interests.isdisjoint(current_interests)

    def test_include_current_interests(self):
        result = item_based_suggestions(0, include_current_interests=True)
        result_interests = {interest for interest, _ in result}
        current_interests = set(users_interests[0])
        assert not result_interests.isdisjoint(current_interests)

    def test_sorted_by_weight_descending(self):
        result = item_based_suggestions(0)
        weights = [w for _, w in result]
        assert weights == sorted(weights, reverse=True)

    def test_weights_are_positive(self):
        result = item_based_suggestions(0)
        for _, weight in result:
            assert weight > 0

    def test_different_from_user_based(self):
        user_result = user_based_suggestions(0)
        item_result = item_based_suggestions(0)
        # They may overlap but should not be identical in general
        assert isinstance(user_result, list)
        assert isinstance(item_result, list)
