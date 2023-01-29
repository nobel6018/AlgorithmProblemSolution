import sys

input = sys.stdin.readline

n, r, c = map(int, input().split())


def new_point(point, n):
    return int(point - 2 ** (n - 1))


def dnc(n, r, c):
    if n == 1:
        return 2 * r + c

    # 1사분면
    if r < 2 ** (n - 1) and c < 2 ** (n - 1):
        return dnc(n - 1, r, c)
    # 2사분면
    elif r < 2 ** (n - 1) and c > 2 ** (n - 1):
        return 2 ** (2 * n - 2) + dnc(n - 1, r, new_point(c, n))
    # 3사분면
    elif r > 2 ** (n - 1) and c < 2 ** (n - 1):
        return 2 ** (2 * n - 1) + dnc(n - 1, new_point(r, n), c)
    # 4사분면
    else:
        return 3 * 2 ** (2 * n - 2) + dnc(n - 1, new_point(r, n), new_point(c, n))


print(dnc(n, r, c))
