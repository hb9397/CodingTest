# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AX8BAN1qTwoDFARO&categoryId=AX8BAN1qTwoDFARO&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=2
'''

'''
from collections import deque
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    answer = "yes"
    temp = [[0] * N for _ in range(N)]
    count = 0

    for y in range(N):
        s = input()
        for x in range(N):
            if count == 0 and s[x] == '#':
                startY = y
                startX = x

            if s[x] == '#':
                temp[y][x] = 1
                count += 1

    for i in range(N):
        for j in range(N):
            if temp[i][j] == 1:
                for k in range(count ** (1//2) + 1):
                    if temp[i][k] != '#':
                        answer = "no"

                    if temp[j][k] != '#':
                        answer = "no"
    print(f"#{tc} {answer}")