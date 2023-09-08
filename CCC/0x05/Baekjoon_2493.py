# https://www.acmicpc.net/problem/2493

import sys

N = int(sys.stdin.readline().rstrip())
tower = list(map(int, sys.stdin.readline().rstrip().split()))
stack = []
answer = [0 for i in range(N)]

for i in range(N):

    # 길이를 비교할 스택( [ [탑 index, 탑 height], [탑 index, 탑 height], ... ]) 에
    # 비교할 탑의 정보가 하나 라도 있는 경우에 스택에 탑에 비교할 정보가 없을 때까지 로직 수행
    while len(stack) != 0:

        # 스택 가장 위에 존재하는 탑 정보 -> [탑 index, 탑 height] 중 탑 height 가
        # 현재 비교 기준의 탑 높이 -> tower[i] 보다 높으면 tower[i] 의 신호를 수신할 수 있기 때문에
        if stack[-1][1] > tower[i]:

            # 정답에 출력해야 하는 현재 탑 i번째의 신호를 수신할 수 있는 탑 중 첫번째 탑의 순서 번호를 저장하기 위해서
            # tower[i] 보다 높은 stack[-1][0] 인 스택 가장 위의 탑 정보중 index + 1 하여
            # 현재 탑의 자리인 answer[i] 에 0의 값을 stack[-1][0] 인 스택 가장 위의 탑 정보중 index + 1 로 초기화한다.
            # 또한 현재 탑 tower[i] 의 신호를 받을 수 있는 첫번째 타워만을 기록해야 하므로 수신할 탑의 번호를 기록했다면
            # break 로 더 이상 추가적인 기록을 하지 않도록 한다.
            answer[i] = stack[-1][0] + 1
            break

        else:
            # 현재 탑 tower[i] 의 높이 보다 높은 타워가 아닌 경우 스택에 저장된 가장 위의 탑의 정보는 필요 없으므로
            # pop 하여 다음 타워의 정보를 비교한다.
            stack.pop()

    # while 문로직 수행 후 tower Stack 에 저장된 각 송신탑의 index와 높이 정보를 스택에 삽입한다.
    stack.append([i, tower[i]])

print(*answer)