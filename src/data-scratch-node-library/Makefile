# Makefile for TypeScript Data Science Library
# Provides convenient commands for building, testing, and development

# Variables
NODE_BIN = node
NPM_BIN = npm
NPX_BIN = npx
TSC_BIN = $(NPX_BIN) tsc
JEST_BIN = $(NPX_BIN) jest
TS_NODE_BIN = $(NPX_BIN) ts-node

# Directories
SRC_DIR = ts-data-scratch
TEST_DIR = tests
DIST_DIR = dist
EXAMPLES_DIR = $(SRC_DIR)/deep_learning/examples

# Files
MAIN_ENTRY = $(SRC_DIR)/index.ts
BUILD_CONFIG = tsconfig.json
TEST_CONFIG = tsconfig.test.json

# Default target
.PHONY: all
all: clean install build test

# Install dependencies
.PHONY: install
install:
	@echo "📦 Installing dependencies..."
	$(NPM_BIN) install

# Clean build artifacts
.PHONY: clean
clean:
	@echo "🧹 Cleaning build artifacts..."
	rm -rf $(DIST_DIR)
	rm -rf dist-test
	rm -rf coverage
	rm -rf .nyc_output
	find . -name "*.js" -path "./$(SRC_DIR)/*" -delete
	find . -name "*.js.map" -path "./$(SRC_DIR)/*" -delete

# Build the project
.PHONY: build
build:
	@echo "🔨 Building TypeScript project..."
	$(TSC_BIN) --project $(BUILD_CONFIG)

# Build with verbose output
.PHONY: build-verbose
build-verbose:
	@echo "🔨 Building TypeScript project (verbose)..."
	$(TSC_BIN) --project $(BUILD_CONFIG) --listFiles

# Type check without emitting files
.PHONY: type-check
type-check:
	@echo "🔍 Running TypeScript type check..."
	$(TSC_BIN) --noEmit --project $(BUILD_CONFIG)

# Run all tests
.PHONY: test
test:
	@echo "🧪 Running all tests..."
	$(NPM_BIN) test

# Run tests with coverage
.PHONY: test-coverage
test-coverage:
	@echo "📊 Running tests with coverage..."
	$(NPM_BIN) run test:coverage

# Run deep learning tests specifically
.PHONY: test-deep-learning
test-deep-learning:
	@echo "🤖 Running deep learning tests..."
	$(JEST_BIN) $(TEST_DIR)/deep_learning

# Run neural network tests
.PHONY: test-neural-networks
test-neural-networks:
	@echo "🧠 Running neural network tests..."
	$(JEST_BIN) $(TEST_DIR)/neural-networks.test.ts

# Run tests in watch mode
.PHONY: test-watch
test-watch:
	@echo "👀 Running tests in watch mode..."
	$(JEST_BIN) --watch

# Development build (watch mode)
.PHONY: dev
dev:
	@echo "🔄 Starting development build (watch mode)..."
	$(TSC_BIN) --project $(BUILD_CONFIG) --watch

# Run examples
.PHONY: examples
examples: build
	@echo "🚀 Running deep learning examples..."
	@echo "📊 XOR Example:"
	$(TS_NODE_BIN) $(EXAMPLES_DIR)/xor_example.ts
	@echo ""
	@echo "🔢 FizzBuzz Example:"
	$(TS_NODE_BIN) $(EXAMPLES_DIR)/fizzbuzz_example.ts

# Run XOR example only
.PHONY: example-xor
example-xor: build
	@echo "📊 Running XOR example..."
	$(TS_NODE_BIN) $(EXAMPLES_DIR)/xor_example.ts

# Run FizzBuzz example only
.PHONY: example-fizzbuzz
example-fizzbuzz: build
	@echo "🔢 Running FizzBuzz example..."
	$(TS_NODE_BIN) $(EXAMPLES_DIR)/fizzbuzz_example.ts

# Lint the code
.PHONY: lint
lint:
	@echo "🔍 Running ESLint..."
	$(NPM_BIN) run lint || echo "ESLint not configured, skipping..."

