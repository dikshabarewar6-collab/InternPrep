# Student System with file saving

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name, "| Age:", self.age)


def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")

    with open("students.txt", "a") as file:
        file.write(name + "," + age + "\n")

    print("Student saved to file!")


def show_students():
    try:
        with open("students.txt", "r") as file:
            data = file.readlines()

            if len(data) == 0:
                print("No data found")
            else:
                for line in data:
                    name, age = line.strip().split(",")
                    print("Name:", name, "| Age:", age)

    except FileNotFoundError:
        print("No file found. Add students first.")


while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice")