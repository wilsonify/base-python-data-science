"""
Test cases for model I/O operations in io.py.
"""

from dsl.c19_deep_learning.deep_learning import shape

def test_weight_loading_consistency():
    """Test that weight loading checks shape consistency"""
    # This is a conceptual test for the assertion in load_weights
    # In practice, this would test with actual model parameters
    
    # Mock model parameters and weights for testing
    mock_params = [[[1, 2], [3, 4]], [5, 6]]
    mock_weights = [[[1, 2], [3, 4]], [5, 6]]
    
    # This should pass - shapes match
    assert all(shape(param) == shape(weight)
               for param, weight in zip(mock_params, mock_weights))
    
    # This would fail - shapes don't match
    wrong_weights = [[[1, 2, 3], [4, 5, 6]], [7, 8, 9]]
    assert not all(shape(param) == shape(weight)
                   for param, weight in zip(mock_params, wrong_weights))

if __name__ == "__main__":
    from test_runner import TestRunner
    runner = TestRunner()
    runner.run_file(__file__)
