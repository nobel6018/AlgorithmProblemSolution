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
for i in range(n + 1):
    parent[i] = i

for _ in range(m):
    operator, a, b = map(int, input().split())
    if operator == 0:  # union
        union_parent(parent, a, b)
    else:  # find
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')

#
# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1
