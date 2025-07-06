#  Bonus Improvements – Reasoning & Implementation

This document outlines the optional improvements made to the original test runner as part of the bonus step in the coding challenge.


## Added Pass/Fail Output to Test Runner

###  Problem

The original test runner only displayed:
Validating step: <step name>

This made it unclear whether the test step passed or failed, especially when the API response matched the expected result silently.

###  Reasoning

A good test runner should clearly indicate whether each test step has passed or failed. This helps to quickly identify issues without manually comparing expected and actual outputs.

###  Solution

- Modified `runner.py` and `main.py` to compare `expected` and `actual` values for each test step.
- Added output that prints either:
PASS: <Step Name>

or

FAIL: <Step Name>

##  Fixed Missing Step Name ("Unnamed Step")

###  Problem

The output previously showed:
PASS: Unnamed Step

This was due to the test result object missing the `name` field, falling back to a default label.

###  Reasoning

Each test step should display a meaningful name so that it can easily identify which part of the test scenario succeeded or failed.

###  Solution

- Updated `executor.py` to attach the original step name to the result dictionary using the `name` key.
- Modified `runner.py` and `validator.py` to reference `result["name"]` instead of `result["step"]` or unnamed fallback.

## Added missing main.py

###  Problem

Project expected `main.py` as a CLI entry point, but no file was provided.

###  Reasoning

A typical Python CLI project starts from `main.py`. Adding it makes the project easier to run and aligns with standard structure.

###  Solution
- Created `main.py` in root folder
- Accepts YAML file as argument
- Runs the test and prints results

###  Usage

poetry run python main.py test_scenario.yaml

**After these improvements:**

  The test runner now shows clear PASS / FAIL status for each test step.

  Each step prints the correct test name, avoiding confusion.

  The project has a proper main.py entry point for easier testing.

  All updates are documented and committed with meaningful messages.