# Format the code
.PHONY: format
format:
	@echo "✨ Formatting code with Prettier..."
	$(NPM_BIN) run format || echo "Prettier not configured, skipping..."

# Check for outdated dependencies
.PHONY: outdated
outdated:
	@echo "📋 Checking for outdated dependencies..."
	$(NPM_BIN) outdated

# Update dependencies
.PHONY: update
update:
	@echo "⬆️ Updating dependencies..."
	$(NPM_BIN) update

# Audit dependencies for security issues
.PHONY: audit
audit:
	@echo "🔒 Auditing dependencies for security issues..."
	$(NPM_BIN) audit

# Fix security issues
.PHONY: audit-fix
audit-fix:
	@echo "🔧 Fixing security issues..."
	$(NPM_BIN) audit fix

# Generate documentation
.PHONY: docs
docs:
	@echo "📚 Generating documentation..."
	$(NPM_BIN) run docs || echo "Documentation generation not configured, skipping..."

# Start local development server (if applicable)
.PHONY: serve
serve:
	@echo "🌐 Starting development server..."
	$(NPM_BIN) run serve || echo "Development server not configured, skipping..."

# Create a new build for production
.PHONY: build-prod
build-prod: clean install build test
	@echo "🏭 Production build complete!"

# Quick development cycle (clean -> install -> build -> test)
.PHONY: dev-cycle
dev-cycle: clean install build test
	@echo "✅ Development cycle complete!"

# Continuous integration target
.PHONY: ci
ci: install build test type-check
	@echo "✅ CI pipeline complete!"

# Show project information
.PHONY: info
info:
	@echo "📋 TypeScript Data Science Library Information:"
	@echo "   Node.js version: $(shell $(NODE_BIN) --version)"
	@echo "   npm version: $(shell $(NPM_BIN) --version)"
	@echo "   TypeScript version: $(shell $(TSC_BIN) --version)"
	@echo "   Jest version: $(shell $(JEST_BIN) --version)"
	@echo "   Source directory: $(SRC_DIR)"
	@echo "   Test directory: $(TEST_DIR)"
	@echo "   Build directory: $(DIST_DIR)"

# Help target
.PHONY: help
help:
	@echo "📖 TypeScript Data Science Library Makefile"
	@echo ""
	@echo "Available targets:"
	@echo "  all              - Clean, install, build, and test (default)"
	@echo "  install          - Install npm dependencies"
	@echo "  clean            - Remove build artifacts"
	@echo "  build            - Build TypeScript project"
	@echo "  build-verbose    - Build with verbose output"
	@echo "  type-check       - Run TypeScript type checking"
	@echo "  test             - Run all tests"
	@echo "  test-coverage    - Run tests with coverage report"
	@echo "  test-deep-learning - Run deep learning tests only"
	@echo "  test-neural-networks - Run neural network tests only"
	@echo "  test-watch       - Run tests in watch mode"
	@echo "  dev              - Start development build (watch mode)"
	@echo "  examples         - Run all deep learning examples"
	@echo "  example-xor      - Run XOR example"
	@echo "  example-fizzbuzz - Run FizzBuzz example"
	@echo "  lint             - Run ESLint (if configured)"
	@echo "  format           - Format code with Prettier (if configured)"
	@echo "  outdated         - Check for outdated dependencies"
	@echo "  update           - Update dependencies"
	@echo "  audit            - Audit for security issues"
	@echo "  audit-fix        - Fix security issues"
	@echo "  docs             - Generate documentation (if configured)"
	@echo "  serve            - Start development server (if configured)"
	@echo "  build-prod       - Create production build"
	@echo "  dev-cycle        - Quick development cycle"
	@echo "  ci               - Continuous integration pipeline"
	@echo "  info             - Show project information"
	@echo "  help             - Show this help message"
	@echo ""
	@echo "Examples:"
	@echo "  make all              # Complete build and test"
	@echo "  make dev              # Start development mode"
	@echo "  make test-deep-learning # Test only deep learning"
	@echo "  make examples         # Run all examples"
