# https://www.acmicpc.net/problem/1037

N = int(input())
numbers = list(map(int, input().split(" ")))

print(max(numbers) * min(numbers))
