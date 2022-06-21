# https://www.acmicpc.net/problem/1009

T = int(input())

for _ in range(T):
    a, b = input().split(" ")
    a = int(a)
    b = int(b)

    if a % 10 == 0:
        print(10)
    else:
        a = a % 10

        cycle = 0
        if a == 1 or a == 5 or a == 6:
            cycle = 1
        elif a == 2 or a == 3 or a == 7 or a == 8:
            cycle = 4
        elif a == 4 or a == 9:
            cycle = 2

        result = cycle if (b % cycle) == 0 else (b % cycle)
        print((a ** result) % 10)
