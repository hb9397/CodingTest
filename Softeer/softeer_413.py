# https://softeer.ai/practice/info.do?idx=1&eid=413
'''
주어진 Diamond-Square-Algorithm 처럼 점의 개수가 증가하면, 점은 A * A 개의 상태를 갖게 되는데 이때 가로
세로를 구성하는 A의 개수는 2^n-1 만큼씩 증가한다.
'''
N = int(input())
pointsEA = 2 # A * A 개의 포인트에서 A를 의미
answer = 0

for i in range(N):
    pointsEA += 2 ** i # range(N) 을 사용하므로 i는 N-1 상태

answer = pointsEA ** 2

print(answer)