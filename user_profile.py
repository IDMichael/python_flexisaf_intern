import json
import os

# Input Validation Functions
def get_valid_name(prompt):
	while True:
		name = input(prompt + " (or 'q' to cancel): ").strip()
		if name.lower() == "q":
			return None
		if name:
			return name
		print("Name must not be empty.")

def get_valid_age(prompt):
	while True:
		age = input(prompt + " (or 'q' to cancel): ").strip()
		if age.lower() == "q":
			return None
		if age.isdigit() and int(age) > 0:
			return int(age)
		print("Age must be numbers.")

def get_valid_email(prompt):
	while True:
		email = input(prompt + " (or 'q' to cancel): ").strip()
		if email.lower() == "q":
			return None
		if "@" in email and "." in email:
			return email
		print("Email must contain '@' and '.'.")

def get_valid_country(prompt):
	while True:
		country = input(prompt + " (or 'q' to cancel): ").strip()
		if country.lower() == "q":
			return None
		if country:
			return country
		print("Country must not be empty.")

# Profile Management Functions
def create_profile():
	print("\n=== Create profile ===\n")
	name = get_valid_name("Enter your name: ")
	if name is None:
		print("Profile creation cancelled.\n")
		return

	age = get_valid_age("Enter your age: ")
	if age is None:
		print("Profile creation cancelled.\n")
		return

	email = get_valid_email("Enter your email: ")
	if email is None:
		print("Profile creation cancelled.\n")
		return

	country = get_valid_country("Enter your country")
	if country is None:
		print("Profile creation cancelled.\n")
		return

	# Store details into a dictionary
	profile = {
		"name": name,
		"age": age,
		"email": email,
		"country": country
	}

	# Save dictionary into a JSON file
	with open("profile.json", "w") as file:
		json.dump(profile, file, indent = 4)
	print("\nProfile saved successfully!\n")

# View saved profile
def view_saved_profile():
	print("\n=== Saved profile ===")
	if not os.path.exists("profile.json"):
		print("No saved profile found.")
		return

	try:
		with open("profile.json", "r") as file:
			saved_profile = json.load(file)
	except json.JSONDecodeError:
		print("Profile file is empty or corrupted. Create one.")
		return

	if not saved_profile:
		print("Profile is empty. Create a profile first.")
		return

	for key, value in saved_profile.items():
		print(f"{key.capitalize()}: {value}")

# Main menu loop
def main():
	while True:
		print("\n=== Select an option ===")
		print("1. Create profile")
		print("2. View profile")
		print("3. Exit")

		choice = input("Choose an option: ").strip()

		if choice == "1":
			create_profile()
		elif choice == "2":
			view_saved_profile()
		elif choice == "3":
			print("Goodbye!")
			break
		else:
			print("Invalid choice. Try again.\n")

if __name__ == "__main__":
	main()
	