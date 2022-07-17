n, m = map(int, input().split())

graph = []
for _ in range(n):
    row = list(map(int, input()))
    graph.append(row)


def dfs(graph, row, column):
    # 주어진 범위를 벗어난 경우에는 즉시 종료
    if row < 0 or row >= n or column < 0 or column >= m:
        return False

    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]

    # 아직 방문하지 않은 경우
    if graph[row][column] == 0:
        for i in range(4):
            graph[row][column] = 1
            dfs(graph, row + dy[i], column + dx[i])

        return True


answer = 0
for i in range(n):
    for j in range(m):
        if dfs(graph, i, j) is True:
            answer += 1

print(answer)

# 4 5
# 00110
# 00011
# 11111
# 00000
