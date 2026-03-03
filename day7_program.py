# Basic Functions

def greet():                    # def = define function
                                # greet = function name
    print("Hello Diksha")

greet()                         # greet = function call



# Function with parameter

def greet(name):
    print("Hello", name)

greet("Diksha")
greet("Riya")


# Function with return

def add(a, b):
    return a + b

result = add(5, 3)
print(result)


# Even odd function

def check_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even(10))
print(check_even(7))

# Scope

x = 10   # Global variable

def show():
    x = 5   # Local variable
    print(x)

show()
print(x)

# Max Finder function

def find_max(numbers):
    max_value = numbers[0]

    for num in numbers:
        if num > max_value:
            max_value = num

    return max_value


values = [45, 60, 120, 30, 150]
result = find_max(values)

print("Highest:", result)