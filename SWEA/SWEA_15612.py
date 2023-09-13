# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYOBfxwaAXsDFATW&categoryId=AYOBfxwaAXsDFATW&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1
'''
체스판 8*8 에는 Look이 딱 맞게 8개 존재해야 하며 서로 공격이 불가능하게 배치되어야 함.
입력으로는 8*8 에 대응되게 .(비어있는 칸), O(룩이 존재하는 칸) 으로 주어진다.

1. 2차원 배열로 취급해서 체스판을 생성한다.
2. 이중 for 문을 이용해서 이차원 체스판 배열에 룩이 존재한다면 해당 좌표를 look이라는 리스트에 보관
3. 이때, look이 존재하는 리스트가 8개를 초과한다면 해당 케이스는 no
4. look을 보관한 리스트가 8개인 경우에 look 의 x좌표 y좌표를 lookX, lookY로 분리하여 가져온 뒤 set으로 중복을 제거한다.
    이렇게 되면 룩을 가지고 있는 x좌표, y좌표의 리스트 모두 길이가 8개여야 서로 공격이 불가능한 위치에 룩이 8개 존재하는 것으로 취급할 수 있다.
    아닌 경우에는 해당 케이스는 no이다.
'''
from collections import deque
T = int(input())

for test_case in range(1, T+1):
    answer = deque()
    pan = []
    look = []
    lookX = []
    lookY = []
    for i in range(8):
        row = input()
        pan.append(row)

    for i in range(8):
        for j in range(8):
            if pan[i][j] == "O":
                look.append([i, j])

    if len(look) != 8:
        answer.append("no")

    else:
        for item in look:
            lookX.append(item[0])
            lookY.append(item[1])

        if len(set(lookX)) == 8 and len(set(lookY)) == 8:
            answer.append("yes")
        else:
            answer.append("no")

    print(f"#{test_case} {answer.popleft()}")