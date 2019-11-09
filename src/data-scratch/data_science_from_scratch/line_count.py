# line_count.py
import logging
import sys
from logging.config import dictConfig

from data_science_from_scratch import config

if __name__ == "__main__":
    dictConfig(config.logging_config_dict)
    count = 0
    for line in sys.stdin:
        count += 1

    # print goes to sys.stdout
    logging.info("%r", "".format(count))
