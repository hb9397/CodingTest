# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYP5JmsqcngDFATW&categoryId=AYP5JmsqcngDFATW&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1\

'''
두 개의 문자열 S 와 T가 있을 때, S == T 이면 F(S) == F(T) 는 당연히 T 이지만, S != T 인 경우 F(S)와 F(T) 는 경우에 따라 달라질 수 있다.
1. 우선 S와 T가 같으면 F(X) 는 당연히 True
2. S와 T의 시작 문자가 다르다면 무조건 False
3. 만약 S와 T의 문자열이 같다면 S 와 T를 구성하는 문자열을 숫자처럼 생각 했을 때 두 문자열 길이의 최소공배수를 각자 자신 S, T 의 길이로 로 나눈 몫을 곱했을 때,
    서로의 문자열의 길이가 같아지는 최소 공배수 길이에 해당되는 문자열이 되는데 이 문자열이 같다면 True, 틀리면 False이다.
'''
import math
from collections import deque
T = int(input())

for test_case in range(1, T+1):

    inputStr = input()
    answer = deque()

   # for item in inputStr:
   #     if item != ' ' or ord(item) < ord('a') or ord(item) > ord('z'):
   #         print("잘 못된 입력 값 이잖아~")

    S = inputStr.split()[:1].pop()
    T = inputStr.split()[1:].pop()
    X = 0

    if S == T :
        answer.append("yes")

    elif S[0] != T[0]:
        answer.append("no")

    else:
        X = len(S) * len(T) // math.gcd(len(S), len(T))

        if S * (X // len(S)) == T * (X // len(T)):
            answer.append("yes")
        else:
            answer.append("no")

    print(f"#{test_case} {answer.popleft()}")