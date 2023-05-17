#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYaf9W8afyMDFAQ9&categoryId=AYaf9W8afyMDFAQ9&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1
'''
BFS, DFS도 있다고 생각했지만, 어떤 수 X의 제곱근에 가장 근접한 약수 A와 그 짝 B라는 숫자 좌표까지의 거리는 앞선 두 방법 모두 최소거리로 동일하다.
그래서 어떤 수 X의 두 약수 A, B(X의 제곱근에 가장 근접한 약수들) 를 구한 뒤 현재 좌표 1,1 을 빼서 이동한 거리를 측정하는 방법을 사용했다.

1. 이 때, 약수들은 제곱근을 기준으로 대칭하기 때문에 제곱근 까지만 반복문을 짜서 도달하고자 하는 수를 1부터 나눠 그 나머지가 0이라면
    그 나눈 수 i와 그 몫을 deque에 삽입.

2. 위와 같이 구해진 n, n+1 의 짝인 두 약수들 중에 가장 마지막에 삽입된 짝들이 제곱근에 가장 근접한 약수로 자연스럽게 pop을 두 번하면
    서로 짝궁인 약수 중 제곱근에 가장 근접한 값을 구할 수 있다.
    -> 위와 같이 하면 25와 같이 제곱근을 갖는 경우 i에 해당되는 5와 그 몫(짝궁)인 5를 모두 삽입하고 pop 할 수 있다.

3. 이후 두 짝을 pop 해서 A-1, B-1 한 값을 더하면 최소 이동 거리를 구 할 수 있다.
'''
from collections import deque
T = int(input())

for test_case in range(1, T+1):
    target = int(input())
    yaksu = deque()
    answer = 0
    x = 0
    y = 0

    # 어떤 수 X 는 자기 자신의 제곱근을 기준으로 약수들이 대칭되므로 제곱근까지 반복해서 구하면 모든 약수 확인 가능
    for i in range(1, int(target**(1/2)+1)):
        if int(target % i) == 0:
            yaksu.append(i)
            yaksu.append(int(target / i))

    y = yaksu.pop()
    x = yaksu.pop()

    answer = x - 1 + y - 1
    print(f"#{test_case} {answer}")