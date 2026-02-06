import sys

# === Loan Eligibility Checker ===

while True:
	print("\n=== AGE CHECK ===")
	# Prompt the user for input or exit command
	age_input = input("Enter your age (or 'q/quit' to cancel): ").strip()

	# Check the exit command and terminate program safely
	if age_input.lower() in ('q', 'quit'):
		print("Exiting program...")
		sys.exit()

	# Ensure that the user input is not empty
	if not age_input:
		print("Field cannot be empty.")
		continue

	# Convert the data type of the input
	try:
		age = int(age_input)
	except ValueError:
		print("Invalid age. Enter a number...\n")
		continue

	# Check the logic for the age of the user
	if age < 18:
		print("Loan Denied:  Age is less than 18 years.")
		sys.exit()

	break

print("\n=== EMPLOYMENT STATUS ===")
while True:
	employed = input("Are you employed ('yes/no'): ").strip().lower()

	if employed in ('yes', 'y'):
		print("Applicant is employed.")
		break

	if employed in ('no', 'n'):
		print("Loan Denied: Applicant must be employed.")
		sys.exit()

	print("Please, enter yes or no.")

print("\n=== MONTHLY INCOME CHECK ===")
while True:
	income_input = input("Enter your monthly income (or 'q/quit' to cancel): ").strip()

	if income_input.lower() in ('q', 'quit'):
		print("Exiting program...")
		sys.exit()

	if not income_input:
		print("Income cannot be empty.")
		continue

	try:
		income = float(income_input)
	except ValueError:
		print("Invalid input. Try again...\n")
		continue

	if income <= 50_000:
		print("Loan Denied: Income too low")
		sys.exit()
	break

while True:
	print("\n=== MONTHLY DEBT CHECK ===")
	debt_input = input("Enter your monthly debt (or 'q/quit' to cancel): ").strip()

	if debt_input.lower() in ('q', 'quit'):
		print("Exiting program...")
		sys.exit()

	if not debt_input:
		print("You are free of debt.")
		continue

	try:
		debt = float(debt_input)
	except ValueError:
		print("Invalid input. Enter a valid debt amount.\n")
		continue

	if debt > income * 0.4:
		print("Loan Denied: Debt exceeds 40% of income")
		sys.exit()

	break

while True:
	print("\n=== LOAN AMOUNT CHECK ===")
	loan_input = input("Enter your loan amount (or 'q/quit' to cancel): ").strip()

	if loan_input.lower() in ('q', 'quit'):
		print("Exiting program..")
		sys.exit()

	if not loan_input:
		print("This field cannot be empty.")
		continue

	try:
		loan = float(loan_input)
	except ValueError:
		print("Invalid input. Enter a valid loan amount.")
		continue

	if loan <= 0:
		print("Loan amount must be greater than zero.")
		continue

	elif loan > income * 10:
		print("Loan Denied: Requested loan is too high!")
		sys.exit()
	break

print("Loan approved. You are eligible!")

