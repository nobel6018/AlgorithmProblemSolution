string = input()

num = 0
char_list = []

for char in string:
    if char.isnumeric():
        num += int(char)
    else:
        char_list.append(char)

char_list.sort()
char_list.append(str(num))
result = "".join(char_list)

# test
print(result == "ABCK12")

# example
# K3C7B0A2
# ABCK12
