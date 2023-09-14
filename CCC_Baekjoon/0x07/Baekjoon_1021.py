# https://www.acmicpc.net/problem/1021

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
pickNum = list(map(int, sys.stdin.readline().rstrip().split()))

circleQ = deque(i for i in range(1, N+1))
count = 0

for item in pickNum:
    while True:
        if circleQ[0] == item:
            circleQ.popleft()
            break
        else:
            if circleQ.index(item) < len(circleQ) / 2:
                while circleQ[0] != item:
                    count += 1
                    circleQ.append(circleQ.popleft())
            else:
                while circleQ[0] != item:
                    count += 1
                    circleQ.appendleft(circleQ.pop())

print(count)