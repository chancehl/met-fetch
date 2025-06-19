.PHONY: test test-verbose test-coverage test-report install-dev clean help

# Default target
help:
	@echo "Available targets:"
	@echo "  install-dev    Install development dependencies"
	@echo "  test          Run all tests"
	@echo "  test-verbose  Run tests with verbose output"
	@echo "  test-coverage Run tests with coverage report"
	@echo "  test-report   Run tests and generate HTML coverage report"
	@echo "  clean         Clean up test artifacts"
	@echo "  help          Show this help message"

# Install development dependencies
install-dev:
	pip install -r requirements-dev.txt

# Run tests
test:
	python -m pytest

# Run tests with verbose output
test-verbose:
	python -m pytest -v

# Run tests with coverage
test-coverage:
	python -m pytest --cov=src --cov-report=term-missing

# Run tests and generate HTML coverage report
test-report:
	python -m pytest --cov=src --cov-report=html:htmlcov --cov-report=term-missing
	@echo "Coverage report generated in htmlcov/index.html"

# Clean up test artifacts
clean:
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
