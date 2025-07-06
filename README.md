# Signi5sys Internship Coding Challenge – REST Test Runner

 Project: REST API Test Runner  
 Status: Completed (with bonus step)


This repository is part of the coding challenge for the Signi5sys internship. The goal was to explore and debug a Python-based REST API test runner, improve its output handling, and document the entire development process. As part of the task, I also built a sample Flask API, ran the test runner against it, and completed bonus improvements.


## Tech Stack & Tools Used

- **Python 3.13** – Primary programming language  
- **Poetry** – Dependency management  
- **Flask** – Used to build the sample API  
- **VS Code** – Code editor  
- **Git & GitHub** – Version control & collaboration  
- **ChatGPT (OpenAI)** – Learning and debugging assistant (disclosed below)


## Prerequisites

The following tools are installed:

Python 3.13+
pip install poetry

## Cloned the repository

git clone <my-private-repo-url>
cd signi_rest_test_runner

## Installed dependencies

poetry install

## Run the sample API

Start the test API server:

poetry run python sample_api/app.py
Navigate to: http://127.0.0.1:5000/hello

## Run the test runner

Opened a new terminal and run:
poetry run python src/signi_rest_test_runner/runner.py test_scenario.yaml

**Sample Output**

PASS: Check Hello Message
Validating step: Check Hello Message

## project structure

This repo contains the following folders and files:

  - `sample_api/`: The simple Flask API with  a `/hello` route
  - `test_results/`:  Logs and screenshot from the test run
  - `test_scenario.yaml`: The test case file
  - `main.py`: Entry point to run the test
  - `findings.md`: Issues, fixes, and improvements

## Improvements & Fixes (Bonus Completed)

-  Added PASS/FAIL success/failure output in runner.py
-  Fixed missing step name (Unnamed Step)

-  Created a working main.py to act as entry point

-  Created detailed documentation (README.md, findings.md, bonus_notes.md)

-  Included output logs and a screenshot of successful test run

All of these are documented in findings.md and bonus_notes.md.

## AI Assistance Disclosure

This project was completed with the assistance of ChatGPT (by OpenAI), which was used as a learning and debugging assistant. It helped me through environment setup, project structure, debugging errors, and implementing improvements. All code was reviewed, tested, and understood by me before applying. AI was used strictly as a support tool for learning and not for direct code generation.

