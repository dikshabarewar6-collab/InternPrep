# Sliding window
arr = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, len(arr)):
    window_sum += arr[i]       # add next
    window_sum -= arr[i-k]     # remove old

    max_sum = max(max_sum, window_sum)

print("Max Sum:", max_sum)





# Two pointer technique
arr = [2, 4, 6, 8, 10]
target = 10

left = 0
right = len(arr) - 1

while left < right:
    curr = arr[left] + arr[right]

    if curr == target:
        print(arr[left], arr[right])
        break

    elif curr < target:
        left += 1
    else:
        right -= 1