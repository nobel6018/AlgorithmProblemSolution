def is_prime(number):
    if number == 1:
        return False

    until = int(number ** 0.5)
    for i in range(2, until + 1):
        if number % i == 0:
            return False
    return True


if __name__ == '__main__':
    print(is_prime(1) is False)
    print(is_prime(2) is True)
    print(is_prime(3) is True)
    print(is_prime(4) is False)
    print(is_prime(5) is True)
    print(is_prime(17) is True)
    print(is_prime(20) is False)
