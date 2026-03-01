import pytest

from dsl.c22_network_analysis.network_analysis import (
    construct_adjacency,
    farness,
    find_eigenvector,
    get_betweeness,
    get_closeness,
    get_eigenvector_centrality,
    get_page_ranks,
    initialize_centrality,
    matrix_multiply,
    matrix_operate,
    matrix_product_entry,
    page_rank,
    populate_betweeness,
    populate_betweeness_v1,
    populate_closeness,
    populate_endorsements,
    populate_endorsments,
    populate_friends,
    populate_shortest_paths,
    process_shortest_paths,
    shortest_paths_from,
    update_centrality,
    vector_as_matrix,
    vector_from_matrix,
)


def _make_users(n):
    """Create a list of n user dicts with default empty fields."""
    return [
        {
            "id": i,
            "friends": [],
            "endorses": [],
            "endorsed_by": [],
            "shortest_paths": {},
            "betweenness_centrality": 0.0,
            "closeness_centrality": 0.0,
        }
        for i in range(n)
    ]


@pytest.fixture
def network():
    """Build a small 5-user network:

    0 - 1 - 2
    |       |
    3 - - - 4
    """
    users = _make_users(5)
    friendships = [(0, 1), (1, 2), (0, 3), (2, 4), (3, 4)]
    populate_friends(users, friendships)
    populate_shortest_paths(users)
    return users, friendships


# ── 1. populate_friends ──────────────────────────────────────────────


class TestPopulateFriends:
    def test_creates_friend_lists(self):
        users = _make_users(3)
        friendships = [(0, 1), (1, 2)]
        populate_friends(users, friendships)
        assert len(users[0]["friends"]) == 1
        assert len(users[1]["friends"]) == 2
        assert len(users[2]["friends"]) == 1

    def test_friends_are_symmetric(self):
        users = _make_users(3)
        populate_friends(users, [(0, 2)])
        assert users[2] in users[0]["friends"]
        assert users[0] in users[2]["friends"]

    def test_no_friendships(self):
        users = _make_users(2)
        populate_friends(users, [])
        assert users[0]["friends"] == []
        assert users[1]["friends"] == []


# ── 2. populate_shortest_paths ───────────────────────────────────────


class TestPopulateShortestPaths:
    def test_shortest_paths_populated(self, network):
        users, _ = network
        for user in users:
            assert "shortest_paths" in user
            assert len(user["shortest_paths"]) > 0

    def test_path_to_self_is_empty(self, network):
        users, _ = network
        for user in users:
            assert user["shortest_paths"][user["id"]] == [[]]

    def test_direct_friend_path_length_one(self, network):
        users, _ = network
        # 0 and 1 are directly connected
        paths_0_to_1 = users[0]["shortest_paths"][1]
        assert all(len(p) == 1 for p in paths_0_to_1)

    def test_indirect_path_length(self, network):
        users, _ = network
        # 0→2 via 1 has length 2
        paths_0_to_2 = users[0]["shortest_paths"][2]
        assert all(len(p) == 2 for p in paths_0_to_2)


# ── 3. populate_closeness ────────────────────────────────────────────


class TestPopulateCloseness:
    def test_closeness_populated(self, network):
        users, _ = network
        populate_closeness(users)
        for user in users:
            assert user["closeness_centrality"] > 0

    def test_closeness_center_higher(self):
        """In line 0-1-2, center node 1 has highest closeness."""
        users = _make_users(3)
        populate_friends(users, [(0, 1), (1, 2)])
        populate_shortest_paths(users)
        populate_closeness(users)
        assert users[1]["closeness_centrality"] > users[0]["closeness_centrality"]


# ── 4. populate_betweeness / populate_betweeness_v1 ──────────────────


class TestPopulateBetweeness:
    def test_betweenness_populated(self, network):
        users, _ = network
        populate_betweeness(users)
        centralities = [u["betweenness_centrality"] for u in users]
        assert any(c > 0 for c in centralities)

    def test_v1_matches_v0(self, network):
        users, _ = network
        populate_betweeness(users)
        vals = [u["betweenness_centrality"] for u in users]
        # reset and run v1
        for u in users:
            u["betweenness_centrality"] = 0.0
        populate_betweeness_v1(users)
        vals_v1 = [u["betweenness_centrality"] for u in users]
        assert vals == vals_v1

    def test_leaf_nodes_have_zero_betweenness(self):
        """In a simple line 0-1-2, node 1 has betweenness, 0 and 2 do not."""
        users = _make_users(3)
        populate_friends(users, [(0, 1), (1, 2)])
        populate_shortest_paths(users)
        populate_betweeness(users)
        assert users[0]["betweenness_centrality"] == 0.0
        assert users[2]["betweenness_centrality"] == 0.0
        assert users[1]["betweenness_centrality"] > 0


