# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AX_N3oSqcyUDFARi&categoryId=AX_N3oSqcyUDFARi&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=2
'''
트러블 슈팅
해당 문제를 풀 때 바로 배열에 화단을 대입하는 것에 꽂혀 버려서 시간 복잡도 불통의 원인 1
또한 배열로 생각하다 보니 주어진 D를 가지고 화단의 index - D 했을 때 1을 하는 것을 구하고 1을 분무기가 포함할 수 있을 때,
해당 index + D 번 째 index까지 구해서 풀이하는 방식으로 진행하다 보니 시간 복자도를 초과했다.

풀이
1. 단순히 생각하면 그냥 화단의 첫 번째를 포함 시키려면 1 = X - D로 두면 최초로 1번째 화단을 포함해서 분무기를 뿌릴 수 있는 X번째
    화단을 구할 수 있으며, 그 X번째 화단에 다시 D를 더하면 1을 포함하고 D에 따라 뿌릴 수 있는 마지막 화단의 index를 알 수 있다.
2. 위와 같이 계산 했을 때 주어진 N, D에 따라 분무기가 최초로 1을 포함하고 조건에 따라 화단에 모두 물을 줄 최초의 경우에 포함되는 마지막
    화단의 index는 2 * D + 1이 된다.
3. 결국, 주어진 N개의 꽃에 [X-D, X+D] 구간에 모두 물을 줄 수 있는 경우는 N을 X+D로 나누었을 때 나머지가 0이상이면 한 번 더 물을 주고
    나머지가 0인 경우는 딱 나눠 떨어지는 경우면 그 몫만큼만 물을 줄 수 있다.
'''
T = int(input())

for tc in range(1, T + 1):
    N, D = map(int, input().split())
    answer = 0
    X = 2 * D + 1

    if N % X > 0:
        answer = N // X + 1
    elif N % X == 0:
        answer = N // X

    print(f"#{tc} {answer}")
