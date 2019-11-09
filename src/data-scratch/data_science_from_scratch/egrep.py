# egrep.py
import re
import sys
from logging.config import dictConfig

from data_science_from_scratch import config

if __name__ == "__main__":
    dictConfig(config.logging_config_dict)  # sys.argv is the list of command-line arguments
    # sys.argv[0] is the name of the program itself
    # sys.argv[1] will be the regex specfied at the command line
    regex = sys.argv[1]

    # for every line passed into the script
    for line in sys.stdin:
        # if it matches the regex, write it to stdout
        if re.search(regex, line):
            sys.stdout.write(line)
