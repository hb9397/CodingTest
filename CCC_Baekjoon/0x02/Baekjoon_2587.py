# https://www.acmicpc.net/problem/2587

import heapq
from collections import deque
heap = []
arr = deque()
for i in range(5):
    heapq.heappush(heap, int(input()))

for i in range(5):
    arr.append(heapq.heappop(heap))

print(sum(arr) // 5)
print(arr[2])