import sys

print("\n=== Age Validator ===")
while True:
	# Prompt the user for an input or a quit command
	user_input = input("Enter age (or 'q/quit' to cancel): ").strip()

	# Check for exit commands and terminate the program safely
	if user_input.lower() in ('q', 'quit'):
		print("Exiting program...")
		sys.exit()

	# Validate that the input is not empty
	if not user_input:
		print("Field cannot be empty.")
		continue

	# Attempt to convert the input to an integer
	# Handles non-numeric input appropriately
	try:
		age = int(user_input)
	except ValueError:
		print("Age must be a number.")
		continue
		
	# Decision making logic based on the user's age
	if age <= 0:
		print("Not eligible to vote in Nigeria")
	elif age >= 18:
		print("Eligible to vote in Nigeria.")
	else:
		print("Age must be 18 and above. Try again...\n")