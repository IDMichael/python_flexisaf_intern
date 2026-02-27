print("\n" + "=" * 31)
print("--- STUDENT CONTACT MANAGER ---")
print("=" * 31)

# --- DATA STRORAGE ---
contacts = {}		# Main Database
emails = set()		# Prevent duplicate emails
phones = set()		# Prevent duplicate phone numbers

ROLES = ["Student", "Parent", "Teacher", "Staff"]

while True:
	print("\n--- MENU LOOP PROGRAM ---")
	print("1. Add Contact")
	print("2. Update Contact")
	print("3. Delete Contact")
	print("4. Search Contact")
	print("5. List All Contact")
	print("6. Exit")

	choice = input("Enter choice: ").strip()

	# === ADD CONTACT ===
	if choice == "1":
		print("\n--- ADD CONTACT ---")

		cancelled = False

		while True:
			# ---- CHECK UNIQUE ID ---
			unique_id = input("Enter Unique ID (e.g., STUD001, or 'q/quit' to cancel): ").strip().upper()

			if unique_id.lower() in ["quit", "q"]:
				cancelled = True
				break

			if not unique_id:
				print("ID field cannot be empty.")
				continue

			elif unique_id in contacts:
				print("A contact with this ID already exits.")

			else:
				break

		if cancelled:
			print("Cancelled adding contact.")
			continue

		# --- FULL NAME ---
		while True:
			name = input("Enter full name (or 'q/quit' to cancel): ").strip().title()

			if name.lower() in ["quit", "q"]:
				cancelled = True
				break

			if not name:
				print("Name field cannot be empty.")
				continue

			elif not all(char.isspace() or char.isalpha() for char in name):
				print("Name must contain letters and spaces only.")
				continue

			else:
				break

		if cancelled:
			print("Cancelled adding contact.")
			continue

		# --- EMAIL ---
		while True:
			email = input("Enter email (or 'q/quit' to cancel): ").strip().lower()
			
			if email.lower() in ["quit", "q"]:
				cancelled = True
				break

			if not email:
				print("Email cannot be empty.")
				continue

			elif "@" not in email or "." not in email:
				print("Invalid Email format.")
				continue

			elif email in emails:
				print("This email is already registerd.")
				continue

			else:
				break

		if cancelled:
			print("Cancelled adding contact.")
			continue

		# --- PHONE ---
		while True:
			phone = input("Enter Phone Number (11 digits, or 'q/quit' to cancel): ").strip()

			if phone.lower() in ["quit", "q"]:
				cancelled = True
				break

			if not phone:
				print("Phone field cannot be empty.")
				continue

			elif not phone.isdigit() or len(phone) != 11:
				print("Phone must be a digit and its length exactly 11 digits.")
				continue

			elif phone in phones:
				print("This phone number already belongs to another contact.")			
				continue

			else:
				break

		if cancelled:
			print("Cancelled adding contact.")
			continue		

		# --- ROLE ---
		while True:
			role = input("Enter role (ROLES or 'q/quit' to cancel): ").strip().title()

			if role.lower() in ["quit", "q"]:
				cancelled = True
				break

			if role not in ROLES:
				print("Invalid role selection.")
				continue

			else:
				break

		if cancelled:
			print("Cancelled adding contact.")
			continue

		# --- SAVE CONTACT ---
		contacts[unique_id] = {
		"name": name,
		"email": email,
		"phone": phone,
		"role": role
		}

		# --- ADD EMAIL AND PHONE NUMBERS TO EMAIL/PHONE SETS ---
		emails.add(email)
		phones.add(phone)
		print("Contact added successfully!")

	# === UPDATE CONTACT ===
	elif choice == "2":
		print("\n--- UPDATE CONTACT ---")
		cancelled = False
		while True:
			unique_id = input("Enter Unique ID (or 'q/quit' to cancel): ").strip().upper()

			if unique_id.lower() in ["quit", "q"]:
				cancelled = True
				break

			if unique_id not in contacts:
				print("No contact found with this ID.")
				continue
			else:
				break

		if cancelled:
			print("Cancelled adding contact.")
			continue
		
		contact = contacts[unique_id]

		print("\nEXISTING DATA:")
		print("Name:", contact["name"])
		print("Email:", contact["email"])
		print("Phone:", contact["phone"])
		print("Role:", contact["role"])

		print("\nWhat do you want to update?")
		print("--- MENU ---")
		print("1. Name")
		print("2. Email")
		print("3. Phone")
		print("4. Role")

		while True:
			option = input("Choose an option (or 'q/quit' to cancel): ").strip()

			if option.lower() in ["quit", "q"]:
				cancelled = True
				break

			if option not in ["1", "2", "3", "4"]:
				print("Invalid option. Choose 1 - 4.")
				continue

			else:
				break

		if cancelled:
			print("Cancelled adding contact.")
			continue

		# UPDATE NAME
		if option == "1":
			while True:
				new_name = input("Enter new name (or 'q/quit' to canceel): ").strip()

				if new_name.lower() in ["quit", "q"]:
					cancelled = True
					break

				if not all(char.isspace() or char.isalpha() for char in new_name):
					print("Invalid name format.")
					continue

				else:
					contact["name"] = new_name
					print("Name updated successfully!")
					break

		# UPDATE EMAIL
		elif option == "2":
			while True:
				new_email = input("Enter new email (or 'q/quit' to cancel): ").strip()

				if new_email.lower() in ["quit", "q"]:
					cancelled = True
					break

				if (
					"@" in new_email
					and "." in new_email
					and (new_email == contact["email"]	# same email
					or new_email not in emails	 		# new unused email
					)):
					emails.remove(contact["email"])
					contact["email"] = new_email
					emails.add(new_email)
					print("Email updated successfully!")
				else:
					print("Invalid or duplicate email.")

		# UPDATE PHONE
		elif option == "3":
			while True:
				new_phone = input("Enter new phone number (or 'q/quit' to cancel): ").strip()

				if new_phone.lower() in ["quit", "q"]:
					cancelled = True
					break

				if (
					new_phone.isdigit()
					and len(new_phone) == 11
					and (new_phone == contact["phone"] or new_phone not in phones)):
					phones.remove(contact["phone"])
					contact["phone"] = new_phone
					phones.add(new_phone)
					print("Phone number updated successfully!")
					break

				else:
					print("Invalid or duplicate phone number.")

		# UPDATE ROLE
		elif option == "4":
			while True:
				new_role = input("Enter new role (or 'q/quit' to cancel): ").strip()

				if new_role.lower() in ["quit", "q"]:
					cancelled = True
					break

				if new_role in ROLES:
					contact["role"] = new_role
					print("Role updated successfully!")
					break

				else:
					print("Invalid role.")
		if cancelled:
			print("Cancelled adding contact.")
			continue

	# === DELETE CONTACT ===
	elif choice == "3":
		print("\n--- DELETE CONTACT ---")
		while True:
			unique_id = input("Enter ID to delete (or 'q/quit' to cancel): ").strip().upper()

			if unique_id.lower() in ["quit", "q"]:
				cancelled = True
				break

			if unique_id not in contacts:
				print("Contact not found")
				continue

			else:
				contact = contacts[unique_id]
				emails.remove(contact["email"])
				phones.remove(contact["phone"])
				del contacts[unique_id]
				print("Contact deleted successfully!")
				break

		if cancelled:
			print("Cancelled adding contact.")
			continue

	# === SEARCH CONTACT ===
	elif choice == "4":
		print("\n--- SEARCH CONTACT ---")
		while True:
			unique_id = input("Enter ID to search (or 'q/quit' to cancel): ").strip().upper()

			if unique_id.lower() in ["quit", "q"]:
				cancelled = True
				break

			if unique_id not in contacts:
				print("No contact found.")
				continue

			else:
				contact = contacts[unique_id]
				print("\n---- CONTACT DETAILS ---")
				print("ID:", unique_id)
				print("Name:", contact["name"])
				print("Email:", contact["email"])
				print("Phone:", contact["phone"])
				print("Role:", contact["role"])
				break
		if cancelled:
			print("Cancelled adding contact.")
			continue

	# === LIST ALL CONTACTS ===
	elif choice == "5":
		print("\n--- ALL CONTACTS ---")

		if len(contacts) == 0:
			print("No contacts available")
			continue

		for unique_id, contact in contacts.items():
			print("*" * 25)
			print("ID:", unique_id)
			print("Name:", contact["name"])
			print("Email:", contact["email"])
			print("Phone:", contact["phone"])
			print("Role:", contact["role"])
			print("*" * 25)

	# --- EXIT PROGRAM
	elif choice == "6":
		print("Thank you for using Student Contact Manager!")
		break
	else:
		print("Invalid choice selection. Please, enter a number between 1 and 6.")