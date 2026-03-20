# Student Score Analyzer

## Overview
This Python program allows users to enter student names and scores, stores the data in a CSV file, calculates the class average, and identifies the top performer(s) with the highest score.

## Features
- Input multiple students’ names and scores.
- Validates input to prevent errors (empty names, invalid scores, negative numbers, scores above 100).
- Stores data in `students.csv`.
- Calculates class average.
- Identifies top performer(s).
- Handles CSV read/write errors gracefully.

## Requirements
- Python 3.x
- Built-in Python libraries: `csv`, `sys` (no external libraries required)

## How to Run
1. Make sure Python 3 is installed on your system.
2. Download the script `student_score_analyzer.py`.
3. Open terminal or command prompt.
4. Navigate to the folder containing the script.
5. Run the program:
```bash
python student_score_analyzer.py