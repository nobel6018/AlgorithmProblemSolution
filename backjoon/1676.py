# https://www.acmicpc.net/problem/1676

n = int(input())

count_10 = 0
count_2 = 0
count_5 = 0

for num in reversed(range(1, n + 1)):
    while num % 10 == 0:
        count_10 += 1
        num = num // 10
    while num % 5 == 0:
        count_5 += 1
        num = num // 5
    while num % 2 == 0:
        count_2 += 1
        num = num // 2

zeros = count_10
zeros += min(count_2, count_5)

print(zeros)
