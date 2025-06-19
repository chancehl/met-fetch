# Testing Guide for met-fetch

This document provides comprehensive information about the testing setup for the met-fetch project.

## Overview

The project uses `pytest` as the testing framework with additional plugins for coverage reporting and mocking. The test suite is designed to ensure code quality and reliability.

## Test Structure

```
tests/
├── __init__.py              # Test package initialization
├── conftest.py              # Shared fixtures and configuration
└── test_report.py           # Tests for report.py module
```

## Dependencies

The testing dependencies are defined in `requirements-dev.txt`:

- `pytest==7.4.3` - Testing framework
- `pytest-cov==4.1.0` - Coverage reporting
- `pytest-mock==3.12.0` - Mocking utilities

## Installation

1. **Install development dependencies:**
   ```bash
   pip install -r requirements-dev.txt
   ```

2. **Or use the Makefile:**
   ```bash
   make install-dev
   ```

## Running Tests

### Basic Test Execution

```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_report.py

# Run with verbose output
python -m pytest -v
```

### Using the Makefile

```bash
# Run tests
make test

# Run tests with verbose output
make test-verbose

# Run tests with coverage
make test-coverage

# Generate HTML coverage report
make test-report
```

### Using the Test Runner Script

```bash
# Run the comprehensive test suite
python run_tests.py
```

## Coverage Reporting

The project is configured to maintain high test coverage:

- **Target Coverage:** 80% minimum (configurable in `pytest.ini`)
- **Coverage Reports:** Terminal output and HTML reports
- **HTML Reports:** Generated in `htmlcov/` directory

### Coverage Commands

```bash
# Terminal coverage report
python -m pytest --cov=src --cov-report=term-missing

# Generate HTML coverage report
python -m pytest --cov=src --cov-report=html:htmlcov

# Both terminal and HTML reports
make test-report
```

## Test Configuration

### pytest.ini

The `pytest.ini` file contains the main test configuration:

```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    -v
    --tb=short
    --strict-markers
    --disable-warnings
    --cov=src
    --cov-report=term-missing
    --cov-report=html:htmlcov
    --cov-fail-under=80
```

### Key Configuration Options

- **Test Discovery:** Automatically finds test files matching `test_*.py`
- **Coverage Threshold:** Tests fail if coverage drops below 80%
- **Output Format:** Verbose output with short tracebacks
- **Warnings:** Disabled for cleaner output

## Test Categories

### Unit Tests

Located in `tests/test_report.py`, these tests cover:

#### `generate_report()` Function
- ✅ Single artwork JSON generation
- ✅ Multiple artworks JSON generation  
- ✅ Empty artwork list handling
- ✅ File I/O error handling
- ✅ Integration test with actual file operations

#### `print_report_to_console()` Function
- ✅ Single artwork console output
- ✅ Multiple artworks console output
- ✅ Empty artwork list handling
- ✅ Unknown artist name handling
- ✅ Special characters in output directory

### Test Techniques Used

1. **Mocking:** Using `unittest.mock` to isolate units under test
2. **Patching:** Intercepting file operations and print statements
3. **Fixtures:** Shared test data in `conftest.py`
4. **Integration Testing:** Real file operations in temporary directories
5. **Edge Case Testing:** Empty lists, missing data, error conditions

## Writing New Tests

### Test File Structure

```python
import pytest
from unittest.mock import patch, mock_open

# Import modules under test
from your_module import your_function

class TestYourFunction:
    """Test cases for your_function."""
    
    def test_basic_functionality(self):
        """Test basic functionality."""
        # Arrange
        input_data = "test input"
        
        # Act
        result = your_function(input_data)
        
        # Assert
        assert result == "expected output"
    
    @patch("builtins.open", new_callable=mock_open)
    def test_file_operations(self, mock_file):
        """Test file operations with mocking."""
        # Test implementation
        pass
```

### Best Practices

1. **Use descriptive test names** that explain what is being tested
2. **Follow the AAA pattern** (Arrange, Act, Assert)
3. **Test edge cases** including empty inputs, None values, and error conditions
4. **Mock external dependencies** to isolate the unit under test
5. **Use fixtures** for common test data
6. **Keep tests independent** - each test should be able to run in isolation

### Adding New Test Files

1. Create test file in `tests/` directory with `test_` prefix
2. Import necessary modules and add to `sys.path` if needed:
   ```python
   import sys
   import os
   sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
   ```
3. Organize tests into classes for better structure
4. Add appropriate fixtures to `conftest.py` if needed

## Continuous Integration

The test suite is designed to be CI-friendly:

- **Exit Codes:** Non-zero exit codes on test failures
- **Coverage Enforcement:** Builds fail if coverage drops below threshold
- **Clean Output:** Minimal noise in test output
- **Fast Execution:** Tests run quickly for rapid feedback

## Troubleshooting

### Common Issues

1. **Import Errors:**
   - Ensure `src` directory is in Python path
   - Check that `__init__.py` files exist where needed

2. **Coverage Issues:**
   - Verify coverage paths in `pytest.ini`
   - Ensure modules are actually imported during tests

3. **Mock Issues:**
   - Check that patches target the correct module path
   - Verify mock assertions match actual function calls

### Debug Commands

```bash
# Run tests with full output
python -m pytest -v -s

# Run specific test with debugging
python -m pytest tests/test_report.py::TestGenerateReport::test_generate_report_single_artwork -v -s

# Show coverage details
python -m pytest --cov=src --cov-report=term-missing -v
```

## Maintenance

### Regular Tasks

1. **Update Dependencies:** Regularly update testing dependencies
2. **Review Coverage:** Ensure new code is properly tested
3. **Refactor Tests:** Keep tests maintainable as code evolves
4. **Performance:** Monitor test execution time

### Adding Coverage for New Modules

When adding new modules to the `src/` directory:

1. Create corresponding test file in `tests/`
2. Update coverage configuration if needed
3. Ensure new tests follow established patterns
4. Maintain coverage threshold

## Resources

- [pytest Documentation](https://docs.pytest.org/)
- [pytest-cov Documentation](https://pytest-cov.readthedocs.io/)
- [unittest.mock Documentation](https://docs.python.org/3/library/unittest.mock.html)
- [Python Testing Best Practices](https://docs.python-guide.org/writing/tests/)
