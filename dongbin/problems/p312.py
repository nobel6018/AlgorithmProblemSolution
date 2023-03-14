numbers = input()

answer = int(numbers[0])
for number in numbers[1:]:
    answer = max(answer + int(number), answer * int(number))

print(answer)
