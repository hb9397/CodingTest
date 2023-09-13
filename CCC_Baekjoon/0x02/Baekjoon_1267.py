# https://www.acmicpc.net/problem/1267

N = int(input())
callTimes = list(map(int, input().split()))
Y, M = [30, 10], [60, 15]
costsY, costsM = [], []
answer =[]

for item in callTimes:
    # 통화한 시간이 0초 이더라도 각 요금제 마다 1회 만큼의 요금이 부과 되기 때문에
    # (나머지가 0이여도 -> 통화를 걸기만 해도 1회의 요금이 부과된다.)
    costsY.append((item // Y[0] + 1) * Y[1])
    costsM.append((item // M[0] + 1) * M[1])

if sum(costsY) > sum(costsM):
    answer.append('M')
    answer.append(sum(costsM))

elif sum(costsY) < sum(costsM):
    answer.append('Y')
    answer.append(sum(costsY))

else:
    answer.append('Y')
    answer.append('M')
    answer.append(sum(costsY))

print(*answer, end =" ")