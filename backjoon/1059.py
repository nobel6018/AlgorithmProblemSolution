# https://www.acmicpc.net/problem/1059

# 1. 최소 수 (입력값으로 들어온 수 중에서)
# 2. 최대 수 (입력값으로 들어온 수 중에서)
# 3. (최소수 ~ n) 개수 * (n ~ 최대수) 개수 - 1 (n,n)

length = int(input())
numbers = list(map(int, input().split(" ")))
n = int(input())

min_number = 0
max_number = 9999

for number in numbers:
    if n >= number > min_number:
        min_number = number
    elif n <= number < max_number:
        max_number = number

if n == min_number or n == max_number:
    print(0)
else:
    print((n - min_number) * (max_number - n) - 1)
