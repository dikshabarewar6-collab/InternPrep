# Find Missing Number
arr = [1, 2, 4, 5]

n = 5
total = n * (n + 1) // 2
actual = sum(arr)

print("Missing:", total - actual)


# Remove Duplicates
arr = [1,2,2,3,3,4]

unique = []

for num in arr:
    if num not in unique:
        unique.append(num)

print(unique)


# Count Vowels
text = "diksha"

count = 0

for ch in text:
    if ch in "aeiou":
        count += 1

print("Vowels:", count)


# Two Sum
arr = [2,7,11,15]
target = 9

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i], arr[j])