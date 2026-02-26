#Simple Calculator (Mini Project Level)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
if op == "*":
    print("Result:", num1 * num2)
if op == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", num1 / num2)

else:
    print("Invalid operator")


#Sensor Range System (Robotics Thinking)

value = int(input("Enter sensor value:"))

if value < 0:
    print("Invalid value")
elif value <= 30:
    print("Very low")
elif value <= 60:
    print("Low")
elif value <= 90:
    print("Medium")
elif value <= 120:
    print("High")

else:
    print("Critical")