# https://www.acmicpc.net/problem/6198
import sys

N = int(sys.stdin.readline().rstrip())
buildings = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
chkStack = []
canSeeBuildingSum = 0

for i in range(N):
    print(chkStack)

    # 포인트는 chkStack 에 빌딩의 높이가 쌓인다는 것은 chkStack 의 가장 위에 존재하는 빌딩의 높이보다 작은 빌딩들이 온다는 것이고,
    # pop 되어 없어지는 빌딩의 높이들은 현재 buildings[i] 보다 짧은 빌딩이기 때문에 관찰할 수 없는 빌딩이므로 제거하는 것이다.

    while len(chkStack) > 0 and chkStack[-1] <= buildings[i]:
        chkStack.pop()

    chkStack.append(buildings[i])

    # 이렇게 되면 현재 buildings[i]가 chkStack 에 들어가 있는 만큼 마치 내림차순으로 정렬되어 연속된 빌딩 들이 내림차순
    # 순서로 빌딩을 관찰할 수 있는 것에 해당되므로 길이 - 1 해서 자신을 제외한다.
    canSeeBuildingSum += len(chkStack) - 1


print(canSeeBuildingSum)