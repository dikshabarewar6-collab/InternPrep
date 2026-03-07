# #1. Error 

# num = int(input("Enter number: "))
# result = 10 / num

# print(result)

# #2. try/except (Agar program crash hone se bachana h)

# try:
#     num = int(input("Enter number: "))
#     result = 10 / num
#     print(result)

# except:
#     print("Error occurred")


# #3. Handle Specific Error


# try:
#     num = int(input("Enter number: "))
#     result = 10 / num
#     print(result)

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# except ValueError:
#     print("Invalid input")


# #4. else Block

# try:
#     num = int(input("Enter number: "))
#     result = 10 / num

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# else:
#     print("Result:", result)


# #5. finally Block

# try:
#     num = int(input("Enter number: "))
#     result = 10 / num

# except ZeroDivisionError:
#     print("Error")

# finally:
#     print("Program finished")


#6. Mini Project

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter numbers only")

else:
    print("Result:", result)