#!/usr/bin/env python
"""
count lines from stdin, write count to stdout
"""

import sys


def main():
    count = 0
    for _ in sys.stdin:
        count += 1
    print(count)  # print goes to sys.stdout


if __name__ == "__main__":
    main()
