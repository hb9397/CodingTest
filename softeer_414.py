# https://softeer.ai/practice/info.do?idx=1&eid=414
'''
주어진 생산라인에 로봇과 부품이 있고 라인의 칸 수 N과 라인 내의 로봇의 팔 길이 K가 있을 때, 최대한 많은 로봇이 부품을 잡게 하는 문제로
최대한 많은 로봇이 부품을 잡게 하려면 항상 로봇은 자신이 잡을 수 있는 최대 거리의 부품을 우선적으로 잡도록 해야, 가장 많은 수가 나올 수 있다.
'''
N, K = map(int, input().split())
line = list(input())
count = 0

for i in range(N):
    # 라인을 순회하다가 로못을 만나면 로못이 좌/우로 움직일 수 있는 거리
    # 좌측 : item[0] - K | 우측 : item[0] + K + 1(+1 은 range라서) 에 대해서 탐색한다,
    # 이 때 그 탐색 index가 0보다 작거나 N 보다 크면 다음 케이스로 넘어간다.
    if line[i] == 'P':
        # 만약 현재 로봇이 잡을 수 있는 위치에 부품이 있으면 count += 1 후 잡힌 부분의 부품은 C 로 이미 잡았다고 표시 후 현재 케이스 break
        # break 를 하므로 부품 한 로봇에게 한 번만 잡히게 된다.
        for j in range(i - K, i + K + 1):
            if j < 0 or j > N - 1: # line 의 index는 N-1 이 최대이므로
                continue

            elif line[j] == 'H':
                count += 1
                line[j] = 'C'
                break

print(count)