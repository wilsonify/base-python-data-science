"""
If you run your Python scripts at the command line,
you can pipe data through them using sys.stdin and sys.stdout.
reads in lines of text and spit back the ones that match a regular expression
"""

import re
import sys
from logging.config import dictConfig

from data_science_from_scratch import config


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
    dictConfig(config.LOGGING_CONFIG_DICT)
    regex = sys.argv[1] if len(sys.argv) > 1 else ""  # sys.argv[0] is the name of the program itself
    main(regex)
