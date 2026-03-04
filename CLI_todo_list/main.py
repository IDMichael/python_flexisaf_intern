# Import functions from another file
from todo_functions import add_task, list_task, mark_task_done, edit_task, delete_task

# Function to display main menu options
def show_menu():
	print("\n--- CLI TO-DO APP ---")
	print("1. Add Task")
	print("2. View Tasks")
	print("3. Mark Task as Done")
	print("4. Delete Task")
	print("5. Exit")

# Main program controller
def main():
	tasks = []

	while True:
		show_menu()

		choice = input("Enter your choice (1 - 5): ").strip()

		# Calling on functions based on choice
		if choice == "1":
			add_task(tasks)
		
		elif choice == "2":
			list_task(tasks)

		elif choice == "3":
			mark_task_done(tasks)

		elif choice == "4":
			delete_task(tasks)

		elif choice == "5":
			print("Exiting program. Goodbye!")
			break
		else:
			print("Invalid choice. Please, select a number between 1 - 5.")
if __name__ == "__main__":
	main()