# House Robber
arr = [2, 7, 9, 3, 1]

prev2 = 0
prev1 = 0

for num in arr:
    curr = max(prev1, prev2 + num)

    prev2 = prev1
    prev1 = curr

print(prev1)



# Maximum Subarray
arr = [-2,1,-3,4,-1,2,1,-5,4]

max_sum = arr[0]
curr_sum = arr[0]

for i in range(1, len(arr)):
    curr_sum = max(arr[i], curr_sum + arr[i])
    max_sum = max(max_sum, curr_sum)

print(max_sum)