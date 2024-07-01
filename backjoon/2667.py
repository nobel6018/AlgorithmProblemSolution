n = int(input())

graph = [list(map(int, input())) for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if not (0 <= x < n and 0 <= y < n):
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        global count
        count += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

        return True

    return False


answer = []
count = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) is True:
            answer.append(count)
            count = 0

answer.sort()
print(len(answer))
for a in answer:
    print(a)
