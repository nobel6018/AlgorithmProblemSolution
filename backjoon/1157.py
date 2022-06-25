# https://www.acmicpc.net/problem/1157

string = list(input().lower())

maps = [0] * 26

for char in string:
    index = ord(char) - ord('a')
    maps[index] += 1

max_occurrence = max(maps)
if maps.count(max_occurrence) >= 2:
    print("?")
else:
    index = maps.index(max_occurrence)
    print(chr(index + ord("A")))
