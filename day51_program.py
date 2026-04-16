# Two Sum
arr = [2,7,11,15]
target = 9

seen = {}

for num in arr:
    diff = target - num

    if diff in seen:
        print(diff, num)

    seen[num] = True

# Duplicate check
arr = [1,2,3,2]

seen = set()

for num in arr:
    if num in seen:
        print("Duplicate found:", num)
        break
    seen.add(num)


# Count frequency
arr = [1,2,2,3,3,3]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

print(freq)