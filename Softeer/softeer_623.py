# https://softeer.ai/practice/info.do?idx=1&eid=623
'''
입력의 두번째로 오는 문자열이, 입력의 세번째로 오는 문자열에 포함되어 있으면 secret 아니면 normal 출력하는 문제
'''
M, N, K = map(int, input().split())
secretM = input().split()
inputN = input().split()

menu = "normal"

# 비밀메뉴 입력이 사용자 입력보다 길면 반드시 일반 메뉴
if M > N:
    print(menu)
    exit()

secretKey = ""
for item in secretM:
    secretKey += item

userInput = ""
for item in inputN:
    userInput += item

if secretKey in userInput:
    menu = "secret"

print(menu)