# Chapter 11 – Machine Learning

Foundational utilities for evaluating machine learning models: splitting data into
train/test sets and computing classification metrics.

## Key Concepts

### What Is Machine Learning?

Machine learning means creating models that are **learned from data** rather than
explicitly programmed. The goal is to use existing data to predict outcomes on new,
unseen data (e.g., spam detection, fraud detection).

Models fall into two broad categories:

- **Supervised** – trained on labeled data (known correct answers).
- **Unsupervised** – discovers structure without labels.

### Overfitting vs. Underfitting

| Problem        | Symptom                                     | Remedy                          |
|----------------|---------------------------------------------|---------------------------------|
| **Overfitting**  | Great on training data, poor on new data  | Reduce features, get more data  |
| **Underfitting** | Poor even on training data                | Add features, increase complexity |

The primary defense is to **evaluate on held-out data** the model has never seen.

### Bias-Variance Tradeoff

- **High bias** (underfitting) – model is too simple; add features.
- **High variance** (overfitting) – model is too complex; remove features or add data.

### Feature Extraction & Selection

Features are the inputs provided to a model. They typically fall into three types:

1. **Boolean** – yes/no (encoded as 1/0).
2. **Numeric** – continuous or discrete counts.
3. **Categorical** – one of a discrete set of options.

Too few features leads to underfitting. Too many leads to overfitting. Use domain
knowledge, dimensionality reduction, or regularization to find the right balance.

---

## Module API

### Data Splitting

#### `split_data(data, prob)`

Splits a list into two parts with fractions `[prob, 1 - prob]`.

```python
from dsl.c11_machine_learning.machine_learning import split_data

train, test = split_data(range(1000), 0.75)
```

#### `train_test_split(x, y, test_pct)`

Splits paired input/output lists into `(x_train, x_test, y_train, y_test)`,
keeping corresponding pairs together.

```python
from dsl.c11_machine_learning.machine_learning import train_test_split

x_train, x_test, y_train, y_test = train_test_split(xs, ys, 0.25)
```

> **Tip:** When comparing multiple models, use a three-way split –
> **train / validation / test** – so the test set is never used for model selection.

### Classification Metrics

All metric functions accept four confusion-matrix counts:
`tp` (true positives), `fp` (false positives), `fn` (false negatives), `tn` (true negatives).

| Function    | Formula                          | Meaning                                          |
|-------------|----------------------------------|--------------------------------------------------|
| `accuracy`  | (tp + tn) / total                | Fraction of all predictions that are correct      |
| `precision` | tp / (tp + fp)                   | Fraction of positive predictions that are correct |
| `recall`    | tp / (tp + fn)                   | Fraction of actual positives correctly identified |
| `f1_score`  | 2 * precision * recall / (p + r) | Harmonic mean of precision and recall             |

**Precision vs. Recall tradeoff:** Lowering the prediction threshold increases recall
but decreases precision (more false positives), and vice versa. `f1_score` provides a
single balanced measure.

```python
from dsl.c11_machine_learning.machine_learning import accuracy, precision, recall, f1_score

accuracy(70, 4930, 13930, 981070)   # 0.98114
precision(70, 4930, 13930, 981070)  # 0.014
recall(70, 4930, 13930, 981070)     # 0.005
```

> High accuracy alone can be misleading – always check precision and recall,
> especially with imbalanced classes.

---

## Further Reading

- *The Elements of Statistical Learning* – Friedman, Tibshirani & Hastie (free PDF).
- Coursera *Machine Learning* course – broad introduction to ML fundamentals.
