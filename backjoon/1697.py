import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

visited = [False] * 100001
visited[n] = True

queue = deque([(n, 0)])
while queue:
    p = queue.popleft()
    if p[0] == k:
        print(p[1])
        break

    p1 = p[0] - 1
    if 0 <= p1 <= 100000 and visited[p1] is False:
        visited[p1] = True
        queue.append((p1, p[1] + 1))

    p2 = p[0] + 1
    if 0 <= p2 <= 100000 and visited[p2] is False:
        visited[p2] = True
        queue.append((p2, p[1] + 1))

    p3 = 2 * p[0]
    if 0 <= p3 <= 100000 and visited[p3] is False:
        visited[p3] = True
        queue.append((p3, p[1] + 1))
