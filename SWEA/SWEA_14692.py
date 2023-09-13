# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYJW0g-qlO8DFASv&categoryId=AYJW0g-qlO8DFASv&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1
'''
이 문제는 통나무의 길이가 주어질 때, Alice와 Bob이라는 두 사람이 본인의 차례에 통나무를 두 조각으로 자르되, 그 조각의 길이는 자연수여야만
하므로 자연수로 나누지 못하는 사람이 지게 되는 게임이며, 항상 게임의 시작은 Alice가 먼저 진행한다.

1. 이렇게 되면 통나무의 길이(게임 횟수)와 상관없이 통나무 길이 N을 이등분 했을 때, 그 나머지가 1이면 Bob이 0이면 Alice가 무조건 이기는
    게임이다.
'''
from collections import deque
T = int(input())

for tc in range(1, T+1):
    tree = int(input())
    answer = deque()

    if tree % 2 == 1:
        answer.append("Bob")
    else:
        answer.append("Alice")

    print(f"#{tc} {answer.popleft()}")