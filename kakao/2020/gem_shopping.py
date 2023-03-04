def solution(gems):
    n = len(gems)
    target = len(set(gems))
    dic = {gems[0]: 1, }

    answer = [0, n]

    s = 0
    e = 0
    while s < n and e < n:
        if len(dic) == target:  # 종류가 같으면
            if (e - s) < (answer[1] - answer[0]):
                answer = [s, e]

            if dic[gems[s]] == 1:
                del dic[gems[s]]
            else:
                dic[gems[s]] -= 1

            s += 1
        else:  # 종류가 부족하면
            e += 1
            if e == n:
                break
            dic[gems[e]] = dic.get(gems[e], 0) + 1

    answer[0] += 1
    answer[1] += 1
    return answer
