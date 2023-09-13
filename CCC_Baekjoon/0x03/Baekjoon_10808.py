alphabet = [chr(97+i) for i in range(26)]
answer = []
inputStr = input()

for item in alphabet:
    countChr = inputStr.count(item)
    answer.append(countChr)

print(*answer, end="")