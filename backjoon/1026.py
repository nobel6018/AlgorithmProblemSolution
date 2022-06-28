# https://www.acmicpc.net/problem/1026

N = int(input())
A = sorted(list(map(int, input().split(" "))))
B = sorted(list(map(int, input().split(" "))), reverse=True)

total = 0
for i in range(N):
    total += A[i] * B[i]

print(total)
