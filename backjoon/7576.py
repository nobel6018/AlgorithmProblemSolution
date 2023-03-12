import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

q = deque()
graph = []
zero_count = 0
for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)

    for j, v in enumerate(line):
        if v == 1:
            q.append((i, j))
        if v == 0:
            zero_count += 1


def visit(i, j):
    global q
    global graph
    global zero_count

    if 0 <= i < n and 0 <= j < m and graph[i][j] == 0:
        graph[i][j] = 1
        zero_count -= 1
        q.append((i, j))


step = 0
while q:
    if zero_count == 0:
        break
    step += 1

    for _ in range(len(q)):
        i, j = q.popleft()

        # 상하좌우 방문
        visit(i - 1, j)
        visit(i + 1, j)
        visit(i, j - 1)
        visit(i, j + 1)

if zero_count > 0:
    print(-1)
else:
    print(step)
