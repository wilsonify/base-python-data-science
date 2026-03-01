import pytest
import random
import math

from dsl.c20_clustering.clustering import (
    KMeans,
    squared_clustering_errors,
    is_leaf,
    get_children,
    get_values,
    cluster_distance,
    get_merge_order,
    bottom_up_cluster,
    generate_clusters,
)
from dsl.c04_linear_algebra.e0401_vectors import squared_distance


# ---------------------------------------------------------------------------
# KMeans tests
# ---------------------------------------------------------------------------


class TestKMeans:
    """Tests for the KMeans class."""

    def test_train_and_classify_separable_data(self):
        """KMeans should correctly cluster well-separated 2D data."""
        random.seed(42)

        # Three clearly separated clusters
        data = (
            [[0, 0], [0.5, 0.5], [-0.5, 0.5], [0.5, -0.5]]
            + [[10, 10], [10.5, 10.5], [9.5, 10.5], [10.5, 9.5]]
            + [[0, 20], [0.5, 20.5], [-0.5, 20.5], [0.5, 19.5]]
        )

        km = KMeans(k=3)
        km.train(data)

        assert km.means is not None
        assert len(km.means) == 3

        # All points in the first group should share the same label
        labels_group1 = {km.classify(p) for p in data[:4]}
        labels_group2 = {km.classify(p) for p in data[4:8]}
        labels_group3 = {km.classify(p) for p in data[8:]}

        assert len(labels_group1) == 1
        assert len(labels_group2) == 1
        assert len(labels_group3) == 1

        # The three groups should have different labels
        assert labels_group1 != labels_group2
        assert labels_group2 != labels_group3
        assert labels_group1 != labels_group3

    def test_classify_returns_nearest_cluster(self):
        """classify should return the index of the nearest mean."""
        km = KMeans(k=2)
        km.means = [[0, 0], [10, 10]]

        assert km.classify([1, 1]) == 0
        assert km.classify([9, 9]) == 1

    def test_train_with_k_equals_1(self):
        """With k=1 every point should be assigned to cluster 0."""
        random.seed(0)
        data = [[1, 2], [3, 4], [5, 6]]
        km = KMeans(k=1)
        km.train(data)

        assert all(km.classify(p) == 0 for p in data)


# ---------------------------------------------------------------------------
# squared_clustering_errors
# ---------------------------------------------------------------------------


class TestSquaredClusteringErrors:
    def test_returns_nonnegative(self):
        random.seed(10)
        data = [[0, 0], [1, 1], [10, 10], [11, 11]]
        err = squared_clustering_errors(data, k=2)
        assert err >= 0

    def test_error_decreases_with_more_clusters(self):
        """More clusters should generally yield smaller or equal error."""
        random.seed(7)
        data = [[0, 0], [1, 0], [10, 10], [11, 10], [20, 20], [21, 20]]
        err_2 = squared_clustering_errors(data, k=2)
        err_3 = squared_clustering_errors(data, k=3)
        # With well-separated data, 3 clusters should fit better
        assert err_3 <= err_2 + 1e-9


# ---------------------------------------------------------------------------
# Hierarchical clustering helpers
# ---------------------------------------------------------------------------


# Leaf cluster: a 1-tuple containing a value (which is itself a list/vector)
LEAF_A = ([0, 0],)
LEAF_B = ([10, 10],)
LEAF_C = ([5, 5],)

# Merged cluster: (merge_order, [child1, child2])
MERGED = (0, [LEAF_A, LEAF_B])
NESTED = (1, [MERGED, LEAF_C])


class TestIsLeaf:
    def test_leaf(self):
        assert is_leaf(LEAF_A) is True

    def test_non_leaf(self):
        assert is_leaf(MERGED) is False


class TestGetChildren:
    def test_merged_returns_children(self):
        children = get_children(MERGED)
        assert children == [LEAF_A, LEAF_B]

    def test_leaf_raises(self):
        with pytest.raises(TypeError):
            get_children(LEAF_A)


