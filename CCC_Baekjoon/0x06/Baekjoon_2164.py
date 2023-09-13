# https://www.acmicpc.net/problem/2164
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
numbers = [i for i in range(1, N+1)]
numbers = deque(numbers)

while len(numbers) != 1:
    numbers.popleft()
    numbers.append(numbers.popleft())

print(numbers[-1])