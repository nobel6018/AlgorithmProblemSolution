# https://www.acmicpc.net/problem/1057

n, player1, player2 = map(int, input().split(" "))

answer = 0
while True:
    answer += 1

    player1 = (player1 // 2) + (player1 % 2)
    player2 = (player2 // 2) + (player2 % 2)
    if player1 == player2:
        break

    n = (n // 2) + (n % 2)

print(answer)
