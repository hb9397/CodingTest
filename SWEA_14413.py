# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYEXgKnKKg0DFARx&categoryId=AYEXgKnKKg0DFARx&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1
'''

'''
# 히든 케이스 두개 틀림
T = int(input())

for tc in range(1, T+1):
    Y, X = map(int, input().split())
    pan = []
    curState = "possible"
    absoluteBreak = False

    for i in range(1, Y + 1):
        pan.append(list(input()))

    for i in range(Y):
        if absoluteBreak:
            break

        for j in range(X):
            if i > 0 and pan[i-1][j] != '?' and pan[i-1][j] == pan[i][j]:
                curState = "impossible"
                break

            if j > 0:
                if pan[i][j] == '.':
                    if pan[i][j-1] == '?':
                        pan[i][j - 1] = '#'
                    elif pan[i][j-1] == '.':
                        curState = "impossible"
                        absoluteBreak = True
                        break
                elif pan[i][j] == '#':
                    if pan[i][j-1] == '?':
                        pan[i][j - 1] = '.'
                    elif pan[i][j-1] == '#':
                        curState = "impossible"
                        absoluteBreak = True
                        break
                else:
                    if pan[i][j-1] == '.':
                        pan[i][j] = '#'

                    if pan[i][j-1] == '#':
                        pan[i][j] = '.'

    print(f"#{tc} {curState}")
