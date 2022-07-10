import sys

input = sys.stdin.readline

n, m = map(int, input().split())
tteuks = list(map(int, input().split()))

candidate_lengths = list(range(min(tteuks), max(tteuks) + 1))
start = 0
end = len(candidate_lengths) - 1

while start <= end:
    middle = (start + end) // 2
    current_length = candidate_lengths[middle]

    total = 0
    for tteuk in tteuks:
        total += 0 if tteuk <= current_length else tteuk - current_length

    if total == m:
        print(candidate_lengths[middle])
        exit(0)
    elif total < m:
        end = middle - 1
    else:
        start = middle + 1

# 4 6
# 19 15 10 17
