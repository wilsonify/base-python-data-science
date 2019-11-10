import logging
import os

import pytest
from data_science_from_scratch.library import linear_algebra

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def test_smoke():
    logging.info("is anything on fire")
