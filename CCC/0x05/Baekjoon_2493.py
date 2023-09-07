# https://www.acmicpc.net/problem/2493

import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
tower = list(map(int, sys.stdin.readline().rstrip().split()))
stack = []
answer = [0 for i in range(N)]

for i in range(N):
    while len(stack) != 0:
        if stack[-1][1] > tower[i]:
            answer[i] = stack[-1][0] + 1
            break

        else:
            stack.pop()
    stack.append([i, tower[i]])

print(*answer)