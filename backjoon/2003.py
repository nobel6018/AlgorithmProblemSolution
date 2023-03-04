import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

answer = 0
i = 0
j = 0
total = numbers[i]
while j < n:
    if total < m:
        if j + 1 == n:
            break
        j += 1
        total += numbers[j]
    elif total > m:
        total -= numbers[i]
        i += 1
    else:  # total == m
        answer += 1
        if j > i:
            total -= numbers[i]
            i += 1
        else:
            if j + 1 == n:
                break
            j += 1
            total += numbers[j]

print(answer)
