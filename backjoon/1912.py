# https://www.acmicpc.net/problem/1912

import sys

input = sys.stdin.readline


def solution1():
    n = int(input())
    numbers = list(map(int, input().split()))

    total = [0] * n
    total[-1] = numbers[-1]

    for i in range(n - 2, -1, -1):
        if total[i + 1] > 0:
            total[i] = numbers[i] + total[i + 1]
        else:
            total[i] = numbers[i]

    print(max(total))


def solution2():
    n = int(input())
    numbers = list(map(int, input().split()))

    total = [0] * n
    total[0] = numbers[0]

    for i in range(1, n):
        if total[i - 1] > 0:
            total[i] = numbers[i] + total[i - 1]
        else:
            total[i] = numbers[i]

    print(max(total))


if __name__ == '__main__':
    solution1()
    # solution2()
