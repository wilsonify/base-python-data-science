import logging
import random
from logging.config import dictConfig

from dsl.c06_probability.c01_kid import simulate


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
