# https://www.acmicpc.net/problem/1065

n = int(input())

answer = 0
for i in range(1, n + 1):
    nums = list(map(int, list(str(i))))
    if len(nums) == 1 or len(nums) == 2:
        answer += 1
    elif len(nums) == 3:
        if nums[2] - nums[1] == nums[1] - nums[0]:
            answer += 1

print(answer)
