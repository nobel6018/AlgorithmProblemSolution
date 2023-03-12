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

step = 0
while q:
    if zero_count == 0:
        break
    step += 1

    for _ in range(len(q)):
        i, j = q.popleft()
        # 방문 처리
        graph[i][j] = 1

        # 상하좌우
        top = (i - 1, j)
        bottom = (i + 1, j)
        left = (i, j - 1)
        right = (i, j + 1)

        if 0 <= top[0] < n and 0 <= top[1] < m and graph[top[0]][top[1]] == 0:
            graph[top[0]][top[1]] = 1
            zero_count -= 1
            q.append((top[0], top[1]))

        if 0 <= bottom[0] < n and 0 <= bottom[1] < m and graph[bottom[0]][bottom[1]] == 0:
            graph[bottom[0]][bottom[1]] = 1
            zero_count -= 1
            q.append((bottom[0], bottom[1]))

        if 0 <= left[0] < n and 0 <= left[1] < m and graph[left[0]][left[1]] == 0:
            graph[left[0]][left[1]] = 1
            zero_count -= 1
            q.append((left[0], left[1]))

        if 0 <= right[0] < n and 0 <= right[1] < m and graph[right[0]][right[1]] == 0:
            graph[right[0]][right[1]] = 1
            zero_count -= 1
            q.append((right[0], right[1]))

if zero_count > 0:
    print(-1)
else:
    print(step)
