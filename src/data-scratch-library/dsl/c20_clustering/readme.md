# Chapter 20 – Clustering

Unsupervised learning algorithms that group data points by similarity: k-means
and bottom-up hierarchical clustering.

---

## Key Concepts

### k-Means Clustering

An iterative algorithm that partitions $n$ points into $k$ clusters:

1. Start with $k$ random cluster assignments.
2. Compute the mean (centroid) of each cluster.
3. Reassign every point to its nearest centroid.
4. Repeat steps 2–3 until assignments stop changing.

**Choosing k** — plot total squared error vs. k and look for the "elbow."

### Hierarchical (Bottom-Up) Clustering

1. Start with each point as its own cluster.
2. Repeatedly merge the two closest clusters.
3. Stop when only one cluster remains.

The merge history forms a dendrogram. Cut at any level to obtain the desired
number of clusters.

**Distance metrics** — the module supports min-linkage (default), max-linkage,
and average-linkage via a `distance_agg` parameter.

---

## Module API

### k-Means

| Name | Signature | Description |
|---|---|---|
| `KMeans` (class) | `KMeans(k)` | k-means clusterer |
| `.train` | `(inputs) → None` | Fit centroids to data |
| `.classify` | `(input) → int` | Return nearest cluster index |
| `squared_clustering_errors` | `(inputs, k) → float` | Total squared error for a given k |

### Hierarchical Clustering

| Name | Signature | Description |
|---|---|---|
| `Leaf` / `Merged` | NamedTuples | Cluster tree nodes |
| `is_leaf` | `(cluster) → bool` | Check if a cluster is a leaf |
| `get_children` | `(cluster) → list` | Children of a merged cluster |
| `get_values` | `(cluster) → list` | All point vectors in a cluster |
| `cluster_distance` | `(c1, c2, agg) → float` | Distance between two clusters |
| `get_merge_order` | `(cluster) → float` | Merge step number (inf for leaves) |
| `bottom_up_cluster` | `(inputs, agg) → Cluster` | Build full dendrogram |
| `generate_clusters` | `(base, num) → List[Cluster]` | Cut dendrogram into *num* clusters |

---

## Example

See [`e01_clustering.py`](e01_clustering.py) for meetup-location clustering and
colour quantisation of images.

---

## Further Reading

- [k-means – Wikipedia](https://en.wikipedia.org/wiki/K-means_clustering)
- [Hierarchical clustering – Wikipedia](https://en.wikipedia.org/wiki/Hierarchical_clustering)
- *Data Science from Scratch*, Chapter 20
