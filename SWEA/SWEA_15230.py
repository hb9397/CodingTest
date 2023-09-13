# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYLnMQT6vPADFATf&categoryId=AYLnMQT6vPADFATf&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1
'''
이 문제는 입력으로 주어진 문자열이 순서대로 abcd,,,xyz로 있을 때, +1 하여 올바르게 연속된 알파벳이 오는지 검사하는 문제이다.
1. 원래 순서인 abcd,,,,xyz를 저장하고, 입력된 문자열이 올바른 알파벳 순서대로 온다면 count할 변수를 선언
2. 맨 처음 입력 받은 문자열의 첫번째가 a로 시작하지 않는 경우에 해당 케이스는 0을 정답으로 처리하고 다음 케이스로 넘어간다.
3. 맨 처음 문자열이 a인 경우에는 입력된 문자열의 길이만큼 올바른 알파벳 순서와 순서대로 비교해서 그 값이 서로 같다면
    count += 1로 올바른 만큼 count를 해주고 중간에 올바르지 않은 순서의 알파벳이 오는 경우 현재까지의 count를 정답 deque에 삽입한뒤
    불필요한 반복을 종료하고 해당 케이스를 마치고 입력된 모든 알파벳의 순서가 옳바른 경우에는 조건문 종료 후 count를 정답 deque에 삽입
'''
from collections import deque
T = int(input())

for tc in range(1, T+1):
    s = input()
    a = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    answer = deque()

    if ord(s[0]) != 97:
        answer.append(count)

    else:
        for i in range(len(s)):
            if s[i] == a[i]:
                count += 1
            else:
                count += 0
                answer.append(count)
                break
        answer.append(count)
    print(f"#{tc} {answer.popleft()}")