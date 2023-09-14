# https://www.acmicpc.net/problem/5430
import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())

    if n != 0:
        numbers = deque(list(map(int, sys.stdin.readline().lstrip('[').rstrip().rstrip(']').split(','))))
    else:
        numbers = []

    print(p, n, len(numbers))

    for command in p:
        if command == 'R':
            numbers = numbers.reverse()

        elif command == 'D':
            if len(numbers) == 0:
                print("error")
                # break

            else:
                numbers.popleft()

        print(numbers)
