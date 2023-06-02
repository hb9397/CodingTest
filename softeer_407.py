# https://softeer.ai/practice/info.do?idx=1&eid=407

k, p, n = map(int,input().split())

# 총 시간동안 바이러스를 증가시킨다.
for i in range(n):
    k = (k * p) % 1000000007

print(k)

''' 틀린 풀이 ~'''
x, y, z = map(int, input().split())
cur = x * (y**z)
if cur < 1000000007:
    print(cur)
else:
    print(cur % 1000000007)