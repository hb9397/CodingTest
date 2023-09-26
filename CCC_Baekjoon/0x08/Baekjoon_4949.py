# https://www.acmicpc.net/problem/4949

import sys

while True:
    strings = sys.stdin.readline().rstrip()
    checkStack = []
    answer = "yes"

    # 문제의 자체의 종료 조건으로 입력 줄에 .가 단독으로 올 경우
    if strings == ".":
        break

    for item in strings:
        if item == '(' or item == '[':
            checkStack.append(item)

        elif item == ')':
            if len(checkStack) != 0 and checkStack[-1] == '(':
                checkStack.pop()
            else:
                checkStack.append(')')

        elif item == ']':
            if len(checkStack) != 0 and checkStack[-1] == '[':
                checkStack.pop()
            else:
                checkStack.append(']')

    if len(checkStack) != 0:
        answer = "no"

    print(answer)