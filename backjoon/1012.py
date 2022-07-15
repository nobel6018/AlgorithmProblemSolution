import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline

t = int(input())


def dfs(map, x, y):
    height = len(map)
    width = len(map[0])

    if x <= -1 or x >= width or y <= -1 or y >= height:
        return False

    if map[y][x] == 1:
        map[y][x] = 0
        dfs(map, x - 1, y)
        dfs(map, x + 1, y)
        dfs(map, x, y - 1)
        dfs(map, x, y + 1)

        return True


for _ in range(t):
    answer = 0
    m, n, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(n):
        for j in range(m):
            result = dfs(graph, j, i)
            if result is True:
                answer += 1

    print(answer)
