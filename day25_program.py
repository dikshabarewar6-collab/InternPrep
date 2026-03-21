#JSON(JavaScript Object Notation)

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


def add_student():
    data = load_data()

    name = input("Enter name: ")
    age = int(input("Enter age: "))

    data.append({"name": name, "age": age})

    save_data(data)
    print("Student added!")


def show_students():
    data = load_data()

    if len(data) == 0:
        print("No students found")
    else:
        print("\n--- Student List ---")
        for i, s in enumerate(data, start=1):
            print(f"{i} | Name: {s['name']} | Age: {s['age']}")


# MENU
while True:
    print("\n====== JSON STUDENT SYSTEM ======")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        break

    else:
        print("Invalid choice")