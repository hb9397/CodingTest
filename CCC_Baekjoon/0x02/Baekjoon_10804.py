# https://www.acmicpc.net/problem/10804

cards = [i for i in range(1, 21)]

for _ in range(10):
    a, b = map(int, input().split())
    cards[a-1 : b] = cards[a-1 : b][::-1]

print(*cards, end = " ")