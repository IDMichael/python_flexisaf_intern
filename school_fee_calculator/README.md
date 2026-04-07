# 🎓 Student Fee Management System (CLI Application)

## 1. Working Application

This project is a **Command-Line Interface (CLI) application** built with Python for managing student fees.

### Type
- CLI Tool (Python Script)

### What the Application Does

The system allows school administrators to:

- Add new students
- Record student payments
- Automatically calculate outstanding balances
- Generate receipts
- Send email notifications (payment + reminders)
- Auto-send reminders for unpaid fees at startup

### Core Requirements Covered

#### 1. Access Input
The application collects user input via the terminal:
- Student ID
- Name
- Email
- Total Fee
- Payment Amount

Example:
Enter Student ID: STU-001
Enter Student Name: John Doe
Enter Email: john@gmail.com

Enter Total Fee: 500


#### 2. Process Data
The system processes data using:
- CSV files (`students.csv`, `payments.csv`)
- Business logic for:
  - Fee tracking
  - Balance calculation
  - Payment validation
  - Smart reminder generation (AI-like tone system)

#### 3. Produce Output

The application produces multiple outputs:

* Terminal Output  
- Student info
- Balance updates
- Payment confirmation

* File Output  
- Receipts saved in `/receipts` folder

Example:
receipts/receipt_st001_2026-04-07_14-32-10.txt


* Email Output  
- Payment receipts
- Fee reminders (automatic + manual)


### How to Run the Application
python school_fee_calculator.py


### Application Flow

START
  ↓
Setup files & folders
  ↓
Auto-send reminders
  ↓
Main Menu:
   1. Add Student
   2. Process Payment
   3. Exit

Example Menu
==== STUDENT FEE SYSTEM ====
1. Add Student
2. Process Payment
3. Exit

### Key Features
- Smart Reminder System (based on balance severity)
- Email Integration (via Gmail SMTP)
- Receipt Generation (timestamped files)
- Persistent Storage using CSV
- Input Validation for all fields


## 2. GitHub Repository (Main Submission)

### Repository Structure
student-fee-system/
│
├── main.py
├── config_example.py
├── students.csv
├── payments.csv
├── receipts/
├── screenshots/
│ ├── add_student.png
│ ├── payment_process.png
│ ├── receipt_output.png
│ └── email_sent.png
└── README.md

### Problem Statement

Managing student fee payments manually can lead to:
- Errors in tracking payments
- Difficulty calculating balances
- Lack of proper communication with parents

This system solves these problems by providing an automated and reliable CLI-based solution.

### Features

- Add new students
- Record and track payments
- Automatically calculate outstanding balances
- Generate payment receipts (saved as files)
- Send email notifications (receipts + reminders)
- Smart reminder system based on debt level
- Persistent storage using CSV files

### Setup Instructions

#### 1. Clone the Repository
git clone https://github.com/IDMichael/python_flexisaf_intern.git
cd python_flexisaf_intern/...

2. Create Config File
Create a file named config.py:
EMAIL_USER = "your_email@example.com"
EMAIL_PASS = "your_app_password"

3. (Recommended) Use Example Config
Use the provided config_example.py as a template.

4. Install Requirements
No external libraries required (uses Python standard library).

5. Run the Application
python school_fee_calculator.py

* Screenshots
All screenshots are available in the /screenshots folder:
- Adding a student
- Processing payment
- Receipt generation
- Email sent confirmation

