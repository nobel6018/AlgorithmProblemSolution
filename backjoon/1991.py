import sys

input = sys.stdin.readline

n = int(input())
graph = dict()
for i in range(n):
    a, b, c = input().split()
    graph[a] = [b, c]


def dfs_in_order(graph, node, visited):
    if node == ".":
        return

    ordinary = ord(node) - 65
    if visited[ordinary] is True:
        return

    visited[ordinary] = True

    print(node, end="")
    dfs_in_order(graph, graph[node][0], visited)
    dfs_in_order(graph, graph[node][1], visited)


def dfs_pre_order(graph, node, visited):
    if node == ".":
        return

    ordinary = ord(node) - 65
    if visited[ordinary] is True:
        return

    visited[ordinary] = True

    dfs_pre_order(graph, graph[node][0], visited)
    print(node, end="")
    dfs_pre_order(graph, graph[node][1], visited)


def dfs_post_order(graph, node, visited):
    if node == ".":
        return

    ordinary = ord(node) - 65
    if visited[ordinary] is True:
        return

    visited[ordinary] = True

    dfs_post_order(graph, graph[node][0], visited)
    dfs_post_order(graph, graph[node][1], visited)
    print(node, end="")


dfs_in_order(graph, "A", [False] * n)
print()
dfs_pre_order(graph, "A", [False] * n)
print()
dfs_post_order(graph, "A", [False] * n)
