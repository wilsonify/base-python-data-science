import os
import sys

# Ensure local subpackages under src/ are importable during tests.
ROOT = os.path.dirname(__file__)
SRC_DIR = os.path.join(ROOT, 'src')

if os.path.isdir(SRC_DIR):
    for entry in os.listdir(SRC_DIR):
        full = os.path.join(SRC_DIR, entry)
        if os.path.isdir(full) and full not in sys.path:
            # insert at front so local packages shadow globally installed ones
            sys.path.insert(0, full)
