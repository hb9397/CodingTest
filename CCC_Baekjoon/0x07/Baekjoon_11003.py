# https://www.acmicpc.net/problem/11003

import sys
from collections import deque

N, L = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))

# 현재 범위의 최솟값을 값 기억
currentMin = deque([])

for i in range(N):
    # 삽입 할 값이 기존 값보다 클 때까지 기존의 currentMin 값 제거
    while currentMin and currentMin[-1][0] > numbers[i]:
        currentMin.pop()

    # 값 삽입
    currentMin.append((numbers[i], i))

    # 현재 슬라이딩 윈도우(범위)가 가능한 인덱스 범위에서 벗어난 경우 제거
    if currentMin[0][1] < i - L:
        currentMin.popleft()

    print(currentMin[0][0], end=" ")