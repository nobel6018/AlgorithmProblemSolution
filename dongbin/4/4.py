# p.110 상하좌우

n = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
move_types = ["L", "R", "U", "D"]

moves = input().split()
position = [1, 1]  # (행, 열), (y, x)
for move in moves:
    idx = move_types.index(move)
    next_y = position[0] + dy[idx]
    next_x = position[1] + dx[idx]
    if 1 <= next_y <= 5 and 1 <= next_x <= 5:
        position[0] = next_y
        position[1] = next_x
print(position[0], position[1])

##
# [input]
# 5
# R R R U D D
#
# [expectation]
# 3 4
