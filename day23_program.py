def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")

    with open("students.txt", "a") as file:
        file.write(name + "," + age + "\n")

    print("Student added!")


def show_students():
    try:
        with open("students.txt", "r") as file:
            data = file.readlines()

            if len(data) == 0:
                print("No students found")
            else:
                for line in data:
                    name, age = line.strip().split(",")
                    print("Name:", name, "| Age:", age)

    except FileNotFoundError:
        print("No file found")


# 🔍 SEARCH FUNCTION
def search_student():
    name_to_search = input("Enter name to search: ")

    found = False

    with open("students.txt", "r") as file:
        for line in file:
            name, age = line.strip().split(",")

            if name.lower() == name_to_search.lower():
                print("Found → Name:", name, "| Age:", age)
                found = True
                break

    if not found:
        print("Student not found")


# ❌ DELETE FUNCTION
def delete_student():
    name_to_delete = input("Enter name to delete: ")

    updated_data = []
    found = False

    with open("students.txt", "r") as file:
        for line in file:
            name, age = line.strip().split(",")

            if name.lower() != name_to_delete.lower():
                updated_data.append(line)
            else:
                found = True

    with open("students.txt", "w") as file:
        file.writelines(updated_data)

    if found:
        print("Student deleted")
    else:
        print("Student not found")


# MENU
while True:
    print("\n1. Add Student")
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
        break

    else:
        print("Invalid choice")