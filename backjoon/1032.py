# https://www.acmicpc.net/problem/1032

N = int(input())

answer = list(input())
for _ in range(N - 1):
    compare = list(input())
    for i in range(len(answer)):
        if answer[i] != "?" and answer[i] != compare[i]:
            answer[i] = "?"

print("".join(answer))
