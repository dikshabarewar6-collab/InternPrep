# OOP + List + Functions
# Mini Project : Student Management System

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name, "| Age:", self.age)

students = []

def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))

    s = Student(name, age)
    students.append(s)

    print("Student added successfully!")


def show_students():
    if len(students) == 0:
        print("No students found")
    else:
        for s in students:
            s.display()


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
    