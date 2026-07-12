# AI Agent Guidance — Base Python Data Science

## Python Environment

- **The project virtual environment is at `.venv/`** in the repo root.
- Dependencies in `requirements.txt` — install with:

  ```bash
  python3 -m venv .venv
  .venv/bin/pip install -r requirements.txt
  ```

## Running Commands

- **Never use the system interpreter.** Always reference `.venv/bin/`:

  ```bash
  .venv/bin/python build.py
  .venv/bin/pytest
  .venv/bin/ruff check src/
  ```

- **Do not use `source .venv/bin/activate`** in scripts or automation.

## Tests

```bash
.venv/bin/pytest
```

## Linting

```bash
.venv/bin/ruff check .
```

## VS Code

The `.vscode/settings.json` sets `python.defaultInterpreterPath` to `.venv/bin/python`.
