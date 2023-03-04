def solution(gems):
    target_count = len(set(gems))

    i = 0
    j = 0
    while j < len(gems):
        if len(set(gems[i:j])) == target_count:
            break
        else:
            j += 1

    temp_i = 0
    while temp_i < j:
        if len(set(gems[temp_i:j])) == target_count:
            i = temp_i
        temp_i += 1

    return [i + 1, j]


if __name__ == '__main__':
    assert solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]) == [3, 7]
    assert solution(["AA", "AB", "AC", "AA", "AC"]) == [1, 3]
    assert solution(["XYZ", "XYZ", "XYZ"]) == [1, 1]
    assert solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]) == [1, 5]
