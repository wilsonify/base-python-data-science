#!/usr/bin/env python
"""
If you run your Python scripts at the command line,
then you can pipe data through them via stdin and stdout.
reads in lines of text and spit back the ones that match a regular expression
"""

import logging
import re
import sys
from logging.config import dictConfig

from dsl import logging_config_dict


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
    dictConfig(logging_config_dict)
    logging.info(f"{sys.argv[0]}")
    regex = sys.argv[1] if len(sys.argv) > 1 else ""  # sys.argv[0] is the name of the program itself
    main(regex)
