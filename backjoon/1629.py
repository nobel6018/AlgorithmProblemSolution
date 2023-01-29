import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())


def dac(a, b):
    if b == 1:
        return a % c

    temp = dac(a, b // 2)
    if b % 2 == 0:
        return temp ** 2 % c
    else:
        return temp ** 2 * a % c


print(dac(a, b))
