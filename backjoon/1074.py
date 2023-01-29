import sys

input = sys.stdin.readline

n, r, c = map(int, input().split())


def new_point(point, n):
    return int(point - 2 ** (n - 1))


def dnc(n, r, c):
    if n == 1:
        return 2 * r + c

    # 2사분면
    if r < 2 ** (n - 1) and c < 2 ** (n - 1):
        return dnc(n - 1, r, c)
    # 1사분면
    elif r < 2 ** (n - 1) and c >= 2 ** (n - 1):
        return 2 ** (2 * n - 2) + dnc(n - 1, r, new_point(c, n))
    # 3사분면
    elif r >= 2 ** (n - 1) and c < 2 ** (n - 1):
        return 2 ** (2 * n - 1) + dnc(n - 1, new_point(r, n), c)
    # 4사분면
    else:
        return 3 * 2 ** (2 * n - 2) + dnc(n - 1, new_point(r, n), new_point(c, n))


print(dnc(n, r, c))

# test code
# print(dnc(2, 0, 0) == 0)
# print(dnc(2, 0, 1) == 1)
# print(dnc(2, 1, 0) == 2)
# print(dnc(2, 1, 1) == 3)
#
# print(dnc(2, 0, 2) == 4)
# print(dnc(2, 0, 3) == 5)
# print(dnc(2, 1, 2) == 6)
# print(dnc(2, 1, 3) == 7)
#
# print(dnc(2, 2, 0) == 8)
# print(dnc(2, 2, 1) == 9)
# print(dnc(2, 3, 0) == 10)
# print(dnc(2, 3, 1) == 11)
#
# print(dnc(2, 2, 2) == 12)
# print(dnc(2, 2, 3) == 13)
# print(dnc(2, 3, 2) == 14)
# print(dnc(2, 3, 3) == 15)
