# https://www.acmicpc.net/problem/10093

A, B = map(int, input().split())
x, y = min(A, B), max(A, B)

if y - x <= 1:
    print(0)
else:
    print(y - x - 1)

arr = [x for x in range(x + 1, y)]
print(*arr, end =" ")