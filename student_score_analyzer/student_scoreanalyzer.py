import csv

print("=" * 32)
print("---- Student Score Analyzer ----")
print("=" * 32)

# File name
FILENAME = "students.csv"

while True:
	# Ask user for number of students
	student_count_input = input("\nEnter number of students (or 'q' to quit): ").strip()

	# Exit option
	if student_count_input.lower() in ["q", "quit"]:
		print("Exiting program...")
		exit()

	# Validate integer input
	if not student_count_input.isdigit():
		print("Error: Please, enter a valid integer.")
		continue

	student_count = int(student_count_input)

	# Prevent zero or negative numbers
	if student_count <= 0:
		print("Error: Number must be greater than 0.")
		continue

	# Open file in write mode and store student data to CSV
	try:
		with open(FILENAME, "w", newline = "") as file:
			writer = csv.writer(file)

			# Write header row
			writer.writerow(["Name", "Score"])

			# Loop to collect student data
			for index in range(student_count):
				# Name validation
				while True:
					student_name = input(f"Enter name of student {index + 1}: ").strip()

					if student_name.lower() in ["q", "quit"]:
						print("Skipping the student...")
						student_name = None
						break

					if not student_name:
						print("Error: Name cannot be empty.")
						continue

					if not all(c.isalpha() or c.isspace() for c in student_name):
						print("Error: Name can only contain letters and spaces.")
						continue
					break

				# Validate score input
				while True:
					score_input = input(f"Enter score of student {index + 1}: ").strip()

					if score_input.lower() in ["q", "quit"]:
						print("Skipping this student...")
						student_score = None
						break

					if not score_input:
						print("Error: Score cannot be empty.")
						continue
					
					try:
						student_score = float(score_input)

						if not (0 <= student_score <= 100):
							print("Score must be between 0 and 100.")
							continue
						break
					except ValueError:
						print("Error: Enter a valid number for score.")

				# Write each student's data into the CSV file
				writer.writerow([student_name, student_score])
		break
	except IOError:
		print("Error: could not write to file.")
		continue

# Initialize variables for calculation
total_score = 0
record_count = 0
top_names = []
top_score = float("-inf") # Start with lowest possible score

# Open file in read mode
try:
	with open(FILENAME, "r") as file:
		reader = csv.DictReader(file)

		# Loop through each row in the CSV file
		for row in reader:
			try:
				student_name = row["Name"]
				student_score = float(row["Score"])

				# Add to total score
				total_score += student_score
				record_count += 1

				# Check for highest score
				if student_score > top_score:
					top_score = student_score
					top_names = [student_name]
				elif student_score == top_score:
					top_names.append(student_name)

			except (ValueError, KeyError):
				print("Warning: Skipping invalid row.")
				continue

except FileNotFoundError:
	print("Error: File not found.")
	exit()

except IOError:
	print("Error: Could not read file.")
	exit()

# Calculate average (avode division by zero)
if record_count > 0:
	average = total_score / record_count
else:
	average = 0

# Display results
print("\n=== Results ===")
print(f"Class Average: {average:.2f}")
if top_names:
	print(f"Top Performer(s): {', '.join(top_names)} with score {top_score}")
else:
	print("No valid student date entered.")	