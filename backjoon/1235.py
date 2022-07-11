# https://www.acmicpc.net/problem/1235

import sys

input = sys.stdin.readline

n = int(input())

students = []
for _ in range(n):
    students.append(input().strip())

answer = 0
number_length = len(students[0])
for i in reversed(range(number_length)):
    is_there_duplicate = False
    numbers = []
    for student in students:
        if student[i:] in numbers:
            is_there_duplicate = True
            break
        else:
            numbers.append(student[i:])

    if is_there_duplicate is False:
        answer = number_length - i
        break

print(answer)
