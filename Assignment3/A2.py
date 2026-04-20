def heapify(a, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and a[left] > a[largest]:
        largest = left

    if right < n and a[right] > a[largest]:
        largest = right

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)


def build_max_heap(a):
    a = a.copy()
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)
    return a


def first_extract_max(a):
    a = a.copy()
    n = len(a)
    a[0], a[n - 1] = a[n - 1], a[0]
    heapify(a, n - 1, 0)
    return a


arr = [58, 26, 68, 76, 17, 46, 44, 30, 88, 90]
heap_array = build_max_heap(arr)
after_extract = first_extract_max(heap_array)

print(heap_array)
print(after_extract)