Console Validation & Decision Programs (Python)
Overview

This repository contains a collection of beginner-friendly Python console programs focused on input validation, control flow, and decision-making logic.
Each program runs independently and demonstrates real-world scenarios such as age validation, login authentication, loan eligibility checks, and expense monitoring.

All programs are written using standard Python libraries only, making them easy to run in any Python environment.

Programs Included
1. Age Validator

Validates a user’s age and determines voting eligibility in Nigeria.

Key Features
* Accepts user input safely

* Handles empty and invalid input

* Allows quitting the program at any time

* Uses age-based decision logic

Outcome
- Confirms whether the user is eligible to vote (18+)

2. Login Flow System
A simple username and password authentication system.

Key Features
* Username validation (letters only)

* Password validation (alphanumeric only)

* Secure exit handling

* Credential comparison against predefined values

Outcome
- Grants or denies access based on correct credentials

3. Loan Eligibility Checker

Determines whether a user qualifies for a loan based on multiple conditions.

Validation Steps
+ Age requirement (18+)

+ Employment status

+ Monthly income threshold

+ Debt-to-income ratio

+ Requested loan amount

Outcome
- Approves or denies loan eligibility with clear reasons

4. Expense Checker

Evaluates expenses against a defined financial threshold.

Key Features
* Accepts numeric input only

* Handles large monetary values

* Compares expenses to a fixed threshold limit

Outcome
- Indicates whether expenses are below, equal to, or above the threshold

How to Run the Programs
Prerequisites:

Python 3.7 or higher

Command-line interface (Terminal, Command Prompt, Git Bash, etc.)

Steps
Save any program into a .py file

Example:
age_validator.py, login_flow.py, loan_checker.py, expense_tracker.py

Open your terminal and navigate to the file location:
cd path/to/your/file

Run the program:
python age_validator.py

Follow the on-screen prompts.

Exit Commands

All programs support safe exit commands:
- q
- quit

Entering either command will immediately terminate the program.

Required Libraries
These programs use only built-in Python libraries:
* sys — for safe program termination using sys.exit()

No external dependencies are required.