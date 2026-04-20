def quick_partition_first_pivot(a):
    a = a.copy()
    pivot = a[0]
    left = 1
    right = len(a) - 1

    while True:
        while left <= right and a[left] < pivot:
            left += 1
        while left <= right and a[right] > pivot:
            right -= 1

        if left < right:
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1
        else:
            break

    a[0], a[right] = a[right], a[0]
    return a, right


arr = [58, 26, 68, 76, 17, 46, 44, 30, 88, 90]
result, pivot_index = quick_partition_first_pivot(arr)
print(result, pivot_index)