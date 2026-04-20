def binary_search_trace(a, target):
    a = sorted(a)
    low = 0
    high = len(a) - 1

    while low <= high:
        mid = (low + high) // 2
        print(low, high, mid, a[mid])

        if a[mid] == target:
            return mid
        elif a[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [58, 26, 68, 76, 17, 46, 44, 30, 88, 90]
print(sorted(arr))
print(binary_search_trace(arr, 46))