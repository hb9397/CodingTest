# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15QRX6APsCFAYD
'''
BFS 를 이용해서 문제 해결
1. 방문했는지 여부를 저장할 배열 chk, 현재 고친 누적 횟수를 저장할 refactorValue 배열 선언
2. 이동 가능한 좌표 값 상하좌우 배열 선언
3. 이동한 Y, X 좌표와 고친 누적 횟수를 함께 저장할 temp 튜플 선언
4, 최초지점인 0,0 은 방문한 상태로 지정하고 최초 좌표 0,0 과 누적횟수 0 을 temp 에 삽입
5. 반복문을 temp가 빌 때 까지 돌아가도록 지정하고, 최초 temp에서 값을 꺼내서 로직에 사용하도록 지정
6. 위 반복문 내부에서 현재 좌표에서 이동 가능한 좌표값에 대하여 반복하도록 하는데 이때, 이동한 Y와 X의 좌표가 양수 이면서 주어진 N을 넘지 않을 때만 로직을 진행
7. 이동한 좌표를 방문한 적이 없다면 무조건 고친 누적횟수를 갱신하고 해당 좌표와 누적횟수를 temp에 삽입한다.
8. 만약 이미 이전회차에서 방문한 좌표라면 현재 갱신되어 있는 누적 횟수 nextValue가 이전 X번째 회차의 누적 횟수(refactor[Y][X])
    보다 적은 경우 고친 누적횟수를 갱신하고 temp에 현재 좌표와 누적횟수를 삽입한다.
9. 방문한 좌표일 때, 현재 좌표까지오기 위해서  갱신한 누적횟수가 이전회차에 저장한 누적횟수 보다 크면 해당 번째 좌표는 작업을 뛰어넘도록 설정
'''
from collections import deque
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    chk = [[0]*N for _ in range(N)]
    refactorValue = [[0] * N for _ in range(N)]
    go = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    answer = 0

    temp = deque()

    chk[0][0] = 1
    temp.append((0, 0, 0))

    while temp:
        curY, curX, curValue = temp.popleft()

        for goY, goX in go:
            Y, X = curY + goY, curX + goX

            if 0 <= Y < N and 0 <= X < N:
                nextValue = curValue + arr[Y][X]

                if chk[Y][X] == 0:
                    chk[Y][X] = 1
                    refactorValue[Y][X] = nextValue
                    temp.append((Y, X, nextValue))

                if chk[Y][X] == 1:
                    if nextValue >= refactorValue[Y][X]:
                        continue

                    refactorValue[Y][X] = nextValue
                    temp.append((Y, X, nextValue))

    answer = refactorValue[N-1][N-1]
    print(f"#{tc} {answer}")