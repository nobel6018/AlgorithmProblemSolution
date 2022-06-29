# https://www.acmicpc.net/problem/1251

def solution1():
    string = input()

    answer = "z" * len(string)

    def is_left_string_first(left, right):
        result = False
        for i in range(len(left)):
            if ord(left[i]) < ord(right[i]):
                result = True
                break
            elif ord(left[i]) > ord(right[i]):
                result = False
                break
        return result

    for i in range(1, len(string) - 2):
        for j in range(i + 1, len(string)):
            s1 = ''.join(reversed(string[:i]))
            s2 = ''.join(reversed(string[i:j]))
            s3 = ''.join(reversed(string[j:]))
            new_string = s1 + s2 + s3
            if is_left_string_first(new_string, answer):
                answer = new_string

    print(answer)


def solution2():
    string = input()

    answer = "z" * len(string)

    for i in range(1, len(string) - 2):
        for j in range(i + 1, len(string)):
            s1 = string[:i][::-1]
            s2 = string[i:j][::-1]
            s3 = string[j:][::-1]
            new_string = s1 + s2 + s3
            answer = min(answer, new_string)

    print(answer)


if __name__ == '__main__':
    # solution1()
    solution2()
