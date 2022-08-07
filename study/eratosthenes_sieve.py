def eratosthenes_sieve(n):
    # 에라토스테네스의 체 초기화
    # n개 모두를 소수로 간주
    sieve = [True] * (n + 1)
    # 0과 1은 소수가 아님
    sieve[0] = False
    sieve[1] = False

    # 루트근까지만 탐색하면 됨
    until = int(n ** 0.5)
    for i in range(until + 1):
        if sieve[i] is True:
            for j in range(i + i, n, i):
                sieve[j] = False

    prime_numbers = [i for i in range(n + 1) if sieve[i] is True]
    return prime_numbers


if __name__ == '__main__':
    print(eratosthenes_sieve(97))
