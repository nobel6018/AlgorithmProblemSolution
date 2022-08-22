# https://www.acmicpc.net/problem/1912

import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

length = len(numbers)
total = [0] * length
total[-1] = numbers[-1]

for i in range(length - 2, -1, -1):
    if total[i + 1] > 0:
        total[i] = numbers[i] + total[i + 1]
    else:
        total[i] = numbers[i]

print(max(total))
