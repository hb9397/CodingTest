# https://www.acmicpc.net/problem/10773

import sys

T = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(T):

    num = int(sys.stdin.readline().rstrip())

    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))