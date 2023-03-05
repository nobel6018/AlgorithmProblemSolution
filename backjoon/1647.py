# shortest spanning tree (크루스칼 알고리즘)
import sys

input = sys.stdin.readline

n, m = map(int, input().split())


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    root_a = find_parent(parent, a)
    root_b = find_parent(parent, b)
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b


parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

edges = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

max_cost = -1
answer = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += cost
        max_cost = max(max_cost, cost)
answer -= max_cost

print(answer)
