# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYCnY9Kqu6YDFARx&categoryId=AYCnY9Kqu6YDFARx&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=2
'''
1. 나열된 수를 list로 받아온다( 맨 처음 숫자를 받아와서 *n 한 다음 sorted로 비교하기 위함)
2. 그 수에 *n 하기 위해 다시 list의 숫자를 문자열로 가져와서 저장한다.
3. n배의 첫 번째는 2배 이기 때문에 n = 2로 초기 값을 준다
4. 현재 숫자를 가지고 조합하는 길이보다 숫자 * n의 길이가 길어지면 안되므로 반복은 숫자*n이 숫자의 길이보다 길어지면 안되도록 한다.
5. 그 길이가 같은 동안에 단 한 번이라도 숫자 * n 과 숫자를 list에 두고 sorted 했을 때 그 조합이 같다면 이건 가능한 경우이므로 break
    아니라면 그대로 불가능한 경우로 둔다.
'''
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