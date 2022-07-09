# https://www.acmicpc.net/problem/1063

king, stone, n = input().split()
n = int(n)

king_x: int = ord(king[0]) - ord("A") + 1
king_y: int = int(king[1])
stone_x: int = ord(stone[0]) - ord("A") + 1
stone_y: int = int(stone[1])

for _ in range(n):
    move = input()
    if move == "R":
        if king_x + 1 <= 8:
            if stone_x == king_x + 1 and stone_y == king_y:
                if stone_x + 1 <= 8:
                    king_x += 1
                    stone_x += 1
            else:
                king_x += 1
    elif move == "L":
        if king_x - 1 >= 1:
            if stone_x == king_x - 1 and stone_y == king_y:
                if stone_x - 1 >= 1:
                    king_x -= 1
                    stone_x -= 1
            else:
                king_x -= 1
    elif move == "T":
        if king_y + 1 <= 8:
            if stone_y == king_y + 1 and stone_x == king_x:
                if stone_y + 1 <= 8:
                    king_y += 1
                    stone_y += 1
            else:
                king_y += 1
    elif move == "B":
        if king_y - 1 >= 1:
            if stone_y == king_y - 1 and stone_x == king_x:
                if stone_y - 1 >= 1:
                    king_y -= 1
                    stone_y -= 1
            else:
                king_y -= 1
    elif move == "RT":
        if king_x + 1 <= 8 and king_y + 1 <= 8:
            if stone_x == king_x + 1 and stone_y == king_y + 1:
                if stone_x + 1 <= 8 and stone_y + 1 <= 8:
                    stone_x += 1
                    stone_y += 1
                    king_x += 1
                    king_y += 1
            else:
                king_x += 1
                king_y += 1
    elif move == "LT":
        if king_x - 1 >= 1 and king_y + 1 <= 8:
            if stone_x == king_x - 1 and stone_y == king_y + 1:
                if stone_x - 1 >= 1 and stone_y + 1 <= 8:
                    stone_x -= 1
                    stone_y += 1
                    king_x -= 1
                    king_y += 1
            else:
                king_x -= 1
                king_y += 1
    elif move == "RB":
        if king_x + 1 <= 8 and king_y - 1 >= 1:
            if stone_x == king_x + 1 and stone_y == king_y - 1:
                if stone_x + 1 <= 8 and stone_y - 1 >= 1:
                    stone_x += 1
                    stone_y -= 1
                    king_x += 1
                    king_y -= 1
            else:
                king_x += 1
                king_y -= 1
    elif move == "LB":
        if king_x - 1 >= 1 and king_y - 1 >= 1:
            if stone_x == king_x - 1 and stone_y == king_y - 1:
                if stone_x - 1 >= 1 and stone_y - 1 >= 1:
                    stone_x -= 1
                    stone_y -= 1
                    king_x -= 1
                    king_y -= 1
            else:
                king_x -= 1
                king_y -= 1

print(chr(king_x + ord("A") - 1) + str(king_y))
print(chr(stone_x + ord("A") - 1) + str(stone_y))
