#1 Python Set
numbers = {1, 2, 3, 4, 5}
print(numbers)

#2 Duplicate remove
numbers = {1, 2, 2, 3, 4, 4, 5}
print(numbers)

#3 List from Set
nums = [10, 20, 20, 30, 30, 40]

unique_nums = set(nums)

print(unique_nums)

#4 Add Element in Set
numbers = {1, 2, 3}

numbers.add(4)

print(numbers)

#5 Remove element
numbers = {1, 2, 3, 4}

numbers.remove(2)

print(numbers)

#6 Loop through Set
numbers = {10, 20, 30}

for num in numbers:
    print(num)

#7 Set Operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)

#8 Student IDs program
classA = {101, 102, 103, 104}
classB = {103, 104, 105}

common_students = classA & classB

print("Students in both classes:", common_students)