from pathlib import Path
import sys


def _prepend_once(path: Path) -> None:
    resolved = str(path.resolve())
    if resolved not in sys.path:
        sys.path.insert(0, resolved)


# Keep imports stable no matter where pytest is launched from.
REPO_ROOT = Path(__file__).resolve().parents[3]
_prepend_once(REPO_ROOT / "src" / "rest-scratch-flask")
_prepend_once(REPO_ROOT / "src" / "data-scratch-library")