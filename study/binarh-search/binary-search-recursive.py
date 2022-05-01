# Binary Search - recursive

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)


# Test
l = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
answer = binary_search(l, 15, 0, len(l) - 1)
print(answer)
