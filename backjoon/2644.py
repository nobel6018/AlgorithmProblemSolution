# https://www.acmicpc.net/problem/2644

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
start_node, end_node = map(int, input().split())
m = int(input())

graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

# (node, cost)
queue = deque([(start_node, 0)])
visited = [False] * (n + 1)

while queue:
    node, cost = queue.popleft()
    for target in range(n + 1):
        if graph[node][target] == 1 and not visited[target]:
            if target == end_node:
                print(cost + 1)
                exit(0)

            graph[node][target] = cost + 1
            visited[target] = True
            queue.append((target, cost + 1))

print(-1)
