import logging
import random
from logging.config import dictConfig

from dsl.probability import random_kid

if __name__ == "__main__":
    dictConfig(dict(
        version=1,
        formatters={"simple": {"format": """%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"""}},
        handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
        root={"handlers": ["console"], "level": logging.DEBUG},
    ))  #
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
