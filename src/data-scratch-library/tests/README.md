# Test Runner for Data Science from Scratch

This directory contains a custom test runner that works without pytest. All tests have been converted to work with the standalone runner.

## Usage

### Run all tests
```bash
python test_runner.py
```

### Run a specific test file
```bash
python test_runner.py test_c01_intro/test_c01_user.py
```

### Run with verbose output
```bash
python test_runner.py -v
```

### Run tests from a specific directory
```bash
python test_runner.py --dir /path/to/tests
```

## Features

- **No pytest dependency**: The runner provides replacements for pytest features
- **Parametrized tests**: Supports `@parametrize` decorator (equivalent to `@pytest.mark.parametrize`)
- **Skip functionality**: Supports `@skip` decorator (equivalent to `@pytest.mark.skip`)
- **Approx assertions**: Provides `Approx` class for floating point comparisons
- **Test discovery**: Automatically finds all `test_*.py` files in subdirectories
- **Clear reporting**: Shows pass/fail/skip counts and detailed error messages

## Test Structure

Tests follow the standard pytest conventions:
- Test functions start with `test_`
- Test files start with `test_`
- Use `assert` statements for assertions
- Import from `test_runner` for special features:

```python
from test_runner import parametrize, Approx, skip

@parametrize("input,expected", [(1, 2), (3, 4)])
def test_example(input, expected):
    assert input + 1 == expected

@skip(reason="test takes too long")
def test_slow():
    # slow test code
    pass

def test_floating_point():
    assert 1.001 == Approx(1.0, abs=0.01)
```

## Migration from pytest

The tests were migrated from pytest by:
1. Replacing `import pytest` with `from test_runner import parametrize, Approx, skip`
2. Replacing `@pytest.mark.parametrize` with `@parametrize`
3. Replacing `@pytest.mark.skip` with `@skip`
4. Replacing `pytest.approx` with `Approx`
5. Adding `if __name__ == "__main__"` blocks to individual test files
6. Converting pytest fixtures to regular functions

## Output

The runner provides clear output showing:
- Individual test results (PASS/FAIL/SKIP)
- Error messages for failed tests
- Summary statistics
- Overall success/failure status
