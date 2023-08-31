# https://www.acmicpc.net/problem/2576

numbers = [int(input()) for _ in range(7)]
minHol = 101
sumHol = 0

for item in numbers:
    if int(item) % 2 == 1:
        sumHol += item

        if item < minHol:
            minHol = item

if(minHol != 101):
    print(sumHol)
    print(minHol)
else:
    print(-1)