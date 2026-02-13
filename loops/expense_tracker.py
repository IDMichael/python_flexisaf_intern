from datetime import datetime, date
import sys

print("\n=== EXPENSE TRACKER ===")

expenses = []
CATEGORIES = ["Food", "Rent", "Beverage", "Internet", "Transport", "Other"]

while True:
	# Prompts user for an amount or a quit command.
	print("\n=== AMOUNT ===")
	amount_input = input("Enter amount (or 'q/quit' to cancel): ").strip().lower()

	# Checks for exit
	if amount_input in ['q', 'quit']:
		print("Exiting program...")
		break

	# Checks if amount is empty
	if not amount_input:
		print("Amount cannot be empty.")
		continue

	# Validate the amount input
	try:
		amount = float(amount_input)

		if amount <= 0:
			print("Amount must be greater than zero.")
			continue
	except ValueError:
		print("Invalid amount. Please, enter a valid amount.")
		continue

	# Get category
	print("\n=== CATEGORY ===")

	for i, cat in enumerate(CATEGORIES, start=1):
		print(f"{i}. {cat}")
	category_input = input("Enter category number (or ('q/quit') to cancel): ").strip().lower()

	if category_input in ['q', 'quit']:
		print("Exiting program...")
		break

	if not category_input:
		print("Category cannot be empty.")
		continue

	elif category_input.isdigit() and 1 <= int(category_input) <= len(CATEGORIES):
		category = CATEGORIES[int(category_input) - 1]
	else:
		print("Invalid category selection.")
		continue
	
	# Get note:
	print("\n=== NOTE ===")
	note = input("Enter note (description): ").strip()

	if note.lower() in ['q', 'quit']:
		print("Exiting program...")
		break

	if not note:
		print("Note cannot be empty.")
		continue

	# Get date (optional)
	print("\n=== DATE ===")
	date_input = input("Enter date (YYYY-MM-DD) or press Enter for today's: ").strip()
	if date_input in ['q', 'quit']:
		print("Exiting program...")
		break

	if not date_input:
		expense_date = date.today()

	else:
		try:
			expense_date = datetime.strptime(date_input, "%Y-%m-%d").date()
		except ValueError:
			print("Invalid date format: Please, use YYYY-MM-DD.")
			continue

	# Store expense
	print("\n=== EXPENSE ===")
	expense = {
		"amount": amount,
		"category": category,
		"note": note,
		"date": expense_date
	}
	expenses.append(expense)
	print("Expense added successfully!")

# Summary
print("\n=== EXPENSE SUMMARY ===")
if not expenses:
	print("No expenses recorded.")
	sys.exit()

total = 0
category_totals = {}

for expense in expenses:
	total += expense["amount"]

	# Get the current name of the category expense
	cat = expense["category"]

	# Add the amount to the corresponding category total. If the category does not exist yet, start from 0.
	category_totals[cat] = category_totals.get(cat, 0) + expense["amount"]
	print(f"{expense['date']} | {expense['category']} | {expense['amount']} | {expense['note']}")
print(f"\nTotal spent: ${total: .2f}")