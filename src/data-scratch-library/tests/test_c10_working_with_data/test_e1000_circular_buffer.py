import pytest
from collections import deque

from dsl.c10_working_with_data.e1000_circular_buffer import demo_deque


# Assuming demo_deque function is imported here

def test_demo_deque_default():
    """Test the demo_deque with maxlen of 20 and 1000 iterations."""
    final_contents = demo_deque(maxlen=20, iterations=1000)
    assert len(final_contents) == 20  # Should only contain the last 20 elements
    assert final_contents == list(range(980, 1000))  # Should contain 980 to 999

def test_demo_deque_small_maxlen():
    """Test the demo_deque with a smaller maxlen."""
    final_contents = demo_deque(maxlen=5, iterations=10)
    assert len(final_contents) == 5  # Should only contain the last 5 elements
    assert final_contents == list(range(5, 10))  # Should contain 5 to 9

def test_demo_deque_zero_iterations():
    """Test the demo_deque with zero iterations."""
    final_contents = demo_deque(maxlen=20, iterations=0)
    assert len(final_contents) == 0  # Should be empty since no iterations

def test_demo_deque_equal_maxlen_iterations():
    """Test the demo_deque where maxlen equals iterations."""
    maxlen = 10
    final_contents = demo_deque(maxlen=maxlen, iterations=maxlen)
    assert len(final_contents) == maxlen  # Should contain 0 to 9
    assert final_contents == list(range(maxlen))  # Should contain 0 to 9

if __name__ == "__main__":
    pytest.main()
