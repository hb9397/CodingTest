# https://www.acmicpc.net/problem/2490

for tc in range(3):
    dict = {0: "D", 1: "C", 2: "B", 3: "A", 4: "E"}
    yoot = list(map(int, input().split()))

    print(dict[sum(yoot)])