# https://www.acmicpc.net/problem/20053
import sys
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    numsLen = int(sys.stdin.readline().rstrip())
    nums = [int(item) for item in sys.stdin.readline().rstrip().split(" ")]

    print(min(nums), max(nums), end=" \n")