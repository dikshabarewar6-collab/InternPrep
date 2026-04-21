# Climbing Stairs
def climb(n):
    if n <= 2:
        return n

    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

print(climb(4))



# Maximum sum
arr = [2, 7, 9, 3, 1]

dp = [0] * len(arr)

dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])

for i in range(2, len(arr)):
    dp[i] = max(dp[i-1], dp[i-2] + arr[i])

print(dp[-1])