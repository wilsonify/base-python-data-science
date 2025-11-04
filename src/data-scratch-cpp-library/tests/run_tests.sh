#!/bin/bash

# Test runner script for C++ Data Science Library
# This script builds and runs all tests with detailed reporting

set -e  # Exit on any error

echo "🧪 C++ Data Science Library Test Runner"
echo "=========================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if we're in the right directory
if [ ! -f "CMakeLists.txt" ]; then
    print_error "CMakeLists.txt not found. Please run this script from the tests directory."
    exit 1
fi

# Clean previous builds
print_status "Cleaning previous builds..."
rm -rf build
mkdir -p build

# Configure with CMake
print_status "Configuring build with CMake..."
cd build
if ! cmake ..; then
    print_error "CMake configuration failed"
    exit 1
fi

# Build the tests
print_status "Building tests..."
if ! make -j$(nproc 2>/dev/null || echo 4); then
    print_error "Build failed"
    exit 1
fi

print_success "Build completed successfully"

# Run tests with detailed output
print_status "Running all tests..."
echo ""

# Run each test suite separately for better reporting
test_suites=(
    "LinearAlgebraTest:Linear Algebra Module"
    "StatisticsTest:Statistics Module"
    "ProbabilityTest:Probability Module"
    "MachineLearningTest:Machine Learning Utilities"
    "KNNTest:K-Nearest Neighbors"
)

total_passed=0
total_failed=0

for suite_info in "${test_suites[@]}"; do
    IFS=':' read -r test_name description <<< "$suite_info"
    
    echo -e "${BLUE}Testing $description...${NC}"
    echo "----------------------------------------"
    
    if ./test-data-scratch-cpp --gtest_filter="$test_name" --gtest_color=yes; then
        print_success "$description tests passed"
        ((total_passed++))
    else
        print_error "$description tests failed"
        ((total_failed++))
    fi
    
    echo ""
done

# Run all tests together for final summary
print_status "Running complete test suite..."
echo "========================================"

if ./test-data-scratch-cpp --gtest_color=yes --gtest_print_time=yes; then
    print_success "All tests completed successfully!"
    exit_code=0
else
    print_warning "Some tests failed. See output above for details."
    exit_code=1
fi

# Generate coverage report if available
if command -v lcov &> /dev/null && [ -f "../CMakeLists.txt" ] && grep -q "ENABLE_COVERAGE" ../CMakeLists.txt; then
    print_status "Generating coverage report..."
    if make coverage 2>/dev/null; then
        print_success "Coverage report generated in build/coverage/"
        print_status "Open build/coverage/index.html in your browser to view"
    else
        print_warning "Coverage report generation failed (lcov may not be installed)"
    fi
fi

echo ""
echo "📊 Test Summary"
echo "=================="
echo "Passed suites: $total_passed"
echo "Failed suites: $total_failed"
echo "Total suites: $((total_passed + total_failed))"

if [ $exit_code -eq 0 ]; then
    print_success "🎉 All tests passed! The C++ Data Science Library is ready for use."
else
    print_error "❌ Some tests failed. Please review the failures above."
fi

exit $exit_code
