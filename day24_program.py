#Project Polish (Sorting + UI)
# Add Student
def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")

    with open("students.txt", "a") as file:
        file.write(name + "," + age + "\n")

    print("Student added successfully!")


# Show Students (Sorted + Numbering)
def show_students():
    try:
        with open("students.txt", "r") as file:
            data = file.readlines()

            if len(data) == 0:
                print("No students found")
                return

            students = []

            for line in data:
                name, age = line.strip().split(",")
                students.append((name, int(age)))

            # Sort by name
            students.sort()

            print("\n--- Student List ---")
            for i, s in enumerate(students, start=1):
                print(f"{i} | Name: {s[0]} | Age: {s[1]}")

    except FileNotFoundError:
        print("No file found")


# Search Student
def search_student():
    name_to_search = input("Enter name to search: ")

    found = False

    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, age = line.strip().split(",")

                if name.lower() == name_to_search.lower():
                    print(f"Found → Name: {name} | Age: {age}")
                    found = True
                    break

        if not found:
            print("Student not found")

    except FileNotFoundError:
        print("No file found")


# Delete Student
def delete_student():
    name_to_delete = input("Enter name to delete: ")

    updated_data = []
    found = False

    try:
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

    except FileNotFoundError:
        print("No file found")


# 🔥 MAIN MENU (Function call yahi hota hai)
while True:
    print("\n====== STUDENT SYSTEM ======")
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
        print("Invalid choice")