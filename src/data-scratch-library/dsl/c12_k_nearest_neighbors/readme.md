# Chapter 12 – k-Nearest Neighbors

A simple, assumption-free classification algorithm: predict a label by letting the
*k* closest labeled points vote.

## Key Concepts

### How It Works

1. Compute the distance from the new point to every labeled point.
2. Select the *k* closest neighbors.
3. Return the most common label among those neighbors (majority vote).

**Requirements:** a distance metric and the assumption that nearby points are similar.

### Choosing *k*

| *k* too small | *k* too large |
|---------------|---------------|
| Sensitive to outliers / noise | Washes out local structure; tends toward predicting the overall most-common class |

Use a validation set (or cross-validation) to pick a good *k*.

### Tie-Breaking

When the top vote is tied, this implementation **drops the farthest neighbor** and
re-votes recursively until a unique winner emerges.

### The Curse of Dimensionality

In high-dimensional spaces:

- Points become roughly equidistant, so "nearest" loses meaning.
- Data is sparse — exponentially more samples are needed for coverage.

**Mitigation:** apply dimensionality reduction before running kNN.

---

## Module API

### Types

`LabeledPoint` — a `Tuple[List[float], str]` pairing a feature vector with its label.

### Voting

#### `raw_majority_vote(labels)`

Returns the most common label. Ties are broken arbitrarily.

#### `majority_vote(labels)`

Returns the most common label. On a tie, drops the last (farthest) label and
retries recursively. **Labels must be ordered nearest → farthest.**

### Classification

#### `knn_classify(k, labeled_points, new_point)`

Classifies `new_point` by majority vote of its `k` nearest neighbors.

```python
from dsl.c12_k_nearest_neighbors.nearest_neighbors import knn_classify

labeled = [([0, 0], "a"), ([1, 1], "b"), ([0, 1], "a")]
knn_classify(3, labeled, [0.5, 0.5])  # "a"
```

### Curse-of-Dimensionality Helpers

#### `random_point(dim)`

Returns a random point uniformly sampled from the `dim`-dimensional unit cube.

#### `random_distances(dim, num_pairs)`

Returns distances between `num_pairs` random point pairs in `dim` dimensions —
useful for visualizing how distance distributions change with dimensionality.

---

## Example: Iris Dataset

The classic Iris dataset (150 flowers, 4 measurements, 3 species) is used to
demonstrate kNN. See [e01_nearest_neighbors.py](e01_nearest_neighbors.py) and
[data.py](data.py) for the full worked example.

---

## Further Reading

- [scikit-learn Nearest Neighbors](https://scikit-learn.org/stable/modules/neighbors.html)
