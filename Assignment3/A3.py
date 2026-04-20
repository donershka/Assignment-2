def bubble_sort_3_passes(a):
    a = a.copy()
    n = len(a)

    for i in range(3):
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
        print(a)


arr = [58, 26, 68, 76, 17, 46, 44, 30, 88, 90]
bubble_sort_3_passes(arr)