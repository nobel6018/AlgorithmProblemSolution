from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


def bfs(graph, start_row, start_col):
    # row, col, step
    queue = deque()
    queue.append((start_row, start_col))

    # 아래, 위, 오른쪽, 왼쪽
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    while queue:
        row, col = queue.popleft()
        for i in range(4):
            if row + dy[i] < 0 or row + dy[i] >= n or col + dx[i] < 0 or col + dx[i] >= m:
                continue

            if graph[row + dy[i]][col + dx[i]] == 1:
                graph[row + dy[i]][col + dx[i]] = graph[row][col] + 1
                queue.append((row + dy[i], col + dx[i]))

    return graph[n - 1][m - 1]


print(bfs(graph, 0, 0))

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
