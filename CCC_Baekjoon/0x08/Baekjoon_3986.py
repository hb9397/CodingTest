# https://www.acmicpc.net/problem/3986
# 괄호를 교차하지 않고 단어 ABBABB 와 같이 있을 때, A(BB)A(BB) -> (AA) -> () 이면
# 좋은 단어로 간주하는 문제
import sys

N = int(sys.stdin.readline().rstrip())
cnt = 0
for _ in range(N):
    abString = sys.stdin.readline().rstrip()
    chkStack = []

    for item in abString:
        if len(chkStack) > 0 and chkStack[-1] == item:
            chkStack.pop()
        else:
            chkStack.append(item)

    if len(chkStack) == 0:
        cnt += 1

print(cnt)