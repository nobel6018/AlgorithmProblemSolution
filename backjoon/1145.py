# https://www.acmicpc.net/problem/1145

numbers = list(map(int, input().split(" ")))

number = 0
count = 0
while count < 3:
    number += 1
    count = 0
    for n in numbers:
        if number % n == 0:
            count += 1
        if count == 3:
            break

print(number)
