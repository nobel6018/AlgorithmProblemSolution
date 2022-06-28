# https://www.acmicpc.net/problem/1018

(n, m) = map(int, input().split(" "))
maps = []
for _ in range(n):
    maps.append(list(input()))

minimum = 99999

for i in range(n - 7):
    for j in range(m - 7):  # 시작 위치
        needs_update = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if maps[k][l] == "B":
                        needs_update += 1
                else:
                    if maps[k][l] == "W":
                        needs_update += 1
        needs_update = min(needs_update, 64 - needs_update)
        minimum = min(minimum, needs_update)

print(minimum)
