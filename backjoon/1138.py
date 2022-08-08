# https://www.acmicpc.net/problem/1138

n = input()
offsets = list(map(int, input().split()))

orders = [0] * len(offsets)

for i in range(len(offsets)):
    zero_count = offsets[i]
    index = 0
    while zero_count > 0 or orders[index] != 0:
        if orders[index] == 0:
            zero_count -= 1
        index += 1

    orders[index] = i + 1

print(" ".join(str(i) for i in orders))
