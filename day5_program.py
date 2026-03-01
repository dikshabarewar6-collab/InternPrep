# Loop of List

numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)


# Sum of list

numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total += num
    print("Total:", total)


#Multiple input from user

numbers = []

for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)

print(numbers)


# list Function

numbers = [10, 20, 30]

numbers.append(40)    #add
numbers.remove(20)    #remove
numbers.pop()         #last remove
numbers.insert(1, 15) #insert at index

print (numbers)

# Sensor Reading

values = [45, 60, 120, 30, 150]

max_value = values[0]
for v in values:
    if v > max_value:
        max_value = v

print("Highest:", max_value)

if max_value > 100:
    print("Alert!")