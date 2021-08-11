# 동빈나 알고리즘 p.367
# from. Zoho 인터뷰
# binary search

# 처음 위치를 찾는 이진 탐색 메서드
def first(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid

    # 중간점의 값보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
    elif array[mid] >= target:
        first(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        first(array, target, mid + 1, end)


def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    # 해당 값을 가지는 원소 중에서 가장 오른쪽에 잇는 경우에만 인덱스 반환
    if (mid == len(array) - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    elif array[mid] <= target:
        last(array, target, mid + 1, end)
    else:
        last(array, target, start, mid - 1)


def count_by_value(array, x):
    n = len(array)

    a = first(array, x, 0, n - 1)

    if a is None:
        return 0

    b = last(array, x, 0, n - 1)

    return b - a + 1


n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_value(array, x)

if count == 0:
    print(-1)
else:
    print(count)

'''
7 2
1 1 2 2 2 2 3
'''
