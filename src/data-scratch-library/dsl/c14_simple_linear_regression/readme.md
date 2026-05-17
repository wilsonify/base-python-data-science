# Chapter 14 – Simple Linear Regression

Fit a straight line $y = \alpha + \beta x$ to data by minimising the sum of
squared errors. This is the simplest regression model and the foundation for
the multiple regression covered in Chapter 15.

## Key Concepts

### The Model

Given input $x$ and output $y$, assume a linear relationship:

$$y_i = \alpha + \beta x_i + \varepsilon_i$$

where $\varepsilon_i$ is the error (residual) for observation $i$.

### Least-Squares Solution

The closed-form values that minimise $\sum \varepsilon_i^2$ are:

$$\beta = r(x,y)\;\frac{\sigma_y}{\sigma_x}, \qquad \alpha = \bar{y} - \beta\,\bar{x}$$

where $r$ is the correlation and $\sigma$ the standard deviation.

### Coefficient of Determination ($R^2$)

$$R^2 = 1 - \frac{\text{sum of squared errors}}{\text{total sum of squares}}$$

- $R^2 = 0$ — model is no better than predicting the mean.
- $R^2 = 1$ — model explains all variation in $y$.

### Gradient Descent Alternative

The same parameters can be found iteratively by gradient descent on the squared
error loss — useful when a closed-form solution isn't available.

### Maximum Likelihood Justification

If errors are normally distributed ($\varepsilon \sim \mathcal{N}(0, \sigma^2)$),
minimising squared errors is equivalent to maximising the likelihood of the
observed data.

---

## Module API

### Prediction & Error

#### `predict(alpha, beta, x_i)`

Returns $\alpha + \beta x_i$.

#### `error(alpha, beta, x_i, y_i)`

Returns the residual $y_i - \text{predict}(\alpha, \beta, x_i)$.

### Fitting

#### `least_squares_fit(x, y)`

Returns `(alpha, beta)` that minimise the sum of squared errors (closed-form).

```python
from dsl.c14_simple_linear_regression.simple_linear_regression import least_squares_fit

alpha, beta = least_squares_fit(x, y)
```

### Evaluation

#### `sum_of_squared_errors(alpha, beta, x, y)`

Total squared residuals for the model on data `(x, y)`.

#### `total_sum_of_squares(y)`

Total squared deviation of `y` from its mean — the baseline the model must beat.

#### `r_squared(alpha, beta, x, y)`

Coefficient of determination ($R^2$).

```python
from dsl.c14_simple_linear_regression.simple_linear_regression import (
    least_squares_fit, r_squared,
)

alpha, beta = least_squares_fit(x, y)
r_squared(alpha, beta, x, y)  # e.g. 0.329
```

### Gradient Helpers

#### `squared_error(x_i, y_i, theta)`

Squared error for one point, where `theta = [alpha, beta]`.

#### `squared_error_gradient(x_i, y_i, theta)`

Gradient of the squared error w.r.t. `theta = [alpha, beta]`. Returns
`[d_alpha, d_beta]`.

---

## Example

See [e01_simple_linear_regression.py](e01_simple_linear_regression.py) for a
worked example fitting the friends-vs-daily-minutes dataset and evaluating with
$R^2$.

---

## Further Reading

- Continue to Chapter 15 for multiple regression.
