# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYCnY9Kqu6YDFARx&categoryId=AYCnY9Kqu6YDFARx&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=2
T = int(input())

for tc in range(1, T+1):
    numberList = list(input())
    number = ""
    answer = "impossible"

    for item in numberList:
        number += item

    n = 2
    while len(str(int(number) * n)) <= len(number) + 1:
        numberXN = list(str(int(number) * n))

        if sorted(numberXN) == sorted(numberList):
            answer = "possible"
            break
        n += 1

    print(f"#{tc} {answer}")