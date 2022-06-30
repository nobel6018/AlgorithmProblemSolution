# https://www.acmicpc.net/problem/2751
# ref: https://www.acmicpc.net/board/view/31887 [필독] 수 정렬하기 2 FAQ
# ref: https://assaeunji.github.io/python/2020-05-06-bj2751/
n = int(input())

numbers = []
for _ in range(n):
    numbers.append(int(input()))

for i in sorted(numbers):
    print(i)
