# GUI Student Adder
import tkinter as tk
import json

# File name
file_name = "students.json"

# Load data
def load_data():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return []

# Save data
def save_data(data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

# Add student
def add_student():
    name = name_entry.get()
    age = age_entry.get()

    if name == "" or age == "":
        result_label.config(text="Enter all fields!")
        return

    try:
        age = int(age)
    except:
        result_label.config(text="Age must be number!")
        return

    data = load_data()
    data.append({"name": name, "age": age})
    save_data(data)

    result_label.config(text="Student Added!")

    # clear fields
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)


# 🔥 MAIN WINDOW
root = tk.Tk()
root.title("Student System")
root.geometry("300x250")

# Name
tk.Label(root, text="Enter Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Age
tk.Label(root, text="Enter Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()

# Button
tk.Button(root, text="Add Student", command=add_student).pack(pady=10)

# Result
result_label = tk.Label(root, text="")
result_label.pack()

# Run GUI
root.mainloop()