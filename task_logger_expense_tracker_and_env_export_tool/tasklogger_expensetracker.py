import csv
from datetime import datetime
import pandas as pd
import os

FILENAME = "expenses.csv"
LOG_FILE = "log_entries.csv"

# Create file with headers if it doesn't exist
def create_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Amount", "Description", "Timestamp"])

# Create a log file
def create_log_file():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Action", "Timestamp"])

# Get timestamp
def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Log user actions
def log_action(action):
    timestamp = get_timestamp()

    with open(LOG_FILE, "a", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow([action, timestamp])

# Save expenses
def save_expenses(amount, description):
    timestamp = get_timestamp()

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, description, timestamp])

    print("Expense added successfully!\n")
    log_action("Added expense")

# Add a new expense
def add_expense():
    while True:
        amount_input = input("Enter amount (or 'done' to exit): ").strip()

        if amount_input.lower() == "done":
            print("Cancelled.\n")
            return

        if not amount_input:
            print("Input amount cannot be empty.")
            continue

        try:
            amount = float(amount_input)
            if amount <= 0:
                print("Amount must be greater than 0. Try again.\n")
                continue
            break
        except ValueError:
            print("Invalid input. Please, enter a valid number.\n")
    
    while True:
        description = input("Enter description (or 'done' to exit): ").strip()

        if description.lower() == "done":
            print("Cancelled.\n")
            return

        if not description:
            print("Description cannot be empty.")
            continue

        if not any(char.isalpha() for char in description):
            print("Description must contain a letter.")
            continue
        break
    save_expenses(amount, description)

# View summary using pandas
def view_summary():
    if not os.path.exists(FILENAME):
        print("No data found.")
        return

    df = pd.read_csv(FILENAME)

    if df.empty:
        print("No expenses recorded yet.\n")
        return

    total = df["Amount"].sum()
    average = df["Amount"].mean()

    print("\n==== Expense Summary ====")
    print(f"Total Spent: ${total:,.2f}")
    print(f"Average Expense: ${average:,.2f}\n")

    log_action("Viewed summary")

# Main menu
def main():
    create_file()
    create_log_file()

    log_action("Application started")
    while True:
        print("==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print("Goodbye!")
            log_action("Exited application")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()