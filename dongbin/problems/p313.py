# 전부 0으로 만드는 경우,
# 전부 1로 만드는 경우,
# 그 중에서 더 작은 경우의 수가 답이다

# 그래서, 0의 그룹과 1의 그룹 갯수를 찾았다

string = input()

group0_count = 0
group1_count = 0

for i in range(1, len(string)):
    if string[i - 1] == '0' and string[i] == '1':
        group0_count += 1
    if string[i - 1] == '1' and string[i] == '0':
        group1_count += 1

if string[-1] == '0':
    group0_count += 1
else:
    group1_count += 1

print(min(group0_count, group1_count))
