# https://www.acmicpc.net/problem/1075

N = int(input())
F = int(input())

N = (N // 100) * 100
modulus = N % F
if modulus != 0:
    N += (F - modulus)

print(str(N)[-2:])
