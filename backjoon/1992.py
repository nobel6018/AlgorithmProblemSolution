# 접근 방법
# 1. 모두 같은 숫자가 아니라면 4등분 한다
# 2. 4등분된 영상을 다시 검사한다
# 3. 2번 과정을 모두 같은 숫자 일 때까지 반복한다

n = int(input())
image = [list(map(int, input())) for _ in range(n)]


def dnc(n, r, c):
    start_color = image[r][c]
    for i in range(r, r + n):
        for j in range(c, c + n):
            if image[i][j] != start_color:
                start_color = -1
                break

    if start_color == -1:
        print("(", end="")
        new_n = n // 2
        dnc(new_n, r, c)
        dnc(new_n, r, c + new_n)
        dnc(new_n, r + new_n, c)
        dnc(new_n, r + new_n, c + new_n)
        print(")", end="")
    elif start_color == 1:
        print(1, end="")
    else:
        print(0, end="")


dnc(n, 0, 0)
