import logging
import random
from logging.config import dictConfig

from dsl.c06_probability.probability import random_kid


def simulate():
    both_girls = 0
    older_girl = 0
    either_girl = 0
    for _ in range(10000):
        younger = random_kid()
        older = random_kid()
        if older == "girl":
            older_girl += 1
        if older == "girl" and younger == "girl":
            both_girls += 1
        if older == "girl" or younger == "girl":
            either_girl += 1
    eps = 0.001
    both_girls_given_older = both_girls / (older_girl + eps)
    both_girls_given_older = round(both_girls_given_older, 4)
    both_girls_given_either = both_girls / (either_girl + eps)
    both_girls_given_either = round(both_girls_given_either, 4)
    return both_girls_given_either, both_girls_given_older


def main():
    # CONDITIONAL PROBABILITY
    random.seed(0)
    both_girls_given_either, both_girls_given_older = simulate()
    logging.info("%r", f"P(both | older): {both_girls_given_older}")  # 0.514 ~ 1/2)
    logging.info("%r", f"P(both | either): {both_girls_given_either}")  # 0.342 ~ 1/3)


if __name__ == "__main__":
    dictConfig(dict(
        version=1,
        formatters={"simple": {"format": """%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"""}},
        handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
        root={"handlers": ["console"], "level": logging.DEBUG},
    ))
    main()
