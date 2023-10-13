# https://www.acmicpc.net/problem/1926
import sys
from collections import deque


def bfs(picture, y, x):
    q = deque()
    q.append((y, x))
    picture[y][x] = 0
    # 이미 현재 좌표가 1인 상태에서 넘어 온것으로 넓이는 1로 시작한다.
    count = 1

    while q:
        currentY, currentX = q.popleft()
        for goY, goX in go:
            movedY, movedX = currentY + goY, currentX + goX

            if Y <= movedY or 0 > movedY or X <= movedX or 0 > movedX:
                continue

            if picture[movedY][movedX] != 1:
                continue

            picture[movedY][movedX] = 0
            q.append((movedY, movedX))
            count += 1
    return count


Y, X = map(int, sys.stdin.readline().rstrip().split())
picture = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(Y)]
go = [(-1, 0), (0, 1), (0, -1), (1, 0)]
answers = []

for y in range(Y):
    for x in range(X):
        if picture[y][x] == 1:
            answers.append(bfs(picture, y, x))


if len(answers) == 0:
    print(0)
    print(0)
else:
    print(len(answers))
    print(max(answers))
