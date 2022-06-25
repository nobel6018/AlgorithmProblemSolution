#  https://www.acmicpc.net/problem/1173

(N, m, M, T, R) = map(int, input().split(" "))

if M < m + T:
    print(-1)
    exit(0)

time = 0
current = m

while True:
    if N == 0:
        print(time)
        exit(0)

    time += 1
    if M >= current + T:
        current += T
        N -= 1
    else:
        current = m if current - R < m else current - R
