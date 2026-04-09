import heapq

n = int(input())
nums = list(map(int, input().split()))
k = int(input())

freq = {}
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

heap = []
for num, count in freq.items():
    heapq.heappush(heap, (count, num))
    if len(heap) > k:
        heapq.heappop(heap)

result = []
while heap:
    result.append(heapq.heappop(heap)[1])

print(*result[::-1])