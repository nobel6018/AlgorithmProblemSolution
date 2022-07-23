# https://www.acmicpc.net/problem/1260
import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, visited, start):
    visited[start] = True

    print(start, end=" ")

    for i in sorted(graph[start]):
        if visited[i] is False:
            dfs(graph, visited, i)


def bfs(graph, visited, start):
    queue = deque()
    queue.append(start)

    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for i in sorted(graph[node]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True


visited = [False] * (n + 1)
dfs(graph, visited, v)
print()

visited = [False] * (n + 1)
bfs(graph, visited, v)
