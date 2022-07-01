# https://www.acmicpc.net/problem/1978
# ref: https://comdoc.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EC%86%8C%EC%88%98prime-%EC%B0%BE%EA%B8%B0

def is_prime(num: int) -> bool:
    if num == 1:
        return False

    until = int(num ** 0.5)
    for i in range(2, until + 1):
        if num % i == 0:
            return False
    return True


n = int(input())
nums = list(map(int, input().split(" ")))
answer = 0
for num in nums:
    if is_prime(num):
        answer += 1
print(answer)
