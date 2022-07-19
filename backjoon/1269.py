# https://www.acmicpc.net/problem/1269

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

hash_map = dict()
for _ in range(2):
    for num in input().split():
        if hash_map.get(num, 0) == 0:
            hash_map[num] = 1
        else:
            hash_map[num] += 1

answer = 0
for value in hash_map.values():
    if value == 1:
        answer += 1

print(answer)
