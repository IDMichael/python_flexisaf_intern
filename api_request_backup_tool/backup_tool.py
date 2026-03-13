import os
import shutil
import datetime

LOG_FILE = "backup_log.txt"

print("\n=== FILE BACKUP TOOL ===")

# Create log file header if it doesn't exist
if not os.path.exists(LOG_FILE):
	with open(LOG_FILE, "w") as log:
		log.write("=========================== FILE BACKUP LOG ============================\n")

while True:
	print("\n=== MENU ===")
	print("1. Backup a file")
	print("2. View Backup Log")
	print("3. Exit")

	choice = input("Select an option: ").strip().lower()

	if choice == "1":
		# Ask for source file
		source_file = input("Enter the source file path: ").strip()

		# Check if the source file exists
		if not os.path.isfile(source_file):
			print(f"Error: Source file '{source_file}' does not exist.")
			continue

		# Ask for destination file
		destination_file = input("Enter the destination file path: ").strip()

		# Check if the destination file already exists
		if os.path.exists(destination_file):

			# Warn the user to avoid accidental overwrite
			confirm = input("Destination file exists. Overwrite? (y/n): ").strip().lower()
			if confirm != "y":
				print("Backup cancelled.")				

				timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
				with open(LOG_FILE, "a") as log:
					log.write(f"\nTime: {timestamp}\n")
					log.write(f"Status: CANCELLED\n")
					log.write(f"Source File: {source_file}\n")
					log.write(f"Destination File: N/A\n")
					log.write("-" * 72 + "\n")
				continue

		# File Copy with Exception Handling
		try:
			shutil.copy2(source_file, destination_file)
			print("Backup successful!")

			timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			with open(LOG_FILE, "a") as log:
				log.write(f"\nTime: {timestamp}\n")
				log.write(f"Status: SUCCESS\n")
				log.write(f"Source File: {source_file}\n")
				log.write(f"Destination File: {destination_file}\n")
				log.write("-" * 70 + "\n")

		except PermissionError:
			print("Error: Permission denied.")

			timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			with open(LOG_FILE, "a") as log:
				log.write(f"\nTime: {timestamp}\n")
				log.write(f"Status: FAILED\n")
				log.write(f"Source File: {source_file}\n")
				log.write(f"Destination File: N/A\n")
				log.write("-" * 72 + "\n")

		except FileNotFoundError:
			print("Error: File path not found.")

			timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			with open(LOG_FILE, "a") as log:
				log.write(f"\nTime: {timestamp}\n")
				log.write(f"Status: FAILED\n")
				log.write(f"Source File: {source_file}\n")
				log.write(f"Destination File: N/A\n")
				log.write("-" * 72 + "\n")

		except Exception as e:
			print(f"Backup failed: {e}")

			timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			with open(LOG_FILE, "a") as log:
				log.write(f"\nTime: {timestamp}\n")
				log.write(f"Status: FAILED\n")
				log.write(f"Source File: {source_file}\n")
				log.write(f"Destination File: N/A\n")
				log.write("-" * 72 + "\n")

	elif choice == "2":
		if os.path.exists(LOG_FILE):
			print("\n=== BACKUP LOG ====")
			with open(LOG_FILE, "r") as log:
				print(log.read())
			input("\nPress Enter to return to menu...")
		else:
			print("No logs found.")

	elif choice == "3":
		print("Exiting program...")
		break

	else:
		print("Invalid option. Please, try again...")
