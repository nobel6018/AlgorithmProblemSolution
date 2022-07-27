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
queue = deque([(start_node, 1)])
while queue:
    node, cost = queue.popleft()
    for i in range(n + 1):
        if graph[node][i] == 1:
            if i == end_node:
                print(cost)
                exit(0)
            graph[node][i] = cost + 1
            queue.append((i, cost + 1))

print(-1)
