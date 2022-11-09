if __name__ == "__main__":
    dictConfig(config.LOGGING_CONFIG_DICT)
    logging.info(
        "%r",
        "accuracy(70, 4930, 13930, 981070) {}".format(
            accuracy(70, 4930, 13930, 981070)
        ),
    )
    logging.info(
        "%r",
        "precision(70, 4930, 13930, 981070) {}".format(
            precision(70, 4930, 13930, 981070)
        ),
    )
    logging.info(
        "%r",
        "recall(70, 4930, 13930, 981070) {}".format(recall(70, 4930, 13930, 981070)),
    )
    logging.info(
        "%r",
        "f1_score(70, 4930, 13930, 981070) {}".format(
            f1_score(70, 4930, 13930, 981070)
        ),
    )
