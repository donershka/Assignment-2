import heapq
from collections import Counter

def top_k(nums, k):
    count = Counter(nums)
    heap = []

    for num in count:
        heapq.heappush(heap, (count[num], num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for freq, num in heap]


n = int(input())
nums = list(map(int, input().split()))
k = int(input())

print(*top_k(nums, k))