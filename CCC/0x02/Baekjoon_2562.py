# https://www.acmicpc.net/problem/2562

inputNumbers = [int(input()) for _ in range(9)]
print(max(inputNumbers))
print(inputNumbers.index(max(inputNumbers)) + 1)