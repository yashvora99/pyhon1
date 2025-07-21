contact_list = []

n = 3

def add_contact():
    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        phone = int(input(f"Enter phone number of contact {i+1}: "))

        contact_list.append({
        "id": str(i + 1),
        "name": name,
        "phone": phone
        })

        print("Contacts added!!")

def display_contacts():
    for data in contact_list:
        for key, value in data.items():
            print(key, ":", value)
        print()

def search_contact():
    name = input("Enter contact name to search: ")
    found = False
    for data in contact_list:
        if data["name"] == name:
            found = True
            print("Contact found!!")
            print(data["name"])
            print(data["phone"])
            break
        if not found:
            print("Contact not found!!")
            break

while True:
    print("Contacts App")
    print("1. Create Contact")
    print("2. Display all contacts")
    print("3. Search from contact list")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        display_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice, please select 1–4.\n")
        break