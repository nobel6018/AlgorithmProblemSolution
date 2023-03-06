plate_format = input()

answer = 1

if plate_format[0] == 'c':
    answer *= 26
else:
    answer *= 10

for i in range(1, len(plate_format)):
    if plate_format[i] == plate_format[i - 1]:
        if plate_format[i] == 'c':
            answer *= 25
        else:
            answer *= 9
    else:
        if plate_format[i] == 'c':
            answer *= 26
        else:
            answer *= 10

print(answer)
