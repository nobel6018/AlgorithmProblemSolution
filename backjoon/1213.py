# https://www.acmicpc.net/problem/1213

string = input()

characters = dict()
for char in string:
    if characters.get(char, 0) == 0:
        characters[char] = 1
    else:
        characters[char] += 1

keys = sorted(characters.keys())
odd_char = ""
for key in keys:
    if characters.get(key) % 2 == 1:
        if odd_char == "":
            odd_char = key
        else:
            print("I'm Sorry Hansoo")
            exit(0)

answer = ""
temp = ""
for key in keys:
    count = characters[key] // 2
    temp += key * count
    characters[key] = int(characters[key] / 2)
answer += temp
if odd_char != "":
    answer += odd_char
answer += temp[::-1]

print(answer)
