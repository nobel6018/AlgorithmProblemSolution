# https://www.acmicpc.net/problem/1010

dp = [[0] * 30 for _ in range(30)]

for i in range(30):
    dp[1][i] = i

for i in range(1, 30):
    for j in range(i, 30):
        k = j - 1
        while k >= i - 1:
            dp[i][j] += dp[i - 1][k]
            k -= 1

length = int(input())
for _ in range(length):
    (N, M) = map(int, input().split(" "))
    print(dp[N][M])
