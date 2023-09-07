# https://www.acmicpc.net/problem/1874
import sys
# 문제의 설명이 복잡할 수 있는데 정수 n 이 첫째 줄에 주어지면 1~n 까지의 정수를 스택에 오름차순 으로 push 하고 자유롭게
# push 사이 사이에 pop 을 하는데, 첫 째 줄 이후 부터 주어지는 n 줄의 수열과 동일하게 결과를 만들 수 있다면,
# 그 수열을 만들기 위한 연산을 +, -로 표현하고 불가능하다면 NO 를 출력하는 문제이다.

n = int(sys.stdin.readline().rstrip())
stack = []
answer = []
pushNumber = 1

for _ in range(n):
    currentNum = int(sys.stdin.readline().rstrip())

    while pushNumber <= currentNum:
        stack.append(pushNumber)
        answer.append('+')

        pushNumber += 1

    if stack[-1] == currentNum:
        stack.pop()
        answer.append('-')
    else:
        answer = ["No"]
        break

for item in answer:
    print(item)