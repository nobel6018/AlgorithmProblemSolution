# 위상정렬

import copy
from collections import deque
from typing import List

v = int(input())

indegree = [0] * (v + 1)

graph: List[List[int]] = [[] for _ in range(v + 1)]
times: List[int] = [0] * (v + 1)

for i in range(1, v + 1):
    info = list(map(int, input().split()))

    times[i] = info[0]

    for pre in info[1:]:
        if pre != -1:
            graph[pre].append(i)
            indegree[i] += 1


def topology_sort():
    result = copy.deepcopy(times)
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for next in graph[now]:
            result[next] = max(result[next], result[now] + times[next])
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)

    for i in range(1, v + 1):
        print(result[i])


topology_sort()

# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1
