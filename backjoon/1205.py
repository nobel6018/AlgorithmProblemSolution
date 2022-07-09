# https://www.acmicpc.net/problem/1205

n, score, p = map(int, input().split(" "))

# 예외 케이스 처리
if n == 0:
    print(1)
    exit(0)

scores = list(map(int, input().split(" ")))

if n == p:
    if scores[p - 1] >= score:
        print(-1)
        exit(0)

grade = len(scores) + 1
for i in range(len(scores)):
    if scores[i] <= score:
        grade = i + 1
        break
print(grade)
