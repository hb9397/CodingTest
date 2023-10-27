# https://www.acmicpc.net/problem/5597
import sys

applyNums = [int(sys.stdin.readline().rstrip()) for item in range(28)]

for currentNum in range(1, 31):
    if currentNum not in applyNums:
        print(currentNum)