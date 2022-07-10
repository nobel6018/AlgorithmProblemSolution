import sys

input = sys.stdin.readline

n = int(input())
items = sorted(list(map(int, input().split())))


def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        middle = (start + end) // 2

        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            start = middle + 1
        else:  # arr[middle] > target
            end = middle - 1

    return -1


m = int(input())
requests = map(int, input().split())
for request in requests:
    if binary_search(items, request) != -1:
        print("yes", end=" ")
    else:
        print("no", end=" ")

# [input]
# 5
# 8 3 7 9 2
# 3
# 5 7 9
