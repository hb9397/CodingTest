# https://www.acmicpc.net/problem/2577
numbers = [int(input()) for _ in range(3)]
numbersCom = 1

for item in numbers:
    numbersCom *= item

numbersCom = str(numbersCom)

for i in range(10):
    print(numbersCom.count(str(i)))