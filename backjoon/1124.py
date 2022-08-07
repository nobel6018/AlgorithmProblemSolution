# https://www.acmicpc.net/problem/1124
from typing import List

a, b = map(int, input().split())


def eratosthenes_sieve(n: int) -> List[int]:
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False

    until = int(n ** 0.5)
    for i in range(until + 1):
        if sieve[i] is True:
            for j in range(i + i, n + 1, i):
                sieve[j] = False

    return [i for i in range(n + 1) if sieve[i] is True]


def is_prime(number: int) -> bool:
    if number == 1:
        return False

    until = int(number ** 0.5)
    for i in range(2, until + 1):
        if number % i == 0:
            return False
    return True


def is_under_prime(prime_numbers: List[int], number: int) -> bool:
    count = 0
    for prime in prime_numbers:
        if number == 1:
            break

        while number % prime == 0:
            count += 1
            number //= prime

    return is_prime(count)


prime_numbers = eratosthenes_sieve(b)

answer = 0
for i in range(a, b + 1):
    if is_under_prime(prime_numbers, i):
        answer += 1

print(answer)
