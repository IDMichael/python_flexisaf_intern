from datetime import datetime
import config
import os
import csv
import smtplib
from email.mime.text import MIMEText


print("==== STUDENT FEE CALCULATOR ====")

# ==============================
# CONFIG
# ==============================
STUDENT_FILE = "students.csv"
PAYMENT_FILE = "payments.csv"
RECEIPT_FOLDER = "receipts"

# ==============================
# SETUP
# ==============================
def setup():
    os.makedirs(RECEIPT_FOLDER, exist_ok=True)

    if not os.path.exists(STUDENT_FILE):
        with open(STUDENT_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["student_id", "name", "email", "total_fee"])

    if not os.path.exists(PAYMENT_FILE):
        with open(PAYMENT_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["student_id", "amount_paid", "date"])

# ==============================
# ADD STUDENT
# ==============================
def add_student():
    print("\n==== ADD NEW STUDENT ====")

    while True:
        student_id = input("Enter Student ID: ").strip().lower()
        if not student_id:
            print("Student ID cannot be empty.")
            continue
        if get_student(student_id):
            print("Student already exists.")
            continue
        break

    while True:
        name = input("Enter Student Name: ").strip()
        if not name:
            print("Name cannot be empty.")
        else:
            break

    while True:
        email = input("Enter Email: ").strip()
        if (
            "@" not in email or
            "." not in email or
            email.startswith("@") or
            email.endswith(".") or
            email.count("@") != 1
        ):
            print("Invalid Email format.")
        else:
            break

    while True:
        fee_input = input("Enter Total Fee: ").strip()
        try:
            total_fee = float(fee_input)
            if total_fee <= 0:
                print("Fee must be greater than 0.")
                continue
            break
        except ValueError:
            print("Enter a valid number.")

    with open(STUDENT_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id.lower(), name, email, total_fee])

    print(f"Student '{name}' added successfully!")

# ==============================
# GET STUDENT
# ==============================
def get_student(student_id):
    with open(STUDENT_FILE, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["student_id"] == student_id:
                return row
    return None

# ==============================
# CALCULATE BALANCE
# ==============================
def calculate_balance(student_id):
    student = get_student(student_id)
    if not student:
        return None

    total_fee = float(student["total_fee"])
    total_paid = 0

    with open(PAYMENT_FILE, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["student_id"] == student_id:
                total_paid += float(row["amount_paid"])

    return total_fee - total_paid

# ==============================
# AI REMINDER (SMART LOGIC)
# ==============================
def generate_reminder(student_name, balance):
    if balance == 0:
        tone = "appreciation"
    elif balance < 100:
        tone = "gentle"
    elif balance < 1000:
        tone = "serious"
    else:
        tone = "urgent"

    if tone == "appreciation":
        return f"""
Dear Parent/Guardian of {student_name},

We are pleased to inform you that all fees have been fully paid.

Thank you for your cooperation.

School Administration
"""

    elif tone == "gentle":
        return f"""
Dear Parent/Guardian of {student_name},

This is a friendly reminder of an outstanding balance of ${balance:.2f}.

Kindly make payment when convenient.

School Administration
"""

    elif tone == "serious":
        return f"""
Dear Parent/Guardian of {student_name},

There is an outstanding balance of ${balance:.2f}.

We kindly request prompt payment.

School Administration
"""

    else:
        return f"""
Dear Parent/Guardian of {student_name},

URGENT: Outstanding balance of ${balance:.2f} remains unpaid.

Immediate payment is required.

School Administration
"""

# ==============================
# RECORD PAYMENT
# ==============================
def record_payment(student_id, amount):
    with open(PAYMENT_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, amount, datetime.now()])

# ==============================
# RECEIPT
# ==============================
def generate_receipt(student, amount):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{RECEIPT_FOLDER}/receipt_{student['student_id']}_{timestamp}.txt"

    receipt = f"""
==== PAYMENT RECEIPT ====

Name: {student['name']}
Student ID: {student['student_id']}
Amount Paid: ${amount}
Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Thank you for your payment!
"""

    with open(filename, "w") as file:
        file.write(receipt)

    print(f"Receipt generated: {filename}")

# ==============================
# EMAIL
# ==============================
def send_email(to_email, subject, message):
    from_email = config.EMAIL_USER
    password = config.EMAIL_PASS

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(from_email, password)
            server.send_message(msg)

        print("Email sent successfully!")

    except Exception as e:
        print("Email failed:", e)

# ==============================
# AUTO REMINDERS (AI SYSTEM)
# ==============================
def auto_send_reminders():
    print("\n[AI SYSTEM] Sending reminders...")

    with open(STUDENT_FILE, "r") as file:
        reader = csv.DictReader(file)

        for student in reader:
            student_id = student["student_id"]
            balance = calculate_balance(student_id)

            if balance > 0:
                message = generate_reminder(student["name"], balance)

                send_email(
                    student["email"],
                    "Fee Payment Reminder",
                    message
                )

# ==============================
# PROCESS PAYMENT
# ==============================
def process_payment():
    student_id = input("Enter Student ID: ").strip().lower()

    student = get_student(student_id)
    if not student:
        print("Student not found.")
        return

    balance = calculate_balance(student_id)

    print(f"Student Found: {student['name']}")
    print(f"Outstanding Balance: ${balance:.2f}")

    print("\n---- PAYMENT REMINDER ----")
    print(generate_reminder(student["name"], balance))

    pay = input("Enter payment amount (or press Enter to skip): ").strip()

    if not pay:
        return

    try:
        amount = float(pay)
        if amount <= 0:
            print("Invalid amount.")
            return

        if amount > balance:
            print("Payment exceeds outstanding balance.")
            return

    except ValueError:
        print("Enter a valid number.")
        return

    record_payment(student_id, amount)
    generate_receipt(student, amount)

    new_balance = calculate_balance(student_id)
    print(f"New Balance: ${new_balance:.2f}")

    send_email(
        student["email"],
        "Payment Receipt",
        f"Payment of ${amount} received.\nNew Balance: ${new_balance:.2f}"
    )

# ==============================
# MAIN MENU
# ==============================
def main():
    setup()
    auto_send_reminders()

    while True:
        print("\n==== STUDENT FEE SYSTEM ====")
        print("1. Add Student")
        print("2. Process Payment")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            process_payment()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()