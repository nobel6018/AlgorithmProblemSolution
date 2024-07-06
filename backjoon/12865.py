# 이론은 https://www.youtube.com/watch?v=rhda6lR5kyQ (코드없는 프로그래밍)
# 코드는 https://inni-iii.tistory.com/74

n, k = map(int, input().split())

# (w, v) 목록 초기화
# [0,0]을 넣는 이유: items[1]부터 탐색하기 때문에 (16번 라인)
items = [[0, 0]]
for _ in range(n):
    w, v = map(int, input().split())
    items.append((w, v))

# 전체 0으로 초기화
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = items[i][0]
        value = items[i][1]

        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[n][k])
