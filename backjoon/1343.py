# https://www.acmicpc.net/problem/1343

def solution1():
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


# 다른 풀이
# ref: https://s0ng.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EA%B7%B8%EB%A6%AC%EB%94%94-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%8F%B4%EB%A6%AC%EC%98%A4%EB%AF%B8%EB%85%B8-1343%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python

def solution2():
    board = input()

    board = board.replace("XXXX", "AAAA")
    board = board.replace("XX", "BB")

    if "X" in board:
        print(-1)
    else:
        print(board)


if __name__ == '__main__':
    # solution1()
    solution2()
