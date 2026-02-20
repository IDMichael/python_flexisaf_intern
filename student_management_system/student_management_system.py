print("=== STUDENT MANAGE SYSTEM ===")  # Program header

# ==============================
# DATA STRUCTURES
# ==============================
tasks = []      # List to store tasks as dictionaries: {"title": str, "done": bool}
expenses = []   # List to store expenses as tuples: (item:str, amount:float)

# ==============================
# MAIN PROGRAM LOOP
# ==============================
while True:
    # Print main menu
	print("\n" + "=" * 15)
	print("== MAIN MENU ==")
	print("=" * 15)
	print("1. Task Manager")
	print("2. Expense Tracker")
	print("3. Exit")

	choice = input("Select: ")  # Get user choice

	# ==============================
	# TASK MANAGER
	# ==============================
	if choice == "1":
		while True:
			# Task Manager menu
			print("\n--- TASK MANAGER ---")
			print("1. Add Task")
			print("2. View Task")
			print("3. Complete Task")
			print("4. Update Task")
			print("5. Delete Task")
			print("6. Return to the Main Menu")

			task_choice = input("Select: ")

			# -------- ADD TASK --------
			if task_choice == "1":
				task = input("Enter assignment: ").strip()  # Remove leading/trailing spaces

				if task:
					# Append a dictionary representing the task
					tasks.append({"title": task, "done": False})
					print("Task added successfully!")
				else:
					# Reject empty input
					print("Task cannot be empty!")

			# -------- VIEW TASKS --------
			elif task_choice == "2":
				if not tasks:
					print("No tasks available.")  # Inform user when list is empty
					continue
				else:
					print("\nYour saved tasks: ")
					# Enumerate allows numbering tasks
					for index, task in enumerate(tasks, start=1):
						# Display task title and status
						status = "Done" if task['done'] else "Not Done"
						print(f"{index}. {task['title']} [{status}]")

			# -------- COMPLETE TASK --------
			elif task_choice == "3":
				if not tasks:
					print("No tasks available.")
					continue

				# Show all tasks with current status
				for index, task in enumerate(tasks, start=1):
					status = "Done" if task['done'] else "Not Done"
					print(f"{index}. {task['title']} - [{status}]")

				# User selects which task to mark as completed
				try:
					num = int(input("Task number completed: "))

					if 1 <= num <= len(tasks):
						task = tasks[num - 1]  # Get the task dictionary

						if not task['done']:
							task['done'] = True  # Mark as completed
							print("Task marked as completed!")
						else:
							print("Task already completed.")
					else:
						print("Invalid task number.")  # Number out of range
				except ValueError:
					# Handle non-integer input
					print("Please, enter a valid number.")

			# -------- UPDATE TASK --------
			elif task_choice == "4":
				if not tasks:
					print("No tasks available.")
					continue

				# Display all tasks with status
				for index, task in enumerate(tasks, start=1):
					print(f"{index}. {task['title']} - [{'Done' if task['done'] else 'Not Done'}]")

				try:
					num = int(input("Task number to edit: "))
					if 1 <= num <= len(tasks):
						new_task = input("Add a new task: ").strip()  # Do not force lowercase

						if new_task:
							# Update task title
							tasks[num - 1]['title'] = new_task
							print("Task updated!")
						else:
							print("New task cannot be empty!")

						# Show updated task list
						for index, task in enumerate(tasks, start=1):
							status = "Done" if task['done'] else "Not Done"
							print(f"{index}. {task['title']} - [{status}]")
					else:
						print("Invalid task number.")
				except ValueError:
					print("Please, enter a valid number.")

			# -------- DELETE TASK --------
			elif task_choice == "5":
				if not tasks:
					print("No tasks available.")
					continue

				# Display tasks before deletion
				for index, task in enumerate(tasks, start=1):
					status = "Done" if task['done'] else "Not Done"
					print(f"{index}. {task['title']} - [{status}]")

				try:
					num = int(input("Task number to delete: "))
					if 1 <= num <= len(tasks):
						# Remove selected task
						removed = tasks.pop(num - 1)
						print(f"Deleted: {removed['title']}")
					else:
						print("Invalid task number to be deleted.")

					# Show updated task list
					for index, task in enumerate(tasks, start=1):
						print(f"{index}. {task['title']} - [{'Done' if task['done'] else 'Not Done'}]")

				except ValueError:
					print("Please, enter a valid number.")

			# -------- RETURN TO MAIN MENU --------
			elif task_choice == "6":
				break

			else:
				print("Invalid option. Try again...")

	# ==============================
	# EXPENSE TRACKER
	# ==============================
	elif choice == "2":
		print("\n" + "=" * 21)
		print("== EXPENSE TRACKER ==")
		print("=" * 21)
		while True:
			print("\n--- EXPENSE TRACKER ---")
			print("1. Add Expense")
			print("2. View Expenses")
			print("3. Filter Expenses by Category")
			print("4. Show Expenses Above Amount")
			print("5. Back to the Main Menu")

			expense_choice = input("Select: ")

			# -------- ADD EXPENSE --------
			if expense_choice == "1":
				item = input("Enter expense item (Lunch, Transport, etc.): ").lower()
				if not item:
					print("Item cannot be empty.")  # Validate input
					continue

				# Get amount and validate
				amount_input = input("Enter amount: ")
				try:
					amount = float(amount_input)
					expenses.append((item, amount))  # Store as tuple
					print("Expenses added!")
				except ValueError:		
					print("Invalid amount.")  # Reject non-numeric input
					continue

			# -------- VIEW EXPENSES --------
			elif expense_choice == "2":
				if not expenses:
					print("No expenses recorded.")
				else:
					print("\nYour expenses recorded: ")
					for index, (item, amount) in enumerate(expenses, start=1):
						print(f"{index}. {item.capitalize()} - ${amount:.2f}")

			# -------- FILTER BY CATEGORY --------
			elif expense_choice == "3":
				category = input("Enter category: ").lower()
				filtered = [(item, amt) for item, amt in expenses if item == category]

				if filtered:
					for item, amt in filtered:
						print(f"{item.capitalize()} - ${amt:.2f}")
				else:
					print("No matching category found.")

			# -------- EXPENSES ABOVE AMOUNT --------
			elif expense_choice == "4":
				try:
					limit_expenses = float(input("Enter minimum amount: "))
					high_expenses = [(item, amt) for item, amt in expenses if amt > limit_expenses]

					if high_expenses:
						for item, amt in high_expenses:
							print(f"{item.capitalize()} - ${amt:.2f}")
					else:
						print("No expenses above that amount.")
				except ValueError:
					print("Invalid amount.")

			# -------- BACK TO MAIN MENU --------
			elif expense_choice == "5":
				break

			else:
				print("Invalid choice.")

	# ==============================
	# EXIT PROGRAM
	# ==============================
	elif choice == "3":
		print("Goodbye!")
		break

	else:
		print("Invalid option.")  # Handle invalid main menu choice