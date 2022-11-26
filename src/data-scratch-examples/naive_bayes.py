import logging
import random
from collections import Counter
from logging.config import dictConfig

from dsl.machine_learning import split_data
from dsl.naive_bayes import get_subject_data, p_spam_given_word, NaiveBayesClassifier


def word_counter(classified):
    counts = Counter(
        (is_spam, spam_probability > 0.5)  # (actual, predicted)
        for _, is_spam, spam_probability in classified
    )

    logging.info("%r", "counts = {}".format(counts))

    classified.sort(key=lambda row: row[2])
    spammiest_hams = list(filter(lambda row: not row[1], classified))[-5:]
    hammiest_spams = list(filter(lambda row: row[1], classified))[:5]

    logging.info("%r", "spammiest_hams {}".format(spammiest_hams))
    logging.info("%r", "hammiest_spams {}".format(hammiest_spams))


def predict_batch(classifier, test_data):
    classified = [
        (subject, is_spam, classifier.classify(subject))
        for subject, is_spam in test_data
    ]
    return classified


def read_classifier(classifier):
    words = sorted(classifier.word_probs, key=p_spam_given_word)
    spammiest_words = words[-5:]
    hammiest_words = words[:5]
    logging.info("%r", "spammiest_words {}".format(spammiest_words))
    logging.info("%r", "hammiest_words {}".format(hammiest_words))


def main(path):
    logging.info("start reading data")
    data = get_subject_data(path)
    logging.info("done reading data")

    logging.info("start splitting data")
    train_data, test_data = split_data(data, 0.75)
    logging.info("done splitting data")

    logging.info("start training classifier")
    classifier = NaiveBayesClassifier()
    classifier.train(train_data)
    logging.info("done training classifier")

    read_classifier(classifier)

    logging.info("start predicting")
    classified = predict_batch(classifier, test_data)
    logging.info("done predicting")

    word_counter(classified)


if __name__ == "__main__":
    random.seed(0)  # just so you get repeatable answers
    dictConfig(dict(
        version=1,
        formatters={"simple": {"format": """%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"""}},
        handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
        root={"handlers": ["console"], "level": logging.DEBUG},
    ))  # train_and_test_model(r"c:\spam\*\*")
    main(r"/home/thom/repos/base-python-data-science/tests/data/spam/*")
