#!/usr/bin/env python
"""
count lines from stdin, write count to stdout
"""

import sys
from data_science_from_scratch import config


def main():
    count = 0
    for line in sys.stdin:
        count += 1
    print(count)  # print goes to sys.stdout


if __name__ == "__main__":
    main()
