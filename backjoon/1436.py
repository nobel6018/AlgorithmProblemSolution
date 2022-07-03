# https://www.acmicpc.net/problem/1436

n = int(input())

answer = 666
counter = 1
while counter != n:
    answer += 1
    if "666" in str(answer):
        counter += 1

print(answer)
