# https://www.acmicpc.net/problem/1676

def solution1():
    n = int(input())

    count_10 = 0
    count_2 = 0
    count_5 = 0

    for num in reversed(range(1, n + 1)):
        while num % 10 == 0:
            count_10 += 1
            num = num // 10
        while num % 5 == 0:
            count_5 += 1
            num = num // 5
        while num % 2 == 0:
            count_2 += 1
            num = num // 2

    zeros = count_10
    zeros += min(count_2, count_5)

    print(zeros)


# 더 효율적인 방법
# 숫자 '5'만 카운트하는 방법
# 숫자 5 뒤에는 2는 항상 더 충분히 있기 때문
# ex. 5! = 5*4*3*2*1
# 5뒤에 숫자 4와 2가 있어서 5만 있다면 2는 세알리지 않아도 된다
# 참고로 50!을 했을 때, 5의 개수는 12, 2의 개수는 47개다

def solution2():
    n = int(input())

    count = 0

    for num in reversed(range(1, n + 1)):
        while num % 5 == 0:
            count += 1
            num = num // 5

    print(count)


# 생각해보면 5의 배수를 찾는 방법은 규칙성이 있습니다
# 10! = 10*9*8*7*6*5*4*3*2*1
# 5, 10으로 5씩 증가하므로 10!에서 5의 배수 개수는 10을 5로 나눈 몫(10//5)과 같습니다
# 그런데 25, 125와 같이 5가 여러번 반복되는 수가 있습니다
# 25! = 25*24*23*22*21*20*19*18*17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1
# 25, 20, 15, 10, 5는 5의 배수입니다 5의 단순 배수 개수는 25//5 = 5개입니다
# 그런데 5의 두번 배수는 25, 20, 15, 10, 5에서 5의 배수 중에서 5번째에 등장합니다
# 그래서 25를 5로 나눈 몫인 5(25//5 = 5)에서 다시 5로 나누면 됩니다 (5//5 = 1)
def solution3():
    n = int(input())

    count = 0
    while n > 1:
        count += n // 5
        n = n // 5

    print(count)


if __name__ == '__main__':
    solution1()
    solution2()
    solution3()
