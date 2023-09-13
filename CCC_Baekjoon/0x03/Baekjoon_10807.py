# https://www.acmicpc.net/problem/10807
N = int(input())
numbers = list(map(int, input().split()))
V = int(input())

print(numbers.count(V))