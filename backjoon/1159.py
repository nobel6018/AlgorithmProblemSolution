# https://www.acmicpc.net/problem/1159

N = int(input())

players = dict()
for _ in range(N):
    last_name = input()
    if players.get(last_name[0]) is None:
        players[last_name[0]] = 1
    else:
        players[last_name[0]] += 1

answer = ""
for i in players.keys():
    if players[i] >= 5:
        answer += i

if answer == "":
    print("PREDAJA")
else:
    print(''.join(sorted(answer)))