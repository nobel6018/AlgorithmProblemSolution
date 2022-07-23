# https://www.acmicpc.net/problem/2606

import sys

input = sys.stdin.readline

nodes = int(input())
edges = int(input())

visited = [False] * (nodes + 1)
visited[1] = True

graph = [[0] * (nodes + 1) for _ in range(nodes + 1)]
for _ in range(edges):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


def dfs(graph, visited, start_node):
    for i in range(len(graph[0])):
        if graph[start_node][i] == 1 and visited[i] is False:
            visited[i] = True
            dfs(graph, visited, i)


dfs(graph, visited, 1)

first_node_visited_count = 1
print(visited.count(True) - first_node_visited_count)
