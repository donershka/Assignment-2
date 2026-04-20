nums = list(map(int, input().split()))
candidate = 0
for num in nums:
    if num > candidate:
        candidate = num
print(candidate)