# ── 5. initialize_centrality ────────────────────────────────────────


class TestInitializeCentrality:
    def test_sets_to_zero(self):
        users = _make_users(3)
        for u in users:
            u["betweenness_centrality"] = 99.0
        initialize_centrality(users)
        for u in users:
            assert u["betweenness_centrality"] == 0.0


# ── 6. update_centrality ────────────────────────────────────────────


class TestUpdateCentrality:
    def test_updates_intermediate_nodes(self):
        users = _make_users(4)
        # path 0→1→2→3, contrib 0.5; only 1 and 2 are intermediate
        update_centrality([0, 1, 2, 3], 0.5, 0, 3, users)
        assert users[0]["betweenness_centrality"] == 0.0
        assert users[1]["betweenness_centrality"] == 0.5
        assert users[2]["betweenness_centrality"] == 0.5
        assert users[3]["betweenness_centrality"] == 0.0

    def test_no_intermediate_nodes(self):
        users = _make_users(2)
        update_centrality([0, 1], 1.0, 0, 1, users)
        assert users[0]["betweenness_centrality"] == 0.0
        assert users[1]["betweenness_centrality"] == 0.0


# ── 7. process_shortest_paths ────────────────────────────────────────


class TestProcessShortestPaths:
    def test_updates_centrality(self):
        users = _make_users(3)
        populate_friends(users, [(0, 1), (1, 2)])
        populate_shortest_paths(users)
        initialize_centrality(users)
        process_shortest_paths(users[0], users)
        # user 1 is on the path from 0→2
        assert users[1]["betweenness_centrality"] > 0

    def test_skips_lower_target_ids(self):
        """source_id < target_id guard: processing user 2 should not
        re-count paths to user 0."""
        users = _make_users(3)
        populate_friends(users, [(0, 1), (1, 2)])
        populate_shortest_paths(users)
        initialize_centrality(users)
        process_shortest_paths(users[2], users)
        # since source_id=2 is > all target_ids, nothing should change
        for u in users:
            assert u["betweenness_centrality"] == 0.0


# ── 8. construct_adjacency ──────────────────────────────────────────


class TestConstructAdjacency:
    def test_shape(self, network):
        users, friendships = network
        adj = construct_adjacency(users, friendships)
        assert len(adj) == 5
        assert all(len(row) == 5 for row in adj)

    def test_symmetric(self, network):
        users, friendships = network
        adj = construct_adjacency(users, friendships)
        for i in range(5):
            for j in range(5):
                assert adj[i][j] == adj[j][i]

    def test_diagonal_zero(self, network):
        users, friendships = network
        adj = construct_adjacency(users, friendships)
        for i in range(5):
            assert adj[i][i] == 0

    def test_known_edge(self, network):
        users, friendships = network
        adj = construct_adjacency(users, friendships)
        assert adj[0][1] == 1
        assert adj[0][4] == 0  # not directly connected


# ── 9. matrix utilities ─────────────────────────────────────────────


class TestMatrixUtilities:
    def test_vector_as_matrix(self):
        assert vector_as_matrix([1, 2, 3]) == [[1], [2], [3]]

    def test_vector_from_matrix(self):
        assert vector_from_matrix([[1], [2], [3]]) == [1, 2, 3]

    def test_roundtrip(self):
        v = [4, 5, 6]
        assert vector_from_matrix(vector_as_matrix(v)) == v

    def test_matrix_multiply_identity(self):
        identity = [[1, 0], [0, 1]]
        m = [[3, 4], [5, 6]]
        assert matrix_multiply(identity, m) == m

    def test_matrix_multiply_known(self):
        a = [[1, 2], [3, 4]]
        b = [[5, 6], [7, 8]]
        result = matrix_multiply(a, b)
        assert result == [[19, 22], [43, 50]]

    def test_matrix_multiply_incompatible(self):
        with pytest.raises(ArithmeticError):
            matrix_multiply([[1, 2]], [[1, 2]])

    def test_matrix_operate(self):
        m = [[1, 0], [0, 1]]
        v = [3, 4]
        assert matrix_operate(m, v) == [3, 4]

    def test_matrix_operate_scaling(self):
        m = [[2, 0], [0, 3]]
        v = [1, 1]
        assert matrix_operate(m, v) == [2, 3]

    def test_matrix_product_entry(self):
        a = [[1, 2], [3, 4]]
        b = [[5, 6], [7, 8]]
        assert matrix_product_entry(a, b, 0, 0) == 19
        assert matrix_product_entry(a, b, 1, 1) == 50


