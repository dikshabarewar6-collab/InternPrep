# Upgrade Student System 
import json

file_name = "students.json"


def load_data():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return []


def save_data(data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


# 🔹 VALIDATED INPUT
def get_valid_age():
    while True:
        try:
            age = int(input("Enter age: "))
            if age > 0:
                return age
            else:
                print("Age must be positive")
        except:
            print("Invalid input! Enter a number.")


def add_student():
    data = load_data()

    name = input("Enter name: ").strip()

    if name == "":
        print("Name cannot be empty!")
        return

    age = get_valid_age()

    data.append({"name": name, "age": age})

    save_data(data)
    print("Student added successfully!")


def show_students():
    data = load_data()

    if len(data) == 0:
        print("No students found")
        return

    # Sort by name
    data.sort(key=lambda x: x["name"])

    print("\n--- Student List ---")
    for i, s in enumerate(data, start=1):
        print(f"{i} | Name: {s['name']} | Age: {s['age']}")


def search_student():
    data = load_data()

    name = input("Enter name to search: ").lower()

    found = False

    for s in data:
        if name in s["name"].lower():   # partial search
            print(f"Found → Name: {s['name']} | Age: {s['age']}")
            found = True

    if not found:
        print("Student not found")


def delete_student():
    data = load_data()

    name = input("Enter name to delete: ").lower()

    new_data = []
    found = False

    for s in data:
        if name not in s["name"].lower():
            new_data.append(s)
        else:
            found = True

    if found:
        confirm = input("Are you sure? (yes/no): ").lower()
        if confirm == "yes":
            save_data(new_data)
            print("Student deleted")
        else:
            print("Cancelled")
    else:
        print("Student not found")


# 🔥 MAIN MENU
while True:
    print("\n====== STUDENT SYSTEM (JSON) ======")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")