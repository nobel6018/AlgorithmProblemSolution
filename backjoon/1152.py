# https://www.acmicpc.net/problem/1152

string = input()
striped_string = string.strip()
if striped_string == "":
    print(0)
else:
    print(len(striped_string.split(" ")))
