# https://www.acmicpc.net/problem/1343

board = input()

answer = ""
counter = 0
for i in range(len(board)):
    if board[i] == "X":
        counter += 1
        if i + 1 == len(board) or board[i + 1] == ".":
            a_num = counter // 4
            answer += "AAAA" * a_num
            counter -= 4 * a_num

            b_num = counter // 2
            answer += "BB" * b_num
            counter -= 2 * b_num

            if counter != 0:
                print(-1)
                exit(0)
    elif board[i] == ".":
        answer += "."

print(answer)
