# https://www.acmicpc.net/problem/1004

T = int(input())
for _ in range(T):
    answer = 0

    (x1, y1, x2, y2) = map(int, input().split(" "))
    n = int(input())
    for _ in range(n):
        (cx, cy, r) = map(int, input().split(" "))
        is_start_point_in_circle = ((cx - x1) ** 2 + (cy - y1) ** 2) <= r ** 2
        is_arrival_point_in_circle = ((cx - x2) ** 2 + (cy - y2) ** 2) <= r ** 2

        if is_start_point_in_circle is True and is_arrival_point_in_circle is False:
            answer += 1
        elif is_start_point_in_circle is False and is_arrival_point_in_circle is True:
            answer += 1

    print(answer)
