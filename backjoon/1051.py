# https://www.acmicpc.net/problem/1051

(n, m) = map(int, input().split(" "))
maps = []
for _ in range(n):
    maps.append(list(map(int, list(input()))))

max_diff = min(n, m)

for diff in reversed(range(1, max_diff)):
    for i in range(n - diff):
        for j in range(m - diff):
            if maps[i][j] == maps[i + diff][j] == maps[i][j + diff] == maps[i + diff][j + diff]:
                print((diff + 1) ** 2)
                exit(0)
print(1)
