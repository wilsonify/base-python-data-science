

if __name__ == "__main__":
    dictConfig(config.LOGGING_CONFIG_DICT)  #
    # CONDITIONAL PROBABILITY
    #

    both_girls = 0
    older_girl = 0
    either_girl = 0

    random.seed(0)
    for _ in range(10000):
        younger = random_kid()
        older = random_kid()
        if older == "girl":
            older_girl += 1
        if older == "girl" and younger == "girl":
            both_girls += 1
        if older == "girl" or younger == "girl":
            either_girl += 1

    logging.info(
        "%r", "P(both | older): {}".format(both_girls / older_girl)
    )  # 0.514 ~ 1/2)
    logging.info(
        "%r", "P(both | either): {}".format(both_girls / either_girl)
    )  # 0.342 ~ 1/3)
