def linear_search(a, target):
    comparisons = 0
    for i in range(len(a)):
        comparisons += 1
        if a[i] == target:
            return i, comparisons
    return -1, comparisons


arr = [58, 26, 68, 76, 17, 46, 44, 30, 88, 90]
index, comparisons = linear_search(arr, 68)

print(index)
print(comparisons)