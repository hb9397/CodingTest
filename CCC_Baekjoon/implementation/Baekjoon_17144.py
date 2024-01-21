# https://www.acmicpc.net/problem/17144
import sys
# 1. 미세먼지 확산
def spread():
    # 이동 가능 인덱스 x, y
    gx = [1, -1, 0, 0]
    gy = [0, 0, 1, -1]
    # 새로운 보드 판
    new_board = [[0] * c for _ in range(r)]
    # 공기 청정기 위치
    new_board[ccw][0] = -1
    new_board[cw][0] = -1

    for x in range(r):
        for y in range(c):
            # 보드판에 현재 위치에 미세먼지가 있는 경우
            if board[x][y] > 0:
                # 새로운 보드에도 미세먼지 표기
                new_board[x][y] += board[x][y]
                # 인접한 4방향에 대해
                for g in range(4):
                    # index 를 옮겨서
                    nx = x + gx[g]
                    ny = y + gy[g]
                    # 확인해 봤을 때, x,y 값이 격자 안에 있으며, 공기청정기가 있지 않은 위치에서만 미세먼지 확산
                    if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != -1:
                        # 인접한 4 방향으로 나누기 5만큼 퍼지며, 현재 좌표의 미세먼지는 나누기 5한 만큼 미세먼지를 잃는다.
                        new_board[nx][ny] += board[x][y] // 5
                        new_board[x][y] -= board[x][y] // 5

    return new_board

# 2. 공기청정기 작동
# 공기청정기 동작 계산을 시작점이 아닌 끝점부터 탐색해서 진행
def rotate():
    # 공기청정기의 윗 방향, 반시계 순환
    for x in range(ccw - 1, 0, -1):
        board[x][0] = board[x-1][0]
    for y in range(c - 1):
        board[0][y] = board[0][y+1]

    for x in range(ccw):
        board[x][-1] = board[x+1][-1]
    for y in range(c - 1, 0, -1):
        board[ccw][y] = board[ccw][y-1]

    # 공기청정기의 아래 방향, 시계 순환
    for x in range(cw + 1, r - 1):
        board[x][0] = board[x+1][0]
    for y in range(c - 1):
        board[-1][y] = board[-1][y+1]

    for x in range(r-1, cw, -1):
        board[x][-1] = board[x-1][-1]
    for y in range(c - 1, 0, -1):
        board[cw][y] = board[cw][y-1]

    # 공기 청정깅 바람은 미세 먼지 없는 바람으로 0 으로 초기화
    board[ccw][1] = 0
    board[cw][1] = 0

r, c, t = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
for i in range(r):
    if board[i][0] == -1:
        ccw, cw = i, i + 1
        break

for _ in range(t):
    board = spread()
    rotate()

print(sum([sum(line) for line in board]) + 2)
