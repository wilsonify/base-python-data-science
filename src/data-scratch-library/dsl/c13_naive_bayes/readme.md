# Chapter 13 – Naive Bayes

A spam classifier built on Bayes' theorem with a "naive" conditional-independence
assumption: the presence of each word is independent of every other word, given
the spam/ham label.

## Key Concepts

### Bayes' Theorem for Spam

$$P(\text{spam} \mid \text{message}) = \frac{P(\text{message} \mid \text{spam})}{P(\text{message} \mid \text{spam}) + P(\text{message} \mid \text{ham})}$$

(Assumes equal prior probabilities for spam and ham.)

### The "Naive" Independence Assumption

Instead of modeling the joint probability of all words, treat each word as
independent:

$$P(w_1, w_2, \dots, w_n \mid \text{spam}) \approx \prod_i P(w_i \mid \text{spam})$$

This is unrealistic but works surprisingly well in practice.

### Smoothing

To avoid zero probabilities for unseen words, a pseudocount *k* (default 0.5) is
added:

$$P(w_i \mid \text{spam}) = \frac{k + \text{spam count of } w_i}{2k + \text{total spams}}$$

### Log-Space Arithmetic

Products of many small probabilities cause underflow. The implementation sums
**log-probabilities** and exponentiates at the end.

---

## Module API

### Tokenization

#### `tokenize(message)`

Lowercases the message and extracts unique alphanumeric tokens (letters, digits,
apostrophes).

```python
from dsl.c13_naive_bayes.naive_bayes import tokenize

tokenize("Data Science is science")  # {"data", "science", "is"}
```

### Word Statistics

#### `count_words(training_set)`

Takes a list of `(message, is_spam)` tuples. Returns a dict mapping each word to
`[spam_count, ham_count]`.

#### `word_probabilities(counts, total_spams, total_non_spams, k=0.5)`

Converts word counts into `(word, P(word|spam), P(word|ham))` triples, with
Laplace smoothing.

### Classification

#### `get_spam_probability(word_probs, message)`

Returns `P(spam | message)` given pre-computed word-probability triples.

#### `NaiveBayesClassifier(k=0.5)`

Convenience class that wraps the above functions.

| Method                | Description                                           |
|-----------------------|-------------------------------------------------------|
| `train(training_set)` | Learn word probabilities from `(message, is_spam)` pairs. |
| `classify(message)`   | Return `P(spam \| message)` as a float in `[0, 1]`.  |

```python
from dsl.c13_naive_bayes.naive_bayes import NaiveBayesClassifier

model = NaiveBayesClassifier(k=0.5)
model.train([("buy now", True), ("hi friend", False)])
model.classify("buy this now")  # high spam probability
```

### Data Loading

#### `get_subject_data(path)`

Reads email files matching a glob `path`, extracts subject lines, and labels each
as spam or ham based on the filename. Returns `List[(subject, is_spam)]`.

### Inspection

#### `p_spam_given_word(word_prob)`

Given a `(word, p_spam, p_ham)` triple, returns `P(spam | word)` — useful for
ranking the most/least spammy words.

---

## Example: SpamAssassin Corpus

The worked example in [e01_naive_bayes.py](e01_naive_bayes.py) trains on email
subject lines from the SpamAssassin public corpus and evaluates precision/recall
on a held-out test set.

---

## Further Reading

- Paul Graham, *A Plan for Spam* and *Better Bayesian Filtering*.
- [scikit-learn `BernoulliNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html)
