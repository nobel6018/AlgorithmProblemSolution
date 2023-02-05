import sys

input = sys.stdin.readline

n = int(input())

image = [[] for _ in range(n)]

for i in range(n):
    for item in input().strip('\n'):
        image[i].append(int(item))


def dnc(image, n, row_start, col_start):
    if n == 1:
        return image[row_start][col_start]

    half = n // 2
    squad_2 = dnc(image, half, row_start, col_start)
    squad_1 = dnc(image, half, row_start, col_start + half)
    squad_3 = dnc(image, half, row_start + half, col_start)
    squad_4 = dnc(image, half, row_start + half, col_start + half)
    if squad_1 == squad_2 == squad_3 == squad_4:
        return squad_1
    else:
        return f"({squad_2}{squad_1}{squad_3}{squad_4})"


print(dnc(image, n, 0, 0))
