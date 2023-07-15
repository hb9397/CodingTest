# DFS - https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 재귀 DFS로 풀이 - >>> 주어진 numbers의 배열의 담긴 숫자 순서대로 첫 숫자부터 뒤의 숫자를 더하거나 빼는 조합(두 조합 모두 검사) 해서 끝까지 더하거나 빼서 마지막 값이
# 주어진 target값과 같을 때 count 를 하여 정답을 도출하는 문제.
def solution(numbers, target):
    answer = 0
    def dfs(index, value):

        # 주어진 list의 길이와 현재 index가 같다면(주어진 숫자 순서 배열을 모두 탐색했을 때)
        if index == len(numbers):

            # 현재 주어진 숫자들을 순서대로 덧셈, 뺄셈한 현재 값 value가 주어진 target과 같을 때, count + 1
            if value == target:
                nonlocal answer
                answer += 1
            return
        # 주어진 숫자 순서를 전부 탐색한 경우가 아니라면 현재 숫자의 다음 숫자를 더하고 빼는 경우로 분기하여 재귀호출
        else:
            dfs(index + 1, value + numbers[index])
            dfs(index + 1, value - numbers[index])

    # numbers 의 최초 index와 value(현재까지 숫자를 더하거나 뺀 값)값인 0, 0으로 dfs 함수 호출
    dfs(0, 0)
    return answer