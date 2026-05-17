# Chapter 17 – Decision Trees

Build classification trees from labelled data using the ID3 algorithm.

---

## Key Concepts

### What Is a Decision Tree?

A decision tree is a flowchart-like structure where each internal node tests an
attribute, each branch corresponds to a test outcome, and each leaf predicts a
class label. Trees are **interpretable**, handle mixed attribute types, and tolerate
missing values.

### Entropy & Information Gain

| Term | Definition |
|---|---|
| **Entropy** | $H = -\sum p_i \log_2 p_i$ — measures class uncertainty |
| **Partition entropy** | Weighted average of subset entropies after a split |
| **Information gain** | Reduction in entropy achieved by splitting on an attribute |

The ID3 algorithm greedily picks the attribute with the **lowest partition entropy**
(highest information gain) at each node.

### Overfitting & Random Forests

Decision trees easily overfit the training data. **Random forests** mitigate this by:

1. **Bootstrap aggregating (bagging)** — train each tree on a bootstrap sample.
2. **Random feature subsets** — at each split, consider only a random subset of
   remaining attributes.

Predictions are combined by majority vote (classification) or averaging (regression).

---

## Module API

### Types

| Name | Description |
|---|---|
| `DecisionTree` | `Union[Leaf, Split]` — recursive tree representation |
| `Leaf` | Terminal node holding a predicted value |
| `Split` | Internal node: attribute name, subtree dict, default value |

### Entropy Functions

| Function | Signature | Description |
|---|---|---|
| `entropy` | `(class_probabilities) → float` | Shannon entropy of a probability distribution |
| `get_class_probabilities` | `(labels) → List[float]` | Relative class frequencies |
| `data_entropy` | `(labeled_data) → float` | Entropy of a labelled dataset |
| `partition_entropy` | `(subsets) → float` | Weighted entropy across subsets |

### Partitioning

| Function | Signature | Description |
|---|---|---|
| `group_by` | `(items, key_fn) → Dict` | Group items by a key function |
| `partition_by` | `(inputs, attribute) → Dict` | Split inputs by an attribute value |
| `partition_entropy_by` | `(inputs, attribute, label_attribute) → float` | Entropy of a partition on a given attribute |

### Tree Operations

| Function | Signature | Description |
|---|---|---|
| `classify` | `(tree, inputs) → bool` | Walk the tree to produce a prediction |
| `build_tree_id3` | `(inputs, split_attributes, target_attribute) → DecisionTree` | Build a tree with the ID3 algorithm |
| `forest_classify` | `(trees, inputs) → bool` | Majority-vote prediction from multiple trees |

---

## Example

See [`e01_decision_trees.py`](e01_decision_trees.py) for a worked example that
builds a hiring-decision tree from candidate data.

---

## Further Reading

- [ID3 algorithm – Wikipedia](https://en.wikipedia.org/wiki/ID3_algorithm)
- [Random forest – Wikipedia](https://en.wikipedia.org/wiki/Random_forest)
- *Data Science from Scratch*, Chapter 17
