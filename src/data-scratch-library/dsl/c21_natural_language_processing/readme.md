# Chapter 21 – Natural Language Processing

Techniques for working with text: n-gram language models, context-free grammars,
Gibbs sampling, and topic modelling with Latent Dirichlet Allocation (LDA).

---

## Key Concepts

### n-Gram Language Models

Build a statistical model of language from a corpus of text.

| Model | Description |
|---|---|
| **Bigram** | Next word depends on the current word only |
| **Trigram** | Next word depends on the two preceding words |

Higher-order n-grams produce more coherent text but require more data.

### Context-Free Grammars

Define a set of rewriting rules (e.g. `_S → _NP _VP`) and recursively expand
non-terminals into terminal words. Useful for both **generating** and **parsing**
sentences.

### Gibbs Sampling

A Markov-chain Monte Carlo method for sampling from joint distributions when
only conditional distributions are known. Used as the inference engine for LDA
topic modelling.

### Topic Modelling (LDA)

Latent Dirichlet Allocation assumes each document is a mixture of $K$ topics
and each topic is a distribution over words. The algorithm:

1. Randomly assign a topic to every word in every document.
2. For each word, resample its topic using weights derived from (a) the topic
   distribution in that document and (b) the word distribution in that topic.
3. Repeat until convergence.

---

## Module API

This chapter is implemented as a conceptual reference module (placeholder
`__init__.py`). The techniques described above are demonstrated in the example
scripts of other packages and chapters.

---

## Further Reading

- [n-gram – Wikipedia](https://en.wikipedia.org/wiki/N-gram)
- [Latent Dirichlet allocation – Wikipedia](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation)
- [Gibbs sampling – Wikipedia](https://en.wikipedia.org/wiki/Gibbs_sampling)
- *Data Science from Scratch*, Chapter 21
