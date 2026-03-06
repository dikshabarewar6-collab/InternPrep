#1. Write in File
file = open("data.txt", "w")

file.write("Hello Diksha\n")
file.write("Learning Python File Handling")

file.close()


#2. Read the File
file = open("data.txt", "r")

content = file.read()

print(content)

file.close()

#3. Append File
file = open("data.txt", "a")

file.write("\nThis line is appended")

file.close()


#4. Student Log System
name = input("Enter student name: ")

with open("students.txt", "a") as file:
    file.write(name + "\n")

print("Student saved successfully!")