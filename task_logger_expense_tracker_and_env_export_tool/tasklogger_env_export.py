from datetime import datetime
import subprocess
import sys

FILENAME = "track_logger_actions.txt"
FULL_REQUIREMENTS_FILE = "requirements.txt"
CLEAN_REQUIREMENTS_FILE = "requirements_clean.txt"

def get_actions():
	"""
	Collect user actions from input until they choose to stop.
	"""
	actions = []
	print("Enter your actions (type 'done' to finish): ")

	while True:
		action = input("Action: ").strip()
		if action.lower() == 'done':
			break

		if not action:
			print("Action cannot be empty.")
			continue

		if action:
			actions.append(action)
	return actions

def get_timestamp():
	"""
	Returns the current timestamp as a formatted string.
	"""
	return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def save_actions(actions):
	with open(FILENAME, "a") as file:
		for action in actions:
			timestamp = get_timestamp()
			file.write(f"[{timestamp}] {action}\n")
	print(f"\nActions saved to {FILENAME}")

def export_full_dependencies():
	"""
	Export installed Python packages to requirements.txt using pip freeze.
	"""
	try:
		with open(FULL_REQUIREMENTS_FILE, "w") as file:
			subprocess.run([sys.executable, "-m", "pip", "freeze"], stdout = file, check = True, text = True)
		print(f"Full environment dependencies exported to {FULL_REQUIREMENTS_FILE}")
	except Exception as e:
		print(f"Error exporting full dependencies {e}")

def generate_clean_requirements_dependencies():
	required_packages = []
	try:
		with open(CLEAN_REQUIREMENTS_FILE, "w") as file:
			for package in required_packages:
				file.write(f"{package}\n")
		print(f"Clean project requirements exported to {CLEAN_REQUIREMENTS_FILE}")
	except Exception as e:
		print(f"Error exporting clean dependencies: {e}")
def main():
	actions = get_actions()

	if actions:
		save_actions(actions)

	else:
		print("No actions to save.")

	export_full_dependencies()
	generate_clean_requirements_dependencies()

if __name__ == "__main__":
	main()
