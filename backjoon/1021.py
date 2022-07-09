# https://www.acmicpc.net/problem/1021

from collections import deque

n, m = map(int, input().split(" "))
removes = list(map(int, input().split(" ")))

queue = deque()
for i in range(n):
    queue.append(i + 1)

count = 0
for remove in removes:
    local_count = 0
    while True:
        item = queue.popleft()
        if item == remove:
            count += min(local_count, len(queue) + 1 - local_count)
            break
        else:
            local_count += 1
            queue.append(item)

print(count)