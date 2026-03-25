# math_tools.py

# ---- ADD ----
def add(first_number, second_number):
	return first_number + second_number

# ---- SUBTRACT ----
def subtract(first_number, second_number):
	return first_number - second_number

# ---- MULTIPLICATION ----
def multiply(first_number, second_number):
	return first_number * second_number

# ---- DIVISION ----
def divide(first_number, second_number):
	if second_number == 0:
		raise ValueError("Error: Cannot divide by zero.")
	return first_number / second_number