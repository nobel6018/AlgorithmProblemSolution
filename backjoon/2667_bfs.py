from collections import deque

n = int(input())

graph = [list(map(int, input())) for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    count = 0
    queue = deque()
    if graph[x][y] == 1:
        queue.append((x, y))
        count += 1
        graph[x][y] = 0

    while queue:
        x, y = queue.popleft()

        # 상하좌우 방문
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:  # 범위 안
                if graph[nx][ny] == 1:  # 방문 가능
                    queue.append((nx, ny))
                    count += 1
                    graph[nx][ny] = 0

    return count


answer = []
for i in range(n):
    for j in range(n):
        result = bfs(i, j)
        if result > 0:
            answer.append(result)

print(len(answer))
for a in answer:
    print(a)
