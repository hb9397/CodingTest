# https://www.acmicpc.net/problem/2752
A = list(map(int, input().split()))
A = sorted(A)

for item in A:
    print(item, end = " ")