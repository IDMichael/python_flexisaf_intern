print("++++ Smart Student Grade Calculator ++++")
def get_valid_score(prompt):
	while True:
		score = input(prompt + " (or 'quit/q' to cancel): ").strip()

		if score.lower() in ["quit", "q"]:
			# print("Goodbye!")
			return None

		try:
			score = float(score)

			if 0 <= score <= 100:
				return score
			else:
				print("Score must be between 0 and 100.")
		except ValueError:
			print("Score must be a valid number.")

print("\n=== Perform Arithmetic Operations ===")
def calculate_student_grade():
	test_score = get_valid_score("Enter test score")
	if test_score is None:
		return

	assignment_score = get_valid_score("Enter assignment score")
	if assignment_score is None:
		return

	exam_score = get_valid_score("Enter exam score")
	if exam_score is None:
		return

	# Add all scores
	total_score = test_score + assignment_score + exam_score
	average_score = total_score / 3

	# Result after performing arithmetic operations
	print("\n=== Result of arithmetic operations ===")
	print("Total score: ", total_score)
	print("Average score: ", average_score)

	# Perform comparison operations for passed/failed status
	print("\n=== Status of student's performance ===")
	if average_score >= 50:
		print("Status: Passed!")
	else:
		print("Status: Failed")

	# Perform logical operations for student's qualification
	print("\n=== Award qualification status ===")
	if average_score >= 80 and exam_score >= 75:
		print("Award Status: Excellence" )
	elif average_score >= 70 and exam_score >= 75:
		print("Award Status: Merit")
	else:
		print("Award Status: No award")

def main():
	while True:
		calculate_student_grade()
		again = input("\nDo you want to calculate again? (y/n): ").lower()
		if again == "y":
			print("Proceed with your calculation.\n")
			continue
		else:
			input("Program ended. Press Enter to exit.")
			break

if __name__ == "__main__":
	main()

