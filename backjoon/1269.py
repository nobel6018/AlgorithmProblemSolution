# https://www.acmicpc.net/problem/1269

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

table = dict()
for _ in range(2):
    for num in input().split():
        if table.get(num, 0) == 0:
            table[num] = 1
        else:
            table[num] += 1

answer = 0
for value in table.values():
    if value == 1:
        answer += 1

print(answer)
