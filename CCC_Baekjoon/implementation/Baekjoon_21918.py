# https://www.acmicpc.net/problem/21918
import sys
N, M = map(int, sys.stdin.readline().rstrip().split(" "))
tasks = [bool(int(item)) for item in sys.stdin.readline().rstrip().split(" ")]

for _ in range(M):
    command = [int(item) for item in sys.stdin.readline().rstrip().split(" ")]

    if command[0] == 1:
        tasks[command[1]-1] = bool(command[2])
    elif command[0] == 2:
        for i in range(command[1]-1, command[2]):
            tasks[i] = not tasks[i]
    elif command[0] == 3:
        for i in range(command[1] - 1, command[2]):
            tasks[i] = False
    elif command[0] == 4:
        for i in range(command[1] - 1, command[2]):
            tasks[i] = True

tasks = [int(item) for item in tasks]
print(*tasks, end=" ")