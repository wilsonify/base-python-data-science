"""
Test cases for metrics module in metrics.py.
"""

def test_slice_assignment():
    """Test slice assignment vs regular assignment"""
    # Test from metrics.py demonstrating slice assignment behavior
    tensor = [[1, 2], [3, 4]]
    
    # Regular assignment doesn't update the original list
    for row in tensor:
        row = [0, 0]
    assert tensor == [[1, 2], [3, 4]], "assignment doesn't update a list"
    
    # Slice assignment does update the original list
    for row in tensor:
        row[:] = [0, 0]
    assert tensor == [[0, 0], [0, 0]], "but slice assignment does"

if __name__ == "__main__":
    from test_runner import TestRunner
    runner = TestRunner()
    runner.run_file(__file__)
