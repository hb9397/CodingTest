# https://www.acmicpc.net/problem/2578

import sys

cheolnsoo = []
bingoAnswer = []
bingoIndex = [[i for i in range(5)], [i for i in range(5, 10)], [i for i in range(10, 15)],
               [i for i in range(15, 20)], [i for i  in range(20, 25)],
               [i for i in range(0, 25, 6)], [i for i in range(4, 21, 4)]]
bingo = 0

for _ in range(5):
    a, b, c, d, e = map(int, sys.stdin.readline().rstrip().split(" "))
    cheolnsoo.append(a)
    cheolnsoo.append(b)
    cheolnsoo.append(c)
    cheolnsoo.append(d)
    cheolnsoo.append(e)

for _ in range(5):
    a, b, c, d, e = map(int, sys.stdin.readline().rstrip().split(" "))
    cheolnsoo.append(a)
    cheolnsoo.append(b)
    cheolnsoo.append(c)
    cheolnsoo.append(d)
    cheolnsoo.append(e)

# for currentNum in bingoAnswer:
#     for num in cheolnsoo:
#         if currentNum == num:
#             num =
#
#     if cheolnsoo.count(False) >= 13:
#         for item in bingoIndex:
#
#             for i in item:
#                 falseCnt = 0
#                 if cheolnsoo[i] == False:
#                     falseCnt += 1
#
#                 if falseCnt == 5:
#                     bingo += 1
print(cheolnsoo)