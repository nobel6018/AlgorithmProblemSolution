import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
j = 0
answer = list()

while i < n and j < m:
    if a[i] <= b[j]:
        answer.append(a[i])
        i += 1
    else:
        answer.append(b[j])
        j += 1

if i == n:
    # append all b elements
    while j < m:
        answer.append(b[j])
        j += 1

if j == m:
    while i < n:
        answer.append(a[i])
        i += 1

print(' '.join(str(e) for e in answer))
