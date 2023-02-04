import sys

input = sys.stdin.readline

n = int(input())

nums = []
for _ in range(n):
    nums.append(int(input()))

dp = [0] * n
dp[0] = nums[0]
if n >= 2:
    dp[1] = nums[0] + nums[1]
if n >= 3:
    dp[2] = max(nums[2] + nums[1], nums[2] + nums[0], nums[1] + nums[0])
    for i in range(3, n):
        dp[i] = max(nums[i] + nums[i - 1] + dp[i - 3], nums[i] + dp[i - 2], dp[i - 1])

print(dp[n - 1])
