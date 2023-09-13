# https://www.acmicpc.net/problem/1475
number = input()
numberCounts = [0] * 10

for item in number:
    num = int(item)
    if num == 6 or num == 9:
        if numberCounts[6] <= numberCounts[9]:
            numberCounts[6] += 1
        else:
            numberCounts[9] += 1

    else:
        numberCounts[num] += 1

print(max(numberCounts))