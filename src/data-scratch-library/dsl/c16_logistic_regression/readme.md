# Chapter 16 – Logistic Regression

A classification model that maps $\mathbf{x} \cdot \boldsymbol{\beta}$ through
the **sigmoid (logistic) function** to produce a probability in $(0, 1)$:

$$P(y=1 \mid \mathbf{x}) = \sigma(\mathbf{x} \cdot \boldsymbol{\beta}) = \frac{1}{1 + e^{-\mathbf{x} \cdot \boldsymbol{\beta}}}$$

## Key Concepts

### Why Not Linear Regression?

Linear regression can produce outputs outside $[0, 1]$ and violates the
exogeneity assumption when the target is binary. The logistic function keeps
predictions bounded and interpretable as probabilities.

### Maximum Likelihood Estimation

Parameters are chosen to **maximise the log-likelihood** (equivalently,
minimise the negative log-likelihood):

$$\ell(\boldsymbol{\beta}) = \sum_i \bigl[ y_i \ln \sigma(\mathbf{x}_i \cdot \boldsymbol{\beta}) + (1 - y_i) \ln(1 - \sigma(\mathbf{x}_i \cdot \boldsymbol{\beta})) \bigr]$$

### Interpreting Coefficients

Each $\beta_j$ shifts the log-odds by $\beta_j$ per unit increase in $x_j$.
The impact on probability depends on the current value of
$\mathbf{x} \cdot \boldsymbol{\beta}$ (non-linear effect).

### Support Vector Machines (aside)

The decision boundary $\mathbf{x} \cdot \boldsymbol{\beta} = 0$ is a
hyperplane. An SVM finds the hyperplane that maximises the margin to the nearest
points. The **kernel trick** maps data to higher dimensions where a separating
hyperplane may exist. SVMs require specialised solvers (e.g. LIBSVM).

---

## Module API

### Logistic Function

| Function | Description |
|----------|-------------|
| `logistic(x)` | Sigmoid $\sigma(x) = 1/(1+e^{-x})$, clamped for numerical stability. |
| `logistic_prime(x)` | Derivative $\sigma'(x) = \sigma(x)(1-\sigma(x))$. |

### Log-Likelihood

| Function | Description |
|----------|-------------|
| `logistic_log_likelihood_i(x_i, y_i, beta)` | Log-likelihood for one observation. |
| `logistic_log_likelihood(x, y, beta)` | Total log-likelihood over the dataset. |

### Gradient

| Function | Description |
|----------|-------------|
| `logistic_log_partial_ij(x_i, y_i, beta, j)` | Partial derivative w.r.t. $\beta_j$ for one observation. |
| `logistic_log_gradient_i(x_i, y_i, beta)` | Full gradient for one observation. |
| `logistic_log_gradient(x, y, beta)` | Total gradient over the dataset. |

### Fitting & Evaluation

#### `logistic_fit(x, y)`

Fits $\boldsymbol{\beta}$ via batch then stochastic gradient ascent on the
log-likelihood.

```python
from dsl.c16_logistic_regression.logistic_regression import logistic_fit, score_logistic

beta = logistic_fit(x_train, y_train)
precision, recall = score_logistic(beta, x_test, y_test)
```

#### `score_logistic(beta_hat, x_test, y_test)`

Returns `(precision, recall)` using a 0.5 probability threshold.

---

## Example

See [e01_logistic_regression.py](e01_logistic_regression.py) for a worked example
predicting paid vs. unpaid accounts from experience and salary.

---

## Further Reading

- [scikit-learn Logistic Regression](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression)
- [LIBSVM](https://www.csie.ntu.edu.tw/~cjlin/libsvm/) – SVM solver used by scikit-learn.
