#1. Array Traversal
arr = [10, 20, 30, 40]

for num in arr:
    print(num)

#2. Sum
arr = [10, 20, 30]

total = 0

for num in arr:
    total += num

print("Sum:", total)

#3. Find maximum
arr = [10, 5, 25, 8]

max_val = arr[0]

for num in arr:
    if num > max_val:
        max_val = num

print("Max:", max_val)

#4. Find Minimum
arr = [10, 5, 25, 8]

min_val = arr[0]

for num in arr:
    if num < min_val:
        min_val = num

print("Max:", min_val)

#5. Count Even numbers
arr = [1,2,3,4,5,6]

count = 0

for num in arr:
    if num % 2 == 0:
        count += 1

print("Even count:", count)