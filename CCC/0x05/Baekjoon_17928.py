# https://www.acmicpc.net/problem/17298

import sys

N = int(sys.stdin.readline().rstrip())
numbersArr = list(map(int, sys.stdin.readline().rstrip().split()))
answer = [-1] * N

# 오른쪽 수가 더 큰가 에 대해 판별할 스택이며, 스택에 쌓이는 값은 index 이다.
chkStack = [0]

for i in range(N):

    while len(chkStack) > 0:
        # 현재 chkStack 상단에 저장된 index 로,
        # numbersArr 의 스택에서 꺼낸 index 에 해당되는 값인
        # numbersArr[chkStack[-1]] 값 (현재 i번째 numbersArr 의 요소 이전에 스택에 입력되었지만, 어떤 수의 오큰 수도 되지 못한 수)
        # 이 숫자 보다 현재 i 번째 numbersArr 의 요소가 크다면 이 수는 stack[-1]의 오큰수에 해당 되므로
        # answer[스택에 저장된 현재 index] 의 오큰수 를 numbersArr[i] 로 변경하므로 pop으로 index를 꺼낸다.

        if numbersArr[chkStack[-1]] < numbersArr[i]:
            answer[chkStack.pop()] = numbersArr[i]

    # 현재 비교 기준의 numbersArr 의 index를 stack에 저장
    chkStack.append(i)

print(*answer, end="")