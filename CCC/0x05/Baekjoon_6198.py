# https://www.acmicpc.net/problem/6198
import sys

N = int(sys.stdin.readline().rstrip())
buildings = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
answer = [0]*N

for i in range(N):
    currentBuildingShortThen = 0

    for j in range(i+1, N):
        if buildings[j] < buildings[i]:
            currentBuildingShortThen += 1

        if buildings[j] >= buildings[i]:
            break

    answer[i] = currentBuildingShortThen
print(sum(answer))