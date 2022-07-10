import sys

input = sys.stdin.readline

n, m = map(int, input().split())
tteuks = list(map(int, input().split()))

start = min(tteuks)
end = max(tteuks)

while start <= end:
    middle = (start + end) // 2

    total = 0
    for tteuk in tteuks:
        total += 0 if tteuk <= middle else tteuk - middle

    if total == m:
        print(middle)
        exit(0)
    elif total < m:
        end = middle - 1
    else:
        start = middle + 1

# 4 6
# 19 15 10 17
