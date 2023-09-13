# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYcllbDqUVgDFASR&categoryId=AYcllbDqUVgDFASR&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1
'''
(0, 0) 을 원의 중심으로 가정하고 원안에 들어가는 좌표값인 x^2 + y^2 <= N^2 를 만족하는 것을 count 하도록 풀이한다.
1. 양수 값만 갖는 1 사분면에 해당되는 좌표들의 개수를 구하고 4배 한다.
    -> 0,0 부터 x나 y축을 기준으로 하여 이중 반복문으로 count += 1 형태로 개수를 셀 수 있음.

2. 이 때, 단순히 4배할 경우 x나 y좌표가 0인 경우와 0,0을 중복으로 count 하기 때문에
    x^2 + y^2 <= N^2 를 만족하는 경우 count 하고 이 때, x나 y가 0인 경우에 앞선 count와 함께 다른 count를 이용해 따로 기억해둔다.

3. 중복을 피하기 위해서 원안에 포함되는 조건을 count 한 수 에서 x나 y가 0인 경우를 빼서 제외 시킨 후 X4 한 뒤,
    x 나 y가 0인 경우는 원점을 기준으로 대각선으로 대칭하므로 X2 해준뒤 원점은 2번 세어지는 것이므로 1을 뺄셈해준다.

4. 그 뒤 2번과 3번의 수를 더하면 원점을 기준으로 반지름이 N 인 원안에 포함되는 정수형 좌표를 모두 구할 수 있게 된다.
'''
T = int(input())

for test_case in range(1, T+1):
    numbers = int(input())
    count = 0
    zeroCount = 0

    for x in range(0, numbers+1):
        for y in range(0, numbers+1):
            if x ** 2 + y ** 2 <= numbers ** 2:
                count += 1
                if x == 0 or y == 0:
                    zeroCount += 1

    print(f"#{test_case} {(count - zeroCount) * 4 + (zeroCount * 2 - 1)}")
