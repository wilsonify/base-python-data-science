#!/usr/bin/env python3
"""
Test runner that works without pytest.
Can run individual test files or all tests in the directory.
"""

import os
import sys
import importlib.util
import inspect
import traceback
from pathlib import Path
import argparse
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


class Approx:
    """Replacement for pytest.approx"""
    def __init__(self, expected, abs=0.0):
        self.expected = expected
        self.abs_tol = abs
    
    def __eq__(self, actual):
        if isinstance(self.expected, (int, float)) and isinstance(actual, (int, float)):
            return abs(actual - self.expected) <= self.abs_tol
        return False
    
    def __repr__(self):
        return f"Approx({self.expected}, abs={self.abs_tol})"


def parametrize(*args):
    """Replacement for pytest.mark.parametrize decorator"""
    def decorator(func):
        # Store parametrize data on the function
        func._parametrize_args = args
        return func
    return decorator


def skip(reason):
    """Replacement for pytest.mark.skip decorator"""
    def decorator(func):
        func._skip_reason = reason
        return func
    return decorator


# Create a mock pytest module
class MockPytest:
    approx = Approx
    mark = type('MockMark', (), {'parametrize': parametrize, 'skip': skip})()


# Inject mock pytest into sys.modules
sys.modules['pytest'] = MockPytest()


class TestRunner:
    def __init__(self, test_dir=None):
        if test_dir is None:
            test_dir = Path(__file__).parent
        self.test_dir = Path(test_dir)
        self.results = {
            'passed': 0,
            'failed': 0,
            'skipped': 0,
            'total': 0
        }
    
    def load_module_from_file(self, file_path):
        """Load a Python module from a file path"""
        spec = importlib.util.spec_from_file_location("test_module", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    
    def run_test_function(self, func, *args, **kwargs):
        """Run a single test function and return result"""
        test_name = func.__name__
        
        # Check if test should be skipped
        if hasattr(func, '_skip_reason'):
            logger.info(f"SKIP {test_name}: {func._skip_reason}")
            self.results['skipped'] += 1
            return True, None
        
        try:
            func(*args, **kwargs)
            logger.info(f"PASS {test_name}")
            self.results['passed'] += 1
            return True, None
        except AssertionError as e:
            logger.error(f"FAIL {test_name}: {e}")
            self.results['failed'] += 1
            return False, str(e)
        except Exception as e:
            logger.error(f"ERROR {test_name}: {e}")
            logger.error(traceback.format_exc())
            self.results['failed'] += 1
            return False, str(e)
    
    def run_parametrized_test(self, func, param_args):
        """Run a parametrized test function"""
        param_names, param_values = param_args[0], param_args[1]
        
        for i, values in enumerate(param_values):
            test_name = f"{func.__name__}[{i}]"
            try:
                func(*values)
                logger.info(f"PASS {test_name}")
                self.results['passed'] += 1
            except AssertionError as e:
                logger.error(f"FAIL {test_name}: {e}")
                self.results['failed'] += 1
            except Exception as e:
                logger.error(f"ERROR {test_name}: {e}")
                logger.error(traceback.format_exc())
                self.results['failed'] += 1
    
    def run_module_tests(self, module):
        """Run all test functions in a module"""
        for name, obj in inspect.getmembers(module):
            if inspect.isfunction(obj) and name.startswith('test_'):
                self.results['total'] += 1
                
                # Check if parametrized
                if hasattr(obj, '_parametrize_args'):
                    self.run_parametrized_test(obj, obj._parametrize_args)
                else:
                    self.run_test_function(obj)
    
    def run_file(self, file_path):
        """Run all tests in a single file"""
        logger.info(f"Running tests in {file_path}")
        try:
            module = self.load_module_from_file(file_path)
            self.run_module_tests(module)
        except Exception as e:
            logger.error(f"Failed to load {file_path}: {e}")
            logger.error(traceback.format_exc())
    
    def find_test_files(self):
        """Find all test files in the test directory"""
        test_files = []
        
        # Find all Python files starting with test_ in subdirectories
        for root, dirs, files in os.walk(self.test_dir):
            for file in files:
                if file.startswith('test_') and file.endswith('.py'):
                    test_files.append(Path(root) / file)
        
        return sorted(test_files)
    
    def run_all_tests(self):
        """Run all tests in the test directory"""
        test_files = self.find_test_files()
        
        if not test_files:
            logger.warning("No test files found")
            return
        
        logger.info(f"Found {len(test_files)} test files")
        
        for test_file in test_files:
            self.run_file(test_file)
        
        self.print_summary()
    
    def print_summary(self):
        """Print test results summary"""
        logger.info("\n" + "="*50)
        logger.info("TEST SUMMARY")
        logger.info("="*50)
        logger.info(f"Total:  {self.results['total']}")
        logger.info(f"Passed: {self.results['passed']}")
        logger.info(f"Failed: {self.results['failed']}")
        logger.info(f"Skipped: {self.results['skipped']}")
        
        if self.results['failed'] == 0:
            logger.info("✅ All tests passed!")
        else:
            logger.error(f"❌ {self.results['failed']} test(s) failed")
    
    def run_specific_file(self, file_path):
        """Run tests in a specific file"""
        if not os.path.exists(file_path):
            logger.error(f"File not found: {file_path}")
            return
        
        self.run_file(file_path)
        self.print_summary()


def main():
    parser = argparse.ArgumentParser(description='Run tests without pytest')
    parser.add_argument('file', nargs='?', help='Specific test file to run')
    parser.add_argument('--dir', help='Test directory to scan', default=None)
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    runner = TestRunner(args.dir)
    
    if args.file:
        runner.run_specific_file(args.file)
    else:
        runner.run_all_tests()


if __name__ == "__main__":
    main()
