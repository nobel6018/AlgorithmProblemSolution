# https://www.acmicpc.net/problem/1003

T = int(input())

dp0 = [1, 0, ]
dp1 = [0, 1, ]

for i in range(2, 41):
    dp0.append(dp0[i - 1] + dp0[i - 2])
    dp1.append(dp1[i - 1] + dp1[i - 2])

for _ in range(T):
    n = int(input())
    print(dp0[n], dp1[n])
