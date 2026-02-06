import sys

print("\n=== EXPENSE CHECKER ===")

THRESHOLD_LIMIT = 50_000_000

while True:
	# Prompt the use for an input or a q command
	expense_input = input("Enter your expense amount (or 'q/quit' to cancel): ").strip()

	# Check for exit command and terminate the program safely
	if expense_input.lower() in ('q', 'quit'):
		print("Exiting program.")
		sys.exit()

	# Ensure that the input is not empty
	if not expense_input:
		print("\nThis field cannot be empty.")
		continue

	# Convert the input into a float number
	try:
		expense = float(expense_input)
	except ValueError:
		print("Invalid input. Enter a valid expense amount.\n")
		continue

	# Decision making logic based on the expense amount and the threshold limit

	# Check if the expense amount is lower than the threshold limit
	if expense < THRESHOLD_LIMIT:
		print("Expense amount is lower than the threshold limit.")

	# Check if the expense amount is equal to the threshold limit
	elif expense == THRESHOLD_LIMIT:
		print("Expense amount is equal to the threshold limit!")
	
	# Run this line of code if the above if and elif conditions are not met
	else:
		print("Expense amount exceeds the threshold limit")
