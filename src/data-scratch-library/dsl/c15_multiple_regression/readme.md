# Chapter 15 – Multiple Regression

Extends simple linear regression to multiple input variables:

$$y_i = \beta_0 + \beta_1 x_{i1} + \cdots + \beta_k x_{ik} + \varepsilon_i$$

By prepending a 1 to each input vector, this becomes $y = \mathbf{x} \cdot \boldsymbol{\beta}$.

## Key Concepts

### Model Assumptions

1. **Linear independence** – no input column is a weighted sum of others.
2. **Exogeneity** – input columns are uncorrelated with the errors $\varepsilon$.

Violating (1) makes $\beta$ unidentifiable; violating (2) biases the estimates.

### Fitting via Gradient Descent

Parameters are estimated by minimising the sum of squared errors using
stochastic gradient descent (no closed-form solution is implemented here).

### Interpreting Coefficients

Each $\beta_j$ is an **all-else-being-equal** effect: the change in $y$ for a
one-unit increase in $x_j$, holding all other variables constant.

### Goodness of Fit ($R^2$)

$$R^2 = 1 - \frac{\text{SSE}}{\text{TSS}}$$

Adding variables always increases $R^2$, so use standard errors and p-values to
check whether each coefficient is meaningfully different from zero.

### Bootstrap Inference

Resample the dataset with replacement, re-fit $\beta$ many times, and use the
spread of the bootstrap estimates as standard errors. Then compute p-values to
test whether each $\beta_j = 0$.

### Regularisation

| Method   | Penalty                                     | Effect                                |
|----------|---------------------------------------------|---------------------------------------|
| **Ridge** (L2) | $\alpha \sum \beta_j^2$              | Shrinks all coefficients toward zero  |
| **Lasso** (L1) | $\alpha \sum \lvert\beta_j\rvert$    | Forces some coefficients exactly to zero |

> Always rescale features before regularising so penalties are comparable.

---

## Module API

### Prediction & Error

| Function | Description |
|----------|-------------|
| `predict(x_i, beta)` | Returns $\mathbf{x}_i \cdot \boldsymbol{\beta}$ (first element of $x_i$ should be 1). |
| `error(x_i, y_i, beta)` | Residual $y_i - \hat{y}_i$. |
| `squared_error(x_i, y_i, beta)` | Squared residual. |
| `squared_error_gradient(x_i, y_i, beta)` | Gradient of squared error w.r.t. $\beta$. |

### Fitting & Evaluation

#### `estimate_beta(x, y)`

Estimates $\beta$ via stochastic gradient descent.

```python
from dsl.c15_multiple_regression.multiple_regression import estimate_beta

beta = estimate_beta(x, y)
```

#### `multiple_r_squared(x, y, beta)`

Returns the coefficient of determination ($R^2$) for the fitted model.

### Bootstrap

#### `bootstrap_sample(data)`

Returns a resample of `data` (same length, with replacement).

#### `bootstrap_statistic(data, stats_fn, num_samples)`

Applies `stats_fn` to `num_samples` bootstrap resamples.

#### `estimate_sample_beta(sample)`

Fits $\beta$ from a bootstrap sample of `(x_i, y_i)` pairs.

#### `p_value(beta_hat_j, sigma_hat_j)`

Two-sided p-value testing $H_0\!: \beta_j = 0$ (normal approximation).

### Ridge Regression

| Function | Description |
|----------|-------------|
| `ridge_penalty(beta, alpha)` | L2 penalty (excludes intercept). |
| `squared_error_ridge(x_i, y_i, beta, alpha)` | Squared error + ridge penalty. |
| `ridge_penalty_gradient(beta, alpha)` | Gradient of the L2 penalty. |
| `squared_error_ridge_gradient(x_i, y_i, beta, alpha)` | Combined gradient. |
| `estimate_beta_ridge(x, y, alpha)` | Fit with ridge regularisation. |

### Lasso

#### `lasso_penalty(beta, alpha)`

L1 penalty (excludes intercept). Not solved via gradient descent here.

---

## Example

See [e01_multiple_regression.py](e01_multiple_regression.py) for a worked example
fitting friends, work hours, and PhD status to daily minutes on site.

---

## Further Reading

- [scikit-learn `linear_model`](https://scikit-learn.org/stable/modules/linear_model.html) — `LinearRegression`, `Ridge`, `Lasso`.
- [Statsmodels OLS](https://www.statsmodels.org/stable/regression.html) — full inference with standard errors and p-values.
