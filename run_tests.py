#!/usr/bin/env python3
"""
Simple test runner script for the met-fetch project.
"""
import subprocess
import sys
import os


def run_command(command, description):
    """Run a command and handle the result."""
    print(f"\n{'='*50}")
    print(f"Running: {description}")
    print(f"Command: {command}")
    print(f"{'='*50}")
    
    result = subprocess.run(command, shell=True, capture_output=False)
    
    if result.returncode != 0:
        print(f"\n❌ {description} failed with exit code {result.returncode}")
        return False
    else:
        print(f"\n✅ {description} completed successfully")
        return True


def main():
    """Main test runner function."""
    print("🧪 Met-Fetch Test Runner")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("src") or not os.path.exists("tests"):
        print("❌ Error: Please run this script from the project root directory")
        sys.exit(1)
    
    # Check if pytest is installed
    try:
        import pytest
        print(f"✅ pytest version: {pytest.__version__}")
    except ImportError:
        print("❌ pytest not found. Please install development dependencies:")
        print("   pip install -r requirements-dev.txt")
        sys.exit(1)
    
    # Run tests
    success = True
    
    # Basic test run
    if not run_command("python -m pytest tests/ -v", "Running unit tests"):
        success = False
    
    # Coverage report
    if not run_command("python -m pytest tests/ --cov=src --cov-report=term-missing", "Generating coverage report"):
        success = False
    
    print(f"\n{'='*50}")
    if success:
        print("🎉 All tests completed successfully!")
    else:
        print("❌ Some tests failed. Please check the output above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
