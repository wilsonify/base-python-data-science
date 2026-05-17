# Chapter 25 – MapReduce

A from-scratch MapReduce framework for distributed-style data processing on a
single machine.

---

## Key Concepts

### The MapReduce Model

1. **Map** — a mapper function transforms each input into zero or more
   (key, value) pairs.
2. **Shuffle** — pairs are grouped by key.
3. **Reduce** — a reducer function aggregates all values for each key into
   output (key, result) pairs.

This model allows work to be distributed across many machines because mappers
run independently and reducers only need the values for a single key.

### Combiners

Before shipping data to reducers, a combiner can pre-aggregate mapper output
on the same machine (e.g. summing local word counts), greatly reducing data
transfer.

---

## Module API

### Core Framework

| Function | Signature | Description |
|---|---|---|
| `map_reduce` | `(inputs, mapper, reducer) → List[KV]` | Run the full MapReduce pipeline |
| `reduce_with` | `(inputs, mapper, reducer) → List[KV]` | Alias / variant |
| `values_reducer` | `(values_fn) → Reducer` | Create a reducer that applies an aggregation function |

### Word Count

| Function | Description |
|---|---|
| `wc_mapper` | Emit `(word, 1)` for each word in a document |
| `wc_reducer` | Sum counts for a word |
| `word_count` | End-to-end word count via MapReduce |

### Status-Update Analysis

| Function | Description |
|---|---|
| `most_popular_word_reducer` | Find the most common word per user |
| `liker_mapper` | Emit `(user, liker)` pairs for distinct-liker counts |

### Matrix Multiplication

| Function | Description |
|---|---|
| `matrix_multiply_mapper` | Emit entries for sparse matrix product |
| `matrix_multiply_reducer` | Combine matching entries and sum products |

---

## Example

See [`e01_mapreduce.py`](e01_mapreduce.py) for word counting, status-update
analysis, and sparse matrix multiplication.

---

## Further Reading

- [MapReduce – Wikipedia](https://en.wikipedia.org/wiki/MapReduce)
- [Apache Spark](https://spark.apache.org/) — modern distributed computing
- *Data Science from Scratch*, Chapter 25
