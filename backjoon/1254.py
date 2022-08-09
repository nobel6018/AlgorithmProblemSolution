# https://www.acmicpc.net/problem/1254

string = input()
reversed_string = string[::-1]

length = len(string)
for i in range(length):
    if string[i:] == reversed_string[0:length - i]:
        print(length + i)
        break
