# https://www.acmicpc.net/problem/1158

N, K = map(int, input().split())

numbers = [i+1 for i in range(N)]
answer = []
deletedNumIndex = 0

for _ in range(N):
    deletedNumIndex += K - 1

    if deletedNumIndex >= len(numbers):
        deletedNumIndex = deletedNumIndex % len(numbers)

    answer.append(str(numbers.pop(deletedNumIndex)))

print("<" + ', ' .join(answer) + ">")