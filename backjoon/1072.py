# https://www.acmicpc.net/problem/1072

x, y = map(int, input().split())
z = int(100 * y / x)

if z == 100:
    print(-1)
    exit(0)

play_count = 0
nx = x
ny = y
nz = z

while True:
    play_count += 1
    nx += 1
    ny += 1
    nz = int(100 * ny / nx)
    if nz != z:
        break

print(play_count)
