# https://www.acmicpc.net/problem/10871
N, X = map(int, input().split())
A = list(map(int, input().split()))

for item in A:
    if(item < X):
        print(item, end = " ")