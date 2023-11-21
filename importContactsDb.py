

def main():
    while True:
        action = input("Enter your action (list, add, update, delete, exit): ")

        if action == "list":
            contacts = contacts_db.list_contacts()
            for contact in contacts:
                print(f"{contact['id']} - {contact['name']} - {contact['email']}")

        elif action == "add":
            name = input("Enter the contact's name: ")
            email = input("Enter the contact's email: ")
            contact_id = contacts_db.add_contact(name, email)
            print(f"Contact added successfully. ID: {contact_id}")

        elif action == "update":
            contact_id = int(input("Enter the contact's ID: "))
            new_name = input("Enter the new name (leave blank if not changing): ")
            new_email = input("Enter the new email (leave blank if not changing): ")
            contacts_db.update_contact(contact_id, new_name, new_email)
            print("Contact updated successfully.")

        elif action == "delete":
            contact_id = int(input("Enter the contact's ID to delete: "))
            contacts_db.delete_contact(contact_id)
            print("Contact deleted successfully.")

        elif action == "exit":
            print("Exiting CLI.")
            break

        else:
            print("Invalid action. Please enter a valid option.")

if __name__ == "__main__":
    main()



