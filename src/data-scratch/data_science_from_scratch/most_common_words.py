# most_common_words.py
import logging
import sys
from collections import Counter
from logging.config import dictConfig

from data_science_from_scratch import config

if __name__ == "__main__":
    dictConfig(config.LOGGING_CONFIG_DICT)  # pass in number of words as first argument
    try:
        num_words = int(sys.argv[1])
    except IndexError:
        logging.info("%r", "".format("usage: most_common_words.py num_words"))
        sys.exit(1)  # non-zero exit code indicates error

    counter = Counter(
        word.lower() for line in sys.stdin for word in line.strip().split() if word
    )

    for word, count in counter.most_common(num_words):
        sys.stdout.write(str(count))
        sys.stdout.write("\t")
        sys.stdout.write(word)
        sys.stdout.write("\n")
