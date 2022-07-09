# https://www.youtube.com/watch?v=hw-SvAR3Zqg&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=32


INF = int(1e9)  # 무한을 10억으로 설정

# 노드의 개수 및 간선의 개수 입력 받기
n = int(input())
m = int(input())

# 2차원 리스트(그래프)를 만들고 무한으로 초기화
graph = [[INF] * (1 + n) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n + 1):
    graph[i][i] = 0

# 각 간선에 대한 정보를 받아 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):  # k를 거쳐 가는 경우
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INF)으로 출력
        if graph[a][b] == INF:
            print("INF", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()

# example.
# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2
