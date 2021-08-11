# https://www.acmicpc.net/problem/1715
# Heap

import heapq

N = int(input())
heap = []

for _ in range(N):
    heapq.heappush(heap, int(input()))

answer = 0
while len(heap) > 1:
    item1 = heapq.heappop(heap)
    item2 = heapq.heappop(heap)

    local_sum = item1 + item2
    answer += local_sum
    heapq.heappush(heap, local_sum)

print(answer)
