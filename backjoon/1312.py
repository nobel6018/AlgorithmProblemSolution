# https://www.acmicpc.net/problem/1312

(a, b, n) = map(int, input().split(" "))

modulus = a % b

for i in range(n):
    if i + 1 == n:
        print(modulus * 10 // b)
    modulus = (modulus * 10) % b