# ── 10. find_eigenvector ─────────────────────────────────────────────


class TestFindEigenvector:
    def test_returns_eigenvector_eigenvalue(self):
        m = [[2, 0], [0, 3]]
        vec, val = find_eigenvector(m)
        assert len(vec) == 2
        assert val > 0

    def test_dominant_eigenvalue(self):
        m = [[2, 0], [0, 3]]
        vec, val = find_eigenvector(m)
        assert abs(val - 3) < 0.01

    def test_eigenvector_is_unit(self):
        from dsl.c04_linear_algebra.e0401_vectors import magnitude

        m = [[4, 0], [0, 1]]
        vec, _ = find_eigenvector(m)
        assert abs(magnitude(vec) - 1.0) < 0.001


# ── 11. page_rank ────────────────────────────────────────────────────


class TestPageRank:
    def test_returns_all_users(self):
        users = _make_users(3)
        populate_friends(users, [(0, 1), (1, 2)])
        # set up endorsements for page_rank
        endorsements = [(0, 1), (1, 2)]
        populate_endorsments(users, endorsements)
        pr = page_rank(users)
        assert set(pr.keys()) == {0, 1, 2}

    def test_values_sum_to_one(self):
        users = _make_users(3)
        populate_friends(users, [(0, 1), (1, 2)])
        # all users must endorse someone for PR to be conserved
        endorsements = [(0, 1), (1, 2), (2, 0)]
        populate_endorsments(users, endorsements)
        pr = page_rank(users)
        assert abs(sum(pr.values()) - 1.0) < 0.01

    def test_endorsed_node_has_higher_rank(self):
        users = _make_users(3)
        populate_friends(users, [(0, 1), (1, 2)])
        endorsements = [(0, 1), (1, 2)]
        populate_endorsments(users, endorsements)
        pr = page_rank(users)
        # user 2 receives endorsement from 1, who receives from 0
        assert pr[2] > pr[0]


# ── 12. populate_endorsements / populate_endorsments ─────────────────


class TestEndorsements:
    def test_populate_endorsments_sets_fields(self):
        users = _make_users(3)
        endorsements = [(0, 1), (1, 2)]
        populate_endorsments(users, endorsements)
        assert len(users[0]["endorses"]) == 1
        assert len(users[1]["endorsed_by"]) == 1
        assert len(users[2]["endorsed_by"]) == 1

    def test_populate_endorsements_counts(self):
        users = _make_users(3)
        endorsements = [(0, 1), (0, 2), (1, 2)]
        populate_endorsments(users, endorsements)
        result = populate_endorsements(users)
        # result is list of (id, count)
        result_dict = dict(result)
        assert result_dict[0] == 0
        assert result_dict[1] == 1
        assert result_dict[2] == 2

    def test_populate_endorsments_returns_users(self):
        users = _make_users(2)
        result = populate_endorsments(users, [(0, 1)])
        assert result is users


# ── 13. farness ──────────────────────────────────────────────────────


class TestFarness:
    def test_farness_center_node(self):
        """In line 0-1-2, node 1 should have the smallest farness."""
        users = _make_users(3)
        populate_friends(users, [(0, 1), (1, 2)])
        populate_shortest_paths(users)
        assert farness(users[1]) < farness(users[0])

    def test_farness_isolated_self(self):
        """A single node with no friends has farness 0."""
        users = _make_users(1)
        populate_friends(users, [])
        populate_shortest_paths(users)
        assert farness(users[0]) == 0


# ── 14. logging functions (smoke tests) ─────────────────────────────


class TestLoggingFunctions:
    def test_get_page_ranks(self):
        get_page_ranks({0: 0.5, 1: 0.5})

    def test_get_closeness(self, network):
        users, _ = network
        populate_closeness(users)
        get_closeness(users)

    def test_get_betweeness(self, network):
        users, _ = network
        populate_betweeness(users)
        get_betweeness(users)

    def test_get_eigenvector_centrality(self):
        get_eigenvector_centrality([0.1, 0.2, 0.3])