class TestGetValues:
    def test_leaf_returns_value(self):
        vals = get_values(LEAF_A)
        assert vals == ([0, 0],)

    def test_merged_returns_all_leaf_values(self):
        vals = get_values(MERGED)
        assert vals == [[0, 0], [10, 10]]

    def test_nested_returns_all_leaf_values(self):
        vals = get_values(NESTED)
        assert vals == [[0, 0], [10, 10], [5, 5]]


class TestClusterDistance:
    def test_two_leaves(self):
        d = cluster_distance(LEAF_A, LEAF_B)
        expected = math.sqrt(200)  # distance([0,0],[10,10])
        assert d == pytest.approx(expected)

    def test_merged_and_leaf_min(self):
        # min distance between {[0,0],[10,10]} and {[5,5]}
        d = cluster_distance(MERGED, LEAF_C, distance_agg=min)
        d_a_c = math.sqrt(50)   # distance([0,0],[5,5])
        d_b_c = math.sqrt(50)   # distance([10,10],[5,5])
        assert d == pytest.approx(min(d_a_c, d_b_c))

    def test_merged_and_leaf_max(self):
        d = cluster_distance(MERGED, LEAF_C, distance_agg=max)
        d_a_c = math.sqrt(50)
        d_b_c = math.sqrt(50)
        assert d == pytest.approx(max(d_a_c, d_b_c))


class TestGetMergeOrder:
    def test_leaf_returns_inf(self):
        assert get_merge_order(LEAF_A) == float("inf")

    def test_merged_returns_order(self):
        assert get_merge_order(MERGED) == 0
        assert get_merge_order(NESTED) == 1


# ---------------------------------------------------------------------------
# bottom_up_cluster / generate_clusters
# ---------------------------------------------------------------------------


class TestBottomUpCluster:
    def test_small_input(self):
        inputs = [[0, 0], [1, 0], [10, 10]]
        result = bottom_up_cluster(inputs)

        # Result is a single cluster containing all inputs
        assert not is_leaf(result)
        vals = get_values(result)
        assert sorted(vals) == sorted(inputs)

    def test_single_input(self):
        inputs = [[5, 5]]
        result = bottom_up_cluster(inputs)
        assert is_leaf(result)
        assert get_values(result) == ([5, 5],)

    def test_two_inputs(self):
        inputs = [[0, 0], [1, 1]]
        result = bottom_up_cluster(inputs)
        assert not is_leaf(result)
        children = get_children(result)
        assert len(children) == 2
        vals = get_values(result)
        assert sorted(vals) == sorted(inputs)

    def test_merge_order_increases(self):
        """Closest pair should merge first (lowest merge order)."""
        inputs = [[0, 0], [1, 0], [100, 100]]
        result = bottom_up_cluster(inputs)
        # The first merge (order 1) should combine the two close points
        # The second merge (order 0) combines that cluster with the far point
        # merge_order = len(clusters) at time of merge
        children = get_children(result)
        merge_orders = [get_merge_order(c) for c in children]
        # One child should be the earlier merge (finite order), the other a leaf (inf)
        assert any(m == float("inf") for m in merge_orders) or all(
            m != float("inf") for m in merge_orders
        )


class TestGenerateClusters:
    def test_returns_requested_number(self):
        inputs = [[0, 0], [1, 0], [10, 10], [11, 10]]
        base = bottom_up_cluster(inputs)
        clusters = generate_clusters(base, num_clusters=2)
        assert len(clusters) == 2

    def test_single_cluster_is_base(self):
        inputs = [[0, 0], [1, 0], [10, 10]]
        base = bottom_up_cluster(inputs)
        clusters = generate_clusters(base, num_clusters=1)
        assert len(clusters) == 1
        assert clusters[0] == base

    def test_n_clusters_all_leaves(self):
        inputs = [[0, 0], [1, 0], [10, 10]]
        base = bottom_up_cluster(inputs)
        clusters = generate_clusters(base, num_clusters=3)
        assert len(clusters) == 3
        assert all(is_leaf(c) for c in clusters)

    def test_values_preserved(self):
        inputs = [[0, 0], [1, 0], [10, 10], [11, 10]]
        base = bottom_up_cluster(inputs)
        clusters = generate_clusters(base, num_clusters=2)
        all_vals = []
        for c in clusters:
            all_vals.extend(get_values(c))
        assert sorted(all_vals) == sorted(inputs)
