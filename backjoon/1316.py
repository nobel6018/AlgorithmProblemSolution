# https://www.acmicpc.net/problem/1316

n = int(input())

answer = 0
for _ in range(n):
    string = input()
    current = string[0]
    appeared = [current, ]

    is_group_word = True
    for i in range(1, len(string)):
        char = string[i]
        if char != current:
            if char not in appeared:
                current = char
                appeared.append(char)
            else:
                is_group_word = False
                break
    if is_group_word:
        answer += 1

print(answer)
