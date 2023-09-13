# https://www.acmicpc.net/problem/5397

from collections import deque

T = int(input())

for _ in range(T):
    chrLeft = deque()
    command = input()
    chrRight = deque()

    for item in command:
        if item == '<':
            if len(chrLeft) > 0:
                chrRight.appendleft(chrLeft.pop())

        elif item == '>':
            if len(chrRight) > 0:
                chrLeft.append(chrRight.popleft())

        elif item == '-':
            if len(chrLeft) > 0:
                chrLeft.pop()

        else:
            chrLeft.append(item)

    answer = chrLeft + chrRight

    print(''.join(answer))