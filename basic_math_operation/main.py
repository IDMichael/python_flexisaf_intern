from math_tools import add, subtract, multiply, divide

print("\n==== BASIC MATH OPERATIONS ====")

def main():
	while True:
		print("\n=== MENU ===")
		print("1. Add")
		print("2. Subtract")
		print("3. Multiply")
		print("4. Divide")
		print("5. Exit")

		# Select an option
		choice = input("\nSelect option (1 - 5): ").strip()

		# Handle empty input
		if not choice:
			print("Error: No input provided.")
			continue

		# Validate option
		if choice not in ["1", "2", "3", "4", "5"]:
			print("Invalid choice. Try again...")
			continue

		# Exit option
		if choice == "5":
			print("Exiting program...")
			break

		# Get user input
		try:
			first_number = float(input("Enter first number: "))
			second_number = float(input("Enter second number: "))
		except ValueError:
			print("Error: Invalid input. Please, enter a number.")
			continue

		if choice == "1":
			result = add(first_number, second_number)

		elif choice == "2":
			result = subtract(first_number, second_number)

		elif choice == "3":
			result = multiply(first_number, second_number)

		elif choice == "4":
			result = divide(first_number, second_number)

		# Display result
		print(f"Result: {result:.2f}")

# Run program
if __name__ == "__main__":
	main()