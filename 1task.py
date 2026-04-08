n = int(input())
arr = list(map(int, input().split()))

candidate = None
count = 0

for num in arr:
    if count == 0:
        candidate = num
    if num == candidate:
        count += 1
    else:
        count -= 1

print(candidate)