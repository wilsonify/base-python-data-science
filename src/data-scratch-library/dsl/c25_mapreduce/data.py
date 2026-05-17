"""
Sample data for MapReduce examples.
"""

from datetime import datetime
from typing import Any, Dict, List, Tuple

status_updates: List[Dict[str, Any]] = [
    {
        "id": 1,
        "username": "joelgrus",
        "text": "Is anyone interested in a data science book?",
        "created_at": datetime(2013, 12, 21, 11, 47, 0),
        "liked_by": ["data_guy", "data_gal", "bill"],
    },
]

A_entries: List[Tuple[str, int, int, float]] = [
    ("A", 0, 0, 3),
    ("A", 0, 1, 2),
]

B_entries: List[Tuple[str, int, int, float]] = [
    ("B", 0, 0, 4),
    ("B", 0, 1, -1),
    ("B", 1, 0, 10),
    ("B", 1, 1, 0),
]
