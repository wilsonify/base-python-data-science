# Chapter 23 – Recommender Systems

Recommend items to users using popularity, user-based collaborative filtering,
item-based collaborative filtering, and matrix factorisation.

---

## Key Concepts

### Approaches

| Approach | Idea |
|---|---|
| **Popularity** | Recommend the most globally popular items the user hasn't seen |
| **User-based CF** | Find similar users (cosine similarity on interest vectors); recommend what they like |
| **Item-based CF** | Find similar items; recommend items similar to what the user already likes |
| **Matrix factorisation** | Learn low-dimensional user and item embeddings whose dot products predict ratings |

### Cosine Similarity

$$\text{sim}(\mathbf{u}, \mathbf{v}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \, \|\mathbf{v}\|}$$

Used to compare both user-interest vectors and item-user vectors.

---

## Module API

| Function | Signature | Description |
|---|---|---|
| `cosine_similarity` | `(v, w) → float` | Cosine similarity between two vectors |
| `most_popular_new_interests` | `(user_interests, max_results) → list` | Top popular interests the user hasn't listed |
| `make_user_interest_vector` | `(user_interests) → List[int]` | Binary interest vector for a user |
| `most_similar_users_to` | `(user_id) → List[(id, sim)]` | Users ranked by similarity |
| `user_based_suggestions` | `(user_id, include_current) → list` | Weighted interest suggestions from similar users |
| `most_similar_interests_to` | `(interest_id) → List[(name, sim)]` | Interests ranked by co-occurrence similarity |
| `item_based_suggestions` | `(user_id, include_current) → list` | Weighted suggestions from similar items |

---

## Example

See [`e01_recommender_systems.py`](e01_recommender_systems.py) for a worked
example on the DataSciencester user-interest dataset.

---

## Further Reading

- [Collaborative filtering – Wikipedia](https://en.wikipedia.org/wiki/Collaborative_filtering)
- [Matrix factorisation (recommender systems)](https://en.wikipedia.org/wiki/Matrix_factorization_(recommender_systems))
- *Data Science from Scratch*, Chapter 23
