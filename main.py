import pytest


def run_tests():
    """Function to run all test cases"""
    pytest.main(["tests"])


def generate_report():
    """Function to generate test report"""
    pytest.main(["tests", "--html=test_report.html"])


if __name__ == "__main__":
    run_tests()
    generate_report()
