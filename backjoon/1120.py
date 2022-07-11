# https://www.acmicpc.net/problem/1120

import sys

input = sys.stdin.readline


def get_different_count(short_str: str, long_str: str, offset: int) -> int:
    count = 0
    for i in range(len(short_str)):
        if short_str[i] != long_str[i + offset]:
            count += 1
    return count


def get_min_different_count(short_str: str, long_str: str) -> int:
    diff_count = int(1e9)

    for offset in range(len(long_str) - len(short_str) + 1):
        diff_count = min(diff_count, get_different_count(short_str, long_str, offset))

    return diff_count


a, b = input().split()
print(get_min_different_count(a, b))
