# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYGtoa3qARcDFARC&categoryId=AYGtoa3qARcDFARC&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1
'''
해당 문제의 정답을 도출하는 방법은 주어진 문자열을 하나씩 리스트에 기억시키면서 이전의 문자가 '('일 때 현재 문자가 '|' 이거나 ')' 일 때
count + 1하고, 또는 이전 문자가 '|' 인 경우 현재 문자가 ')' 인 경우 count + 1 을 해서 주어진 문자열에서 (|, |), () 인 3가지 경우에
대한 count를 구하는 것 이라 생각하고 풀이했다.
1. 문자열을 하나씩 받아올 temp 리스트 선언, 정답이자 count의 갯수를 셀 변수 선언
2. 주어진 문자열의 길이 만큼 문자열을 temp에 집어 넣으면서 이전의 문자가 '('일 때 현재 문자가 '|' 이거나 ')' 일 때 count + 1
3. 혹은 이전 문자가 '|' 인 경우 현재 문자가 ')' 인 경우 count + 1 을 하도록 설정한다.
4. 이 때, 내가 비교하는 문자는 2개 이므로 문자열의 첫번째 만 삽입된 경우 (temp 와 문자열 s의 index를 같이 이용하므로 )를 제외한다.
    ( index i > 0 부터 두 문자를 비교하도록 설정)
'''
from collections import deque
T = int(input())

for tc in range(1, T+1):
    s = input()
    temp = deque()
    answerCnt = 0

    for i in range(len(s)):
        temp.append(s[i])

        if i > 0 and temp[i-1] == '(' and (temp[i] == '|' or temp[i] == ')'):
            answerCnt += 1
        elif i > 0 and temp[i-1] == '|' and temp[i] == ')':
            answerCnt += 1
        else:
            answerCnt += 0

    print(f"#{tc} {answerCnt}")