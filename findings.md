FINDINGS – signi_rest_test_runner Internship Challenge

This document summarizes the bugs, issues, and limitations I encountered while setting up and testing the provided REST API test runner. It also outlines how I diagnosed and solved them, along with improvements made during the bonus task.

ISSUE 1: Missing `main.py`

PROBLEM:

The challenge instructions mentioned running `main.py`, but no such file existed in the project.

OBSERVATION:

The only files available were:
- `runner.py`
- `executor.py`
- `validator.py`

There was no clear "entry point" to the program.

FIX: 

- I created a custom `main.py` file in the root folder
- It accepts a YAML scenario file as an argument and executes the test

USAGE EXAMPLE:

poetry run python main.py test_scenario.yaml


ISSUE 2: Test Runner – getaddrinfo Error

PROBLEM:

Running the test runner gave this error:
httpx.ConnectError: [Errno 11001] getaddrinfo failed

CAUSE:

This occurred because the Flask API server was not running when the test was triggered.

FIX:

Started the sample API first using:

poetry run python sample_api/app.py
Then ran the test runner in a separate terminal window.
After that, the connection worked.


ISSUE 3: No Output Message on Success message

PROBLEM:

Even when the API returned the correct response, the runner only printed:

Validating step: Check Hello Message
No indication of success or failure was shown.

FIX:

Updated runner.py to compare actual vs expected values
Added clear output using PASS and FAIL symbols

NEW OUTPUT EXAMPLE:

PASS: Check Hello Message

BONUS FIXES AND IMPROVEMENTS:

 1. Step Name Was Missing (Unnamed Step)

PROBLEM:

Test runner output said:

PASS: Unnamed Step

CAUSE:

The result dictionary used the key 'step' instead of 'name'.

FIX:

Changed 'step' to 'name' in executor.py

Also updated validator.py to read 'name'

 Now the step name displays correctly in all output.

2. Added main.py

REASONING:

The project expected a main.py, but none was provided. To make the project easier to run and align with standard practice, I created one.

How It Helps:

Users can now run tests with:


poetry run python main.py test_scenario.yaml
Internally, it performs the same tasks as runner.py, but with clearer structure and CLI support.

 3. Added Screenshot and Logs

Saved terminal test output in: test_results/output.txt

Added a screenshot showing test pass screenshot.png



All issues I faced were fixed using logical debugging, documentation, and guidance tools like ChatGPT 

I also did the required steps by improving the test runner and creating missing components like main.py.

This solution is complete, functional, and demonstrates my ability to solve real-world development challenges.

## AI & Development Tools Used

To complete this challenge, I used CHATGPT (by OpenAI) as a continuous learning and development assistant. 
chatgpt helped me understand unfamiliar concepts, make sense of errors, and helps complete each task .
     - Helped me troubleshoot Python and pip setup issues when Poetry installation failed.

     - Guided me through the folder structure and explained how `runner.py` works.

     - Suggested the logic to add PASS/FAIL output in the test runner.

     - Helped create the missing `main.py` file to make the project more complete.


All code was written in real-time under AI guidance. I actively followed, learned, and understood every step. Alongside ChatGPT, I used **Visual Studio Code** as my development environment, **Git and GitHub** for version control, **Poetry** for dependency management, and **Flask** to build and test the sample API. This approach allowed me to complete the challenge successfully while gaining practical development experience.

