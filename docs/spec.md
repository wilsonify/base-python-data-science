# Specification: base-python-data-science

**Version:** 1.0.0  
**Status:** Draft  
**Date:** 2026-02-28  
**Authors:** Derived from *Data Science from Scratch* by Joel Grus  
**License:** See repository LICENSE  

---

## Table of Contents

1. [Introduction](#1-introduction)  
2. [Repository Architecture](#2-repository-architecture)  
3. [Core Library Specification](#3-core-library-specification)  
4. [Dependency Policy](#4-dependency-policy)  
5. [Build & Installation Specification](#5-build--installation-specification)  
6. [Testing Specification](#6-testing-specification)  
7. [REST API Specification](#7-rest-api-specification)  
8. [Messaging Consumer Specification](#8-messaging-consumer-specification)  
9. [Cross-Language Port Specification](#9-cross-language-port-specification)  
10. [Coding Standards](#10-coding-standards)  
11. [CI/CD Requirements](#11-cicd-requirements)  
12. [Non-Functional Requirements](#12-non-functional-requirements)  
13. [Roadmap](#13-roadmap)  

---

## 1. Introduction

### 1.1 Purpose

This document defines the formal specification for **base-python-data-science**, an
educational data science system implementing core algorithms from first principles
with minimal external dependencies. The system provides:

- A self-contained core library of data science algorithms.
- Multiple language ports demonstrating cross-language algorithmic equivalence.
- Multiple transport layers (REST, message queue, pub/sub) exposing core
  algorithms as services.
- A visualization layer separated from algorithmic logic.
- A data ingestion layer separated from algorithmic logic.

### 1.2 Educational Philosophy

The following principles govern every design decision:

| Principle | Description |
| ----------- | ------------- |
| **Mathematical Transparency** | Every algorithm SHALL be implemented in terms of explicit mathematical operations. No opaque library calls SHALL replace fundamental computations. |
| **Minimal Abstraction** | Abstractions SHALL exist only where they reduce duplication without hiding mathematical intent. |
| **Readable over Clever** | Implementations SHALL favor clarity over optimization. A reader with introductory linear algebra and statistics knowledge SHALL be able to follow every function. |
| **Learn by Building** | Each module SHALL be independently understandable as a teaching unit corresponding to a chapter of study. |

### 1.3 Non-Goals

The following are explicitly **NOT** goals of this project:

- Production-grade performance optimization.
- Replacement of established numerical or machine learning ecosystems.
- Support for GPU-accelerated computation.
- Real-time or low-latency serving.
- Enterprise authentication, authorization, or multi-tenancy.

### 1.4 Architectural Principles

All implementations across all languages and transport layers SHALL adhere to:

1. **Minimal External Dependencies** — The core library SHALL depend only on the
   base language runtime and standard library.
2. **Deterministic Execution** — Given identical inputs, every pure function SHALL
   produce identical outputs across invocations and across language ports.
3. **Explicit Data Transformations** — Data SHALL flow through explicit function
   parameters and return values. No implicit mutation of shared state is permitted.
4. **Functional-First Design** — Functions SHALL be pure where possible.
   Side-effecting operations (I/O, randomness) SHALL be isolated at system
   boundaries and clearly documented.
5. **No Hidden Global State** — Module-level mutable state is prohibited in the
   core library. Configuration SHALL be passed explicitly via parameters or
   dedicated configuration objects.

---

## 2. Repository Architecture

### 2.1 Folder Responsibilities

| Folder | Layer | Description |
| -------- | ------- | ------------- |
| `data-scratch-library` | **Core** | Canonical implementation of all algorithms in the primary dynamic language. This is the single source of truth for algorithmic behavior. |
| `data-scratch-matplotlib` | **Extension — Visualization** | Visualization layer. Depends on core. MAY depend on a plotting library. SHALL NOT contain algorithmic logic. |
| `data-scratch-scrape` | **Extension — Ingestion** | Data acquisition layer. Depends on core. MAY depend on HTTP and HTML parsing libraries. SHALL NOT contain algorithmic logic. |
| `data-scratch-cpp-library` | **Port — Systems Language** | Behavioral port of core algorithms to a statically-typed, compiled systems language. |
| `data-scratch-node-library` | **Port — Typed Scripting** | Behavioral port of core algorithms to a typed scripting language runtime. |
| `data-scratch-amqp` | **Transport — Message Queue** | Message-queue consumer that dispatches incoming messages to core library functions and publishes results. |
| `data-scratch-mqtt` | **Transport — Pub/Sub** | Pub/sub consumer that dispatches incoming messages to core library functions and publishes results. |
| `rest-scratch-flask` | **Transport — REST (Dynamic)** | REST API server implemented in the primary dynamic language. |
| `rest-scratch-node-express` | **Transport — REST (Scripting)** | REST API server implemented in a scripting language runtime. |
| `rest-scratch-pistache` | **Transport — REST (Systems)** | REST API server implemented in a compiled systems language. |
| `rest-scratch-rust` | **Transport — REST (Memory-Safe Systems)** | REST API server implemented in a memory-safe compiled systems language. |
| `rest-client-ts-node` | **Client** | Typed REST client implementation generated from the shared API contract. |

### 2.2 Core vs. Extension Boundary

```txt
┌─────────────────────────────────────────────────────────────────────────┐
│                          CORE BOUNDARY                                  │
│                                                                         │
│   data-scratch-library                                                  │
│   ┌────────────────────────────────────────────────────────────────┐    │
│   │  Linear Algebra   Statistics   Probability   Optimization      │    │
│   │  Supervised Learning   Unsupervised Learning   Data Utilities  │    │
│   └────────────────────────────────────────────────────────────────┘    │
│                                                                         │
│   RULES:                                                                │
│   • Zero external dependencies beyond the language runtime              │
│   • No I/O operations                                                   │
│   • No network calls                                                    │
│   • No file system access                                               │
│   • Deterministic output for deterministic input                        │
└─────────────────────────────────────────────────────────────────────────┘
         │                    │                      │
         ▼                    ▼                      ▼
┌─────────────┐   ┌─────────────────┐   ┌─────────────────────┐
│ Viz Layer   │   │ Ingestion Layer │   │ Language Ports      │
│ (matplotlib)│   │ (scrape)        │   │ (cpp, node)         │
└─────────────┘   └─────────────────┘   └─────────────────────┘
                                                  │
                          ┌───────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                        TRANSPORT LAYER                                  │
│                                                                         │
│   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐                │
│   │ REST     │  │ REST     │  │ REST     │  │ REST     │                │
│   │ Dynamic  │  │ Scripting│  │ Systems  │  │ Mem-Safe │                │
│   └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘                │
│        │              │              │              │                   │
│   ┌────┴─────┐  ┌─────┴────┐                                            │
│   │ Msg Queue│  │ Pub/Sub  │                                            │
│   │ Consumer │  │ Consumer │                                            │
│   └──────────┘  └──────────┘                                            │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────┐
│ Typed Client    │
│ (rest-client)   │
└─────────────────┘
```

### 2.3 Architecture Diagram

```txt
                        ┌────────────────────┐
                        │   Core Library     │
                        │   (Pure Algorithms)│
                        └────────┬───────────┘
                                 │
               ┌─────────────────┼─────────────────┐
               │                 │                 │
               ▼                 ▼                 ▼
     ┌─────────────────┐ ┌────────────┐  ┌──────────────────┐
     │ Language Ports  │ │ Viz Layer  │  │ Ingestion Layer  │
     │ (Systems, TS)   │ │ (Plotting) │  │ (HTTP, Parsing)  │
     └────────┬────────┘ └────────────┘  └──────────────────┘
              │
     ┌────────┴────────────────────────────┐
     │         Transport Adapters          │
     │                                     │
     │  ┌─────────┐ ┌────────┐ ┌────────┐  │
     │  │  REST   │ │  MQ    │ │ PubSub │  │
     │  │ Servers │ │Consumer│ │Consumer│  │
     │  └────┬────┘ └────────┘ └────────┘  │
     └───────┼─────────────────────────────┘
             │
             ▼
     ┌───────────────┐
     │  REST Clients │
     └───────────────┘
```

### 2.4 Transport Abstraction

All transport layers SHALL adhere to the following contract:

1. **Incoming payload** — Deserialized into language-native data structures
   before being passed to core functions.
2. **Core invocation** — The transport layer SHALL call core library functions
   with deserialized, validated arguments. The transport layer SHALL NOT
   implement algorithmic logic.
3. **Outgoing payload** — Core function return values SHALL be serialized into
   the transport-specific format before transmission.
4. **Error propagation** — Errors raised by the core library SHALL be caught by
   the transport layer and translated into transport-appropriate error responses
   (see §7.5 and §8.4).

### 2.5 Service Boundary Rules

- Each transport module SHALL be independently deployable.
- Transport modules SHALL NOT depend on each other.
- Transport modules SHALL depend on exactly one core library (or its language port).
- Transport modules SHALL NOT expose internal data structures of the core library
  in their public API; they SHALL define their own request/response schemas.

### 2.6 Serialization Format

- All inter-service communication SHALL use a structured, text-based,
  language-agnostic serialization format (e.g., key-value pair notation).
- The serialization format SHALL support: null, boolean, integer, floating-point
  number, string, ordered list, and string-keyed map.
- Floating-point numbers SHALL be serialized with sufficient precision to
  preserve at least 10 significant decimal digits.
- Date/time values, if used, SHALL be represented as strings in ISO 8601 format.

### 2.7 Error Modeling Consistency

All layers SHALL represent errors as structured objects containing at minimum:

| Field | Type | Required | Description |
| ----- | ---- | -------- | ----------- |
| `code` | string | YES | Machine-readable error identifier |
| `message` | string | YES | Human-readable error description |
| `details` | any | NO | Additional context (input values, constraints violated) |

Error codes SHALL be consistent across all transport layers and language ports
for equivalent failure conditions.

---

## 3. Core Library Specification

The core library is organized into modules corresponding to chapters of study.
Each module SHALL satisfy the contracts defined below.

### 3.1 Linear Algebra

**Module Identifier:** `c04_linear_algebra`

#### 3.1.1 Type Definitions

| Type | Definition |
| ---- | ---------- |
| `Vector` | An ordered sequence of floating-point numbers. |
| `Matrix` | An ordered sequence of `Vector` values where all vectors have equal length. |

#### 3.1.2 Required Functions — Vector Operations

| Function | Signature | Description |
| ---------- | ----------- | ------------- |
| `vector_add` | `(Vector, Vector) → Vector` | Element-wise addition. Inputs MUST have equal length. |
| `vector_subtract` | `(Vector, Vector) → Vector` | Element-wise subtraction. Inputs MUST have equal length. |
| `vector_sum` | `(List[Vector]) → Vector` | Element-wise sum of a list of vectors. All MUST have equal length. |
| `scalar_multiply` | `(Scalar, Vector) → Vector` | Multiply each element by a scalar. |
| `vector_mean` | `(List[Vector]) → Vector` | Element-wise arithmetic mean. |
| `dot` | `(Vector, Vector) → Scalar` | Inner product. Inputs MUST have equal length. |
| `sum_of_squares` | `(Vector) → Scalar` | Sum of squared elements; equivalent to `dot(v, v)`. |
| `magnitude` | `(Vector) → Scalar` | Euclidean norm; square root of `sum_of_squares`. |
| `squared_distance` | `(Vector, Vector) → Scalar` | Sum of squared element-wise differences. |
| `distance` | `(Vector, Vector) → Scalar` | Euclidean distance; square root of `squared_distance`. |

#### 3.1.3 Required Functions — Matrix Operations

| Function | Signature | Description |
| ---------- | ----------- | ------------- |
| `shape` | `(Matrix) → (int, int)` | Returns (rows, columns). |
| `get_row` | `(Matrix, int) → Vector` | Returns the i-th row. |
| `get_column` | `(Matrix, int) → Vector` | Returns the j-th column. |
| `make_matrix` | `(int, int, Callable) → Matrix` | Constructs a matrix using a generator function `f(i, j)`. |
| `identity_matrix` | `(int) → Matrix` | Returns the n×n identity matrix via `make_matrix`. |

#### 3.1.4 Contracts

- **Dimension mismatch** — Functions accepting two vectors SHALL raise a
  descriptive error if lengths differ.
- **Empty input** — `vector_sum([])` and `vector_mean([])` SHALL raise a
  descriptive error.
- **Determinism** — All functions are pure; identical inputs SHALL produce
  identical outputs.
- **Numerical precision** — Results SHALL be accurate to within 1e-10 of the
  mathematically exact result for inputs whose absolute values do not exceed
  1e+6.

#### 3.1.5 Complexity Expectations

| Function | Time Complexity | Space Complexity |
| ---------- | ---------------- | ----------------- |
| `vector_add` | O(n) | O(n) |
| `dot` | O(n) | O(1) |
| `shape` | O(1) | O(1) |
| `make_matrix` | O(n×m) | O(n×m) |

---

### 3.2 Statistics

**Module Identifier:** `c05_statistics`

#### 3.2.1 Required Functions — Central Tendency

| Function | Signature | Description |
| ---------- | ----------- | ------------- |
| `mean` | `(Vector) → Scalar` | Arithmetic mean. |
| `median` | `(Vector) → Scalar` | Middle value; average of two middle values for even-length input. |
| `quantile` | `(Vector, Scalar) → Scalar` | p-th quantile where 0 ≤ p ≤ 1. |
| `mode` | `(Vector) → List[Scalar]` | Most frequently occurring value(s). |

#### 3.2.2 Required Functions — Dispersion

| Function | Signature | Description |
| ---------- | ----------- | ------------- |
| `data_range` | `(Vector) → Scalar` | Difference between maximum and minimum. |
| `variance` | `(Vector) → Scalar` | Population or sample variance (document which). |
| `standard_deviation` | `(Vector) → Scalar` | Square root of variance. |
| `interquartile_range` | `(Vector) → Scalar` | Difference between 75th and 25th percentiles. |

#### 3.2.3 Required Functions — Correlation

| Function | Signature | Description |
| ---------- | ----------- | ------------- |
| `covariance` | `(Vector, Vector) → Scalar` | Sample covariance. |
| `correlation` | `(Vector, Vector) → Scalar` | Pearson correlation coefficient in [-1, 1]. |

#### 3.2.4 Required Data Structures

| Structure | Description |
| ----------- | ------------- |
| `Bucket` | Represents a histogram bucket with boundary and count fields. Supports construction from raw data. |

#### 3.2.5 Contracts

- **Single-element input** — `variance` and `standard_deviation` of a
  single-element vector SHALL return 0 or raise an error (document which).
- **Zero standard deviation** — `correlation` SHALL handle the case where one or
  both inputs have zero standard deviation without producing NaN or infinity;
  it SHALL return 0 or raise a descriptive error.
- **Determinism** — All functions are pure.
- **Numerical precision** — `correlation` SHALL return values in the closed
  interval [-1, 1]. Values outside this range due to floating-point error
  SHALL be clamped.

---

### 3.3 Probability

**Module Identifier:** `c06_probability`

#### 3.3.1 Required Functions — Continuous Distributions

| Function | Signature | Description |
| ---------- | ----------- | ------------- |
| `uniform_pdf` | `(Scalar) → Scalar` | Probability density of the continuous uniform distribution on [0, 1]. |
| `uniform_cdf` | `(Scalar) → Scalar` | Cumulative distribution function of the uniform distribution. |
| `normal_pdf` | `(Scalar, Scalar?, Scalar?) → Scalar` | PDF of the normal distribution with optional mean (default 0) and standard deviation (default 1). |
| `normal_cdf` | `(Scalar, Scalar?, Scalar?) → Scalar` | CDF of the normal distribution. |
| `inverse_normal_cdf` | `(Scalar, Scalar?, Scalar?, Scalar?) → Scalar` | Inverse CDF (quantile function) via binary search. Tolerance parameter controls precision. |
| `bernoulli_trial` | `(Scalar) → int` | Returns 1 with probability p, 0 otherwise. |
| `binomial` | `(int, Scalar) → int` | Sum of n Bernoulli trials with probability p. |

#### 3.3.2 Required Functions — Conditional Probability

| Function | Signature | Description |
| ---------- | ----------- | ------------- |
| `random_kid` | `() → enum` | Returns a random gender label. |
| `conditional_probability_demo` | `(int) → dict` | Monte Carlo estimation of conditional probabilities for the "two children" problem. |

#### 3.3.3 Contracts

- **Domain validation** — `inverse_normal_cdf` SHALL reject inputs outside (0, 1).
- **Standard deviation** — Functions accepting standard deviation SHALL reject
  non-positive values.
- **Output bounds** — `uniform_cdf` and `normal_cdf` SHALL return values in [0, 1].
- **Convergence** — `inverse_normal_cdf` SHALL converge to within the specified
  tolerance. Default tolerance SHALL be at most 1e-5.
- **Stochastic functions** — `bernoulli_trial`, `binomial`, and
  `random_kid` are stochastic. They SHALL accept an optional random seed
  parameter or use an explicitly-passed random number generator to enable
  reproducible testing.

---

### 3.4 Optimization (Gradient Descent)

**Module Identifier:** `c08_gradient_descent`

#### 3.4.1 Required Functions

| Function | Signature | Description |
| ---------- | ----------- | ------------- |
| `difference_quotient` | `(Callable, Scalar, Scalar) → Scalar` | Numerical approximation of the derivative using the difference quotient. |
| `partial_difference_quotient` | `(Callable, Vector, int, Scalar) → Scalar` | Partial derivative with respect to the i-th variable. |
| `estimate_gradient` | `(Callable, Vector, Scalar) → Vector` | Gradient estimate via partial difference quotients. |
| `gradient_step` | `(Vector, Vector, Scalar) → Vector` | `v + step_size * gradient`. |
| `linear_gradient` | `(Scalar, Scalar, Scalar, Scalar) → (Scalar, Scalar)` | Gradient of squared error for a linear model. |
| `minibatch` | `(Iterable, int, bool?) → Iterator` | Yields minibatches from a dataset. Optional shuffle with explicit seed. |
| `minimize_batch` | `(Callable, Callable, Vector, Scalar?) → Vector` | Batch gradient descent to minimize a target function. |
| `minimize_stochastic` | `(Callable, Callable, Iterable, Iterable, Vector, Scalar?) → Vector` | Stochastic gradient descent. |

#### 3.4.2 Required Decorators / Wrappers

| Name | Description |
| ------ | ------------- |
| `safe` | Wraps a function so that domain errors return positive infinity instead of raising exceptions. |
| `negate` | Returns a function that negates the output of the wrapped function. |
| `negate_all` | Returns a function that negates all elements of a vector-valued function. |

#### 3.4.3 Contracts

- **Step size** — `gradient_step` SHALL NOT modify its input vectors.
- **Convergence** — `minimize_batch` SHALL terminate when the improvement
  between iterations falls below a configurable tolerance, or when a maximum
  iteration count is reached.
- **Reproducibility** — When shuffle is enabled, `minibatch` SHALL accept a
  random seed to produce deterministic orderings.
- **Numerical stability** — `safe` SHALL return positive infinity (not NaN) on
  domain errors.

---

### 3.5 Supervised Learning Primitives

This section covers modules that implement supervised learning algorithms.

#### 3.5.1 Machine Learning Utilities — `c11_machine_learning`

| Function | Signature | Description |
| ---------- | ----------- | ------------- |
| `train_test_split` | `(Dataset, Scalar, int?) → (Dataset, Dataset)` | Splits data into training and test sets at the given ratio. Optional seed for reproducibility. |
| `accuracy` | `(int, int, int, int) → Scalar` | (TP + TN) / total from a confusion matrix. |
| `precision` | `(int, int, int, int) → Scalar` | TP / (TP + FP). Returns 0 when denominator is 0. |
| `recall` | `(int, int, int, int) → Scalar` | TP / (TP + FN). Returns 0 when denominator is 0. |
| `f1_score` | `(int, int, int, int) → Scalar` | Harmonic mean of precision and recall. Returns 0 when both are 0. |

**Contracts:**

- **Zero-division** — Metrics SHALL return 0 (not NaN or error) when the
  denominator is zero.
- **Range** — All metric values SHALL be in [0, 1].
- **Split reproducibility** — `train_test_split` SHALL produce identical splits
  for identical seeds.

#### 3.5.2 K-Nearest Neighbors — `c12_k_nearest_neighbors`

| Function | Signature | Description |
| ---------- | ----------- | ------------- |
| `knn_classify` | `(int, LabeledPoints, Vector) → Label` | Classifies a point by majority vote of its k nearest neighbors. |
| `majority_vote` | `(List[Label]) → Label` | Returns the most common label, breaking ties deterministically. |

**Contracts:**

- **k validation** — k SHALL be a positive integer not exceeding the dataset size.
- **Tie-breaking** — `majority_vote` SHALL break ties deterministically (e.g.,
  lexicographic order of labels).
- **Distance metric** — SHALL use Euclidean distance as defined in §3.1.

#### 3.5.3 Naive Bayes — `c13_naive_bayes`

| Operation | Description |
| ----------- | ------------- |
| `train` | Accepts labeled text documents; computes per-class word probabilities with Laplace smoothing. |
| `classify` | Accepts a text document; returns the class label with the highest posterior log-probability. |

**Contracts:**

- **Smoothing** — Laplace smoothing constant SHALL be configurable, defaulting to a value that prevents zero probabilities.
- **Numerical stability** — Classification SHALL operate in log-space to prevent underflow.
- **Tokenization** — The tokenization function SHALL be configurable and SHALL default to case-insensitive word-boundary splitting.

#### 3.5.4 Simple Linear Regression — `c14_simple_linear_regression`

| Function | Signature | Description |
| ---------- | ----------- | ------------- |
| `least_squares_fit` | `(Vector, Vector) → (Scalar, Scalar)` | Returns (alpha, beta) minimizing sum of squared residuals. |
| `predict` | `(Scalar, Scalar, Scalar) → Scalar` | Returns `alpha + beta * x`. |
| `r_squared` | `(Scalar, Scalar, Vector, Vector) → Scalar` | Coefficient of determination. |

#### 3.5.5 Multiple Regression — `c15_multiple_regression`

| Function | Signature | Description |
| ---------- | ----------- | ------------- |
| `predict` | `(Vector, Vector) → Scalar` | Dot product of feature vector and coefficient vector. |
| `error` | `(Vector, Scalar, Vector) → Scalar` | Residual: predicted minus actual. |
| `least_squares_fit` | `(Matrix, Vector) → Vector` | Coefficient vector minimizing squared error via gradient descent. |

#### 3.5.6 Logistic Regression — `c16_logistic_regression`

| Function | Signature | Description |
| ---------- | ----------- | ------------- |
| `logistic` | `(Scalar) → Scalar` | Sigmoid function: $\sigma(x) = \frac{1}{1 + e^{-x}}$. |
| `logistic_log_likelihood` | `(Vector, Scalar, Vector) → Scalar` | Log-likelihood for a single data point. |
| `logistic_log_gradient` | `(Vector, Scalar, Vector) → Vector` | Gradient of the log-likelihood. |

**Contracts:**

- `logistic` SHALL return values in the open interval (0, 1).
- For very large positive inputs, `logistic` SHALL return a value indistinguishable from 1.0 within floating-point precision (no overflow).
- For very large negative inputs, `logistic` SHALL return a value indistinguishable from 0.0 within floating-point precision (no underflow to exactly 0 causing log-domain errors).

#### 3.5.7 Decision Trees — `c17_decision_trees`

| Function | Signature | Description |
| ---------- | ----------- | ------------- |
| `entropy` | `(List[Scalar]) → Scalar` | Shannon entropy: $H = -\sum p_i \log_2 p_i$. |
| `class_probabilities` | `(List[Label]) → List[Scalar]` | Relative frequencies of each class. |
| `data_entropy` | `(List[Label]) → Scalar` | Entropy of a labeled dataset. |
| `partition_entropy` | `(List[List[Label]]) → Scalar` | Weighted average entropy of a partition. |
| `build_tree` | `(Dataset) → TreeNode` | Recursively builds a decision tree by minimizing partition entropy. |
| `classify` | `(TreeNode, DataPoint) → Label` | Classifies a data point by traversing the tree. |

#### 3.5.8 Neural Networks — `c18_neural_networks`

| Function | Signature | Description |
| ---------- | ----------- | ------------- |
| `neuron_output` | `(Vector, Vector) → Scalar` | Applies activation function to the dot product of weights and inputs. |
| `feed_forward` | `(Network, Vector) → Vector` | Propagates input through a multi-layer network. |
| `backpropagate` | `(Network, Vector, Vector) → Gradients` | Computes gradients via backpropagation. |
| `train` | `(Network, Dataset, int, Scalar) → Network` | Trains via repeated forward/backward passes. |

**Contracts:**

- Activation functions SHALL be configurable; the default SHALL be the sigmoid function.
- Weight initialization SHALL accept a random seed for reproducibility.
- `feed_forward` SHALL NOT mutate the network.
- `backpropagate` SHALL NOT mutate the network; it SHALL return gradient values.

---

### 3.6 Unsupervised Learning Primitives

#### 3.6.1 Clustering — `c20_clustering`

| Component | Description |
| ----------- | ------------- |
| `KMeans` class | Accepts k (number of clusters). Provides `train(data)` and `classify(point)` methods. |
| `train` | Iteratively assigns points to nearest centroid and recomputes centroids until convergence or max iterations. |
| `classify` | Returns the index of the nearest centroid. |
| `bottom_up_cluster` | Agglomerative hierarchical clustering via a linkage function. |

**Contracts:**

- k SHALL be a positive integer strictly less than the number of data points.
- Convergence SHALL be defined as zero reassignments or reaching a maximum iteration count (configurable, default ≥ 100).
- `train` SHALL accept a random seed for centroid initialization reproducibility.
- Distance metric SHALL default to Euclidean distance (§3.1).
- `bottom_up_cluster` SHALL return a dendrogram-compatible nested structure.

#### 3.6.2 Network Analysis — `c22_network_analysis`

| Function | Signature | Description |
| ---------- | ----------- | ------------- |
| `betweenness_centrality` | `(Graph) → Dict[Node, Scalar]` | Computes betweenness centrality for all nodes. |
| `closeness_centrality` | `(Graph) → Dict[Node, Scalar]` | Computes closeness centrality for all nodes. |
| `pagerank` | `(Graph, Scalar?, int?) → Dict[Node, Scalar]` | Iterative PageRank with configurable damping factor and max iterations. |

#### 3.6.3 Natural Language Processing — `c21_natural_language_processing`

| Function | Signature | Description |
| ---------- | ----------- | ------------- |
| `bigrams` | `(List[str]) → List[(str, str)]` | Returns consecutive word pairs. |
| `trigrams` | `(List[str]) → List[(str, str, str)]` | Returns consecutive word triples. |
| `grammar_generate` | `(Grammar, str) → List[str]` | Generates sentences from a context-free grammar. |

---

### 3.7 Data Utilities

#### 3.7.1 General Utilities — `c10_working_with_data`

| Function | Signature | Description |
| ---------- | ----------- | ------------- |
| `rescale` | `(Matrix) → Matrix` | Rescales each column to have mean 0 and standard deviation 1. |
| `de_mean` | `(Matrix) → Matrix` | Centers each column by subtracting its mean. |
| `principal_component_analysis` | `(Matrix, int) → Matrix` | Returns the top-k principal components. |

#### 3.7.2 MapReduce — `c25_mapreduce`

| Function | Signature | Description |
| ---------- | ----------- | ------------- |
| `map_reduce` | `(Iterable, Callable, Callable) → Dict` | Single-machine MapReduce implementation. |
| `word_count` | `(List[str]) → Dict[str, int]` | Word frequency count via MapReduce. |

---

### 3.8 Cross-Cutting Contracts

The following contracts apply to ALL core library modules:

| Requirement | Description |
| ------------- | ------------- |
| **Purity** | Functions SHALL NOT modify their inputs. Return values SHALL be new objects. |
| **Type safety** | Functions SHALL validate input types where the language supports it. Invalid types SHALL produce descriptive errors, not silent corruption. |
| **Edge cases** | Empty collections, single-element collections, and zero-valued inputs SHALL be handled gracefully with documented behavior. |
| **Error messages** | Error messages SHALL include the function name, the constraint violated, and the actual input that violated it. |
| **Numerical precision** | Unless otherwise specified, functions SHALL produce results accurate to within $1 \times 10^{-10}$ relative error for inputs with absolute values in $[10^{-6}, 10^{6}]$. |
| **Complexity** | Where not specified, functions SHALL have at most polynomial time complexity in the size of their input. |
| **Test coverage** | Every public function SHALL have at least one positive test, one boundary test, and one negative (error-case) test. |

---

## 4. Dependency Policy

### 4.1 Core Library Dependencies

| Rule | Description |
| ------ | ------------- |
| **DP-1** | The core library SHALL depend exclusively on the base language runtime and its standard library. |
| **DP-2** | No third-party numerical, statistical, or machine learning libraries SHALL be imported in core modules. |
| **DP-3** | Mathematical functions (square root, logarithm, exponentiation) SHALL be sourced from the language's standard math library only. |
| **DP-4** | Random number generation SHALL use the language's standard library, with explicit seed control. |

### 4.2 Extension Layer Dependencies

| Rule | Description |
| ------ | ------------- |
| **DP-5** | Extension layers (visualization, ingestion) MAY introduce external dependencies. |
| **DP-6** | Extension layer dependencies SHALL be declared in layer-specific dependency manifests, NOT in the core library's manifest. |
| **DP-7** | Extension layer dependencies SHALL NOT be transitive — installing the core library SHALL NOT install extension dependencies. |

### 4.3 Transport Layer Dependencies

| Rule | Description |
| ------ | ------------- |
| **DP-8** | Transport layers MAY depend on I/O, networking, and serialization libraries. |
| **DP-9** | Transport layers SHALL NOT depend on each other. |
| **DP-10** | Transport layer code SHALL NOT leak into the core library's module namespace. |

### 4.4 Portability

| Rule | Description |
| ------ | ------------- |
| **DP-11** | The core library SHALL be installable and testable on any platform where the base language runtime is available. |
| **DP-12** | No platform-specific system calls, file paths, or environment variables SHALL appear in core library code. |
| **DP-13** | I/O operations SHALL be strictly separated from algorithmic logic. Functions that perform I/O SHALL be in dedicated I/O modules, never in algorithm modules. |

---

## 5. Build & Installation Specification

### 5.1 Installation Behavior

1. A user SHALL be able to install the core library using the language's standard
   package manager from the repository root.
2. Installation SHALL NOT require compilation of native extensions for the
   primary dynamic language implementation.
3. Installation SHALL NOT trigger downloads of additional data files.
4. Installation SHALL complete in under 60 seconds on a standard development
   machine with a warm package cache.

### 5.2 Packaging Structure

```txt
data-scratch-library/
├── pyproject.toml (or equivalent build manifest)
├── dsl/
│   ├── __init__.py (or equivalent module entry point)
│   ├── c04_linear_algebra/
│   ├── c05_statistics/
│   ├── c06_probability/
│   ├── c08_gradient_descent/
│   ├── c11_machine_learning/
│   ├── c12_k_nearest_neighbors/
│   ├── c13_naive_bayes/
│   ├── c14_simple_linear_regression/
│   ├── c15_multiple_regression/
│   ├── c16_logistic_regression/
│   ├── c17_decision_trees/
│   ├── c18_neural_networks/
│   ├── c19_deep_learning/
│   ├── c20_clustering/
│   ├── c21_natural_language_processing/
│   ├── c22_network_analysis/
│   ├── c23_recommender_systems/
│   ├── c24_databases/
│   └── c25_mapreduce/
└── tests/
    └── (mirrors dsl/ structure)
```

### 5.3 Import Contract

After installation, the following import SHALL succeed and provide access to all
core modules:

```bash
import dsl
```

Individual modules SHALL be importable directly:

```bash
from dsl.c04_linear_algebra import vector_add, dot, magnitude
from dsl.c05_statistics import mean, standard_deviation, correlation
```

### 5.4 Versioning Policy

| Rule | Description |
| ------ | ------------- |
| **VER-1** | The project SHALL follow Semantic Versioning 2.0.0 (`MAJOR.MINOR.PATCH`). |
| **VER-2** | `MAJOR` version increments indicate breaking changes to the public API. |
| **VER-3** | `MINOR` version increments indicate new modules or functions added without breaking existing APIs. |
| **VER-4** | `PATCH` version increments indicate bug fixes, documentation improvements, or test additions that do not change public API behavior. |
| **VER-5** | All public function signatures, return types, and error behaviors documented in this specification constitute the public API. |

### 5.5 Backward Compatibility Guarantees

- Functions documented in §3 SHALL NOT change their input/output contracts within
  a major version.
- New optional parameters MAY be added to existing functions in minor versions,
  but SHALL have defaults that preserve existing behavior.
- Removal or renaming of public functions SHALL occur only in major version
  increments and SHALL be preceded by a deprecation warning in at least one
  minor version.

---

## 6. Testing Specification

### 6.1 General Principles

| Rule | Description |
| ------ | ------------- |
| **TEST-1** | All tests SHALL be deterministic. No test SHALL depend on wall-clock time, network availability, or system-specific state. |
| **TEST-2** | Tests SHALL NOT make network calls. All external data SHALL be provided as fixtures or constants. |
| **TEST-3** | Tests involving randomness SHALL use explicit seeds, producing identical results on every run. |
| **TEST-4** | Test execution order SHALL NOT affect results. Each test SHALL be independent. |

### 6.2 Test Categories

#### 6.2.1 Unit Tests

- Every public function defined in §3 SHALL have at least:
  - **One positive test** — valid inputs producing expected output.
  - **One boundary test** — edge-case inputs (empty list, single element, zero, very large/small values).
  - **One negative test** — invalid inputs producing the documented error.

#### 6.2.2 Property-Based Tests

Mathematical invariants SHALL be verified via property-based testing:

| Property | Example |
| ---------- | --------- |
| Commutativity | `dot(a, b) == dot(b, a)` |
| Associativity | `vector_add(a, vector_add(b, c)) == vector_add(vector_add(a, b), c)` |
| Identity | `vector_add(v, zero_vector) == v` |
| Idempotence | `mean([x]) == x` for any x |
| Bounds | `0 <= normal_cdf(x) <= 1` for all x |
| Inverse | `normal_cdf(inverse_normal_cdf(p)) ≈ p` for p in (0, 1) |
| Triangle inequality | `distance(a, c) <= distance(a, b) + distance(b, c)` |
| Correlation bounds | `-1 <= correlation(x, y) <= 1` |
| Metric symmetry | `distance(a, b) == distance(b, a)` |

#### 6.2.3 Cross-Language Behavioral Equivalence Tests

- A shared set of **test vectors** SHALL be maintained in a language-agnostic
  serialization format in the repository root `data/` directory.
- Each test vector SHALL specify: function name, input values, expected output
  values, and floating-point tolerance.
- Every language port SHALL execute all shared test vectors and verify output
  within the specified tolerance.

#### 6.2.4 API Golden-Response Tests

- The REST API SHALL maintain a set of golden request/response pairs.
- These pairs SHALL be version-controlled.
- Regression tests SHALL compare actual responses to golden responses.
- Comparison SHALL use tolerance-aware floating-point comparison for numeric
  fields.

### 6.3 Test Directory Structure

```txt
tests/
├── test_c04_linear_algebra/
│   ├── test_vector_operations.py
│   └── test_matrix_operations.py
├── test_c05_statistics/
│   ├── test_central_tendency.py
│   ├── test_dispersion.py
│   └── test_correlation.py
├── test_c06_probability/
│   ├── test_distributions.py
│   └── test_conditional.py
├── test_c08_gradient_descent/
│   └── test_optimization.py
├── test_c11_machine_learning/
│   └── test_metrics.py
├── test_c12_k_nearest_neighbors/
├── test_c13_naive_bayes/
├── test_c14_simple_linear_regression/
├── test_c17_decision_trees/
├── test_c18_neural_networks/
├── test_c20_clustering/
│   ├── test_kmeans.py
│   └── test_hierarchical.py
├── shared_vectors/
│   └── (language-agnostic test vector files)
└── golden_responses/
    └── (REST API golden request/response pairs)
```

### 6.4 Coverage Requirements

| Scope | Minimum Coverage |
| ------- | ----------------- |
| Core library (line coverage) | ≥ 90% |
| Core library (branch coverage) | ≥ 80% |
| Transport layer (line coverage) | ≥ 75% |
| Language ports (line coverage) | ≥ 85% |

---

## 7. REST API Specification

### 7.1 Endpoint Naming Conventions

| Rule | Convention |
| ------ | ----------- |
| **URI structure** | `/api/{domain}/{operation}` |
| **Domain names** | Lowercase, hyphen-separated. Examples: `clustering`, `naive-bayes`, `neural-networks`, `knn`, `decision-trees`. |
| **Operation names** | Lowercase, hyphen-separated verb-noun. Examples: `train`, `classify`, `predict`, `analyze`. |
| **Plural vs. singular** | Domain names SHALL be singular when referring to an algorithm family (`/api/knn/classify`). |

### 7.2 Versioning Strategy

- The API version SHALL be included in the URI path: `/v1/api/...`
- Major version changes (breaking changes) SHALL increment the version number.
- Minor additions (new endpoints) SHALL NOT require version increment.
- Deprecated endpoints SHALL return a `Deprecation` header with the sunset date.

### 7.3 Request/Response Schema Rules

#### 7.3.1 Request Format

- All request bodies SHALL use the serialization format defined in §2.6.
- Content-Type headers SHALL be validated; unsupported types SHALL produce a 415
  status response.
- All numeric arrays SHALL be represented as ordered lists of numbers.
- All matrices SHALL be represented as ordered lists of ordered lists of numbers.

#### 7.3.2 Response Format

- All successful responses SHALL include:

```json
{
  "result": <computed value>,
  "metadata": {
    "function": "<function name>",
    "execution_time_ms": <integer>
  }
}
```

- Numeric results SHALL preserve the precision defined in §3.8.

### 7.4 Required Endpoints

#### 7.4.1 Health Endpoint

| Property | Value |
| ---------- | ------- |
| **Path** | `GET /health` |
| **Response (healthy)** | `200 OK` with `{"status": "healthy"}` |
| **Response (degraded)** | `503 Service Unavailable` with `{"status": "unhealthy", "details": "..."}` |
| **Latency** | SHALL respond within 100ms under normal conditions. |
| **Dependencies** | SHALL NOT depend on downstream services. SHALL test only the server process itself. |

#### 7.4.2 Root Information Endpoint

| Property | Value |
| ---------- | ------- |
| **Path** | `GET /` |
| **Response** | `200 OK` with API name, version, and list of available endpoints. |

#### 7.4.3 Compute Endpoints

All compute endpoints SHALL:

1. Accept a request body containing input data.
2. Deserialize and validate input against the documented schema.
3. Invoke the corresponding core library function.
4. Serialize the result into the response format (§7.3.2).
5. Return `200 OK` on success.

### 7.5 Error Response Format

All error responses SHALL use the following structure:

```json
{
  "error": {
    "code": "<MACHINE_READABLE_CODE>",
    "message": "<Human-readable description>",
    "details": <optional additional context>
  }
}
```

#### Standard Error Codes

| HTTP Status | Error Code | Condition |
| ------------- | ----------- | ----------- |
| 400 | `INVALID_INPUT` | Request body fails schema validation. |
| 400 | `DIMENSION_MISMATCH` | Vector/matrix dimensions are incompatible. |
| 400 | `DOMAIN_ERROR` | Input is outside the mathematical domain of the function. |
| 404 | `NOT_FOUND` | Endpoint does not exist. |
| 405 | `METHOD_NOT_ALLOWED` | HTTP method not supported for this endpoint. |
| 415 | `UNSUPPORTED_MEDIA_TYPE` | Content-Type header is unsupported. |
| 422 | `COMPUTATION_ERROR` | Core function raised an error during computation. |
| 500 | `INTERNAL_ERROR` | Unexpected server error. |
| 503 | `SERVICE_UNAVAILABLE` | Server is overloaded or shutting down. |

### 7.6 Idempotency Rules

- All `GET` endpoints SHALL be idempotent and side-effect-free.
- All `POST` compute endpoints SHALL be **functionally idempotent**: identical
  request bodies SHALL produce identical response bodies (excluding `execution_time_ms`).
- No compute endpoint SHALL maintain server-side state between requests unless
  explicitly documented (e.g., model training endpoints that create sessions).

### 7.7 Input Validation Requirements

1. **Type validation** — Every field SHALL be validated against its declared type.
   Type mismatches SHALL produce `INVALID_INPUT`.
2. **Range validation** — Numeric fields with documented constraints (e.g.,
   probability in [0, 1]) SHALL be validated. Violations SHALL produce
   `DOMAIN_ERROR`.
3. **Dimension validation** — Array and matrix inputs SHALL be validated for
   dimensional consistency before invoking core functions.
4. **Size limits** — The server SHALL enforce maximum input sizes to prevent
   resource exhaustion. Limits SHALL be configurable and documented.

---

## 8. Messaging Consumer Specification

### 8.1 Architecture Overview

```txt
┌─────────────┐      ┌──────────────────┐     ┌──────────────┐
│  Message    │────▶│  Consumer        │───▶│  Core        │
│  Broker     │      │  (Dispatcher)    │     │  Library     │
│  Pub/Sub    │◀─── │                  │◀───│  Function    │
│  Server     │      │  (Publisher)     │     │              │
└─────────────┘      └──────────────────┘     └──────────────┘
```

### 8.2 Topic / Queue Naming Strategy

| Rule | Convention |
| ------ | ----------- |
| **Pattern** | `dsl.{module}.{function}` |
| **Examples** | `dsl.linear_algebra.dot`, `dsl.statistics.mean`, `dsl.clustering.kmeans` |
| **Case** | All lowercase with dots as separators. |
| **Wildcards** | Consumers MAY subscribe to `dsl.#` (all) or `dsl.{module}.#` (all functions in a module). |

### 8.3 Payload Structure

#### 8.3.1 Request Payload

```json
{
  "id": "<unique request identifier>",
  "function": "<module>.<function_name>",
  "args": [<positional arguments>],
  "kwargs": {<keyword arguments>},
  "reply_to": "<optional reply topic/queue>",
  "timestamp": "<ISO 8601>"
}
```

| Field | Required | Description |
| ------- | ---------- | ------------- |
| `id` | YES | Unique identifier for deduplication and correlation. |
| `function` | YES | Fully qualified function name within the core library. |
| `args` | YES | Ordered list of positional arguments. |
| `kwargs` | NO | Key-value map of keyword arguments. |
| `reply_to` | NO | Destination for the response message. |
| `timestamp` | YES | Time the message was created. |

#### 8.3.2 Response Payload

```json
{
  "id": "<same id as request>",
  "status": "success" | "error",
  "result": <function return value>,
  "error": {
    "code": "...",
    "message": "...",
    "details": ...
  },
  "timestamp": "<ISO 8601>"
}
```

### 8.4 Acknowledgment Semantics

| Rule | Description |
| ------ | ------------- |
| **ACK-1** | Messages SHALL be acknowledged only after the core function has returned successfully and the response has been published (if `reply_to` is specified). |
| **ACK-2** | If the core function raises an error, the consumer SHALL publish an error response and then acknowledge the message (it SHALL NOT be requeued). |
| **ACK-3** | If the consumer process crashes before acknowledgment, the message SHALL remain available for redelivery by the broker. |

### 8.5 Idempotency Guarantees

- The consumer SHALL maintain a deduplication cache keyed by message `id`.
- If a message with a previously-seen `id` is received, the consumer SHALL:
  - Return the cached response (if available), OR
  - Acknowledge and discard the message without re-execution.
- Cache entries SHALL have a configurable TTL (default: 1 hour).

### 8.6 Retry Strategy

| Parameter | Default | Configurable |
| ----------- | --------- | ------------- |
| Maximum retries | 3 | YES |
| Backoff strategy | Exponential with jitter | YES |
| Initial delay | 1 second | YES |
| Maximum delay | 60 seconds | YES |
| Dead-letter routing | After max retries, route to a dead-letter destination | YES |

### 8.7 Failure Isolation

- A failure in one function invocation SHALL NOT affect the processing of other
  messages.
- The consumer SHALL catch all exceptions from the core library and translate
  them into error response payloads.
- Resource exhaustion (memory, CPU) SHALL be mitigated by configurable
  concurrency limits and input size limits.
- The consumer SHALL expose a health check mechanism equivalent to §7.4.1.

---

## 9. Cross-Language Port Specification

### 9.1 Behavioral Equivalence Requirements

Each language port SHALL implement the full public API defined in §3 for the
modules it covers. Specifically:

| Requirement | Description |
| ------------- | ------------- |
| **EQ-1** | For every function `f` in the core library, the port SHALL provide a function with the same name and equivalent semantics. |
| **EQ-2** | Given identical inputs, the port's output SHALL match the canonical implementation's output within the floating-point tolerance defined in §9.2. |
| **EQ-3** | Error conditions SHALL be equivalent: the same invalid inputs SHALL produce errors in both implementations. |
| **EQ-4** | The port MAY use language-idiomatic naming conventions (e.g., camelCase vs. snake_case) provided a documented mapping exists. |

### 9.2 Floating-Point Tolerance Strategy

| Precision Level | Tolerance | Applies To |
| ---------------- | ----------- | ------------ |
| Exact | 0 | Integer-valued results, counts, boolean logic |
| Standard | $\leq 1 \times 10^{-10}$ | Linear algebra, basic statistics |
| Relaxed | $\leq 1 \times 10^{-6}$ | Iterative algorithms (gradient descent, inverse CDF) |
| Stochastic | Statistical equivalence | Monte Carlo simulations (verified by distribution tests over many runs) |

### 9.3 Random Seed Determinism

- All language ports SHALL support explicit random seed parameters.
- Identical seeds SHALL produce identical sequences of random numbers within
  a single language port.
- Cross-language seed compatibility is NOT required (different PRNGs are
  acceptable), but the shared test vectors (§6.2.3) SHALL provide
  pre-generated random data so that algorithmic behavior can be verified
  independently of PRNG implementation.

### 9.4 Shared Test Vectors

- The repository SHALL maintain a directory of test vector files in a
  language-agnostic serialization format.
- Each test vector file SHALL contain:

```txt
{
  "function": "<module>.<function_name>",
  "cases": [
    {
      "description": "<human-readable description>",
      "input": { "args": [...], "kwargs": {...} },
      "expected_output": <value>,
      "tolerance": <float>,
      "expected_error": "<error code or null>"
    }
  ]
}
```

- Every language port's test suite SHALL load and execute these shared vectors.

### 9.5 Serialization Compatibility

- All language ports SHALL be able to deserialize the shared test vector format.
- All REST servers (regardless of implementation language) SHALL accept and
  produce responses conforming to §7.3.
- Numeric serialization SHALL preserve at least 15 significant decimal digits
  (double-precision).

### 9.6 Error Parity Rules

| Rule | Description |
| ------ | ------------- |
| **ERR-1** | The same categories of invalid input SHALL produce errors in all ports. |
| **ERR-2** | Error codes (§2.7) SHALL be identical across ports. |
| **ERR-3** | Error messages MAY differ in wording but SHALL convey equivalent information (function name, constraint violated, offending value). |
| **ERR-4** | Ports SHALL NOT silently succeed where the canonical implementation raises an error, and vice versa. |

### 9.7 Port Coverage Matrix

The following table defines which modules each port category SHALL implement:

| Module | Dynamic Language (Canonical) | Systems Language | Typed Scripting |
| -------- | :---: | :---: | :---: |
| Linear Algebra | ✓ | ✓ | ✓ |
| Statistics | ✓ | ✓ | ✓ |
| Probability | ✓ | ✓ | ✓ |
| Gradient Descent | ✓ | ✓ | ✓ |
| ML Metrics | ✓ | ✓ | ✓ |
| KNN | ✓ | ✓ | ✓ |
| Naive Bayes | ✓ | ✓ | ✓ |
| Decision Trees | ✓ | ✓ | ✓ |
| Neural Networks | ✓ | ✓ | ✓ |
| Clustering | ✓ | ✓ | ✓ |
| NLP | ✓ | OPTIONAL | OPTIONAL |
| Network Analysis | ✓ | OPTIONAL | OPTIONAL |
| MapReduce | ✓ | OPTIONAL | OPTIONAL |
| Deep Learning | ✓ | OPTIONAL | ✓ |

---

## 10. Coding Standards

### 10.1 Style Consistency

| Rule | Description |
| ------ | ------------- |
| **STY-1** | Each language port SHALL adopt the dominant style guide for its language ecosystem. |
| **STY-2** | Automated formatting SHALL be enforced via a language-appropriate formatting tool configured in the repository. |
| **STY-3** | Maximum line length: 120 characters (soft limit), 140 characters (hard limit). |
| **STY-4** | Indentation SHALL be consistent within each language port (spaces preferred; tab width 4 for indentation-sensitive languages). |

### 10.2 Documentation Standards

| Rule | Description |
| ------ | ------------- |
| **DOC-1** | Every public function SHALL have a documentation comment specifying: purpose, parameters (with types), return value (with type), exceptions/errors raised, and at least one usage example. |
| **DOC-2** | Every module SHALL have a module-level documentation comment describing its purpose and relationship to the chapter of study. |
| **DOC-3** | Mathematical formulas SHALL be included in documentation where the function implements a named formula (e.g., Pearson correlation, Shannon entropy, sigmoid). |
| **DOC-4** | Non-obvious algorithmic choices SHALL be documented with inline comments citing the relevant mathematical justification. |

### 10.3 Public API Stability Rules

| Rule | Description |
| ------ | ------------- |
| **API-1** | Any function, class, or constant listed in §3 is considered public API and is subject to the versioning policy in §5.4. |
| **API-2** | Functions prefixed with an underscore (or language-equivalent private marker) are internal and MAY change without notice. |
| **API-3** | The set of public functions SHALL be explicitly enumerated in each module's entry point (e.g., `__all__` or equivalent export mechanism). |

### 10.4 Error Handling Conventions

| Rule | Description |
| ------ | ------------- |
| **ERR-H1** | Functions SHALL validate inputs at the function boundary, not deep within helper calls. |
| **ERR-H2** | Error types/exceptions SHALL be domain-specific (e.g., `DimensionMismatchError`, `DomainError`), not generic runtime exceptions. |
| **ERR-H3** | Error messages SHALL follow the template: `"{function_name}: {constraint} violated — got {actual_value}"`. |
| **ERR-H4** | Functions SHALL NOT catch and suppress exceptions silently. If an exception is caught, it SHALL be re-raised, wrapped, or logged. |

### 10.5 Prohibited Patterns

The following patterns are PROHIBITED in all core library code:

| Pattern | Reason |
| --------- | -------- |
| Module-level mutable state (global variables) | Violates determinism and testability. |
| Implicit mutation of input arguments | Violates functional-first design. |
| Side effects in pure functions (logging, I/O, printing) | Violates purity contract. |
| Wildcard imports (`from module import *`) | Obscures dependencies and pollutes namespace. |
| Circular imports between modules | Indicates architectural coupling. |
| Hard-coded file paths or URLs | Violates portability. |
| Bare exception handlers (`except:` or `catch(...)`) | Masks errors and violates error handling conventions. |
| Magic numbers without named constants | Reduces readability and maintainability. |
| Mutable default arguments | Language-specific pitfall that causes hidden shared state. |

---

## 11. CI/CD Requirements

### 11.1 Multi-Language Test Matrix

The CI pipeline SHALL execute the following matrix on every commit to a
protected branch and on every pull/merge request:

| Dimension | Values |
| ----------- | -------- |
| Language | Primary dynamic language, systems language, typed scripting language |
| Language Version | Latest stable release, previous stable release |
| Operating System | At least two distinct operating system families |
| Test Tier | Unit, property-based, integration, cross-language vectors |

### 11.2 Coverage Thresholds

| Metric | Threshold | Enforcement |
| -------- | ----------- | ------------- |
| Core library line coverage | ≥ 90% | Build FAILS if below threshold |
| Core library branch coverage | ≥ 80% | Build FAILS if below threshold |
| Transport layer line coverage | ≥ 75% | Build WARNS if below threshold |
| Language port line coverage | ≥ 85% | Build FAILS if below threshold |

### 11.3 Reproducible Builds

| Rule | Description |
| ------ | ------------- |
| **BLD-1** | Dependency versions SHALL be pinned (lock files or equivalent). |
| **BLD-2** | Build outputs SHALL be byte-for-byte reproducible given identical inputs and dependency versions. |
| **BLD-3** | Build timestamps SHALL NOT be embedded in artifacts. |
| **BLD-4** | Container images (if produced) SHALL use digest-pinned base images. |

### 11.4 Deterministic Artifact Generation

- Package artifacts SHALL be generated from tagged commits only.
- Artifact names SHALL include the version number and commit hash.
- Format: `{package_name}-{version}+{short_commit_hash}.{extension}`

### 11.5 Static Analysis Enforcement

| Check | Scope | Enforcement |
| ------- | ------- | ------------- |
| Linting | All languages | Build FAILS on lint errors |
| Type checking | Languages with static type systems or optional type checkers | Build FAILS on type errors |
| Dependency audit | All dependency manifests | Build WARNS on known vulnerabilities |
| Complexity analysis | Core library | Build WARNS if cyclomatic complexity exceeds 15 per function |
| Dead code detection | Core library | Build WARNS on unreachable code |

---

## 12. Non-Functional Requirements

### 12.1 Determinism

| Requirement | Description |
| ------------- | ------------- |
| **NFR-D1** | All pure functions SHALL produce identical outputs for identical inputs across invocations, process restarts, and language ports (within tolerance). |
| **NFR-D2** | Functions with stochastic behavior SHALL document this and accept explicit seed parameters. |
| **NFR-D3** | Test suites SHALL verify determinism by running each test at least twice and asserting identical results. |

### 12.2 Numerical Stability

| Requirement | Description |
| ------------- | ------------- |
| **NFR-N1** | Algorithms operating on floating-point numbers SHALL be implemented to minimize catastrophic cancellation and accumulation of rounding errors. |
| **NFR-N2** | Log-space computation SHALL be used where probabilities may underflow (naive Bayes, logistic regression). |
| **NFR-N3** | The sigmoid function SHALL be implemented to avoid overflow for large positive inputs and underflow for large negative inputs. |
| **NFR-N4** | Summation of many small values SHALL use a compensated summation technique or equivalent where precision is critical. |
| **NFR-N5** | Correlation and covariance functions SHALL clamp outputs to their mathematically valid ranges. |

### 12.3 Portability

| Requirement | Description |
| ------------- | ------------- |
| **NFR-P1** | The core library SHALL run unmodified on 64-bit and 32-bit architectures (where the language runtime supports both). |
| **NFR-P2** | No endianness assumptions SHALL be present in serialization code. |
| **NFR-P3** | Character encoding SHALL be UTF-8 throughout. |
| **NFR-P4** | File path separators SHALL NOT be hard-coded; path construction SHALL use language-standard path utilities. |

### 12.4 Security Constraints

| Requirement | Description |
| ------------- | ------------- |
| **NFR-S1** | REST endpoints SHALL validate and sanitize all inputs. No input SHALL be passed to shell commands or dynamic code evaluation. |
| **NFR-S2** | Error responses SHALL NOT expose internal stack traces, file paths, or system information in production mode. |
| **NFR-S3** | Serialization/deserialization SHALL NOT permit arbitrary code execution (no unsafe deserialization). |
| **NFR-S4** | Messaging consumers SHALL validate payload structure before invoking core functions. |
| **NFR-S5** | Dependencies SHALL be audited for known vulnerabilities as part of the CI pipeline (§11.5). |
| **NFR-S6** | Container images SHALL run as non-root users. |

### 12.5 Performance Baseline Expectations

These are baseline expectations for educational correctness, NOT production targets:

| Operation | Expected Baseline | Measurement Condition |
| ----------- | ------------------- | ---------------------- |
| Vector dot product (n=1000) | < 10 ms | Single-threaded, primary dynamic language |
| Matrix multiply (100×100) | < 5 s | Single-threaded, primary dynamic language |
| KMeans (1000 points, 10 clusters, 2D) | < 30 s | Single-threaded, primary dynamic language |
| Naive Bayes train (10,000 documents) | < 60 s | Single-threaded, primary dynamic language |
| REST health check | < 100 ms | Warm server, local network |
| REST compute (small input) | < 2 s | Warm server, local network |

Performance SHALL NOT be a blocker for correctness. If an optimization
would obscure the mathematical intent of the code, the unoptimized version
SHALL be preferred with the optimization documented as a comment.

---

## 13. Roadmap

### Phase 1: Core Mathematical Foundation

**Acceptance Criteria:**

- [ ] All §3 modules implemented in the primary dynamic language.
- [ ] All unit tests passing with ≥ 90% line coverage.
- [ ] All property-based tests for mathematical invariants passing.
- [ ] Zero external dependencies in core library.
- [ ] Documentation complete for all public functions.
- [ ] Package installable via standard tooling.

### Phase 2: Visualization & Ingestion Layers

**Acceptance Criteria:**

- [ ] Visualization layer produces static chart output for each algorithm category (distributions, regression lines, clustering, decision boundaries, network graphs).
- [ ] Ingestion layer can retrieve and parse structured data from HTTP sources and HTML documents.
- [ ] Both layers depend on core library only through the public API defined in §3.
- [ ] Both layers have independent dependency manifests.
- [ ] Both layers have ≥ 75% test coverage.

### Phase 3: Service Layer (REST)

**Acceptance Criteria:**

- [ ] At least one REST server implements all endpoints in the API contract.
- [ ] Health endpoint operational.
- [ ] All compute endpoints pass golden-response tests.
- [ ] Error responses conform to §7.5.
- [ ] Input validation covers all rules in §7.7.
- [ ] API contract document (machine-readable) is version-controlled and serves as the single source of truth for all REST implementations.

### Phase 4: Messaging Layer

**Acceptance Criteria:**

- [ ] Message queue consumer operational with at least one broker.
- [ ] Pub/sub consumer operational with at least one broker.
- [ ] Both consumers pass idempotency tests.
- [ ] Retry strategy implemented and tested.
- [ ] Dead-letter routing functional.
- [ ] Consumers dynamically discover and dispatch to all core library functions.

### Phase 5: Cross-Language Parity

**Acceptance Criteria:**

- [ ] Systems language port covers all REQUIRED modules in §9.7.
- [ ] Typed scripting port covers all REQUIRED modules in §9.7.
- [ ] Shared test vectors pass in all three language families.
- [ ] REST servers in all language ports pass the same golden-response tests.
- [ ] Naming convention mapping documented.

### Phase 6: Benchmarking & Optimization

**Acceptance Criteria:**

- [ ] Performance baselines (§12.5) measured and recorded for all language ports.
- [ ] Performance regression tests added to CI pipeline.
- [ ] Optimization opportunities identified and documented as comments in code.
- [ ] Any optimization that obscures mathematical intent has the unoptimized version preserved in comments or documentation.
- [ ] Cross-language performance comparison published in repository documentation.

---

## Appendix A: Glossary

| Term | Definition |
| ------ | ----------- |
| **Core Library** | The set of modules defined in §3, containing pure algorithmic implementations with zero external dependencies. |
| **Extension Layer** | A module that depends on the core library and introduces external dependencies for I/O, visualization, or data acquisition. |
| **Transport Layer** | A module that exposes core library functions over a network protocol (REST, message queue, pub/sub). |
| **Language Port** | A re-implementation of the core library in a different programming language, maintaining behavioral equivalence. |
| **Test Vector** | A language-agnostic specification of function inputs, expected outputs, and tolerances used for cross-language verification. |
| **Golden Response** | A version-controlled request/response pair used to verify REST API behavior. |
| **Behavioral Equivalence** | The property that two implementations produce outputs within specified tolerance for all inputs in the defined domain. |

## Appendix B: Document Conventions

- **SHALL** — Absolute requirement. Non-compliance is a specification violation.
- **SHALL NOT** — Absolute prohibition.
- **MAY** — Optional behavior; implementation is permitted but not required.
- **SHOULD** — Recommended behavior; deviation requires documented justification.
- **OPTIONAL** — Explicitly optional; absence does not constitute non-compliance.

These terms are used in accordance with RFC 2119.

---

## *End of Specification*
