# https://www.acmicpc.net/problem/20546

import sys
money = int(sys.stdin.readline().rstrip())
prices = list(map(int, sys.stdin.readline().rstrip().split(" ")))

bMoney, tMoney = money, money
BNP, Timing = 0, 0
bnpSum, timingSum = 0, 0

for item in prices:
    BNP += bMoney // item
    bMoney = bMoney % item

    if bMoney == 0:
        break

for i in range(len(prices)-4):
    if prices[i] < prices[i+1] < prices[i+2] < prices[i+3]:
        tMoney += Timing * prices[i+3]
        Timing = 0

    if prices[i] > prices[i+1] > prices[i+2] > prices[i+3]:
        Timing += tMoney // prices[i+3]
        tMoney = tMoney % prices[i+3]

bnpSum = BNP*prices[-1] + bMoney
timingSum = Timing*prices[-1] + tMoney

if bnpSum > timingSum:
    print("BNP")
elif bnpSum == timingSum:
    print("SAMESAME")
else:
    print("TIMING")