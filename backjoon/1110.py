# https://www.acmicpc.net/problem/1110

N = input()
if len(N) == 1:
    N = "0" + N
target = N

cycle = 0
while True:
    cycle += 1
    temp_sum = str(int(N[0]) + int(N[1]))
    new_number = N[1] + temp_sum[-1]

    if target == new_number:
        print(cycle)
        exit(0)
    N = new_number
