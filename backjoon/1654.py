# https://www.acmicpc.net/problem/1654

import sys

input = sys.stdin.readline

k, n = map(int, input().split())

cables = []
for _ in range(k):
    cables.append(int(input()))

start = 1
end = max(cables)

while start <= end:
    mid = (start + end) // 2

    count = 0
    for cable in cables:
        count += (cable // mid)

    if count >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)

# 4 11
# 822
# 743
# 457
# 539
# expected: 205