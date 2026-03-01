"""
Example: train a Naive Bayes spam classifier and evaluate it.
"""

import logging
import random
from collections import Counter
from logging.config import dictConfig

from dsl.c11_machine_learning.machine_learning import split_data
from dsl.c13_naive_bayes.naive_bayes import (
    get_subject_data,
    p_spam_given_word,
    NaiveBayesClassifier,
)


def evaluate(classifier, test_data):
    """Classify test data and report accuracy breakdown."""
    classified = [
        (subject, is_spam, classifier.classify(subject))
        for subject, is_spam in test_data
    ]
    counts = Counter(
        (is_spam, spam_probability > 0.5)
        for _, is_spam, spam_probability in classified
    )
    logging.info("confusion: %s", counts)

    classified.sort(key=lambda row: row[2])
    spammiest_hams = [r for r in classified if not r[1]][-5:]
    hammiest_spams = [r for r in classified if r[1]][:5]
    logging.info("spammiest hams: %s", spammiest_hams)
    logging.info("hammiest spams: %s", hammiest_spams)


def inspect_words(classifier):
    """Log the most/least spammy words."""
    words = sorted(classifier.word_probs, key=p_spam_given_word)
    logging.info("hammiest words: %s", words[:5])
    logging.info("spammiest words: %s", words[-5:])


def main(path: str) -> None:
    random.seed(0)
    data = get_subject_data(path)
    train_data, test_data = split_data(data, 0.75)

    classifier = NaiveBayesClassifier()
    classifier.train(train_data)

    inspect_words(classifier)
    evaluate(classifier, test_data)


if __name__ == "__main__":
    dictConfig(
        {
            "version": 1,
            "formatters": {
                "simple": {
                    "format": "%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "simple",
                }
            },
            "root": {"handlers": ["console"], "level": logging.DEBUG},
        }
    )
    main(r"/home/thom/repos/base-python-data-science/tests/data/spam/*")
