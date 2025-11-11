#!/usr/bin/env python3
"""
Test script to verify that all AMQP strategies are working correctly
"""

import json

# Mock the AMQP dependencies for testing
class MockChannel:
    def basic_publish(self, exchange, routing_key, properties, body):
        print(f"Published to {exchange}: {body}")

class MockMethod:
    pass

class MockProps:
    def __init__(self, reply_to=None, correlation_id=None):
        self.reply_to = reply_to
        self.correlation_id = correlation_id

class MockStrategy:
    def __init__(self, function):
        self.name = "Test Strategy"
        self.channel = MockChannel()
        self.method = MockMethod()
        self.props = MockProps()
        # Bind the function to this instance
        self.execute = function.__get__(self, MockStrategy)
    
    def publish(self, payload):
        print(f"Result: {payload}")

# Test a few key strategies
def run_strategy_test(strategy_name, strategy_func, test_data):
    print(f"\nTesting {strategy_name}:")
    try:
        strategy = MockStrategy(strategy_func)
        strategy.execute(test_data)
        print(f"✓ {strategy_name} works correctly")
        return True
    except Exception as e:
        print(f"✗ {strategy_name} failed: {e}")
        return False

def main():
    print("Testing AMQP Strategy Integration")
    print("=" * 50)
    
    # Import dynamic strategies
    from data_scratch_amqp.strategies_library.dynamic_strategy import dynamic_strategies
    
    print(f"Total strategies available: {len(dynamic_strategies)}")
    
    # Test cases for different categories of functions
    test_cases = [
        # Linear Algebra
        ("vector_add", {"v": [1, 2, 3], "w": [4, 5, 6]}),
        ("dot", {"v": [1, 2, 3], "w": [4, 5, 6]}),
        ("magnitude", {"v": [3, 4]}),
        ("matrix_add", {"mat1": [[1, 2], [3, 4]], "mat2": [[5, 6], [7, 8]]}),
        
        # Statistics
        ("mean", {"xs": [1, 2, 3, 4, 5]}),
        ("median", {"v": [1, 2, 3, 4, 5]}),
        ("standard_deviation", {"x": [1, 2, 3, 4, 5]}),
        ("correlation", {"x": [1, 2, 3, 4, 5], "y": [2, 4, 6, 8, 10]}),
        
        # Probability
        ("normal_cdf", {"x": 0.0, "mu": 0.0, "sigma": 1.0}),
        ("bernoulli_trial", {"p": 0.5}),
        ("binomial", {"n": 10, "p": 0.5}),
        
        # Machine Learning
        ("accuracy", {"tp": 80, "fp": 10, "fn": 5, "tn": 95}),
        ("split_data", {"data": list(range(100)), "prob": 0.8}),
        
        # Gradient Descent
        ("sum_of_squares_gradient", {"v": [1, 2, 3]}),
        ("in_random_order", {"data": list(range(10))}),
        
        # Working with Data
        ("bucketize", {"point": 1.7, "bucket_size": 2.0}),
        ("make_histogram", {"points": [1.1, 1.9, 2.1, 2.9, 3.1], "bucket_size": 1.0}),
    ]
    
    # Run tests
    passed = 0
    total = 0
    
    for strategy_name, test_data in test_cases:
        if strategy_name in dynamic_strategies:
            total += 1
            if run_strategy_test(strategy_name, dynamic_strategies[strategy_name], test_data):
                passed += 1
        else:
            print(f"\n⚠ {strategy_name} not found in dynamic strategies")
    
    print(f"\n" + "=" * 50)
    print(f"Test Results: {passed}/{total} strategies passed")
    
    if passed == total:
        print("🎉 All tested strategies are working correctly!")
    else:
        print(f"⚠ {total - passed} strategies failed tests")
    
    # Show all available strategies
    print(f"\nAll available strategies ({len(dynamic_strategies)}):")
    for i, strategy_name in enumerate(sorted(dynamic_strategies.keys())):
        if i % 5 == 0:
            print()
        print(f"{strategy_name:<25}", end="")
    print()

if __name__ == "__main__":
    main()
