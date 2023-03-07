import sys

input = sys.stdin.readline

n, m = map(int, input().split())

relations = [[False for _ in range(n + 1)] for _ in range(n + 1)]
friends = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    relations[a][b] = True
    relations[b][a] = True
    friends[a] += 1
    friends[b] += 1

answer = 1e10
for i in range(1, n + 1):
    relation = relations[i]
    for j in range(i + 1, n + 1):
        if relations[i][j] is True:
            for k in range(j + 1, n + 1):
                if relations[j][k] is True and relations[i][k] is True:
                    answer = min(answer, friends[i] + friends[j] + friends[k] - 6)

if answer == 1e10:
    print(-1)
else:
    print(answer)
