import sys

print("\n--------------------------------------------")
print("=== Welcome to Password Strength Checker ===")
print("--------------------------------------------")

MIN_LENGTH = 8
SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[]{}\\|;:'\",.<>/?~`"

while True:
	# Prompt the user for a password or a quit command
	password = input("Enter your password (or 'q/quit' to cancel): ").strip()

	# Check for exit 
	if password.lower() in ('q', 'quit'):
		print("Exiting program.")
		sys.exit()

	# Check for empty input by the user
	if not password:
		print("Password field cannot be empty.")
		continue

	# Initialize a counter
	score = 0

	# Check for the password length
	if len(password) >= MIN_LENGTH:
		score += 1
	else:
		print(f"Use at least {MIN_LENGTH} characters.")

	# Check for password characters
	if any(char.islower() for char in password):
		score += 1
	else:
		print("Add lowercase letters.")

	if any(char.isupper() for char in password):
		score += 1
	else:
		print("Add uppercase letters.")

	if any(char.isdigit() for char in password):
		score += 1
	else:
		print("Add numbers.")

	if any(char in SPECIAL_CHARACTERS for char in password):
		score += 1
	else:
		print("Add special characters.")

	# Label password strength
	if score <= 2:
		strength = "Weak"

	elif score <= 4:
		strength = "Medium"

	else:
		strength = "Strong"

	print(f"Password Strength: {strength}")

	while True:
		again = input("\nCheck another password? (yes/no): ").strip().lower()
		if again in ("yes", "y"):
			print("Wow!\nThat's great!\n")
			break

		elif again in ("no", "n"):
			print("Program terminated!")
			sys.exit()
		else:
			print("Please, enter yes or no.")