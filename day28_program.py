import tkinter as tk

def calculate():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())

        result = num1 + num2

        result_label.config(text="Result: " + str(result))

    except:
        result_label.config(text="Enter valid numbers!")

# window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")

# input 1
tk.Label(root, text="Enter first number").pack()
entry1 = tk.Entry(root)
entry1.pack()

# input 2
tk.Label(root, text="Enter second number").pack()
entry2 = tk.Entry(root)
entry2.pack()

# button
tk.Button(root, text="Add", command=calculate).pack(pady=10)

# result
result_label = tk.Label(root, text="")
result_label.pack()

# run
root.mainloop()