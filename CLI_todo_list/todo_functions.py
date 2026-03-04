print("\n=== A Function-based CLI To-Do List Application.")

# Function to add a new task to the list
def add_task(tasks):
	print("\n--- ADD TASK ---")
	task_title = input("Enter your task (or press Enter to cancel): ").strip().capitalize()


	if not task_title:
		print("Task creation cancelled.")
		return

	# Add new task as a dictionary
	tasks.append({"title": task_title, "done": False})
	print(f"Task '{task_title}' added successfully!")

def list_task(tasks):
	print("\n--- TO DO LIST ---")
	if not tasks:
		print("No tasks available.")
		return
		
	for index, task_record in enumerate(tasks, start = 1):
		status = "Done" if task_record['done'] else "Not Done"
		print(f"{index}. {task_record['title']} - [{status}]")

def mark_task_done(tasks):
	print("\n" + "==" * 15)
	print("--- MARK TASK AS DONE ---")
	print("==" * 15)

	if not tasks:
		print("No tasks available.")
		return

	# Display tasks so user can choose
	list_task(tasks)

	try:
		# Convert user input to an integer
		task_number = int(input("Enter a task number to be marked as done: "))

		# Valdidate range
		if 1 <= task_number <= len(tasks):
			task = tasks[task_number - 1]

			# Update task status
			task['done'] = True
			print(f"Task '{task['title']}' marked as done successfully!")

		else:
			print("Task number out of range.")

	# Catch invalid inputs
	except ValueError:
		print("Invalid input. Please, enter a valid number.")

def delete_task(tasks):
	print("\n--- DELETE TASK ---")
	if not tasks:
		print("No tasks available.")
		return

	list_task(tasks)

	try:
		task_number = int(input("Enter a task number to delete: "))

		if 1 <= task_number <= len(tasks):
			removed_task = tasks.pop(task_number - 1)
			print(f"Task '{removed_task['title']}' deleted successfully!")

		else:
			print("Task number out of range.")
	except ValueError:
		print("Invalid input. Please, enter a valid number.")
