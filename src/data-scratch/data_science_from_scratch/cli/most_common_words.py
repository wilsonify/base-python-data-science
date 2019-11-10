#!/usr/bin/env python
"""
counts the words in stdin and writes the most common ones to stdout

example:

```sh
cat the_bible.txt | python most_common_words.py 10
```
outputs:
64193   the
51380   and
34753   of
13643   to
12799   that
12560   in
10263   he
9840    shall
8987    unto
8836    for
"""

import sys
from collections import Counter


def main(num_words):
    counter = Counter(
        word.lower() for line in sys.stdin for word in line.strip().split() if word
    )

    for word, count in counter.most_common(num_words):
        sys.stdout.write(str(count))
        sys.stdout.write("\t")
        sys.stdout.write(word)
        sys.stdout.write("\n")


if __name__ == "__main__":
    num_words = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    main()
