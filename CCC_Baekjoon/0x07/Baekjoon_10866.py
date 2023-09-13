# https://www.acmicpc.net/problem/10866
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
command = []
dq = deque()
for _ in range(N):
    command = list(map(str, sys.stdin.readline().rstrip().split()))

    if command[0] == 'push_back':
        dq.append(command[1])

    elif command[0] == 'push_front':
        dq.appendleft(command[1])

    elif command[0] == 'pop_front':
        if len(dq) == 0:
            print('-1')
        else:
            print(dq.popleft())

    elif command[0] == 'pop_back':
        if len(dq) == 0:
            print('-1')
        else:
            print(dq.pop())

    elif command[0] == 'size':
        print(len(dq))

    elif command[0] == 'empty':
        if len(dq) == 0:
            print('1')
        else:
            print('0')

    elif command[0] == 'front':
        if len(dq) == 0:
            print('-1')
        else:
            print(dq[0])

    elif command[0] == 'back':
        if len(dq) == 0:
            print('-1')
        else:
            print(dq[-1])