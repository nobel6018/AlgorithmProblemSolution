# https://www.acmicpc.net/problem/1193

X = int(input())

# 1. 라인을 찾자 (오름, 내림도 같이 판단)
# 2. 그 라인에서 몇 번째

line = 0
for n in range(1, 100000000):
    if X <= n * (n + 1) / 2:
        line = n
        break

# 짝수: 분자 오름, 홀수: 분자 내림
nth = X - int((line - 1) * line / 2)
if line % 2 == 0:
    print(str(nth) + "/" + str(line-nth+1))
else:
    print(str(line-nth+1) + "/" + str(nth))
