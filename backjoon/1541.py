# https://www.acmicpc.net/problem/1541

numbers = input().split("-")

minimum_sum = 0
for i in numbers[0].split("+"):
    minimum_sum += int(i)

for i in numbers[1:]:
    for j in i.split("+"):
        minimum_sum -= int(j)

print(minimum_sum)
