# https://www.acmicpc.net/problem/1057

def next_number(num):
    return (num // 2) + (num % 2)


n, player1, player2 = map(int, input().split())

answer = 0
while True:
    answer += 1

    player1 = next_number(player1)
    player2 = next_number(player2)
    if player1 == player2:
        break

print(answer)
