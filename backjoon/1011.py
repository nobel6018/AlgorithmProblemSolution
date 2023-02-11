import math

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    delta = b - a

    mod = int(math.sqrt(delta))
    left = delta - mod ** 2
    if left == 0:
        print(2 * mod - 1)
        continue
    else:
        half = ((mod + 1) ** 2 - mod ** 2) // 2
        if half < left:
            print(2 * mod - 1 + 2)
            continue
        else:
            print(2 * mod - 1 + 1)
