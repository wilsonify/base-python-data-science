#!/usr/bin/env python
"""
If you run your Python scripts at the command line,
you can pipe data through them using sys.stdin and sys.stdout.
reads in lines of text and spit back the ones that match a regular expression
"""

import logging
import re
import sys
from logging.config import dictConfig

LOGGING_CONFIG_DICT = dict(
    version=1,
    formatters={"simple": {"format": """%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"""}},
    handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
    root={"handlers": ["console"], "level": logging.DEBUG},
)


def main(regex):
    """
    reads in lines of text and spit back the ones that match a regular expression
    :param regex:
    :return:
    """
    for line in sys.stdin:
        if re.search(regex, line):
            sys.stdout.write(line)


if __name__ == "__main__":
    dictConfig(LOGGING_CONFIG_DICT)
    logging.info(f"{sys.argv[0]}")
    regex = sys.argv[1] if len(sys.argv) > 1 else ""  # sys.argv[0] is the name of the program itself
    main(regex)
