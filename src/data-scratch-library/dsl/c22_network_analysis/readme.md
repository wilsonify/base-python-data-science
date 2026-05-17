# Chapter 22 – Network Analysis

Analyse graph-structured data: centrality measures, shortest paths, eigenvectors,
and the PageRank algorithm.

---

## Key Concepts

### Centrality Measures

| Measure | Idea |
|---|---|
| **Degree** | Number of connections |
| **Betweenness** | Fraction of all shortest paths that pass through a node |
| **Closeness** | Inverse of the sum of shortest-path lengths to all other nodes |
| **Eigenvector** | Being connected to other high-centrality nodes (recursive) |

### Shortest Paths (BFS)

`shortest_paths_from` uses breadth-first search to find **all** shortest paths
from a source node to every other node in an undirected graph.

### Eigenvector Centrality

Computed via power iteration on the adjacency matrix. The eigenvector's entries
give each node's centrality score.

### Directed Graphs & PageRank

For directed networks (e.g. endorsements), PageRank distributes a fixed total
rank across nodes. At each iteration:

- Each node shares a fraction (`damping`) of its rank equally among its
  outgoing links.
- The remainder is distributed uniformly to all nodes.

---

## Module API

| Function | Signature | Description |
|---|---|---|
| `populate_friends` | `(users, friendships) → users` | Add `friends` list to each user dict |
| `shortest_paths_from` | `(from_user) → Dict[int, List[Path]]` | BFS shortest paths |
| `farness` | `(user) → int` | Sum of shortest-path lengths |
| `populate_shortest_paths` | `(users) → users` | Attach shortest-path data |
| `populate_betweeness` | `(users) → users` | Compute betweenness centrality |
| `populate_closeness` | `(users) → users` | Compute closeness centrality |
| `construct_adjacency` | `(users, friendships) → Matrix` | Build adjacency matrix |
| `matrix_product_entry` | `(A, B, i, j) → float` | Single entry of A × B |
| `matrix_multiply` | `(A, B) → Matrix` | Full matrix multiplication |
| `vector_as_matrix` / `vector_from_matrix` | — | Shape conversions |
| `matrix_operate` | `(A, v) → Vector` | Matrix–vector product |
| `find_eigenvector` | `(matrix, tol) → (Vector, float)` | Power-iteration eigenvector |
| `compute_eigenvectors` | `(adjacency) → Vector` | Eigenvector centrality scores |
| `populate_endorsements` | `(users, endorsements) → users` | Track endorsers/endorsees |
| `page_rank` | `(users, endorsements, damping, iters) → Dict[int, float]` | PageRank scores |

---

## Example

See [`e01_network_analysis.py`](e01_network_analysis.py) for a worked example
on the DataSciencester social network.

---

## Further Reading

- [Centrality – Wikipedia](https://en.wikipedia.org/wiki/Centrality)
- [PageRank – Wikipedia](https://en.wikipedia.org/wiki/PageRank)
- [NetworkX](https://networkx.org/) — production-grade Python graph library
- *Data Science from Scratch*, Chapter 22
