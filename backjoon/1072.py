# https://www.acmicpc.net/problem/1072
import sys

input = sys.stdin.readline

x, y = map(int, input().split())
z = int(100 * y / x)

start = 0
end = x

answer = -1
while start <= end:
    middle = (start + end) // 2
    new_z = int(100 * (y + middle) / (x + middle))

    if new_z > z:
        answer = middle
        end = middle - 1
    else:
        start = middle + 1

print(answer)
