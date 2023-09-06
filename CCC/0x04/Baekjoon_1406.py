# https://www.acmicpc.net/problem/1406

# 해당 문제는 연결리스트를 구현하는 문제가 맞으나 파이썬으로는 시간 초과 이슈 발생
# 따라서 커서를 생각하지 않고 두 개의 스택이나 큐 를 사용해 풀이를 한다.
# 풀이에 대한 설명은 다음의 블로그를  참조하는 것이 좋다. -> https://corin-e.tistory.com/entry/%EB%B0%B1%EC%A4%80-1406-%EC%97%90%EB%94%94%ED%84%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC

from collections import deque
chrLeftStack = deque(map(str, input()))
chrRightStack = deque()
T = int(input())

for tc in range(T):
    command = list (map(str, input().split()))

    if command[0] == 'L' and chrLeftStack:
        chrRightStack.appendleft(chrLeftStack.pop())

    elif command[0] == 'D' and chrRightStack:
        chrLeftStack.append(chrRightStack.popleft())

    elif command[0] == 'B' and chrLeftStack:
        chrLeftStack.pop()

    elif command[0] == 'P':
        chrLeftStack.append(command[1])

answer = chrLeftStack + chrRightStack
print(*answer, end="")