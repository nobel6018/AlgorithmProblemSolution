# https://www.acmicpc.net/problem/1075

N = int(input())
F = int(input())

N = (N // 100) * 100
modulus = N % F
answer = "00"
if modulus != 0:
    answer = str(F - modulus)
print(answer)
