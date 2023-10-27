# https://www.acmicpc.net/problem/14467

import sys

N = int(sys.stdin.readline().rstrip())
checkCows = {}
count = 0
for _ in range(N):
    cow, place = map(int, sys.stdin.readline().rstrip().split(" "))

    if cow not in checkCows.keys():
        checkCows[cow] = place
    else:
        if checkCows[cow] != place:
            checkCows[cow] = place
            count += 1

print(count)
