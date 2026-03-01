"""
Sample data: 5×5 pixel representations of digits 0-9.
"""

from typing import List

raw_digits: List[str] = [
    """11111
       1...1
       1...1
       1...1
       11111""",
    """..1..
       ..1..
       ..1..
       ..1..
       ..1..""",
    """11111
       ....1
       11111
       1....
       11111""",
    """11111
       ....1
       11111
       ....1
       11111""",
    """1...1
       1...1
       11111
       ....1
       ....1""",
    """11111
       1....
       11111
       ....1
       11111""",
    """11111
       1....
       11111
       1...1
       11111""",
    """11111
       ....1
       ....1
       ....1
       ....1""",
    """11111
       1...1
       11111
       1...1
       11111""",
    """11111
       1...1
       11111
       ....1
       11111""",
]

INPUT_SIZE = 25
NUM_HIDDEN = 5
OUTPUT_SIZE = 10


def make_digit(raw_digit: str) -> List[int]:
    """Convert a raw digit string to a 25-element binary vector."""
    return [
        1 if c == "1" else 0
        for row in raw_digit.split("\n")
        for c in row.strip()
    ]
