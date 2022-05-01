# Binary Search - iterative

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None


# Test
l = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
answer = binary_search(l, 15, 0, len(l) - 1)
print(answer)
