# Description
Profile Manager is a simple command-line Python application to create, view, and manage a personal profile.

This script allows users to:
* Create a personal profile (Name, Age, Email, Country)
* Validate input to prevent empty or invalid entries
* Save profiles in a profile.json file
* View the saved profile
* Cancel input at any step by typing "q"
* Navigate via a simple, menu-driven interface

This project is beginner-friendly and ideal for learning Python basics, functions, JSON file handling, and input validation.

# Features
* Input validation for all fields ✅
* Cancel option (q) during input ✅
* Persistent JSON storage ✅
* Menu-driven navigation ✅
* Beginner-friendly code structure ✅


# Install Required Libraries
This program uses only Python standard libraries. No external packages required.

Library	Purpose
json    - 	Save and load profile data
os      -   Check if profile file exists

# Running the Program
* Save the Python code as user_profile.py in your project folder.
* Open Git Bash / terminal in the folder.

Run the program:
python user_profile.py

On some systems you may need to use python3 user_profile.py.

Using the Menu
=== Select an option ===
1. Create profile
2. View profile
3. Exit

Enter the number of your choice and follow the prompts
Type q to cancel input at any step

# Data Storage
Profiles are saved in profile.json.

Example:
{
    "name": "Michael",
    "age": 25,
    "email": "michael@example.com",
    "country": "Nigeria"
}

# Demo
Example terminal interaction:
=== Select an option ===
1. Create profile
2. View profile
3. Exit
Choose an option: 1

Enter your name: Michael
Enter your age: 30000
Enter your email: michael@example.com
Enter your country: Nigeria

Profile saved successfully!

# Author
Michael Ukana – Python beginner-friendly CLI projects