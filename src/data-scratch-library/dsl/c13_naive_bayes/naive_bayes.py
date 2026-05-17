"""
Naive Bayes spam classifier.
"""

import glob
import math
import re
from collections import defaultdict
from typing import List, Tuple, Set, Dict


def tokenize(message: str) -> Set[str]:
    """Lowercase *message* and extract unique alphanumeric tokens."""
    message = message.lower()
    all_words = re.findall("[a-z0-9']+", message)
    return set(all_words)


def count_words(
    training_set: List[Tuple[str, bool]],
) -> Dict[str, List[int]]:
    """Count word occurrences in spam vs. non-spam messages."""
    counts: Dict[str, List[int]] = defaultdict(lambda: [0, 0])
    for message, is_spam in training_set:
        for word in tokenize(message):
            counts[word][0 if is_spam else 1] += 1
    return counts


def word_probabilities(
    counts: Dict[str, List[int]],
    total_spams: int,
    total_non_spams: int,
    k: float = 0.5,
) -> List[Tuple[str, float, float]]:
    """Convert word counts to (word, P(word|spam), P(word|¬spam)) triples."""
    return [
        (
            w,
            (spam + k) / (total_spams + 2 * k),
            (non_spam + k) / (total_non_spams + 2 * k),
        )
        for w, (spam, non_spam) in counts.items()
    ]


def get_spam_probability(
    word_probs: List[Tuple[str, float, float]], message: str
) -> float:
    """Return P(spam | message) using the Naive Bayes model."""
    message_words = tokenize(message)
    log_prob_if_spam = log_prob_if_not_spam = 0.0

    for word, prob_if_spam, prob_if_not_spam in word_probs:
        if word in message_words:
            log_prob_if_spam += math.log(prob_if_spam)
            log_prob_if_not_spam += math.log(prob_if_not_spam)
        else:
            log_prob_if_spam += math.log(1.0 - prob_if_spam)
            log_prob_if_not_spam += math.log(1.0 - prob_if_not_spam)

    prob_if_spam = math.exp(log_prob_if_spam)
    prob_if_not_spam = math.exp(log_prob_if_not_spam)
    return prob_if_spam / (prob_if_spam + prob_if_not_spam)


class NaiveBayesClassifier:
    """Train on (message, is_spam) pairs and classify new messages."""

    def __init__(self, k: float = 0.5) -> None:
        self.k = k
        self.word_probs: List[Tuple[str, float, float]] = []

    def train(self, training_set: List[Tuple[str, bool]]) -> None:
        num_spams = len([is_spam for _, is_spam in training_set if is_spam])
        num_non_spams = len(training_set) - num_spams
        word_counts = count_words(training_set)
        self.word_probs = word_probabilities(
            word_counts, num_spams, num_non_spams, self.k
        )

    def classify(self, message: str) -> float:
        if not self.word_probs:
            raise ValueError("Classifier has not been trained yet")
        return get_spam_probability(self.word_probs, message)


def get_subject_data(path: str) -> List[Tuple[str, bool]]:
    """Read email subjects from *path* glob; label ham/spam by filename."""
    data: List[Tuple[str, bool]] = []
    subject_regex = re.compile(r"^Subject:\s+")
    for fn in glob.glob(path):
        is_spam = "ham" not in fn
        with open(fn, "r", encoding="ISO-8859-1") as file:
            for line in file:
                if line.startswith("Subject:"):
                    subject = subject_regex.sub("", line).strip()
                    data.append((subject, is_spam))
    return data


def p_spam_given_word(
    word_prob: Tuple[str, float, float],
) -> float:
    """P(spam | word) from a (word, p_spam, p_not_spam) triple."""
    _, prob_if_spam, prob_if_not_spam = word_prob
    return prob_if_spam / (prob_if_spam + prob_if_not_spam)
