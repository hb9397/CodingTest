# https://www.acmicpc.net/problem/11328
from collections import deque

T = int(input())

for _ in range(T):
    strA, strB = map(str, input().split())

    answer = "Possible"
    chrStrAArr = sorted([item for item in strA])
    chrStrBArr = sorted([item for item in strB])


    if len(chrStrAArr) == len(chrStrBArr):
        lenStr = len(chrStrAArr)
        sameChrCount = 0

        chrStrAArr = deque(chrStrAArr)
        chrStrBArr = deque(chrStrBArr)

        for i in range(lenStr):
            if chrStrBArr[i] != chrStrAArr[i]:
                answer = "Impossible"
                break
            else:
                sameChrCount += 1

        if sameChrCount != lenStr:
            answer = "Impossible"

    else:
        answer = "Impossible"

    print(answer)