Important Links
GitHub Repository: https://github.com/IDMichael/python_flexisaf_intern/tree/main/school_fee_calculator
Presentation Slides (PDF): [https://acrobat.adobe.com/id/urn%3Aaaid%3Asc%3AEU%3A234d387b-ca65-4584-8151-f164d417a7ab/?x_api_client_id=anonymous_home&x_api_client_location=signin&annonBboxWorkflow=false&filetype=application%2Fpdf]

## 3. Data Handling Explanation

### Data Storage Format

This application uses **CSV files** for storing and managing data:

- `students.csv` → Stores student details
- `payments.csv` → Stores payment records

---

### Sample Data

#### students.csv
student_id,name,email,total_fee
st001,John Doe,john@example.com,500
st002,Jane Smith,jane@example.com,1200

payments.csv
student_id,amount_paid,date
st001,200,2026-04-07 10:00:00
st001,100,2026-04-08 12:30:00

* How Data is Processed
1. Adding Students
New student data is appended to students.csv
Ensures:
Unique student ID
Valid email format
Positive fee value

2. Recording Payments
Each payment is stored in payments.csv
Includes:
Student ID
Amount paid
Timestamp

3. Calculating Balance
The system calculates balance dynamically:

Balance = Total Fee - Sum of All Payments
- Reads students.csv to get total fee
- Reads payments.csv to sum all payments for that student

4. Data Persistence
- Data is saved permanently in CSV files
- No database required
- Data remains available after program restarts
	
Data Safety Notes
- Uses sample/dummy data only
- No real personal or sensitive data is stored
- Email credentials are kept in a separate config.py file (not uploaded)

## 4. Core Logic Explanation

### How the System Works

The application follows a simple workflow:

1. Initialize system (create files & folders)
2. Load student data
3. Allow user interaction via CLI menu
4. Process payments and update records
5. Generate receipts and send emails
6. Automatically send reminders for unpaid fees

### Key Logic Components

#### 1. Student Management
- `add_student()`
  - Collects and validates user input
  - Prevents duplicate student IDs
  - Stores student data in `students.csv`

- `get_student(student_id)`
  - Searches and retrieves student details from CSV

#### 2. Payment Processing

- `process_payment()`
  - Fetches student details
  - Displays current balance
  - Validates payment amount
  - Records payment
  - Updates balance

#### 3. Balance Calculation

- `calculate_balance(student_id)`

**Approach:**
- Get total fee from `students.csv`
- Sum all payments from `payments.csv`
- Subtract to get remaining balance

#### 4. Smart Reminder System (AI Logic)

- `generate_reminder(student_name, balance)`

The system uses condition-based logic to adjust message tone:

- Balance = 0 → Appreciation message
- Balance < 100 → Gentle reminder
- Balance < 1000 → Serious reminder
- Balance ≥ 1000 → Urgent warning

#### 5. Receipt Generation

- `generate_receipt(student, amount)`

- Creates a `.txt` file
- Uses timestamp for uniqueness
- Stores in `/receipts` folder

#### 6. Email System

- `send_email(to_email, subject, message)`

**Process:**
- Uses SMTP (Gmail)
- Logs in using credentials from `config.py`
- Sends:
  - Payment confirmation
  - Fee reminders

#### 7. Automated Reminder System

- `auto_send_reminders()`

**Logic:**
- Runs at program startup
- Loops through all students
- Sends reminders only if balance > 0

### System Flow Summary
User Input → Validation → Data Storage (CSV)
        ↓
Balance Calculation
        ↓
Payment Processing → Receipt Generation
        ↓
Email Notification
        ↓
Auto Reminder System

## 5. Results / Output

### Overview

The system produces outputs in three main forms:
- Terminal (CLI) output
- Generated receipt files
- Email notifications

### Sample CLI Output

#### Adding a Student
==== ADD NEW STUDENT ====
Enter Student ID: st001
Enter Student Name: John Doe
Enter Email: john@example.com

Enter Total Fee: 500

Student 'John Doe' added successfully!

#### Processing Payment
Enter Student ID: st001
Student Found: John Doe
Outstanding Balance: $300.00

---- PAYMENT REMINDER ----
Dear Parent/Guardian of John Doe,
This is a friendly reminder of an outstanding balance of $300.00.

Enter payment amount: 200

New Balance: $100.00

### 2. Generated Receipt Output
Example receipt file (`receipts/receipt_st001_2026-04-07_14-32-10.txt')

==== PAYMENT RECEIPT ====

Name: John Doe
Student ID: st001
Amount Paid: $200
Date: 2026-04-07 14:32:10

Thank you for your payment!

### 3. Email Output Examples

#### Payment Confirmation Email
Subject: Payment Receipt

Payment of $200 received.
New Balance: $100.00

#### Reminder Email
Subject: Fee Payment Reminder

Dear Parent/Guardian of John Doe,

This is a friendly reminder of an outstanding balance of $100.00.

Kindly make payment when convenient.

School Administration

### 4. Sample Calculations

Example:

- Total Fee = $500  
- Payments Made = $200 + $100  
- Total Paid = $300  

Balance = 500 - 300 = $200

### Summary of Outputs

  Output Type       |  Description                         
 -----------------     -------------------
  CLI Output        - User interaction and results         
  Receipt Files     - Stored payment confirmations         
  Email Messages    - Notifications to users               
  CSV Files         - Persistent data storage              

## 6. Presentation Slides (PDF Link)

### Presentation Overview

The presentation slides summarize:
- Problem statement
- System approach
- Core features
- Data handling
- Outputs and results

### Slide Contents

#### Slide 1: Title Slide
- Project Name: Student Fee Management System
- Developer: Your Name
- Course / Submission Info

#### Slide 2: Problem Statement
- Challenges in manual fee tracking
- Errors in calculations
- Lack of automated reminders

#### Slide 3: Proposed Solution
- CLI-based automated system
- CSV-based data storage
- Email notifications
- Receipt generation

#### Slide 4: System Architecture
- User Input (CLI)
- Processing Layer (Python logic)
- Storage Layer (CSV files)
- Output Layer (Receipts + Emails)

#### Slide 5: Core Features
- Add student
- Record payment
- Calculate balance
- Send reminders
- Generate receipts

#### Slide 6: Data Handling
- Use of CSV files
- Structure of student and payment data
- Balance computation method

#### Slide 7: Output Results
- CLI outputs
- Receipt files
- Email notifications

#### Slide 8: Conclusion
- Automation improves efficiency
- Reduces human error
- Scalable and extendable system

### PDF Link
Then paste the link here:
https://acrobat.adobe.com/id/urn%3Aaaid%3Asc%3AEU%3A234d387b-ca65-4584-8151-f164d417a7ab/?x_api_client_id=anonymous_home&x_api_client_location=signin&annonBboxWorkflow=false&filetype=application%2Fpdf

## 7. Final Submission Requirements Checklist

This section ensures all required components are properly included before submission.

### 1. GitHub Repository Contents

Ensure your repository includes:

- [x] Source code (`python school_fee_calculator.py`)
- [x] `config_example.py` (no real credentials)
- [x] `students.csv` (sample data)
- [x] `payments.csv` (sample data)
- [x] `receipts/` folder (generated outputs)
- [x] `screenshots/` folder
- [x] `README.md` (this file)

### 2. README.md Must Include

- [x] Problem statement
- [x] Features of the system
- [x] Setup instructions
- [x] Data handling explanation
- [x] Core logic explanation
- [x] Results / outputs
- [x] Presentation slides PDF link
- [x] GitHub repository link

### 3. Screenshots Folder

Include clear screenshots such as:

- CLI menu interface
- Adding a student
- Processing a payment
- Receipt generation
- Email success confirmation

### 4. Data Handling

- Use sample/dummy data only
- No real personal or sensitive data
- CSV files used for persistence

### 5. Presentation Slides

- Must be exported as PDF
- Must include:
  - Problem
  - Approach
  - Outputs
- Must be publicly accessible via a link

### 6. Final GitHub README Links Section
Include all important links in your README:

