def train_and_test_model(path):
    data = get_subject_data(path)
    random.seed(0)  # just so you get the same answers as me
    train_data, test_data = split_data(data, 0.75)

    classifier = NaiveBayesClassifier()
    classifier.train(train_data)

    classified = [
        (subject, is_spam, classifier.classify(subject))
        for subject, is_spam in test_data
    ]

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

    words = sorted(classifier.word_probs, key=p_spam_given_word)

    spammiest_words = words[-5:]
    hammiest_words = words[:5]

    logging.info("%r", "spammiest_words {}".format(spammiest_words))
    logging.info("%r", "hammiest_words {}".format(hammiest_words))


if __name__ == "__main__":
    dictConfig(config.LOGGING_CONFIG_DICT)  # train_and_test_model(r"c:\spam\*\*")
    train_and_test_model(r"/home/joel/src/spam/*/*")
