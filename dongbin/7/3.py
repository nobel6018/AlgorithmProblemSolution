import sys

input = sys.stdin.readline

n, m = map(int, input().split())
tteuks = list(map(int, input().split()))

start = min(tteuks)
end = max(tteuks)

answer = 0
while start <= end:
    middle = (start + end) // 2

    total = 0
    for tteuk in tteuks:
        total += 0 if tteuk <= middle else tteuk - middle

    if total == m:
        answer = middle
        break
    elif total > m:
        answer = middle
        start = middle + 1
    else:
        end = middle - 1

print(answer)

# [input]
# 4 6
# 19 15 10 17

# [expectation]
# 15
