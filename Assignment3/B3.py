def hash_with_linear_probing(a, size=7):
    table = [None] * size

    for key in a:
        index = key % size
        start = index

        while table[index] is not None:
            index = (index + 1) % size
            if index == start:
                break
        else:
            table[index] = key

    return table


arr = [58, 26, 68, 76, 17, 46, 44, 30, 88, 90]
print(hash_with_linear_probing(arr, 7))