# https://www.acmicpc.net/problem/1094

target = int(input())

count = 0
current_length = 64

if target == current_length:
    print(1)
    exit(0)

while current_length > 1:
    current_length = current_length // 2
    if current_length <= target:
        target -= current_length
        count += 1
        if target == 0:
            break

print(count)
