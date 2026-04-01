# Task Logger, Expense Tracker & Environment Export

## Description

This repository contains two simple Python command-line programs:

### Task Logger & Expense Tracker

This program allows users to:

* Add expenses with a description
* Automatically record the timestamp of each entry
* Store all expenses in a CSV file (`expenses.csv`)
* View a summary of total and average expenses using pandas

### Task Logger & Environment Export

This Python script allows users to:

* Input actions and log each action with a timestamp into a text file
* Export Python environment dependencies into a `requirements.txt` file using `pip freeze`

The project demonstrates basic file handling, logging, and working with Python environments.



## How to Run

### Task Logger & Expense Tracker

1. Ensure Python is installed on your system
2. Install the required library:
   pip install pandas
3. Run the program:
   python tasklogger_expensetracker.py



### Task Logger & Environment Export

1. Ensure Python is installed on your system
2. Save the script as .py file (e.g., tasklogger_env_export.py)
3. Open a terminal or command prompt in the script directory
4. Run the script using:
   python task_logger.py
5. Enter actions when prompted. Type `done` to finish

The program will:

* Save your actions with a timestamp in `track_logger_actions.txt`
* Export dependencies to `requirements.txt`



## Required Libraries

### Task Logger & Expense Tracker

* pandas

(Standard libraries used: csv, datetime, os)

### Task Logger & Environment Export

This program uses only Python standard library modules:

* datetime - for generating timestamps
* subprocess - for running the pip freeze command
* sys - to ensure the correct Python interpreter is used

No external dependencies are required.
