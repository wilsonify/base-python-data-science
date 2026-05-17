"""
Sample data: interview-outcome records for decision-tree learning.
"""

from typing import Any, Dict, List, Tuple

# Each record is (attribute_dict, hired?)
inputs_list: List[Tuple[Dict[str, str], bool]] = [
    ({"level": "Senior", "lang": "Java",   "tweets": "no",  "phd": "no"},  False),
    ({"level": "Senior", "lang": "Java",   "tweets": "no",  "phd": "yes"}, False),
    ({"level": "Mid",    "lang": "Python", "tweets": "no",  "phd": "no"},  True),
    ({"level": "Junior", "lang": "Python", "tweets": "no",  "phd": "no"},  True),
    ({"level": "Junior", "lang": "R",      "tweets": "yes", "phd": "no"},  True),
    ({"level": "Junior", "lang": "R",      "tweets": "yes", "phd": "yes"}, False),
    ({"level": "Mid",    "lang": "R",      "tweets": "yes", "phd": "yes"}, True),
    ({"level": "Senior", "lang": "Python", "tweets": "no",  "phd": "no"},  False),
    ({"level": "Senior", "lang": "R",      "tweets": "yes", "phd": "no"},  True),
    ({"level": "Junior", "lang": "Python", "tweets": "yes", "phd": "no"},  True),
    ({"level": "Senior", "lang": "Python", "tweets": "yes", "phd": "yes"}, True),
    ({"level": "Mid",    "lang": "Python", "tweets": "no",  "phd": "yes"}, True),
    ({"level": "Mid",    "lang": "Java",   "tweets": "yes", "phd": "no"},  True),
    ({"level": "Junior", "lang": "Python", "tweets": "no",  "phd": "yes"}, False),
]
