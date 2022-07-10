# https://www.acmicpc.net/problem/1463
import sys

input = sys.stdin.readline

target = int(input())

INF = int(1e8)
dp = [INF] * (target + 1)
dp[1] = 0

for num in range(1, target + 1):
    if num * 3 <= target:
        dp[num * 3] = min(dp[num * 3], dp[num] + 1)
    if num * 2 <= target:
        dp[num * 2] = min(dp[num * 2], dp[num] + 1)
    if num + 1 <= target:
        dp[num + 1] = min(dp[num + 1], dp[num] + 1)

print(dp[target])
