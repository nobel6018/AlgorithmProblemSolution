# https://www.acmicpc.net/problem/1100

board = []

for _ in range(8):
    board.append(list(input()))

answer = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0 and board[i][j] == "F":
            answer += 1

print(answer)
