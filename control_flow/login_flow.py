import sys

print("\n=== Login Flow ===")

USERNAME = 'admin'
PASSWORD = 'pass'

while True:
	# === USERNAME CHECK ===
	username = input("\nEnter your username (or 'q/quit' to cancel): ").strip()

	if username.lower() in ('q', 'quit'):
		print("Exiting the program...")
		sys.exit()

	if not username:
		print("This field cannot be empty.")
		continue

	if not username.isalpha():
		print("Username must be letters only.")
		continue

	# === PASSWORD CHECK ===
	password = input("Enter your password (or 'q/quit' to cancel): ").strip()

	if password.lower() in ('q', 'quit'):
		print("Exiting program...")
		sys.exit()

	if not password:
		print("Password field cannot be empty.")
		continue

	if not password.isalnum():
		print("Password must contain letters only.")
		continue
	
	if username == USERNAME and password == PASSWORD:
		print("Access granted!")
		sys.exit()
		
	else:
		print("Access denied. Try again...")
