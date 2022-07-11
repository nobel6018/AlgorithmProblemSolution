# https://www.acmicpc.net/problem/1158

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

queue = deque()
for i in range(n):
    queue.append(i + 1)

answer = []
while len(queue) > 0:
    for i in range(k):
        if i + 1 == k:
            answer.append(queue.popleft())
        else:
            queue.append(queue.popleft())

print(f"<{', '.join([str(x) for x in answer])}>")
